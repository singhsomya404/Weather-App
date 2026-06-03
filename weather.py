from tkinter import *

# Weather data
weather_data = {
    "Pune": {
        "Temperature": "28°C",
        "Weather": "☀ Sunny",
        "Humidity": "45%",
        "Wind": "12 km/h"
    },

    "Mumbai": {
        "Temperature": "31°C",
        "Weather": "☁ Cloudy",
        "Humidity": "70%",
        "Wind": "18 km/h"
    },

    "Delhi": {
        "Temperature": "35°C",
        "Weather": "🔥 Hot",
        "Humidity": "40%",
        "Wind": "10 km/h"
    },

    "Chennai": {
        "Temperature": "33°C",
        "Weather": "🌧 Rainy",
        "Humidity": "80%",
        "Wind": "20 km/h"
    },

    "Nagpur": {
        "Temperature": "30°C",
        "Weather": "☀ Sunny",
        "Humidity": "50%",
        "Wind": "14 km/h"
    }
}

# Function
def show_weather():
    city = city_entry.get().strip().title()

    if city in weather_data:
        data = weather_data[city]

        result.config(
            text=f"""
📍 City : {city}

🌡 Temperature : {data['Temperature']}

🌤 Weather : {data['Weather']}

💧 Humidity : {data['Humidity']}

🌬 Wind Speed : {data['Wind']}
""",
            fg="white",
            bg="#1e3d59"
        )

    else:
        result.config(
            text="❌ City data not available",
            fg="yellow",
            bg="#1e3d59"
        )


# Main window
root = Tk()
root.title("Weather App")
root.geometry("450x500")
root.config(bg="#0f3460")

# Heading
heading = Label(
    root,
    text="🌦 Weather App",
    font=("Arial", 24, "bold"),
    bg="#0f3460",
    fg="white"
)
heading.pack(pady=20)

# City label
city_label = Label(
    root,
    text="Enter City Name",
    font=("Arial", 14),
    bg="#0f3460",
    fg="white"
)
city_label.pack()

# Entry box
city_entry = Entry(
    root,
    font=("Arial", 16),
    width=20,
    justify="center",
    bd=3
)
city_entry.pack(pady=15)

# Button
search_btn = Button(
    root,
    text="Show Weather",
    font=("Arial", 14, "bold"),
    bg="#ffcc00",
    fg="black",
    padx=10,
    pady=5,
    command=show_weather
)
search_btn.pack(pady=10)

# Result box
result = Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    justify=LEFT,
    bg="#1e3d59",
    fg="white",
    width=30,
    height=12,
    relief=RIDGE,
    bd=4
)
result.pack(pady=25)

# Footer
footer = Label(
    root,
    text="Made with Python & Tkinter",
    font=("Arial", 10),
    bg="#0f3460",
    fg="lightgray"
)
footer.pack(side=BOTTOM, pady=10)

# Run app
root.mainloop()
