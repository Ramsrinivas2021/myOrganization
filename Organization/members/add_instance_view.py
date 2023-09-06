import logging
from django.shortcuts import redirect
from .models import Team, Instance
from .ec2_class import EC2Instance
from members.team_instances_view import team_instances_view
from . import config


logger = logging.getLogger(__name__)


def add_instance_view(request, team_id):
    team = Team.objects.get(id=team_id) 
    # Creating an instance of the EC2Instance class with the AWS access keys
    ec2_instance = EC2Instance(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
    invalid_instance_ids = []
    
    logger.info('Entering add_instance_view function')  # Logging the start of the function
    
    if request.method == 'POST':
        instance_ids = request.POST.getlist('instance_id')
        
        for instance_id in instance_ids:
            is_valid = ec2_instance.validate_instance_id(instance_id)
        
            if is_valid:
                Instance.objects.create(team=team, instance_id=instance_id)
            else:
                invalid_instance_ids.append(instance_id)
        if invalid_instance_ids:
            logger.warning('Invalid instance IDs detected: %s', invalid_instance_ids)
            return team_instances_view(request, team_id, invalid_instance_ids=invalid_instance_ids) 
        
        logger.info('Redirecting to team_instances_view after adding instances')
        return redirect('team_instances_view', team_id=team_id)
    
    logger.info('Redirecting to team_instances_view')    
    return redirect('team_instances_view', team_id=team_id)