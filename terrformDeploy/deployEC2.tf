# Security group
resource "aws_security_group" "server" {
  name        = "allow_ssh"
  description = "Allow ssh inbound traffic"
  vpc_id      = "${aws_vpc.main.id}"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}

# Select AMI from filter
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# Deploy instance
resource "aws_instance" "testVm" {
  ami                          = "${data.aws_ami.ubuntu.id}"
  instance_type                = "${var.instance_type}"
  security_groups              = ["${aws_security_group.server.id}"]
  subnet_id                    = "${aws_subnet.public.id}"
  key_name                     = "${var.keypair}"
  associate_public_ip_address  = true

  root_block_device {
    volume_type = "gp2"
    volume_size = "40"
  }

  tags = {
    Name = "TestVM"
  }
}

# Connect using this ip and Private pem key
output "ip" {
  description = "SSH using below IP address"
  value = aws_instance.testVm.public_ip
}