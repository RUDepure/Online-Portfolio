from django.db import models
#https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/creating-the-models-in-django?autoSkip=true&autoplay=true&resume=false

# Create your models here.
# A model is a python class that can be saved into a database

class Job(models.Model):
    # Images
    # New property, that is a type of ImageField
    # ImageField is data that is going to be saved as an Image
    # Saved in a folder named "images"
    # NEED TO pip install PILLOW FOR IMAGES TO WORK
    image = models.ImageField(upload_to = 'images/')
    
    # Summary
    # New property that is type CharField
    # CharField that is data saved as text
    # It has a maximum number of characters of 200
    summary = models.CharField(max_length = 200)

    # Makes the job summaries to become their names in the database
    def __str__(self):
        return self.summary