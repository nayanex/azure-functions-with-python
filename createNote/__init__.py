import logging

import azure.functions as func
import pymongo

from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Attempting to create a new Note instance.")

    request = req.get_json()

    if request:
        try:
            # add your connection string here
            client = pymongo.MongoClient(Config.MONGO_URL)

            # you will need this fill in
            database = client[Config.MONGO_DB_NAME]
            notes_collection = database["notes"]

            # replace the insert_one variable with what you think should be in the bracket
            notes_collection.insert_one(request)

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse("Database connection error.", status_code=500)
    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400,
        )
