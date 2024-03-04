from flask import request
from flask_restful import Resource

from models.models import LogSchema, db, LogModel

log_schema = LogSchema()

class BaseSection(Resource):
    def get(self):
        logs = LogModel.query.all()
        print(logs)
        return {"api_code": "1", "mensaje": "Service is UP."}
