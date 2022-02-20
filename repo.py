import boto3
from boto3.dynamodb.conditions import Key
from job_site import JobSite

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jobs')

default_job_site = JobSite.INDEED.value


def get_items():
    response = table.query(
        KeyConditionExpression=Key('site_id').eq(default_job_site))

    return response['Items']
