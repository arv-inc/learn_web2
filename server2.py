from flask import Flask, render_template

from weather import weather_by_city
from python_org_news import get_python_news, get_html

app = Flask(__name__)


@app.route('/')
def index():
    page_title = "Новости Python"
    city_name = "Norilsk,Russia"
    weather = weather_by_city(city_name)
    city_name2 = "Saint-Petersburg,Russia"
    weather2 = weather_by_city(city_name2)
    news_list = get_python_news()
    return render_template('bootstrap.html', page_title=page_title, weather=weather, city_name=city_name, weather2=weather2, city_name2=city_name2, news_list=news_list)


if __name__ == "__main__":
    app.run(debug=True)
