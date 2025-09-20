import boto3

def lambda_handler(event, context):
    # Create EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe running EC2 instances
    response = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    # Extract instance IDs of running EC2 instances
    running_instances = [
        instance['InstanceId'] for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]
    
    # Return a summary of running EC2 instances
    return {
        'statusCode': 200,
        'body': {
            'running_ec2_instances': running_instances
        }
    }
