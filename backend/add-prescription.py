#add-prescription

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rain-appointments')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    table.update_item(
        Key={'appointment-id': body['appointment-id']},
        UpdateExpression='SET prescription = :p, #s = :status',
        ExpressionAttributeNames={'#s': 'status'},
        ExpressionAttributeValues={
            ':p': body['prescription'],
            ':status': 'completed'
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({'message': 'Prescription added successfully'})
    }