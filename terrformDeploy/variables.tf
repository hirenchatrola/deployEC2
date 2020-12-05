variable "aws_region" {
	default = "ap-south-1"
}

variable "vpc_cidr" {
	default = "120.20.0.0/16"
}

variable "public_subnets_cidr" {
	default = "120.20.1.0/24"
}

variable "private_subnets_cidr" {
	default = "120.20.2.0/24"
}

variable "azs" {
	type    = "list"
	default = ["ap-south-1a", "ap-south-1b"]
}

variable "webservers_ami" {
  default = "ami-0e502bbbe5de26d28"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "keypair" {
	default = "connectVm" 
}