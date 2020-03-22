import os

import boto3
from boto3.dynamodb.conditions import Key

dynamo = boto3.resource('dynamodb')

sm = boto3.client('ssm')
""" :type : pyboto3.ssm """

table_name = os.environ['VEHICLE_REGISTRY_TABLE_NAME']


def save(input_data):
    event_lower_cased = dict((k.lower(), v) for k, v in input_data.items())
    dynamo.Table(table_name).put_item(Item=event_lower_cased)
    return [event_lower_cased]


def query(input_data):
    response = dynamo.Table(table_name).query(
        KeyConditionExpression=Key('registration-number').eq(input_data['registration-number'])
    )
    return response['Items']


actions = {
    'save': save,
    'query': query
}


def lambda_handler(event, null):
    items = actions[event['action']](event['input'])
    print(f'items: {items}')
    return {'items': items}
