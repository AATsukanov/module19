"""
URL configuration for Module19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task1.views import platform, games, cart, sign_up_by_html, sign_up_by_django
from task5.views import post_list, post_list_with_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', platform),
    path('platform/', platform),
    path('games/', games),
    path('cart/', cart),
    path('signup/', sign_up_by_html),
    path('signup_dj/', sign_up_by_django),
    path('posts/', post_list),
    path('posts_check/', post_list_with_check)
]
