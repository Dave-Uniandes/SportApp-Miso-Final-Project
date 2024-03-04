from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class LogModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = name = db.Column(db.String(150))

class LogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LogModel
        include_relationships = True
        load_instance = True