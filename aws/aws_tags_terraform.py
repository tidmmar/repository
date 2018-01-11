#
# Get AWS tags information for every EC2 resource
# Create a dictionary of AWS tags keyed by ResourceId
# Find all resources that are NOT managed by Terraform
# 
# @author tidmmar
#

import boto3

def list_tags(describe_tags):
    for t in describe_tags['Tags']: 
        seen = False
        for k in t:
            if k == 'ResourceId':
                continue
            elif k == 'ResourceType' and seen == False:
                resourceid.setdefault(t['ResourceId'],[]).insert(0, k)
                resourceid.setdefault(t['ResourceId'],[]).insert(1, t[k])
                seen = True
            elif k == 'ResourceType' and seen == True:
                continue
            else:
                resourceid.setdefault(t['ResourceId'],[]).append(k)
                resourceid.setdefault(t['ResourceId'],[]).append(t[k])
            
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
response_tags = ec2client.describe_tags()
resourceid, resourceattributes ={},[]
seen = False

list_tags(response_tags)

for i in resourceid:
    managed = False
    x = len(resourceid[i])
    tags = resourceid[i]
    while x > 0:
        if tags[x-1] == 'Terraform':
            print("Resource with id {} is managed by terraform".format(i))
            managed = True
        x -= 1
    if managed == False: print("Resource with id {} IS NOT managed by terraform".format(i))