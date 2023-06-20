from django.contrib import admin
from embed_video.admin  import  AdminVideoMixin
# We import the model we create for Jobs
from .models import Job

# Register your models here.
# This sets the site for the Job model available for our admin

class  jobAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Job, jobAdmin)
