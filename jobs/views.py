from django.shortcuts import render

# Create your views here.
#Django needs a Templates Folder in which we store our html files
def home(request):
    #renders the html file inside templates/jobs folder
    return render(request, 'jobs/home.html')