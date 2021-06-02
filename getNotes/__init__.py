import json
import logging
import os

import azure.functions as func
from bson.json_util import dumps
from pymongo import MongoClient

from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Attempting to connect to MongoDB database :)")

    try:
        client = MongoClient(Config.connection_uri)
        db = client[Config.MONGO_DB_NAME]
        notes_collection = db["notes"]

        result = notes_collection.find({})
        result = dumps(result)

        return func.HttpResponse(
            result, mimetype="application/json", charset="utf-8", status_code=200
        )

    except ConnectionError:
        return func.HttpRequest("Unable to connect to MongoDB", status_code=400)
