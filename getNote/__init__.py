import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Attempting to connect to MongoDB database :) .')

    try:
        url = """
        client = """
        database = """
        collection = """

        result = 
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application.json", charset="utf-8")
    
    except ConnectionError:
        return func.HttpRequest("Unable to connect to MongoDB", status_code=400)
