### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID= AKIAQQ54HIH2KPGJ6WBA

AWS_SECRET_ACCESS_KEY= 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

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 036365091316.dkr.ecr.us-east-1.amazonaws.com/networksecurity
ECR_REPOSITORY_NAME = networksecurity


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker