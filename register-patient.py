#register-patient

import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rain-patients')

def generate_id(prefix):
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{suffix}"

def lambda_handler(event, context):
    body = json.loads(event['body'])

    patient = {
        'patient-id': generate_id('PAT'),
        'name': body['name'],
        'email': body['email'],
        'phone': body['phone']
    }

    table.put_item(Item=patient)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({
            'message': 'Patient registered successfully',
            'patient': patient
        })
    }