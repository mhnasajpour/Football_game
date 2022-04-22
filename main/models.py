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
    chairman = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Team(models.Model):
    Federation = models.ForeignKey(
        Federation, ondelete=models.SET_NULL, null=True, blank=True)
    competitions = models.ManyToManyField(
        'Competition', on_delete=models.SET_NULL, null=True, blank=True)
    achievments = models.ForeignKey(
        'Achievment', on_delete=models.CASCADE, null=True, blank=True)
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
        Team, on_delete=models.CASCADE, null=True, default=NULL)
    role = models.CharField(max_length=3, choice=ROLE_CHOICES)


class Player(models.Model):
    POSITION_CHOICES = [
        ('G', 'Goalkeeper'),
        ('D', 'Defender'),
        ('M', 'Midfielder'),
        ('F', 'Forward')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, on_delete=models.PROTECT, null=True, blank=True)
    achievments = models.ManyToManyField(
        'Achievment', on_delete=models.CASCADE, null=True, blank=True)
    purchasable = models.BooleanField(default=True)
    position = models.CharField(max_length=1, choice=POSITION_CHOICES)

    health = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    shoot = models.PositiveSmallIntegerField()
    passing = models.PositiveSmallIntegerField()
    tackle = models.PositiveSmallIntegerField()

    national_player = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
