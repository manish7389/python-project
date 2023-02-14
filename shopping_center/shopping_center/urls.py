"""shopping_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from shopping_center import views
from register.views import saveregister
from register.views import login
from register.views import profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name="home"),
    path('log-in/', views.login, name="login"),
    path('resister/', views.register, name="register"),
    path('saveregister/', saveregister , name="saveregister"),
    path('login/', login , name="login"),
    path('profile/', profile , name="profile"),
]
