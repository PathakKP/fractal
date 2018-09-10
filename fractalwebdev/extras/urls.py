
from django.urls import path
from . import views

urlpatterns = [
			path('', views.question, name="explore"),
			path('question/', views.question, name="questions"),
			
	       
	        path('filter/', views.filter, name="filter"),
	        path('archive/', views.archive, name="archive"),
            path('resources/', views.resources, name="resources"),
	        
]
