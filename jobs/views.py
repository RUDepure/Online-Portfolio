from django.shortcuts import render
# Import our Job model to be able to display it in our site
from .models import Job

# Create your views here.
#Django needs a Templates Folder in which we store our html files
def home(request):
    jobs = Job.objects
    #renders the html file inside templates/jobs folder
    return render(request, 'jobs/home.html', {'jobs': jobs}) #this render passes the Job model's objects as a list to home.html