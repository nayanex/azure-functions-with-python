import json
import logging
import os

import azure.functions as func
from bson.json_util import dumps

# importing ObjectId from bson library
from bson.objectid import ObjectId
from pymongo import MongoClient

from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Attempting to connect to MongoDB database :)")

    id = req.params.get("id")
    if not id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get("id")

    if id:
        try:
            client = MongoClient(Config.MONGO_URL)
            db = client[Config.MONGO_DB_NAME]
            notes_collection = db["notes"]

            objInstance = ObjectId(id)
            result = notes_collection.find_one({"_id": objInstance})
            result = dumps(result)

            return func.HttpResponse(
                result, mimetype="application.json", charset="utf-8", status_code=200
            )

        except ConnectionError:
            return func.HttpRequest("Bad Request", status_code=400)
