## Tagging docker image with AWS account

#!/bin/bash
set -ex

# Variables - replace with your actual values
REPO_NAME=model_prediction
AWS_ACCOUNT_ID="<account id here>"  # Replace with your AWS account ID
REGION=us-west-2 # Replace with your desired AWS region

## Authenticate Docker to ECR
aws ecr get-login-password --region $REGION | \
    docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

## push image to AWS
docker push $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest


echo "Docker image pushed to AWS!"

