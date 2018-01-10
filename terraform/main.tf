# Specify the provider and access details
provider "aws" {
  region = "${var.aws_region}"
}

# Create a VPC to launch our instances into
resource "aws_vpc" "default" {
  cidr_block = "10.0.0.0/16"
  tags   = {
  	Name = "TestEnvVPC"
  	Terraform = "True"
  	}
}

# Create an internet gateway to give our subnet access to the outside world
resource "aws_internet_gateway" "default" {
  vpc_id = "${aws_vpc.default.id}"
  tags   = {
  	Name = "TestEnvGateway"
  	Terraform = "True"
  	}
}

# Grant the VPC internet access on its main route table
resource "aws_route" "internet_access" {
  route_table_id         = "${aws_vpc.default.main_route_table_id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = "${aws_internet_gateway.default.id}"
}

# Create a routing table from public to private subnet
resource "aws_route_table" "TestEnv" {
  vpc_id = "${aws_vpc.default.id}"
  tags {
    Name = "TestEnv_route"
    Terraform = "True"
  }
}

# Create a subnet to launch instances into
resource "aws_subnet" "public" {
  vpc_id                  = "${aws_vpc.default.id}"
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  tags					  = {
  	Name = "TestEnvPublicSubnet"
  	Terraform = "True"
  	}
}

# Create a private subnet to launch instances into
resource "aws_subnet" "private" {
  vpc_id                  = "${aws_vpc.default.id}"
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = false
  tags					  = {
  	Name = "TestEnvPrivateSubnet"
  	Terraform = "True"
  	}
}

# A security group for the ELB so it is accessible via the web
resource "aws_security_group" "elb" {
  name        = "test_env_elb"
  description = "ELB points to EC2 resource on public subnet"
  vpc_id      = "${aws_vpc.default.id}"
  tags		 = {
  	Terraform = "True"
  	}

  # HTTP access from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# A security group to access
# the public instance over SSH and HTTP
resource "aws_security_group" "public" {
  name        = "test_env_public_SG"
  description = "SSH and HTTP access"
  vpc_id      = "${aws_vpc.default.id}"
  tags		 = {
  	Terraform = "True"
  	}

  # SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP access from the VPC
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# A security group to access
# the private subnet from the public subnet
resource "aws_security_group" "private" {
  name        = "test_env_private_SG"
  description = "SSH"
  vpc_id      = "${aws_vpc.default.id}"
  tags		 = {
  	Terraform = "True"
  	}

 # SSH access from public subnet
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
 }
  
/*
resource "aws_elb" "web" {
  name = "test-env-elb"

  subnets         = ["${aws_subnet.public.id}"]
  security_groups = ["${aws_security_group.elb.id}"]
  instances       = ["${aws_instance.web.id}"]

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }
}*/

resource "aws_key_pair" "auth" {
  key_name   = "${var.key_name}"
  public_key = "${file(var.public_key_path)}"
}


	
resource "aws_instance" "web" {
  # The connection block tells our provisioner how to
  # communicate with the resource (instance)
  connection {
    # The default username for our AMI
    user = "ubuntu"

    # The connection will use the local SSH agent for authentication.
  }

  instance_type = "t2.micro"
  iam_instance_profile = "S3_Admin_Access"

  # Lookup the correct AMI based on the region
  ami = "${lookup(var.aws_amis, var.aws_region)}"

  # The id of the SSH public key.
  key_name = "${aws_key_pair.auth.id}"

  # Security group to allow HTTP and SSH access
  vpc_security_group_ids = ["${aws_security_group.public.id}"]

  # We're going to launch into the public subnet as it has internet access
  # and it's the same as the ELB (when uncommented).
  subnet_id = "${aws_subnet.public.id}"
}

resource "aws_instance" "backend" {
  connection {
    # The default username for our AMI
    user = "ubuntu"

    # The connection will use the local SSH agent for authentication.
  }

  instance_type = "t2.micro"
  iam_instance_profile = "S3_Admin_Access"

  # Lookup the correct AMI based on the region
  # we specified
  ami = "${lookup(var.aws_amis, var.aws_region)}"

  # The name of our SSH keypair we created above.
  key_name = "${aws_key_pair.auth.id}"

  # Our Security group to allow HTTP and SSH access
  vpc_security_group_ids = ["${aws_security_group.private.id}"]

  # launch the instance into the private subnet
  subnet_id = "${aws_subnet.private.id}"

}