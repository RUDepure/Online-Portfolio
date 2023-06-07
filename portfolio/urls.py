"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#imported jobs views
import jobs.views
from django.conf import settings #imported the settings we are going to use
from django.conf.urls.static import static #imported the settings we defined for our static url

#implemented the home path
urlpatterns = [
    # url in which we login with our admin users
    path('admin/', admin.site.urls),
    #sends them to the views file and looks at the home function
    path('', jobs.views.home, name = 'home'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #We define the root for the static files we defined in settings