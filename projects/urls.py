from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap


urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]

