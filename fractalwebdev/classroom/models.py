from django.db import models
import os
from django.utils import timezone
class Question(models.Model):
    heading=models.CharField(max_length=200)
    url=models.URLField(max_length=555,blank=True,null=True)
    question_date = models.DateTimeField(
            default=timezone.now)
    #tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.heading
class Slide(models.Model):
        url=models.URLField(max_length=555,blank=True,null=True)
        question_date = models.DateTimeField(
            default=timezone.now)
class Archive(models.Model):
    session=models.CharField(max_length=60)  # since 2017-18 contains "-" character

    def __str__(self):
        return self.session

    class Meta:                   # ordering ka mtlb sorting (here sorting the results by headline)
        ordering = ('session',)        
'''        
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Tentative_Schedule(models.Model):
    schedule_image = ImageField(upload_to=get_image_path, blank=True, null=True) '''
        
        
# Create your models here.
