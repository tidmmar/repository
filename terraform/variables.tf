variable "public_key_path" {
  default	= "/Users/marktid/eclipse-workspace/euler/terraform/aws_linux.pub"
}

variable "key_name" {
  default	= "aws_linux.pub"
}

variable "aws_region" {
  default     = "eu-west-2"
}

# Ubuntu
variable "aws_amis" {
  default = {
    eu-west-1 = "ami-674cbc1e"
    eu-west-2 = "ami-fcc4db98"
  }
}

# Redhat
variable "aws_rh_amis" {
  default = {
    eu-west-2 = "ami-c1d2caa5"
  }
}