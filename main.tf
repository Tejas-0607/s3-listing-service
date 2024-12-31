provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-flask-bucket"
  acl    = "private"
}

resource "aws_instance" "flask_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "your-keypair"
  security_groups = [aws_security_group.flask_sg.name]
}

resource "aws_security_group" "flask_sg" {
  name_prefix = "flask-app-sg"
  description = "Allow HTTP and SSH inbound traffic"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

