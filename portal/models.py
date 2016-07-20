from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import django   


# Create your models here.

class Info(models.Model):
    roll_no = models.IntegerField(default = 0,blank = False)
    upvotes_junior = models.IntegerField(default = 0,blank = False)
    upvotes_senior = models.IntegerField(default = 0,blank = False)
    total = models.IntegerField(default = 0,blank=False)          
    user = models.OneToOneField(User)
    def __str__(self):
        return (self.roll_no)
        
class Question(models.Model):
    question_text = models.CharField(max_length=500,blank=False)
    option_a = models.CharField(max_length = 50,blank = False)
    option_b = models.CharField(max_length = 50,blank =False)
    option_c = models.CharField(max_length = 50,blank =False)
    option_d = models.CharField(max_length = 50,blank =False)
    correct_option = models.CharField(max_length = 1,blank = False)
    upvotes_junior = models.IntegerField(default = 0,blank=False)
    upvotes_senior = models.IntegerField(default = 0,blank=False)
    user = models.ForeignKey(User)
    def __str__(self):
        return (str(self.id))


