import logging
from django.shortcuts import redirect,render

from django.shortcuts import redirect, get_object_or_404
from .models import Instance

# Create a logger instance
logger = logging.getLogger(__name__)

def delete_instance(request, instance_id):
    instance = get_object_or_404(Instance, id=instance_id)

    if request.method == 'POST':
        instance.delete()
        logger.info(f"Instance {instance_id} deleted.")
        return redirect('team_instances_view', team_id=instance.team_id)

    # If the request method is not POST, render a confirmation page
    return render(request, 'delete_instance.html', {'instance': instance})
