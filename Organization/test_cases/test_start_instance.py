from django.shortcuts import redirect, get_object_or_404
from ..members.models import Team, Instance
from members.ec2_class import EC2Instance
from ..members import config



def start_instance_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    instance = team.instance_set.first()  # Get the first instance associated with the team
    if instance:
        instance_id = instance.instance_id
        
        # Check if it is a testing environment
        is_testing = 'test' in request.META.get('AWS', '')
        
        if is_testing:
            # Stub the EC2Instance class methods for testing
            ec2_instance = EC2InstanceStub(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
        else:
            # Create an instance of the EC2Instance class with the AWS access keys from config.py
            ec2_instance = EC2Instance(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
        
        # Start the EC2 instance using the provided instance ID
        ec2_instance.start_instance(instance_id)
        
    return redirect('team_instances_view', team_id=team_id)


# Stubbed EC2Instance class for testing
class EC2InstanceStub:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def start_instance(self, instance_id):
        # Stubbed method for starting an EC2 instance
        # Perform any necessary testing logic here
        pass
