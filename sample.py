import json

def lambda_handler(event, context):
    # Retrieve a message from the event object if provided
    message = event.get('message', 'Hello from AWS Lambda!')

    response = {
        'statusCode': 200,
        'body': json.dumps(message)
    }

    return response

