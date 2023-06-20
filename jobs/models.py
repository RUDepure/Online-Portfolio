from django.db import models
from embed_video.fields  import  EmbedVideoField
#https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/creating-the-models-in-django?autoSkip=true&autoplay=true&resume=false

# Create your models here.
# A model is a python class that can be saved into a database

JOB_OR_PROJECT = [
    ("Job", "Job"),
    ("Project", "Project"),
]

class Job(models.Model):
    
    title = models.CharField(max_length = 200, null=False, default="placeholder")
    job_or_project = models.CharField(max_length = 10, choices=JOB_OR_PROJECT, default="Job")
    # Images
    # New property, that is a type of ImageField
    # ImageField is data that is going to be saved as an Image
    # Saved in a folder named "images"
    # NEED TO pip install PILLOW FOR IMAGES TO WORK
    image = models.ImageField(upload_to = 'images/', null=False)
    
    # Summary
    # New property that is type CharField
    # CharField that is data saved as text
    # It has a maximum number of characters of 200
    summary = models.CharField(max_length = 200, null=False, default="placeholder")

    detailed_description = models.TextField(null=False, default="placeholder")
    
    #We are using a char field for date since we also want the option to specify is it is currently ongoing or on hold
    #Format we use: DD/MM/YYYY - DD/MM/YYYY  OR   DD/MM/YYYY - Ongoing/On Hold
    date = models.CharField(max_length = 36, default="DD/MM/YYYY") 
    project_video = EmbedVideoField(default=None, blank=True, null=True)
    
    class  Meta:
          verbose_name_plural = "Jobs and Projects"
		
    # Makes the job summaries to become their names in the database
    def __str__(self):
        return self.title if  self.title  else  " "
    
