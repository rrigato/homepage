#!/bin/bash

set -e

aws s3 cp --recursive ./dist s3://ryanrigato.com 
