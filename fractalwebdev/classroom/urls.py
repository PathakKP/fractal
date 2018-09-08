from django.urls import path
from . import views

urlpatterns = [
		#path('', views.home,name="home"),
		path('', views.classroom, name="classroom"),
	        path('question/', views.question, name="question"),
	        path('slide/', views.slide, name="slide"),
	        path('archive/', views.archive, name="archive"),
	        path('tentative_schedule/', views.tentative_schedule, name="tentative_schedule"),
	        
]