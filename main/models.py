from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=20)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(null=True, blank=True)


class Federation(models.Model):
    chairman = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Competition(models.Model):
    TYPE_CHOICES = [
        ('FR', 'Friendly'),
        ('LG', 'league'),
        ('KN', 'knockout')
    ]

    federation = models.ForeignKey(Federation, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    week = models.PositiveSmallIntegerField()
    date_created = models.DateField()
    date_updated = models.DateField()


class Achievment(models.Model):
    TYPE_CHOICES = [
        ('1', 'Gold'),
        ('2', 'Silver'),
        ('3', 'Bronze'),
        ('G', 'Goal'),
        ('P', 'Pass')
    ]

    federation = models.ForeignKey(Federation, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    details = models.TextField()
    date_created = models.DateTimeField()


class Team(models.Model):
    Federation = models.ForeignKey(
        Federation, on_delete=models.SET_NULL, null=True, blank=True)
    achievments = models.ForeignKey(
        Achievment, on_delete=models.SET_NULL, null=True, blank=True)
    competitions = models.ManyToManyField(Competition)
    name = models.CharField(max_length=50)
    money = models.PositiveIntegerField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Staff(models.Model):
    ROLE_CHOICES = [
        ('Man', 'Manager'),
        ('HCO', 'Headcoach'),
        ('COA', 'Coach'),
        ('TMA', 'Technical manager'),
        ('ANZ', 'Analyzer'),
        ('OTR', 'Other')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='OTR')


class Player(models.Model):
    POSITION_CHOICES = [
        ('G', 'Goalkeeper'),
        ('D', 'Defender'),
        ('M', 'Midfielder'),
        ('F', 'Forward')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True)
    achievments = models.ManyToManyField(Achievment)
    purchasable = models.BooleanField(default=True)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES)

    health = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    shoot = models.PositiveSmallIntegerField()
    passing = models.PositiveSmallIntegerField()
    tackle = models.PositiveSmallIntegerField()

    national_player = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
