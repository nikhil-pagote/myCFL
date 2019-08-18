from troposphere import GetAtt, Output, Ref, Template, Parameter, Condition 
from troposphere import Equals, And, Or, Not, If
from troposphere.iam import Role, InstanceProfile
from awacs.aws import Allow, Statement, Principal, PolicyDocument
from awacs.sts import AssumeRole

import boto3

# Create the object that will generate our template
t = Template()
t.set_description("Test to create first template using troposphere")
t.set_version("2012-10-17")


# The subnet resource defined must be added to the template
cfnrole = t.add_resource(Role(
    "my0cfl0role",
    AssumeRolePolicyDocument=PolicyDocument(
        Statement=[
            Statement(
                Effect=Allow,
                Action=[AssumeRole],
                Principal=Principal("Service", ["ec2.amazonaws.com"])
            )
        ]
    ),
    Path="/",
    MaxSessionDuration=3600,
    RoleName="my0cfl0role"
))

# Add outputs to template
#t.add_output(my0cfl0role)
#t.add_output(Output(
    #"SecretKey",
    #Value=GetAtt(my0cfl0role, "SecretAccessKey"),
    #Description="AWSSecretKey of new user",
#))

# Finally, write the template to a file
#print(t.to_yaml())
with open('role.yaml', 'w') as f:
    f.write(t.to_yaml())