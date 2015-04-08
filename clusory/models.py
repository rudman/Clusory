from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    user=models.ForeignKey(User)
    text=models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    rounds = models.IntegerField(default=3)


    def __unicode__(self):
        return self.text

class DebateSide(models.Model):
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question) #eventually should get rid of
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text

class DebatePair(models.Model):
    question=models.ForeignKey(Question)
    proUser=models.ForeignKey(User, related_name='proUser')
    conUser=models.ForeignKey(User, related_name='conUser')
    proText=models.CharField(max_length=140)
    conText=models.CharField(max_length=140)
    matched=models.BooleanField()

class Debate(models.Model):
    user = models.ForeignKey(User)

    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return self.text
