"""visionStudios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="homepage"),
    path('modele', views.modelsPage, name="modelsPage"),
    path('aboutus', views.aboutUsPage, name="modelsPage"),
    path('galerie', views.galeryPage, name="galeryPage"),
    path('contact', views.contactPage, name="contactPage"),
    path('submitFloater', views.submitFloater, name="submitFloater"),
    path('aplica', views.applyPage, name="applyPage"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
