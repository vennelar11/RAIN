#upload-report

import json
import boto3
import random
import string
import base64
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rain-reports')
BUCKET_NAME = 'rain-medical-reports'

def generate_id(prefix):
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{suffix}"

def lambda_handler(event, context):
    body = json.loads(event['body'])

    file_content = base64.b64decode(body['file-content'])
    file_name = body['file-name']
    patient_id = body['patient-id']

    report_id = generate_id('REP')
    s3_key = f"{patient_id}/{report_id}-{file_name}"

    s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=file_content)

    report = {
        'report-id': report_id,
        'patient-id': patient_id,
        'file-name': file_name,
        's3-key': s3_key,
        'uploaded-at': datetime.utcnow().isoformat()
    }

    table.put_item(Item=report)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({
            'message': 'Report uploaded successfully',
            'report': report
        })
    }