import logging
from django.shortcuts import redirect, get_object_or_404, render
from .models import Team
from .ec2_class import EC2Instance
from . import config

# Create a logger instance
logger = logging.getLogger(__name__)

def stop_instance_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    instances = team.instance_set.all()  # Get all instances associated with the team
    if instances:
        
        # Creating an instance of the EC2Instance class with the AWS access keys from config.py
        ec2_instance = EC2Instance(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
        stopped_instances = []
        
        # Stop each instance in the list
        for instance in instances:
            instance_id = instance.instance_id
            # Stop the EC2 instance using the provided instance ID
            ec2_instance.stop_instance(instance_id)
            stopped_instances.append(instance_id)
            logger.info(f"Instance stopped - ID: {instance_id}")
            
        # Wait for all instances to reach the 'stopped' state
        for instance_id in stopped_instances:
            ec2_instance.wait_for_instance_state(instance_id, 'stopped')
        # Check if all instances have stopped
        all_instances_stopped = all(
            ec2_instance.describe_instance_state(instance_id) == 'stopped' for instance_id in stopped_instances
        )
        if all_instances_stopped:
            message = f"All instances for team '{team.name}' have been stopped."
            logger.info(message)
            return render(request, 'stop_instance.html', {'team': team, 'message': message})
        else:
            error_message = "Failed to stop one or more instances."
            logger.error(error_message)
            return render(request, 'stop_instance.html', {'team': team, 'error_message': error_message})
    # If no instances found, render an error message
    error_message = "No instances found for the team."
    logger.warning(error_message)
    return render(request, 'stop_instance.html', {'team': team, 'error_message': error_message})
