## Authenticate Docker to ECR
aws ecr get-login-password --region <region> | \
    docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

## push image to AWS
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:latest

