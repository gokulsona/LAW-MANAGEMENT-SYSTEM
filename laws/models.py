from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#model for LawList
class LawList(models.Model):
    image=models.ImageField(upload_to="practice")
    icon=models.ImageField(upload_to="practice")
    category=models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self):
        return self.category
 
    
#models for DetailLaw
class DetailLaw(models.Model):
    act = models.CharField(max_length=256)
    category = models.ForeignKey(LawList, on_delete=models.CASCADE) #foreign key 
    description = models.TextField()
    
    def __str__(self):
        return self.act
    
    
#models for Lawyers
class Lawyers(models.Model):
    image = models.ImageField(upload_to="lawyers")
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=50)
    experience = models.IntegerField()
    fees = models.IntegerField()

    def __str__(self):
        return self.name
    
    
#models for district
class CourtDistrict(models.Model):
    district = models.CharField(max_length=45)


    def __str__(self):
        return self.district
    
    
class Court(models.Model):
    court = models.CharField(max_length=80)
    
    def __str__(self):
        return self.court

