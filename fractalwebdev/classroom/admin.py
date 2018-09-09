from django.contrib import admin
from .models import Question,Archive
admin.site.register(Question)
admin.site.register(Archive)
admin.site.register(Slide)
admin.site.register(Schedule)
# Register your models here.
