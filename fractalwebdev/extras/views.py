
from django.shortcuts import render, get_object_or_404
from fractalweb.models import User
from .models import Questions,Tag,Category
from classroom.models import Question,Archive
from django.shortcuts import redirect

def question(request):
	questions=Questions.objects.all().order_by('-question_date')
	return render(request, 'extras/questions.html', {'questions': questions})

def filter(request):
	if request.method == 'POST':	
		import requests
		quote = request.POST['quote']
		quote1 = request.POST['quote1']
		if quote1 is None or quote1 =='':
			if quote:
				p=Questions.objects.filter(tags__tag_name=quote)
				context ={ 
				'filterap':p,
				}
				return render(request,'extras/filter.html',context=context)

			else:
				notfound="Enter Tags Or Category to filter"	
				return render(request,'extras/filter.html', {'notfound':notfound})		

		elif quote is None or quote =='':
			if quote1:
				p=Questions.objects.filter(category__category_name=quote1)
				context ={ 
				'filterap':p,
				}
				return render(request,'extras/filter.html',context=context) 

			else:
				notfound="Enter Tags Or Category to filter"	
				return render(request,'extras/filter.html', {'notfound':notfound})	

		elif quote and quote1:
				p=Questions.objects.filter(tags__tag_name=quote,category__category_name=quote1)
				context ={ 
				'filterap':p,
				}
				return render(request,'extras/filter.html',context=context) 		

	else:
		notfound="Enter Tags Or Category to filter"		
		return render(request,'extras/filter.html', {'notfound':notfound})
def explore(request):
    return render(request, 'extras/explore.html', {})

def archive(request):
    return render(request, 'extras/archive.html', {})

def resources(request):
    return render(request, 'extras/resources.html', {})

	
# Create your views here.
