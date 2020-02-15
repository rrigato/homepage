#!/bin/bash

#Gets the required parameters necessary for the
#cloudformation import
aws cloudformation get-template-summary \
    --template-body file://legacy/resources/legacy_resources.yml

##########################
#ResourceType = s3 bucket
#LogicalResourceId = what you called the resource in
#the cloudformation template you are importing
#ResourceIdentifier = key of existing resource, for s3
# the bucket name
##########################
aws cloudformation create-change-set \
    --stack-name prod-homepage --change-set-name S3ImportChangeSet \
    --change-set-type IMPORT \
    --resources-to-import "[{\"ResourceType\":\"AWS::S3::Bucket\",\"LogicalResourceId\":\"WebsiteBucket\",\"ResourceIdentifier\":{\"BucketName\":\"ryanrigato.com\"}}]" \
    --template-body file://templateToImport.json
