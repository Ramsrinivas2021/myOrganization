import logging
from django.shortcuts import render

# Create a logger instance
logger = logging.getLogger(__name__)

def home(request):
    logger.info("Rendering home page.") 
    return render(request, 'home.html')