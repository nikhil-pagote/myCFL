from troposphere import GetAtt, Output, Ref, Template, Equals
from troposphere.iam import ManagedPolicy

import boto3

t = Template()
t.set_description("Test to create first template using troposphere")
t.set_version("2010-09-09")

conditions = {
    "ValidateRegion": Equals(
        Ref("aws:RequestedRegion"),
        "eu-west-1"
    )
}
for k in conditions:
    t.add_condition(k, conditions[k])

t.add_resource(ManagedPolicy(
    "my0cfl0policy",
    ManagedPolicyName="my0cfl0policy",
    Path="/",
    Condition="ValidateRegion",
    PolicyDocument={
        "Version": "2012-10-17",       
        "Statement": [{
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Effect": "Allow",
            "Resource": ["arn:aws:s3:::my0cfl0bucket"]
        }],
        "Roles": "my0cfl0role"
    }
))

#print(t.to_yaml())
with open('policy.yaml', 'w') as f:
    f.write(t.to_yaml())