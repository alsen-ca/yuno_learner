import ctypes

# Cross-platform screen size fetching
def get_screen_size():
    try:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # width, height
    except Exception:
        # Fallback for Linux
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        return root.winfo_screenwidth(), root.winfo_screenheight()