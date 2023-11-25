#!/bin/bash

set -e

aws s3 cp --recursive . s3://ryanrigato.com 
