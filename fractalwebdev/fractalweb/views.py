from django.shortcuts import render, get_object_or_404
from .models import User
from extras.models import Questions,Tag,Category
from classroom.models import Question,Archive
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from classroom import views
from extras import views
from . import views


def home(request):
	return render(request, 'fractalweb/index.html', {})
'''
@login_required
def classroom(request):
    return render(request, 'fractalweb/classroom.html', {})


def explore(request):
	questions=Questions.objects.all().order_by('-question_date')
	return render(request, 'fractalweb/explore.html', {'questions': questions})

def filter(request):
	if request.method == 'POST':	
		import requests
		quote = request.POST['quote']
		c=0
		for each in Tag.objects.all():
			if quote==each.tag_name:
			  c=c+1

		if c==0:
		   if quote=="":
		   	 notfound1="Enter a tag.."
		   else:	 
		     notfound1=quote+" is unavailable"	
		   return render(request, 'fractalweb/filter.html', {'notfound1':notfound1})

		else:   
			 
			p=Tag.objects.get(tag_name=quote)
			ap=p.questions_set.all()
			context ={ 
			'filterp':p,
			'filterap':ap,
			}
			return render(request,'fractalweb/filter.html',context=context)

	'''
