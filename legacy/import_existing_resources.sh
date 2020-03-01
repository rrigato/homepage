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
    --resources-to-import file://legacy/resources/resources_to_import.txt \
    --template-body file://legacy/resources/legacy_resources.yml


aws cloudformation describe-change-set \
--change-set-name S3ImportChangeSet --stack-name prod-homepage

aws cloudformation execute-change-set \
--change-set-name S3ImportChangeSet --stack-name prod-homepage



##########################
#ResourceType = Route53 HostedZone
#LogicalResourceId = what you called the resource in
#the cloudformation template you are importing
#ResourceIdentifier = key of existing resource,
#HostedZoneId
##########################
aws cloudformation create-change-set \
    --stack-name prod-homepage --change-set-name Route53ImportChangeSet \
    --change-set-type IMPORT \
    --resources-to-import file://legacy/resources/route53_resources_to_import.txt \
    --template-body file://templates/prod_resource_import.yml
