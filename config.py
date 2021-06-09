import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    MONGO_HOST = os.environ.get("MONGO_HOST")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME")
    MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
    MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
    MONGO_PORT = os.environ.get("MONGO_PORT")
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    FROM_EMAIL = os.environ.get("FROM_EMAIL")
    TO_EMAIL = os.environ.get("TO_EMAILS")
    ARGS = "ssl=true&retrywrites=false&ssl_cert_reqs=CERT_NONE"

    # Below URL may need some adjustments for driver version, based on your OS, if running locally
    # MONGO_URL = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?{ARGS}"
    MONGO_URL = os.environ["MyMongoDBConnectionString"]
