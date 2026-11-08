import tkinter as tk

from weather import get_weather, get_mood


MOOD_STYLES = {
    "sunny": {"background": "#FFD97D", "emoji": "☀️", "text_color": "#333333"},
    "cloudy": {"background": "#B0BEC5", "emoji": "☁️", "text_color": "#263238"},
    "rainy": {"background": "#5C9BD6", "emoji": "🌧️", "text_color": "#FFFFFF"},
    "stormy": {"background": "#546E7A", "emoji": "⛈️", "text_color": "#FFFFFF"},
    "snowy": {"background": "#E3F2FD", "emoji": "❄️", "text_color": "#263238"},
    "foggy": {"background": "#CFD8DC", "emoji": "🌫️", "text_color": "#263238"},
    "unknown": {"background": "#ECEFF1", "emoji": "🌡️", "text_color": "#263238"},
}


root = tk.Tk()
root.title("Weather Mood App")
root.geometry("420x520")
root.resizable(False, False)
root.configure(bg="#ECEFF1")

search_frame = tk.Frame(root, bg=root.cget("bg"))
search_frame.pack(pady=(28, 16))

city_entry = tk.Entry(search_frame, font=("Arial", 14), width=22)
city_entry.pack(side="left", padx=(0, 8), ipady=6)

def on_search():
    city = city_entry.get().strip()
    try:
        weather = get_weather(city)
        mood = get_mood(weather["condition"])
        style = MOOD_STYLES.get(mood, MOOD_STYLES["unknown"])

        root.configure(bg=style["background"])
        for label in (
            emoji_label,
            temperature_label,
            city_label,
            description_label,
            error_label,
        ):
            label.configure(bg=style["background"], fg=style["text_color"])

        emoji_label.configure(text=style["emoji"])
        temperature_label.configure(text=f"{weather['temp']}°C")
        city_label.configure(text=f"{weather['city']}, {weather['country']}")
        description_label.configure(text=weather["description"].capitalize())
        error_label.configure(text="")
    except ValueError:
        error_label.configure(text="City not found.", fg="red")
    except RuntimeError:
        error_label.configure(text="API error — try again.", fg="red")


search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 12),
    command=on_search,
)
search_button.pack(side="left", ipady=4)

emoji_label = tk.Label(root, text="", font=("Arial", 80), bg=root.cget("bg"))
emoji_label.pack(pady=(8, 0))

temperature_label = tk.Label(
    root,
    text="",
    font=("Arial", 42, "bold"),
    bg=root.cget("bg"),
)
temperature_label.pack(pady=(0, 8))

city_label = tk.Label(root, text="", font=("Arial", 18), bg=root.cget("bg"))
city_label.pack(pady=4)

description_label = tk.Label(root, text="", font=("Arial", 14), bg=root.cget("bg"))
description_label.pack(pady=4)

error_label = tk.Label(root, text="", font=("Arial", 12), fg="red", bg=root.cget("bg"))
error_label.pack(pady=12)

city_entry.bind("<Return>", lambda event: on_search())

root.mainloop()
