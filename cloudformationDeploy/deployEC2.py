'''
python3 deployEC2.py --AMIId ami-08f63db601b82ff5f --KEYName connectVm --InstanceType t2.micro --CIDRRange 120.2.0.0/16 --CIDRRangeSN 120.2.2.0/24 --Region ap-south-1 --AZ ap-south-1a --Bucketname cloudformationtemp --Templatename deployEC2.yaml
'''

import os
import sys
import traceback
import logging
import time
from datetime import datetime
from time import gmtime, strftime
from argparse import ArgumentParser
import boto3

parser = ArgumentParser()

parser.add_argument("--AMIId", dest="AMIId", required=True, metavar="<AMIId>", help="Provide Latest AMI Id")
parser.add_argument("--KEYName", dest="KEYName", required=True, metavar="<KEYName>", help="Provide OpenSSH Keypair Name")
parser.add_argument("--InstanceType", dest="InstanceType", required=True, metavar="<InstanceType>", help="Provide Instance Type")
parser.add_argument("--CIDRRange", dest="CIDRRange", required=True, metavar="<CIDRRange>", help="Provide CIDRRange for VPC")
parser.add_argument("--CIDRRangeSN", dest="CIDRRangeSN", required=True, metavar="<CIDRRangeSN>", help="Provide CIDRRange for Subnet based on VPC CIDR range")
parser.add_argument("--Region", dest="Region", required=True, metavar="<Region>", help="Provide AWS Region")
parser.add_argument("--AZ", dest="AZ", required=True, metavar="<AZ>", help="Provide AZ name")
parser.add_argument("--Bucketname", dest="Bucketname", required=True, metavar="<Bucketname>", help="Provide S3 bucket name")
parser.add_argument("--Templatename", dest="Templatename", required=True, metavar="<Templatename>", help="Provide CF Template name")

args = parser.parse_args()

# Function to print the state for CF template creation
def get_stack_status(cloudformation, stack_name):
    ret = 0

    while True:
        stack = cloudformation.Stack(stack_name)
        #print stack
        if (stack.stack_status.find("CREATE_COMPLETE") != -1) :
            logging.info( "Stack creation completed...")
            print("Stack creation completed...")
            ret = 0
            break
        elif (stack.stack_status.find("CREATE_IN_PROGRESS") != -1) :
            logging.info( "Stack creation is in progress ... ")
            print("Stack creation is in progress ... ")
            time.sleep(10)
        # added below elif conditions for update stack status check
        elif (stack.stack_status.find("UPDATE_IN_PROGRESS") != -1) :
            logging.info( "Stack update is in progress ... ")
            print("Stack update is in progress ... ")
            time.sleep(10)
        elif (stack.stack_status.find("UPDATE_COMPLETE") != -1) :
            logging.info( "Stack update is in progress ... ")
            print("Stack update is in progress ... ")
            time.sleep(10)
            break
        elif (stack.stack_status.find("DELETE_IN_PROGRESS") != -1) :
            logging.info( "Stack update is in progress ... ")
            print("Stack update is in progress ... ")
            time.sleep(10)
        elif (stack.stack_status.find("DELETE_COMPLETE") != -1) :
            logging.info( "Stack update is in progress ... ")
            print("Stack update is in progress ... ")
            time.sleep(10)    	
        elif (stack.stack_status.find("UPDATE_COMPLETE_CLEANUP_IN_PROGRESS") != -1) :
            logging.info( "Stack update is in progress ... ")
            print("Stack update is in progress ... ")
            time.sleep(10)
        # added above elif conditions for update stack status check
        else:
            #print stack.stack_status
            logging.error( "Stack creation failed with below status: %s", stack.stack_status)
            print("Stack creation failed with below status: %s", stack.stack_status)
            ret  = 1
            raise OSError("Stack creation failed RollBack in progress.")
            break
    
    return ret

# Deploy EC2 using CF Template
def deployEC2():
	input_params = dict()
	input_params['AMIId'] = args.AMIId
	input_params['KEYName'] = args.KEYName
	input_params['InstanceType'] = args.InstanceType
	input_params['CIDRRange'] = args.CIDRRange
	input_params['CIDRRangeSN'] = args.CIDRRangeSN
	input_params['AZ'] = args.AZ
	input_params['templateUrl'] = "https://" + args.Bucketname + ".s3." + args.Region + ".amazonaws.com/" + args.Templatename + ".yaml"
	input_params['stackName'] = args.Templatename +""+ datetime.now().strftime("-%Y-%m-%d-%H-%M")

	cloudformation = boto3.resource('cloudformation')
	cloudformation.create_stack(StackName=input_params['stackName'], \
												TemplateURL=input_params['templateUrl'], \
												Parameters=
												[{'ParameterKey': 'AMIId','ParameterValue' : input_params['AMIId']},
												 {'ParameterKey': 'KEYName','ParameterValue': input_params['KEYName']},
												 {'ParameterKey': 'InstanceType','ParameterValue' : input_params['InstanceType']},
												 {'ParameterKey': 'CIDRRange','ParameterValue' : input_params['CIDRRange']},
												 {'ParameterKey': 'CIDRRangeSN','ParameterValue' : input_params['CIDRRangeSN']},
												 {'ParameterKey': 'AZ','ParameterValue' : input_params['AZ']}
												 ],
												Capabilities=['CAPABILITY_IAM']
											   )
	get_stack_status(cloudformation, input_params['stackName'])

if __name__ == '__main__':
	deployEC2()