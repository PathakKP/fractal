from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def classroom(request):
    return render(request, 'classroom/classroom.html', {})

@login_required
def question(request):
    return render(request, 'classroom/question.html', {})

@login_required
def slide(request):
    return render(request, 'classroom/slide.html', {})

@login_required
def archive(request):
    return render(request, 'classroom/archive.html', {})

@login_required
def schedule(request):
    return render(request, 'classroom/schedule.html', {})

# Create your views here.
