import boto3

### client import & boto3 Filters
ec2_client = boto3.client('ec2',region_name='ap-northeast-2')
response = ec2_client.describe_volumes(
    Filters = [{
        'Name': 'status',
        'Values': ['available'],
    }]
)
lst = response['Volumes']
volume_ids = []

### Add Snapshot
for volumes in lst:
    volume_ids.append(volumes['VolumeId'])
    

for sanp in volume_ids:
    snapshots = ec2_client.create_snapshot(VolumeId=sanp)