## Tagging docker image with AWS account

#!/bin/bash
set -ex

# Variables - replace with your actual values
REPO_NAME=model_prediction
AWS_ACCOUNT_ID="<account id here>"  # Replace with your AWS account ID
REGION=us-west-2

# Build the Docker image
docker build -t $REPO_NAME .

# Tag the Docker image
docker tag $REPO_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest

echo "Docker image built and tagged successfully!"
