#!/usr/local/Cellar/python/2.7.13/bin/python
import boto3
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)