#!/bin/bash

set -e

cd dist

ls

aws s3 cp --dry-run . $AWS_S3_BUCKET_NAME \
--recursive
