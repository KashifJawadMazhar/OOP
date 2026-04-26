import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

#  Music (Windows only) 
def play_music():
    try:
        import winsound
        notes = [262, 294, 330, 349, 392, 440, 494, 523]
        while not stop_music:
            for freq in notes:
                if stop_music:
                    break
                winsound.Beep(freq, 200)
    except Exception:
        pass

stop_music = False

# Moon is displayed at center top 
moon_display = np.array([50.0, 90.0])

# Each rocket flies to its OWN landing spot on the moon (left side / right side)
# This way their paths NEVER cross and they NEVER collide
target1 = np.array([44.0, 90.0])   # Ernest  lands left of moon center
target2 = np.array([56.0, 90.0])   # Kernest lands right of moon center

MOON_RADIUS = 2.0   # how close = "landed"
SPEED       = 1.2   # units per step
STEP_DELAY  = 0.05  # seconds per step

# State 
rocket1    = np.array([20.0, 5.0])
rocket2    = np.array([80.0, 5.0])
countdown  = 3
running    = False
r1_reached = False
r2_reached = False
launch_time = None
eta1_text  = ""
eta2_text  = ""


def calc_eta(pos, target):
    dist  = np.linalg.norm(target - pos)
    steps = dist / SPEED
    return steps * STEP_DELAY


def draw():
    ax.cla()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Ernest and Kernest travel to the moon!")

    # Moon
    ax.scatter(*moon_display, color='yellow', s=500, zorder=5, label="Moon")

    # Rockets
    if not r1_reached:
        ax.scatter(*rocket1, color='red',   s=120, zorder=6, label="Ernest's Rocket")
    if not r2_reached:
        ax.scatter(*rocket2, color='green', s=120, zorder=6, label="Kernest's Rocket")

    ax.legend(loc='upper right', fontsize=8)

    # Status text
    if countdown > 0:
        ax.text(50, 3, f"Launch in {countdown}...",
                ha='center', fontsize=14, color='blue', fontweight='bold')
    else:
        y = 3
        if r1_reached:
            ax.text(50, y, "Ernest:  REACHED THE MOON! ✓",
                    ha='center', fontsize=10, color='green', fontweight='bold')
        elif eta1_text:
            ax.text(50, y, f"Ernest ETA:  {eta1_text}",
                    ha='center', fontsize=10, color='black')
        y += 7
        if r2_reached:
            ax.text(50, y, "Kernest: REACHED THE MOON! ✓",
                    ha='center', fontsize=10, color='green', fontweight='bold')
        elif eta2_text:
            ax.text(50, y, f"Kernest ETA: {eta2_text}",
                    ha='center', fontsize=10, color='black')

    canvas.draw()


def simulation_loop():
    global rocket1, rocket2, countdown, running
    global r1_reached, r2_reached, stop_music
    global eta1_text, eta2_text, launch_time

    # Countdown 3-2-1
    for i in range(3, 0, -1):
        countdown = i
        root.after(0, draw)
        time.sleep(1)

    countdown = 0
    launch_time = time.time()

    # Start music
    stop_music = False
    threading.Thread(target=play_music, daemon=True).start()

    while running:

        # Move rocket 1 toward its own target
        if not r1_reached:
            d1    = target1 - rocket1
            dist1 = np.linalg.norm(d1)
            if dist1 > MOON_RADIUS:
                rocket1   = rocket1 + (d1 / dist1) * SPEED
                eta1_text = f"{calc_eta(rocket1, target1):.1f}s"
            else:
                rocket1    = target1.copy()
                r1_reached = True
                eta1_text  = ""
                elapsed    = time.time() - launch_time
                root.after(0, draw)
                time.sleep(0.15)
                msg = f"Ernest's rocket reached the Moon!\nTravel time: {elapsed:.1f} seconds 🚀🌕"
                root.after(0, lambda m=msg: messagebox.showinfo("Ernest reached the Moon!", m))

        # Move rocket 2 toward its own target
        if not r2_reached:
            d2    = target2 - rocket2
            dist2 = np.linalg.norm(d2)
            if dist2 > MOON_RADIUS:
                rocket2   = rocket2 + (d2 / dist2) * SPEED
                eta2_text = f"{calc_eta(rocket2, target2):.1f}s"
            else:
                rocket2    = target2.copy()
                r2_reached = True
                eta2_text  = ""
                elapsed    = time.time() - launch_time
                root.after(0, draw)
                time.sleep(0.15)
                msg = f"Kernest's rocket reached the Moon!\nTravel time: {elapsed:.1f} seconds 🚀🌕"
                root.after(0, lambda m=msg: messagebox.showinfo("Kernest reached the Moon!", m))

        root.after(0, draw)

        if r1_reached and r2_reached:
            running    = False
            stop_music = True
            return

        time.sleep(STEP_DELAY)


def start_simulation():
    global rocket1, rocket2, countdown, running
    global r1_reached, r2_reached, eta1_text, eta2_text, launch_time

    if running:
        return  # prevent double-click

    rocket1    = np.array([20.0, 5.0])
    rocket2    = np.array([80.0, 5.0])
    countdown  = 3
    running    = True
    r1_reached = False
    r2_reached = False
    eta1_text  = ""
    eta2_text  = ""
    launch_time = None

    threading.Thread(target=simulation_loop, daemon=True).start()


# Window 
root = tk.Tk()
root.title("Ernest and Kernest travel to the moon!")

fig, ax = plt.subplots(figsize=(5, 5))
fig.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

tk.Button(root, text="Launch Rockets! 🚀", font=("Arial", 13),
          command=start_simulation).pack(pady=6)

draw()
root.mainloop()