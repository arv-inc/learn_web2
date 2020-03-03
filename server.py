from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    page_title = "Прогноз погоды"
    city_name = "Norilsk,Russia"
    weather = weather_by_city("Norilsk,Russia")
    if weather:
        weather_text = f"Погода в {city_name}: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text = "Сервис погоды временно недоступен"
    return weather_text
if __name__ == "__main__":
    app.run(debug=True)
