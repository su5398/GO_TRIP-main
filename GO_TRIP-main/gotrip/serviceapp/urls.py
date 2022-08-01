"""gotrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from serviceapp.views import intro, main, course, login, membership, write

app_name = "serviceapp"

urlpatterns = [
    path('', intro, name='intro'),
    path('main/', main, name='main'),
    path('course/', course, name='course'),
    path('login/', login, name='login'),
    path('membership/', membership, name='membership'),
    path('write/', write, name='write'),

]
