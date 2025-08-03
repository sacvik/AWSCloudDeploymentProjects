## Tagging docker image with AWS account

docker build -t <your-repo-name> .
docker tag <your-repo-name>:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:latest
