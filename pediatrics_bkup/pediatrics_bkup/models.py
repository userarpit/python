import datetime
from django.db import models
from django.utils import timezone

# # Create your models here.

# class Question(models.Model):
#     def __str__(self):
#         return self.question_text
    
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

    

# class Choice(models.Model):
#     def __str__(self):
#         return self.choice_text

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)   

class BabyServer(models.Model):

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    delivery = models.CharField(max_length=30)
    neonatal_status = models.CharField(max_length=30)
    birth_weight = models.CharField(max_length=20)
    length = models.CharField(max_length=20)
    head_circumference = models.CharField(max_length=20)
    chest_circumference = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3)
    remarks = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    mother_blood_group = models.CharField(max_length=3)
    father_name = models.CharField(max_length=30)
    father_blood_group = models.CharField(max_length=3)
    details_of_siblings = models.CharField(max_length=30)
    phone_number = models.IntegerField()