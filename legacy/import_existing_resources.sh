#!/bin/bash

#Gets the required parameters necessary for the
#cloudformation import
aws cloudformation get-template-summary \
    --template-body file://legacy/resources/legacy_resources.yml
