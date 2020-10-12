import boto3

ec2_client = boto3.client('ec2', region_name = 'ap-northeast-2')
response = ec2_client.describe_instances()
instances = response['Reservations']
instance_ids = []

for instance in instances:
    instance_ids.append(instance['Instances'][0]['InstanceId'])

tage_creation = ec2_client.create_tags(

        Resources =
            instance_ids,
        Tags = [
            {
                'Key' : 'Changman',
                'Value' : 'hi',
                'Key' : 'Operation',
                'Value' : 'Start',
                'Key' : 'Name',
                'Value' : 'CHANG',
            }
            ]
        )

print(instances)
