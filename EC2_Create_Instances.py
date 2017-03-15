#!/usr/local/Cellar/python/2.7.13/bin/python
import boto3
ec2 = boto3.resource('ec2')
ec2.create_instances(
	ImageId='ami-4e686b2d', 
	MinCount=1, 
	MaxCount=5, 
	InstanceType='t2.micro', 
	KeyName='augfront_core', 
	SubnetId='subnet-828b0ee6')
