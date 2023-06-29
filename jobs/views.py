from django.shortcuts import render, get_object_or_404
# Import our Job model to be able to display it in our site
from .models import Job
from .models import Education


# Create your views here.
# Django needs a Templates Folder in which we store our html files
def home(request):
    jobs = Job.objects
    education = Education.objects
    context = {
              'jobs': jobs,
              'education': education
       }
    #renders the html file inside templates/jobs folder
    return render(request, 'jobs/home.html', context) #this render passes the Job model's objects as a list to home.html

# Function made to return the detailed page of each job
def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail}) 
