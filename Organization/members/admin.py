import logging
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

# Create a logger instance
logger = logging.getLogger(__name__)

admin.site.unregister(User)  # Unregister the default User model
admin.site.unregister(Group)  # Unregister the default Group model

# Register a custom UserAdmin class
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    logger.info("CustomUserAdmin registered.")
    pass
