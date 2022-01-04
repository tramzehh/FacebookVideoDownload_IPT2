from django.urls import path
from downloader import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
]