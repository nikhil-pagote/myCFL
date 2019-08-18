from troposphere import GetAtt, Output, Ref, Template
from troposphere.iam import ManagedPolicy

import boto3

t = Template()
t.set_description("Test to create first template using troposphere")
t.set_version("2012-10-17")

t.add_resource(ManagedPolicy(
    "my0cfl0policy",
    PolicyName="my0cfl0policy",
    PolicyDocument={
        "Version": "2012-10-17",       
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": ["arn:aws:s3:::my0cfl0bucket"]
        }],
        "Roles": "my0cfl0role"
    }
))

#print(t.to_yaml())
with open('policy.yaml', 'w') as f:
    f.write(t.to_yaml())