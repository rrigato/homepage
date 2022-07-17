#!/bin/bash

set -e


aws s3api put-object --bucket $AWS_S3_BUCKET_NAME \
  --key "favicon.ico" \
  --body "web/images/favicon.ico" \
  --content-type "image/x-icon" \
  --cache-control "max-age 60"

aws s3api put-object --bucket $AWS_S3_BUCKET_NAME \
  --key "favicon.png" \
  --body "web/images/favicon.png" \
  --content-type "image/svg+xml" \
  --cache-control "max-age 60"
