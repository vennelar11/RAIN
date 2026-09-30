#book-appointment

import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rain-appointments')

def generate_id(prefix):
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{suffix}"

def lambda_handler(event, context):
    body = json.loads(event['body'])
    doctor_name = body['doctor-name']
    date = body['date']
    time = body['time']

    existing = table.scan(
        FilterExpression='#d = :doc AND #dt = :date AND #t = :time AND #s = :status',
        ExpressionAttributeNames={'#d': 'doctor-name', '#dt': 'date', '#t': 'time', '#s': 'status'},
        ExpressionAttributeValues={':doc': doctor_name, ':date': date, ':time': time, ':status': 'scheduled'}
    )

    if existing.get('Items'):
        return {
            'statusCode': 409,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
            },
            'body': json.dumps({'message': f'{doctor_name} is already booked at {time} on {date}. Please choose another slot.'})
        }

    appointment = {
        'appointment-id': generate_id('APT'),
        'patient-id': body['patient-id'],
        'doctor-name': doctor_name,
        'date': date,
        'time': time,
        'status': 'scheduled'
    }

    table.put_item(Item=appointment)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({
            'message': 'Appointment booked successfully',
            'appointment': appointment
        })
    }