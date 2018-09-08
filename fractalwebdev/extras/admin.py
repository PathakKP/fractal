from django.contrib import admin
from .models import Questions,Tag,Category

#admin.site.register(Questions)
admin.site.register(Tag)
admin.site.register(Category)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'title','display_tags','category')
admin.site.register(Questions, QuestionAdmin)
# Register your models here.
