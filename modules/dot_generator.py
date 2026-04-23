import numpy as np

def generate_dot_grid(n, pattern_type="grid"):
    if pattern_type == "grid":
        spacing = 1.5
        offset = (n-1) * spacing / 2
        return [(i*spacing - offset, j*spacing - offset) 
                for i in range(n) for j in range(n)]
    
    elif pattern_type == "circle":
        radius = n
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        return [(radius * np.cos(a), radius * np.sin(a)) for a in angles]
    
    elif pattern_type == "diamond":
        points = []
        for i in range(n):
            for j in range(n):
                x = i - j
                y = i + j - (n-1)
                points.append((x, y))
        return points
    
    else:  
        points = []
        for i in range(n):
            for j in range(n):
                x = i * 1.5
                y = j * np.sqrt(3) + (i % 2) * (np.sqrt(3)/2)
                points.append((x - n*0.75, y - n))
        return points

def generate_dot_grid_original(n):
    return [(i, j) for i in range(n) for j in range(n)]