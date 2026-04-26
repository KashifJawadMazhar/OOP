import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#  Square points (4 corners) 
square = np.array([
    [1,  1, 0],
    [-1,  1, 0],
    [-1, -1, 0],
    [1, -1, 0],
    [1,  1, 0],   # close the shape
])

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

def draw_square():
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Rotate The Square")

    # Get slider values
    rx = slider_x.get()
    ry = slider_y.get()
    rz = slider_z.get()

    # Apply rotations
    R = rotate_z(rz) @ rotate_y(ry) @ rotate_x(rx)
    rotated = (R @ square.T).T

    ax.plot(rotated[:, 0], rotated[:, 1], rotated[:, 2], 'g--o', markersize=8)
    canvas.draw()

# Tkinter Window 
root = tk.Tk()
root.title("Rotate The Square")

fig = plt.Figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Sliders
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="X°:").grid(row=0, column=0)
slider_x = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_square())
slider_x.grid(row=0, column=1)

tk.Label(frame, text="Y°:").grid(row=1, column=0)
slider_y = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_square())
slider_y.grid(row=1, column=1)

tk.Label(frame, text="Z°:").grid(row=2, column=0)
slider_z = tk.Scale(frame, from_=0, to=360, orient=tk.HORIZONTAL, command=lambda e: draw_square())
slider_z.grid(row=2, column=1)

draw_square()
root.mainloop()