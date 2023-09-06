import boto3
from botocore.exceptions import ClientError




# Defining a class for EC2 instances
class EC2Instance:
         # Constructor function to initialize the object
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        # Storing the AWS access keys as instance variables
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        # Creating an EC2 client using the access keys and the desired region
        self.ec2 = boto3.client('ec2', 
                                aws_access_key_id=self.aws_access_key_id, 
                                aws_secret_access_key=self.aws_secret_access_key, 
                                region_name='us-east-1')


    def validate_instance_id(self, instance_id):
        try:
            # Use the EC2 client to describe the instance and check if it exists
            response = self.ec2.describe_instances(InstanceIds=[instance_id])
            reservations = response.get('Reservations', [])
            instances = sum((reservation.get('Instances', []) for reservation in reservations), [])
            if instances:
                return True  # The instance with the given ID exists
            else:
                return False  # The instance with the given ID does not exist
        except ClientError:
            return False  # An error occurred, indicating an invalid instance ID
 
    def start_instance(self, instance_id):
        try:
            # Use the EC2 client to start the instance
            self.ec2.start_instances(InstanceIds=[instance_id])
            return True  # Instance start request successful
        except ClientError:
            return False  # An error occurred, indicating unsuccessful instance start request
        
    def stop_instance(self, instance_id):
        try:
            response = self.ec2.stop_instances(InstanceIds=[instance_id])
            stopping_instances = response.get('StoppingInstances', [])
            if stopping_instances and stopping_instances[0]['CurrentState']['Name'] == 'stopping':
                return True  # Instance stop request successful
            else:
                return False  # Failed to stop the instance
        except ClientError as e:
            print(f"Error stopping instance: {e}")
            return False  # An error occurred, indicating unsuccessful instance stop request
  
    def describe_instance_state(self, instance_id):
        response = self.ec2.describe_instances(InstanceIds=[instance_id])
        instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        return instance_state
    
    def wait_for_instance_state(self, instance_id, state):
        waiter = self.ec2.get_waiter('instance_stopped' if state == 'stopped' else 'instance_running')
        waiter.wait(InstanceIds=[instance_id])