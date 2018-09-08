
from django.shortcuts import render, get_object_or_404
from fractalweb.models import User
from .models import Questions,Tag,Category
from classroom.models import Question,Archive
from django.shortcuts import redirect

def question(request):
	questions=Questions.objects.all().order_by('-question_date')
	return render(request, 'extras/explore.html', {'questions': questions})

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
		   return render(request, 'extras/filter.html', {'notfound1':notfound1})

		else:   
			
			p=Tag.objects.get(tag_name=quote)
			ap=p.questions_set.all()
			#pp=Category.objects.get(category_name='E')
			#aap=pp.ap.all()

			context ={ 
			'filterp':p,
			'filterap':ap,
			}
			return render(request,'extras/filter.html',context=context)
def explore(request):
    return render(request, 'extras/explore.html', {})

def archive(request):
    return render(request, 'extras/archive.html', {})

def resources(request):
    return render(request, 'extras/resources.html', {})

	
# Create your views here.
