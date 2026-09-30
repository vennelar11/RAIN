#get-patient-history

import json
import boto3

dynamodb = boto3.resource('dynamodb')
appointments_table = dynamodb.Table('rain-appointments')
reports_table = dynamodb.Table('rain-reports')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    patient_id = body['patient-id']

    appt_response = appointments_table.scan(
        FilterExpression='#pid = :pid',
        ExpressionAttributeNames={'#pid': 'patient-id'},
        ExpressionAttributeValues={':pid': patient_id}
    )
    appointments = appt_response.get('Items', [])

    report_response = reports_table.scan(
        FilterExpression='#pid = :pid',
        ExpressionAttributeNames={'#pid': 'patient-id'},
        ExpressionAttributeValues={':pid': patient_id}
    )
    reports = report_response.get('Items', [])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({
            'appointments': appointments,
            'reports': reports
        }, default=str)
    }