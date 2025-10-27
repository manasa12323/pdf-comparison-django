from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),        # Handles '/'
    path('upload/', views.upload_pdf, name='upload_pdf'), # Handles '/upload/'
    path('success/', views.upload_success, name='upload_success'),
]
