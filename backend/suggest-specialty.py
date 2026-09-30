#suggest-specialty

import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    symptoms = body['symptoms'].lower()

    if any(word in symptoms for word in ['chest pain', 'shortness of breath', 'palpitations', 'heart']):
        suggestion = 'Cardiology'
    elif any(word in symptoms for word in ['rash', 'itching', 'skin', 'acne']):
        suggestion = 'Dermatology'
    elif any(word in symptoms for word in ['child', 'infant', 'baby', 'fever in kid']):
        suggestion = 'Pediatrics'
    else:
        suggestion = 'General Medicine'

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
        },
        'body': json.dumps({'suggested_specialty': suggestion})
    }