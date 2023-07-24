```python
import boto3

def create_ec2_instance():
    try:
        ec2_resource = boto3.resource('ec2')

        instances = ec2_resource.create_instances(
            ImageId='ami-0abcdef1234567890',  # replace with your AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='my-key-pair',  # replace with your key pair name
            SubnetId='subnet-06a692ed4ef84368d'  # replace with your subnet id
        )

        print('New instance created:', instances[0].id)

    except Exception as e:
        print('Error creating instance:', e)


def create_s3_bucket(bucket_name):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.create_bucket(Bucket=bucket_name)

        print('New bucket created:', response['Location'])

    except Exception as e:
        print('Error creating bucket:', e)


def main():
    create_ec2_instance()
    create_s3_bucket('ai-powered-travel-booker')  # replace with your bucket name


if __name__ == '__main__':
    main()
```