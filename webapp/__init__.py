from flask import Flask, render_template

from webapp.weather import weather_by_city
from webapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = "Новости Python"
        city_name = app.config["WEATHER_DEFAULT_CITY"]
        weather = weather_by_city(city_name)
        city_name2 = "Saint-Petersburg,Russia"
        weather2 = weather_by_city(city_name2)
        city_name3 = "Yeisk,Russia"
        weather3 = weather_by_city(city_name3)
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template(
            'weather.html', page_title=page_title, weather=weather, city_name=city_name, weather2=weather2, city_name2=city_name2, news_list=news_list,
            weather3=weather3, city_name3=city_name3
            )

    return app


# if __name__ == "__main__":
#     app.run(debug=True)
