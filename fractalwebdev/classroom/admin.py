from django.contrib import admin
from .models import Question,Archive,Schedule,Slide
admin.site.register(Question)
admin.site.register(Archive)
admin.site.register(Slide)
admin.site.register(Schedule)