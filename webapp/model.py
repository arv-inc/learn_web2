from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        # return '<News {} {}>'.format(self.title, self.url)
        return f'<News {self.title} {self.url}'


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False, unique=True)
    observation_time = db.Column(db.String, nullable=False)
    temp_C = db.Column(db.Integer, nullable=False)
    feels_like = db.Column(db.String, nullable=True)
    windspeedKmph = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        # return '<News {} {}>'.format(self.title, self.url)
        return f'<Weather {self.observation_time} {self.city} {self.temp_C} {self.feels_like} {self.windspeedKmph}'
