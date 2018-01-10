#
# Some AWS instance information
# Plus a list of all VPCs and the instances that reside in each VPC 
#
# @author tidmmar
#

import boto3

def instance_in_vpc(vpcid):
    vpc = ec2.Vpc(vpcid)
    vpclist = vpc.instances.all()
    print('For VPC {} instances are:'.format(vpc.vpc_id))
    for instance in vpclist:
        print('the instance is {}'.format(instance.instance_id))
    for subnet in vpc.subnets.all():
        # if the subnet has tags use the Name of the subnet to make it easier to identify
        # try: block is needed as a TypeError is thrown if no tags exist
        try:
            for tags in subnet.tags:
                if tags["Key"] == 'Name':
                    print('The IP address range of the subnet {} is {}'.format(tags["Value"], subnet.cidr_block))
        except TypeError:
                #print('error')
                print('The IP address range of the subnet {} is {}'.format(subnet.subnet_id, subnet.cidr_block))
    print()
        
def vpc_found(vpcid):
    if vpcid in vpcs_found:
        #print('vpc {} already seen'.format(vpcid))
        #print()
        pass
    else:
        #print('adding vpc {} to the list of found VPCs'.format(vpcid))
        vpcs_found.append(vpcid)
        instance_in_vpc(vpcid)
        
        
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
vpc = ''
vpcs_found = []
response = ec2client.describe_instances()
response_vpc = ec2client.describe_vpcs()
response_tags = ec2client.describe_tags()

print('Instance Information')
for r in response['Reservations']:
    for i in r['Instances']:
        print('The instance id is {}'.format(i['InstanceId']))
        for b in i['BlockDeviceMappings']:
            print('The EBS delete on termination flag is {}'.format(b['Ebs']['DeleteOnTermination']))
    print()       
        
print('VPC Information')
for r in response['Reservations']:
    for i in r['Instances']:        
        vpcid = i['VpcId']
        if vpcid != "":
            vpc_found(i['VpcId'])

print(vpcs_found)
