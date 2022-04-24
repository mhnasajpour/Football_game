from tkinter import CASCADE
from django.db import models


# Create your models here.
class Achievment(models.Model):
    federation = models.ForeignKey(Federation,on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    type_choices = (('Goalkeeper','Goalkeeper'),('Defender','Defender'),('Midfielder','Midfielder'),('Forward','Forward'))
    type = models.CharField(choices=type_choices)
    details = models.TextField()
    date_create = models.DateTimeField()
    date_update = models.DateTimeField()# i think we dont need both time just which year



class Goal_detail(models.Model):
    game = models.ForeignKey(Match,on_delete=models.CASCADE)
    assist = models.ForeignKey(Player,on_delete= models.CASCADE) #because of we have a 'pass' in python i can't use 'pass'
    goal = models.ForeignKey(Player,on_delete= models.CASCADE)
    minute = models.SmallIntegerField()



class Competition(models.Model):
    federation = models.ForeignKey(Federation,on_delete=models.CASCADE)
    type_choices = (('Friendly','friendly'),('Champions League','champions_league'),('other','other'))
    type = models.CharField(choices=type_choices)
    week = models.SmallIntegerField()
    date_create = models.DateTimeField()
    date_update = models.DateTimeField()



class Match(models.Model):
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE)
    time_create = models.DateTimeField()
    time_update = models.DateTimeField()

