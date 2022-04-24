from django.db import models
from main.models import Competition, Player, Team


class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    team1 = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='match_team1')
    team2 = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='match_team2')
    time_created = models.DateTimeField()
    time_updated = models.DateTimeField()


class Goal_detail(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    score = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='score_set')
    assist = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='assist_set')
    minute = models.PositiveSmallIntegerField()
