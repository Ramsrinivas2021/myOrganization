from django.shortcuts import redirect, render
from .models import Team, Instance
from .ec2_class import EC2Instance


def add_instance_view(request, team_id):
    team = Team.objects.get(id=team_id)
    # Creating an instance of the EC2Instance class with the AWS access keys
    ec2_instance = EC2Instance("AKIAX2VFF7LDHXK4OL6B", "CK/U32uqLuGhQLSk9H/g5L9lFt/qoAtvPpE+yTlY")
    invalid_instance_ids = []
    
    if request.method == 'POST':
        instance_ids = request.POST.getlist('instance_id')
        
        for instance_id in instance_ids:
            is_valid = ec2_instance.validate_instance_id(instance_id)
        
            if is_valid:
                Instance.objects.create(team=team, instance_id=instance_id)
            else:
                invalid_instance_ids.append(instance_id)
        if invalid_instance_ids:
            return render(request, 'invalid_instance.html', {'invalid_instance_ids': invalid_instance_ids})
        return redirect('team_instances_view', team_id=team_id)
        
    return redirect('team_instances_view', team_id=team_id)

