import cv2
import numpy as np
from modules.symmetry_detection import detect_symmetry

def analyze_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    symmetry = detect_symmetry(gray)

    return edges, symmetry