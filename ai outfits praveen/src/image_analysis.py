"""
Image Analysis Module
Analyzes uploaded images for skin tone, face shape, and body structure
Uses OpenCV for face detection and color analysis
"""

import cv2
import numpy as np
from PIL import Image
import io


class ImageAnalyzer:
    """
    Analyzes images to extract features like skin tone, face shape, and body structure
    """
    
    def __init__(self):
        """Initialize face detection using OpenCV cascade classifiers"""
        # Load Haar cascade for face detection (built-in to OpenCV)
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        # Load eye cascade for additional feature detection
        eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'
        self.eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    
    def load_image(self, uploaded_file):
        """
        Load image from uploaded file
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            cv2 image in BGR format
        """
        try:
            # Read image from uploaded file
            image_bytes = uploaded_file.read()
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise ValueError("Could not decode image")
            
            return img
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
    
    def analyze_skin_tone(self, image):
        """
        Analyze skin tone from the image
        Uses HSV color space analysis on detected face region
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with skin tone category and confidence
        """
        try:
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'tone': 'medium', 'confidence': 0.5, 'message': 'Face not clearly visible'}
            
            # Get the largest face (first one is usually largest)
            x, y, w, h = faces[0]
            
            # Extract face region with some padding
            x1 = max(0, x)
            y1 = max(0, y)
            x2 = min(image.shape[1], x + w)
            y2 = min(image.shape[0], y + h)
            
            # Extract face region
            face_roi = image[y1:y2, x1:x2]
            
            if face_roi.size == 0:
                return {'tone': 'medium', 'confidence': 0.5, 'message': 'Face region too small'}
            
            # Convert to HSV for better skin tone analysis
            hsv_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)
            
            # Calculate average HSV values
            avg_h = np.mean(hsv_face[:, :, 0])
            avg_s = np.mean(hsv_face[:, :, 1])
            avg_v = np.mean(hsv_face[:, :, 2])
            
            # Classify skin tone based on value channel
            # V (brightness) correlates with skin tone lightness
            if avg_v > 180:
                tone = 'light'
                confidence = 0.85
            elif avg_v > 130:
                tone = 'medium'
                confidence = 0.90
            else:
                tone = 'dark'
                confidence = 0.85
            
            return {
                'tone': tone,
                'confidence': confidence,
                'message': f'Skin tone analyzed successfully',
                'hsv_values': {'h': avg_h, 's': avg_s, 'v': avg_v}
            }
        
        except Exception as e:
            print(f"Error in skin tone analysis: {e}")
            return {'tone': 'medium', 'confidence': 0.5, 'message': f'Analysis error: {str(e)}'}
    
    def analyze_gender(self, image):
        """
        Estimate gender based on facial features (basic estimation)
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with gender estimation and confidence
        """
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'gender': 'not_determined', 'confidence': 0.5, 'message': 'Could not estimate gender'}
            
            x, y, w, h = faces[0]
            face_roi = gray[y:y+h, x:x+w]
            
            # Simple heuristics based on facial feature patterns
            # Calculate edge detection (more edges might indicate facial hair patterns)
            edges = cv2.Canny(face_roi, 100, 200)
            edge_density = np.sum(edges) / (face_roi.shape[0] * face_roi.shape[1])
            
            # Analyze brightness patterns (slightly different for male/female faces)
            brightness_variance = np.var(face_roi)
            
            # Simple classification based on combined features
            if edge_density > 0.03 or brightness_variance > 800:
                gender = 'Male'
                confidence = 0.70
            else:
                gender = 'Female'
                confidence = 0.70
            
            return {
                'gender': gender,
                'confidence': confidence,
                'message': f'Estimated gender: {gender}',
                'edge_density': round(edge_density, 3)
            }
        
        except Exception as e:
            print(f"Error in gender analysis: {e}")
            return {'gender': 'not_determined', 'confidence': 0.5, 'message': f'Analysis error: {str(e)}'}
    
    def analyze_face_shape(self, image):
        """
        Analyze face shape based on face detection bounding box
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with face shape and confidence
        """
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'shape': 'oval', 'confidence': 0.5, 'message': 'Face not detected'}
            
            x, y, w, h = faces[0]
            
            # Calculate aspect ratio to determine face shape
            aspect_ratio = w / h
            
            # Simple classification based on aspect ratio
            if aspect_ratio > 1.0:
                face_shape = 'oblong'
            elif aspect_ratio > 0.85:
                face_shape = 'oval'
            elif aspect_ratio > 0.75:
                face_shape = 'square'
            else:
                face_shape = 'round'
            
            confidence = 0.75
            
            return {
                'shape': face_shape,
                'confidence': confidence,
                'message': f'{face_shape.capitalize()} face shape detected',
                'aspect_ratio': round(aspect_ratio, 2)
            }
        
        except Exception as e:
            print(f"Error in face shape analysis: {e}")
            return {'shape': 'oval', 'confidence': 0.5, 'message': f'Analysis error: {str(e)}'}
    
    def analyze_body_structure(self, image):
        """
        Estimate basic body structure from image
        Returns basic estimation: slim, average, or athletic
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with body structure estimation
        """
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'structure': 'average', 'confidence': 0.5, 'message': 'Cannot estimate body structure'}
            
            x, y, w, h = faces[0]
            img_h, img_w = image.shape[:2]
            
            # Estimate based on face-to-image ratio
            # A larger face-to-image ratio might suggest closer proximity or smaller frame
            face_area_ratio = (w * h) / (img_w * img_h)
            
            if face_area_ratio > 0.15:
                structure = 'slim'
                confidence = 0.65
            elif face_area_ratio > 0.08:
                structure = 'average'
                confidence = 0.75
            else:
                structure = 'athletic'
                confidence = 0.60
            
            return {
                'structure': structure,
                'confidence': confidence,
                'message': 'Body structure estimated based on image composition',
                'area_ratio': round(face_area_ratio, 3)
            }
        
        except Exception as e:
            print(f"Error in body structure analysis: {e}")
            return {'structure': 'average', 'confidence': 0.5, 'message': f'Analysis error: {str(e)}'}
    
    def comprehensive_analysis(self, image):
        """
        Perform comprehensive image analysis
        Combines skin tone, face shape, body structure, and gender analysis
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with all analysis results
        """
        analysis_results = {
            'gender': self.analyze_gender(image),
            'skin_tone': self.analyze_skin_tone(image),
            'face_shape': self.analyze_face_shape(image),
            'body_structure': self.analyze_body_structure(image),
            'image_quality': self._check_image_quality(image)
        }
        
        return analysis_results
    
    def _check_image_quality(self, image):
        """
        Check basic image quality metrics
        
        Args:
            image: cv2 image
            
        Returns:
            Dictionary with quality assessment
        """
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Calculate Laplacian variance (blur detection)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # Assess brightness
            brightness = np.mean(gray)
            
            # Determine quality
            if laplacian_var < 100:
                quality = 'blurry'
                quality_score = 0.3
            elif brightness < 50 or brightness > 200:
                quality = 'poor lighting'
                quality_score = 0.6
            else:
                quality = 'good'
                quality_score = 0.9
            
            return {
                'quality': quality,
                'score': quality_score,
                'laplacian_variance': round(laplacian_var, 2),
                'brightness': round(brightness, 2)
            }
        
        except Exception as e:
            print(f"Error checking image quality: {e}")
            return {'quality': 'unknown', 'score': 0.5, 'message': str(e)}
    
    def get_detailed_observation(self, image):
        """
        Get detailed observation of the person
        
        Args:
            image: cv2 image in BGR format
            
        Returns:
            Dictionary with detailed observations
        """
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'observation': 'Could not detect face clearly in image'}
            
            x, y, w, h = faces[0]
            
            # Calculate various metrics
            face_height = h
            img_height = image.shape[0]
            face_prominence = (face_height / img_height) * 100
            
            # Detect eyes
            eyes = self.eye_cascade.detectMultiScale(gray[y:y+h, x:x+w])
            eye_count = len(eyes)
            
            # Create detailed observation
            observations = []
            
            # Face prominence
            if face_prominence > 60:
                observations.append("Close-up shot with prominent face")
            elif face_prominence > 40:
                observations.append("Medium distance - clear facial features")
            else:
                observations.append("Full body or far distance shot")
            
            # Eyes detected
            if eye_count >= 2:
                observations.append("Clear eye visibility - good for analysis")
            
            # Hair color estimation (top part of face)
            face_roi = image[y:y+h, x:x+w]
            hsv_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)
            
            # Hair analysis
            hair_region = hsv_roi[:h//4, :, :]
            avg_hue = np.mean(hair_region[:, :, 0])
            
            if avg_hue < 20 or avg_hue > 160:
                observations.append("Dark hair tones - sophisticated look")
            elif avg_hue < 50:
                observations.append("Brown/golden hair tones - warm palette")
            else:
                observations.append("Light/blonde hair tones - cool palette")
            
            # Brightness level
            brightness = np.mean(gray[y:y+h, x:x+w])
            if brightness > 150:
                observations.append("Excellent lighting - natural glow")
            elif brightness > 100:
                observations.append("Good lighting conditions")
            else:
                observations.append("Low lighting - needs more brightlight")
            
            # Calculate face metrics for body type hints
            img_w = image.shape[1]
            face_width_ratio = (w / img_w) * 100
            
            if face_width_ratio > 35:
                observations.append("Appears slim/petite frame")
            elif face_width_ratio < 20:
                observations.append("Broader frame - taller or wider shot")
            else:
                observations.append("Standard frame proportions")
            
            return {
                'observation': observations,
                'face_prominence': round(face_prominence, 1),
                'lighting_quality': 'excellent' if brightness > 150 else ('good' if brightness > 100 else 'low'),
                'face_width_ratio': round(face_width_ratio, 1)
            }
        
        except Exception as e:
            print(f"Error in detailed observation: {e}")
            return {'observation': ['Could not generate detailed observation'], 'error': str(e)}
