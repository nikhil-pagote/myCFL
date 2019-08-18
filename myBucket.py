from troposphere import GetAtt, Output, Ref, Template
from troposphere.iam import ManagedPolicy

import boto3

t = Template()

t.set_description("Test to create first template using troposphere")
t.add_resource(ManagedPolicy(
    "EnriquePolicy",
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "cloudformation:Describe*",
                "cloudformation:List*",
                "cloudformation:Get*"
            ],
            "Resource": "*"
        }],
    }
))


#cfn = boto3.client('cloudformation', region_name='eu-west-1')
#response = cfn.create_stack(
    #StackName="EnriquePolicyCreationTest",
    #TemplateBody=t.to_json(),
    #Capabilities=[
        #'CAPABILITY_IAM'
        #],
    #OnFailure='DELETE'
#)
#print(response)
print(t.to_yaml())