import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='awssnap')
    ec2 = session.resource('ec2')