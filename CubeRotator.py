import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Cube corners (8 points) 
cube_corners = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
])

# Edges: pairs of corner indices
edges = [
    (0,1),(1,2),(2,3),(3,0),   # bottom face
    (4,5),(5,6),(6,7),(7,4),   # top face
    (0,4),(1,5),(2,6),(3,7),   # vertical edges
]

def rotate_x(angle_deg):
    a = np.radians(angle_deg)
    return np.array([
        [1, 0,          0         ],
        [0, np.cos(a), -np.sin(a) ],
        [0, np.sin(a),  np.cos(a) ]
    ])

def rotate_y(angle_deg):
    a = np.radians(angle_deg)
    return np.array([
        [ np.cos(a), 0, np.sin(a)],
        [ 0,         1, 0        ],
        [-np.sin(a), 0, np.cos(a)]
    ])

def rotate_z(angle_deg):
    a = np.radians(angle_deg)
    return np.array([
        [np.cos(a), -np.sin(a), 0],
        [np.sin(a),  np.cos(a), 0],
        [0,          0,         1]
    ])

def draw_cube():
    ax.cla()
    lim = 2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Cube Rotator")

    rx = slider_x.get()
    ry = slider_y.get()
    rz = slider_z.get()

    # Scale cube to fit nicely
    scale = 1
    R = rotate_z(rz) @ rotate_y(ry) @ rotate_x(rx)
    rotated = (R @ (cube_corners * scale).T).T

    for (i, j) in edges:
        p1 = rotated[i]
        p2 = rotated[j]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'b-')

    canvas.draw()

# Tkinter Window 
root = tk.Tk()
root.title("Cube Rotator")

fig = plt.Figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="X°:").grid(row=0, column=0)
slider_x = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_cube())
slider_x.grid(row=0, column=1)

tk.Label(frame, text="Y°:").grid(row=1, column=0)
slider_y = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_cube())
slider_y.grid(row=1, column=1)

tk.Label(frame, text="Z°:").grid(row=2, column=0)
slider_z = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_cube())
slider_z.grid(row=2, column=1)

draw_cube()
root.mainloop()