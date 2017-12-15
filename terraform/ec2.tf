
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "eu-west-2"
}

resource "aws_instance" "dev_host1" {
  ami           = "ami-e7d6c983"
  instance_type = "t2.micro"
}