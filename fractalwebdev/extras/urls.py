
from django.urls import path
from . import views

urlpatterns = [
			path('', views.explore, name="explore"),
			path('questions/', views.question, name="question"),
			
	       
	        path('filter/', views.filter, name="filter"),
	        path('archive/', views.archive, name="archive"),
          path('resources/', views.resources, name="resources"),
	        
]
