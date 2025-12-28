import tkinter as tk
import requests
from datetime import datetime, timedelta

def update_temp(label):
    try:
        r = requests.get("http://192.168.0.123:8000/temp", timeout=3)
        r.raise_for_status()

        data = r.json()[-1]
        dt = datetime.fromisoformat(data['time'])
        dt = dt + timedelta(hours=1)
        time_str = dt.strftime("%H:%M") 

        temp = data['temp']
        hum  = data['humidity']
        room = data['room']

        label.config(
            text=f"{room}\n"
                 f"{temp:.1f} °C    {hum:.0f}%    {time_str}"
        )

    except requests.RequestException as e:
        label.config(text=f"Connection error\n{str(e)}")
    except (KeyError, IndexError, TypeError, ValueError) as e:
        label.config(text=f"Data format error\n{str(e)}")
    except Exception as e:
        label.config(text="Unexpected error")
        print(f"Update error: {e}")

    # Schedule next update (60 seconds = 60000 ms)
    root.after(60000, update_temp, label)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Widget")
    root.overrideredirect(True)
    root.geometry("340x140+2215+1250") # 1440p position
    root.configure(bg="#1a1a1a")

    label = tk.Label(
        root,
        text="Loading...",
        font=("Segoe UI", 14),
        bg="#1a1a1a",
        fg="#e0e0e0",
        justify="left",
        padx=20,
        pady=20
    )
    label.pack(fill="both", expand=True)

    update_temp(label)

    root.mainloop()
