import json
import logging

from fastapi import FastAPI
from mangum import Mangum

# Set up proper logger
logger = logging.getLogger("lambda-handler")
logger.setLevel(logging.DEBUG)

app = FastAPI(
    title="Authentication API",
    description="""
    """,
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "User management and authentication",
        },
    ]
)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # Use the logger you've defined
    logger.debug(f"API Event: {event}")
    
    # Rest of your handler code...
    handler = Mangum(app)
    response = handler(event, context)
    return response

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.get("/users")
def get_users():
    return {"users": ["user1", "user2"]}

@app.post("/items")
def create_item():
    return {"status": "created"}
