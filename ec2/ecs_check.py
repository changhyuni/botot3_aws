import boto3

ecs_client = boto3.client('ecs', 'ap-northeast-2')
cluster_info = ecs_client.list_clusters()['clusterArns']

### 딕셔너리 형태로 정보만 빼올수 있다면, 여러 서비스에서 사용이 가능하다.

for cluster in cluster_info:
        clustername = cluster.split('/')[1]
        services = ecs_client.list_services(cluster=clustername)['serviceArns']
        if services:
            service_names = ecs_client.describe_services(cluster=cluster, services=services)['services']
            for service in service_names:
                print(service['desiredCount'])
                print(service['runningCount'])
