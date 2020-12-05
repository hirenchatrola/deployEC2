# deploy EC2 Using Cloudformation template
Deploy EC2 on AWS using CloudFormation and python script


# Files details
1. deployEC2.py ---> This file contains script to deploy the CF template
2. deployEC2.yaml ---> This file contains AWS infra configuration

# Prerequisite to run terraform deployment
1. Install AWS CLI
2. Install AWS Python boto3 lib (pip install boto3)

# Steps deploying CF configuration
Step 1:

	Configure AWS CLI using below commands:
		aws configure set aws_access_key_id <enter_access_key>
		aws configure set aws_secret_access_key <enter_secret_access_key>
		aws configure set default.region
		aws configure set default.output

Step 2:

	Below are the argument to run the script (refer: sample run command inside python script with value, you can modify as per your configuration)
		  --AMIId <AMIId>               Provide Latest AMI Id
		  --KEYName <KEYName>           Provide OpenSSH Keypair Name
		  --InstanceType <InstanceType> Provide Instance Type
		  --CIDRRange <CIDRRange>       Provide CIDRRange for VPC
		  --CIDRRangeSN <CIDRRangeSN>   Provide CIDRRange for Subnet based on VPC CIDR range
		  --Region <Region>             Provide AWS Region
		  --AZ <AZ>                     Provide AZ name
		  --Bucketname <Bucketname>     Provide S3 bucket name
		  --Templatename <Templatename> Provide CF Template name
