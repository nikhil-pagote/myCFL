from troposphere import GetAtt, Output, Ref, Template, Parameter, Condition 
from troposphere import Equals, And, Or, Not, If
from troposphere.iam import Role, InstanceProfile
from awacs.aws import Allow, Statement, Principal, PolicyDocument
from awacs.sts import AssumeRole

import boto3

#Define parameters here.
parameters = {
    "One": Parameter(
        "One",
        Type="String",
    ),
    "Two": Parameter(
        "Two",
        Type="String",
    ),
    "Three": Parameter(
        "Three",
        Type="String",
    ),
    "Four": Parameter(
        "Four",
        Type="String",
    ),
    "SshKeyName": Parameter(
        "SshKeyName",
        Type="String",
    )
}

#Define conditions here.
conditions = {
    "ValidateRegion": Equals(
        Ref("AWS::Region"),
        "eu-west-1"
    ),
    "NotOneEqualsFoo": Not(
        Condition("OneEqualsFoo")
    ),
    "BarEqualsTwo": Equals(
        "Bar",
        Ref("Two")
    ),
    "ThreeEqualsFour": Equals(
        Ref("Three"),
        Ref("Four")
    ),
    "OneEqualsFooOrBarEqualsTwo": Or(
        Condition("OneEqualsFoo"),
        Condition("BarEqualsTwo")
    ),
    "OneEqualsFooAndNotBarEqualsTwo": And(
        Condition("OneEqualsFoo"),
        Not(Condition("BarEqualsTwo"))
    ),
    "OneEqualsFooAndBarEqualsTwoAndThreeEqualsPft": And(
        Condition("OneEqualsFoo"),
        Condition("BarEqualsTwo"),
        Equals(Ref("Three"), "Pft")
    ),
    "OneIsQuzAndThreeEqualsFour": And(
        Equals(Ref("One"), "Quz"),
        Condition("ThreeEqualsFour")
    ),
    "LaunchInstance": And(
        Condition("OneEqualsFoo"),
        Condition("NotOneEqualsFoo"),
        Condition("BarEqualsTwo"),
        Condition("OneEqualsFooAndNotBarEqualsTwo"),
        Condition("OneIsQuzAndThreeEqualsFour")
    ),
    "LaunchWithGusto": And(
        Condition("LaunchInstance"),
        Equals(Ref("One"), "Gusto")
    )
}
# Create the object that will generate our template
t = Template()


t.set_description("Test to create first template using troposphere")
t.set_version("2012-10-17")
t.add_condition

#Add parameters, condition to template
for p in parameters.values():
    t.add_parameter(p)
for k in conditions:
    t.add_condition(k, conditions[k])
#for r in resources.values():
    #t.add_resource(r)

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
    RoleName="my0cfl0role",
    #Condition="ValidateRegion"
))

# Add outputs to template
#t.add_output(my0cfl0role)
#t.add_output(Output(
    #"SecretKey",
    #Value=GetAtt(cfnkeys, "SecretAccessKey"),
    #Description="AWSSecretKey of new user",
#))


# Finally, write the template to a file
#print(t.to_yaml())
with open('role.yaml', 'w') as f:
    f.write(t.to_yaml())