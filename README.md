Personal website homepage.

- 2015 Originally a J2EE application hosted on google app engine.

- 2016 Converted to AWS elasticbeanstalk (basically lift and shift)

- 2017 Converted to statically hosted s3 bucket where the access point was cloudfront

- 2020 Refactoring to get all (or at least most) resources into cloudformation now that you can import resources that were not originally created in cloudformation.
    - Adding a CI/CD code pipeline to accomplish this

- 2022 migrate to github actions for ci/cd 

- 2023 frontend built in ReactJS

### CloudFormation Limitations


#### DeletionPolicy attribute must be string
[According to this forum post](https://forums.aws.amazon.com/message.jspa?messageID=560586)
The DeletionPolicy must be a string, this limits flexibility when trying to pass it as a parameter dependent on environment...

### Development Tooling Overview

Followed [this aws example](https://forums.aws.amazon.com/thread.jspa?threadID=228206) on how to have multiple rsa key pairs in the same local machine being used with different accounts


#### Git Secrets Scan

[git secrets](https://github.com/awslabs/git-secrets.git) is a command line utility for validating that you do not have any git credentials stored in your git repo commit history

This is useful for not only open source projects, but also to make sure best practices are being followed with limited duration credentials (IAM roles) instead of long term access keys

- Global install

```
    git init

    git remote add origin https://github.com/awslabs/git-secrets.git

    git fetch origin

    git merge origin/master

    sudo make install
```

- Web Hook install

Configuring git secrets as a web hook will ensure that git secrets runs on every commit, scanning for credentials
```
    cd ~/Documents/devdocs

    git secrets --install

    git secrets --register-aws
```



- Run a git secrets check recursively on all files in directory

```
git secrets --scan -r .
```


### Project Directory Overview
Provides information on each directory/ source file

#### builds

- buildspec_dev_homepage.yml = Creates templates/static_webpage.yml
and tests static html/webpage configuration


- buildspec_prod.yml = Prod homepage deployment




##### Buildspec Files
- buildspec_dev.yml = Buildspec to use for the development (QA)
    CodeBuild project

- buildspec_prod.yml = Buildspec to use for the prod deployment CodeBuild project



#### devops

##### images
Repository for images that relate to resources for our code pipeline

#### legacy
awscli bash scripts used to import existing resources into
cloudformation templates.

Since the website implementation was originally created outside of
cloudformation

[List of resources that can be imported into cloudformation](
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html
    )

##### Prepare Existing CloudFront for migration

Documenting various one-time setup procedures that
were required when creating a new cloudfront distribution
via cloudformation because cloudformation resource import
does not support cloudfront

Get the existing CloudFront Distribution config via
the cli:

```
aws cloudfront get-distribution-config \
--id <distribution_id> > distribution_config_backup.json
```

Lower the default and max ttl (time to live ) json file from the get-distribution-config api call as you prepare to
change the distribution.

```
aws cloudfront update-distribution \
--id <distribution_id> \
--distribution-config file://<new_distribution_config.json>\
--if-match <ETag_value_returned_by_get_config>
```

Get the existing Route53 hosted zone and associated
record sets using the following cli command:

```
#hosted zone info
aws route53 get-hosted-zone \
--id <hosted_zone_id>

#record set info
aws route53 list-resource-record-sets
--hosted-zone-id <hosted_zone_id>
```

Note that the domain servers associated with your NS
and SOA record sets must match what is listed for the domain
names you own in Route53 "Registered Domains" listing.

You can create a new hosted zone for a subdomain
Ex:
example.com
test.example.com

Each having a distinct hosted zone, just the
NS and SOA record sets must match

#### logs
- directory for python log files





#### templates



Who the user is allowed to pass the role to is limited by
the [iam:PassedToService condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html)


Note: stacks that were never initially created successfully can
only be deleted and recereated when in [ROLLBACK_COMPLETE state](https://stackoverflow.com/a/36550496)


- code_pipeline.yml = Creates CodeBuild/Code Pipeline resources
    necessary for Dev/Prod

- prod_resource_import.yml = Importing existing S3 Bucket and Route53 hosted zone to cloudformation



#### tests

- test_dev_aws_resources.py = tests dev website


- test_prod_aws_resources.py = ryanrigato.com resources and webpage
testing

#### web
Static html/js/css hosted in the s3 bucket




# detect-secrets-scan

```bash

detect-secrets scan > .secrets.baseline

detect-secrets scan | \
python3 -c "import sys, json; print(json.load(sys.stdin)['results'])"

```