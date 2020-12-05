# terraformTest
EC2 deployment using terraform

# Files details
1. provider.tf ---> This file contains the configuration for terraform and aws config
2. variables.tf ---> This file contains Terraform variables
3. vpc.tf ---> This file create VPC, Internet GW, Public Subnet and Rout table
4. deployEC2.tf --> This file will create the Security group, search for ubuntu AMI and deploy EC2 instance

# Prerequisite to run terraform deployment
1. Install AWS CLI
2. Configure Terraform

# Steps before deploying terraform configuration
Step 1:

	Configure AWS CLI using below commands:
		aws configure set aws_access_key_id <enter_access_key>
		aws configure set aws_secret_access_key <enter_secret_access_key>
		aws configure set default.region
		aws configure set default.output

Step 2:

	Edit variable.tf & provider.tf file:
		1. Edit provider.tf with your account region
		2. Edit variables.tf with region AZs and AWS region
		3. Gerate and Edit keypair with your AWS keypair

#Step to run the terraform
Step 1:
	
	Run git clone <repo>

Step 2:
	
	Go to directory

Step 3:

	Run terraform init

Step 4:

	Run terraform apply
		** check deployment configuration and give approval as yes

Step 5:
	
	Check output for public IP, connect to the VM using your public key and IP over SSH.