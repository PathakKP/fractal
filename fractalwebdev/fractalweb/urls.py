from django.urls import path,include

from classroom import views
from extras import views
from . import views
urlpatterns = [
		path('', views.home,name="home"),
		path('classroom/', include('classroom.urls')),
		path('question/', include('extras.urls')),
	        #'''path('filter/', views.filter,name='filter'),
             #   path('login/', views.login,name='login'),
              #  path('signup/', views.signup,name='signup'), '''
]
