Personal website homepage.

- 2015 Originally a J2EE application hosted on google app engine.

- 2016 Converted to AWS elasticbeanstalk (basically lift and shift)

- 2017 Converted to statically hosted s3 bucket where the access point was cloudfront

- 2020 Refactoring to get all (or at least most) resources into cloudformation now that you can import resources that were not originally created in cloudformation.
    - Adding a CI/CD code pipeline to accomplish this

- 2022 migrate to github actions for ci/cd 

- 2023 frontend built in ReactJS



## scan-git-repo-for-secrets

[git secrets](https://github.com/awslabs/git-secrets.git) command line utility adds a git hook to make sure you haven't commited any aws credentials


- [install script](requirements/git_secrets.sh)


- Scan before making repo public

```
git secrets --scan-history
```


### Project Directory Overview
Provides information on each directory/ source file




#### templates



Who the user is allowed to pass the role to is limited by
the [iam:PassedToService condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html)


Note: stacks that were never initially created successfully can
only be deleted and recereated when in [ROLLBACK_COMPLETE state](https://stackoverflow.com/a/36550496)


- code_pipeline.yml = Creates CodeBuild/Code Pipeline resources
    necessary for Dev/Prod

- prod_resource_import.yml = Importing existing S3 Bucket and Route53 hosted zone to cloudformation




#### web
Static html/js/css hosted in the s3 bucket




# detect-secrets-scan

```bash

detect-secrets scan > .secrets.baseline

detect-secrets scan | \
python3 -c "import sys, json; print(json.load(sys.stdin)['results'])"

```