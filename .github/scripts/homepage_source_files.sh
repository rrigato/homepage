#!/bin/bash

set -e

cd dist

ls

aws s3 cp --dryrun . s3://$AWS_S3_BUCKET_NAME \
--recursive
