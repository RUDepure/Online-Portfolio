from django.contrib import admin
# We import the model we create for Jobs
from .models import Job

# Register your models here.
# This sets the site for the Job model available for our admin
admin.site.register(Job)