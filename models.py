from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)

class Farm(db.Model):
    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String)

    foods = db.relationship('Food', backref='farm', lazy=True)

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, city={self.city}'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

foods_seasons = db.Table('foods_seasons',
    db.Column('food_id', db.Integer, db.ForeignKey('fodss.id'), primary_key=True),
    db.Column('season_id', db.Integer, db.ForeignKey('seasons.id'), primary_key=True)
)

class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    nutrients = db.Column(db.String, nullable=False)
    food_group = db.Column(db.String, nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id', ondelete='SET NULL'))

    seasons = db.relationship('Season',
        secondary=foods_seasons,
        lazy='subquery', 
        backref=db.backref('posts', lazy=True)
    )
    
    def __repr__(self):
        return f'Post(id={self.id}, name="{self.name}", nutrients="{self.nutrients}"...)'
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nutrients': self.nutrients,
            'food_group': self.food_group,
            'farm': self.farm.as_dict(),
            'seasons': [season.as_dict()["season"] for season in self.seasons]
        }

class Season(db.Model):
    __tablename__ = 'seasons'

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'Season(id={self.id}, season="{self.season}")'

    def as_dict(self):
        return {'id': self.id, 'season': self.season}

def get_or_create(model, defaults=None, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items())
        params.update(defaults or {})
        instance = model(**params)
        db.session.add(instance)
        db.session.commit()
        return instance, True

