
Personal website homepage.

- 2015 Originally a J2EE application hosted on google app engine.

- 2016 Converted to AWS elasticbeanstalk (basically lift and shift)

- 2017 Converted to statically hosted s3 bucket where the access point was cloudfront

- 2020 Refactoring to get all (or at least most) resources into cloudformation now that you can import resources that were not originally created in cloudformation.
    - Adding a CI/CD code pipeline to accomplish this

### Development Tooling Overview
#### cfn-lint (cloudformation Linting)
[cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint.git) Provides yaml/json cloudformation validation and checks for best practices

- Install

```
    pip install cfn-lint
```

- Run on a file
```
    cfn-lint <filename.yml>

    cfn-lint templates/code_pipeline.yml
```

- Run on all files in Directory
```
    cfn-lint templates/*.yml
```


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

##### py
    Directory for custom python scripts that setup build configuration



##### Buildspec Files
- buildspec_dev.yml = Buildspec to use for the development (QA)
    CodeBuild project

- buildspec_prod.yml = Buildspec to use for the prod deployment CodeBuild project

#### docs


#### devops



#### logs
- directory for python log files





#### templates



Who the user is allowed to pass the role to is limited by
the [iam:PassedToService condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html)


Note: stacks that were never initially created successfully can
only be deleted and recereated when in [ROLLBACK_COMPLETE state](https://stackoverflow.com/a/36550496)


- code_pipeline.yml = Creates CodeBuild/Code Pipeline resources
    necessary for Dev/Prod


#### tests




#### Setup Continuous Integration

Add the remote repo using the following:
```
git init

git remote add origin <origin_url_or_ssh>

```


Fetch origin repo locally and merge if the remote

has any references you do not

```
    git fetch origin

    git merge origin/<branch_name>
```



#### Setup Infrastructure
