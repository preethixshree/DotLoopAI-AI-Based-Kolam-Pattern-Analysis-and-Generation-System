import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2

from modules.dot_generator import generate_dot_grid
from modules.pattern_generation import generate_kolam, smooth_path
from modules.image_analysis import analyze_image

st.set_page_config(page_title="DotLoopAI", layout="wide")

st.title("DotLoopAI: Kolam Generator")

menu = st.sidebar.selectbox("Menu", [
    "Home",
    "Upload & Analyze",
    "Dot Generator",
    "AI Generator"
])

# ---------------- HOME ----------------
if menu == "Home":
    st.write("AI-based Kolam pattern generator using real loop logic.")

# ---------------- IMAGE ANALYSIS ----------------
elif menu == "Upload & Analyze":
    uploaded = st.file_uploader("Upload Kolam Image")

    if uploaded:
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        edges, symmetry = analyze_image(image)

        st.subheader("Detected Edges")
        st.image(edges, channels="GRAY")

        st.subheader("Symmetry")
        st.write(symmetry)

# ---------------- DOT GENERATOR ----------------
# In the Dot Generator section:
elif menu == "Dot Generator":
    col1, col2 = st.columns(2)
    
    with col1:
        n = st.slider("Grid size", 3, 8, 5)
    
    with col2:
        dot_pattern = st.selectbox("Dot arrangement", ["grid", "circle", "diamond", "hexagon"])
    
    kolam_style = st.selectbox("Kolam style", ["sikku", "pulli", "neli"])
    
    if st.button("Generate Kolam"):
        from modules.dot_generator import generate_dot_grid
        from modules.pattern_generation import generate_kolam, smooth_path
        
        dots = generate_dot_grid(n, pattern_type=dot_pattern)
        path = generate_kolam(dots)
        x, y = smooth_path(path)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(x, y, 'k-', linewidth=1.5)
        
        # Optional: Show dots as reference
        if st.checkbox("Show reference dots"):
            dot_x = [d[0] for d in dots]
            dot_y = [d[1] for d in dots]
            ax.scatter(dot_x, dot_y, c='red', s=10, alpha=0.5)
        
        ax.invert_yaxis()
        ax.axis("equal")
        ax.axis("off")
        ax.set_facecolor('#f5f0e1')  # Traditional paper color
        
        st.pyplot(fig)
elif menu == "AI Generator":

    symmetry = st.selectbox("Symmetry Type", ["None", "Horizontal", "Vertical"])
    complexity = st.slider("Complexity", 1, 10, 5)

    if st.button("Generate AI Kolam"):

        dots = generate_dot_grid(complexity)
        path = generate_kolam(dots)

        x, y = smooth_path(path)

        fig, ax = plt.subplots()
        ax.plot(x, y)

        if symmetry == "Horizontal":
            ax.plot(x, [-i for i in y])
        elif symmetry == "Vertical":
            ax.plot([-i for i in x], y)

        ax.invert_yaxis()
        ax.axis("equal")
        ax.axis("off")

        st.pyplot(fig)