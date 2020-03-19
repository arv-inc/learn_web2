from flask import Flask, render_template

from webapp.model import db, News, Weather


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = "Новости Python"
        weather_list = Weather.query.all()
        news_list = News.query.order_by(News.published.desc()).all()
        # return render_template(
        #     'weather.html', page_title=page_title, weather=weather, city_name=city_name, weather2=weather2, city_name2=city_name2, news_list=news_list,
        #     weather3=weather3, city_name3=city_name3
        #     )
        return render_template(
            'weather.html', page_title=page_title, news_list=news_list,
            weather_list=weather_list
            )

    return app


# if __name__ == "__main__":
#     app.run(debug=True)
