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

#     def validate_instance_id(self,instance_id):
#         try:
#             response = self.ec2.describe_instances(InstanceIds=[instance_id])
#             if len(response['Reservations']) == 0:
#                 print(f"Invalid instance ID: {instance_id}")
#                 return False
#             self.instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
#         except ClientError as e:
#             if e.response['Error']['Code'] == 'InvalidInstanceID.Malformed':
#                 print(f"Invalid instance ID: {instance_id}")
#             else:
#                 print(f"An error occurred: {e}")
#             return False
#         return True
#     # Place your instance ID validation code here
#     # Return True if the instance ID is valid, False otherwise
#     pass
# # # Creating an instance of the EC2Instance class with passing the AWS access keys as argument values
# ec2_instance = EC2Instance("key",'key2')