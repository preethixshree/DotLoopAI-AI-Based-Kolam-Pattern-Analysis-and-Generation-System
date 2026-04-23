import numpy as np

def detect_symmetry(img):
    flipped_h = np.flipud(img)
    flipped_v = np.fliplr(img)

    h_score = np.mean(img == flipped_h)
    v_score = np.mean(img == flipped_v)

    if h_score > 0.9 and v_score > 0.9:
        return "Radial Symmetry"
    elif h_score > 0.9:
        return "Horizontal Symmetry"
    elif v_score > 0.9:
        return "Vertical Symmetry"
    else:
        return "No strong symmetry"