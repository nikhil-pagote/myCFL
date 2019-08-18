Prerequisite:
1. S3 bucket should be available.

Steps:
1. create policy first.
2. Create role next

aws cloudformation create-stack --stack-name learncf-subnet --template-body file://learncf-subnet.yaml
aws cloudformation create-stack --stack-name learncf-ec2    --template-body file://learncf-ec2.yaml

Pseudo Parameters Reference:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html