import boto3
import os
from boto3.dynamodb.conditions import Key
from job_site import JobSite


aws_region = os.environ.get('AWS_REGION', default='us-east-1')
dynamodb = boto3.resource('dynamodb', region_name=aws_region)
table = dynamodb.Table('jobs')

default_job_site = JobSite.INDEED.value


def get_items():
    response = table.query(
        KeyConditionExpression=Key('site_id').eq(default_job_site), Limit=50)

    return response['Items']
