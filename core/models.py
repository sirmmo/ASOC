from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
	name = models.CharField(max_length=300)
	address = models.TextField()
	x = models.FloatField()
	y = models.FloatField()

	def __str__(self):
		return self.name


class Team(models.Model):
	school = models.ForeignKey(School, related_name="classes")
	for_class = models.CharField(max_length=100)
	name = models.CharField(max_length=300)
	logo = models.ImageField()
	mission = models.TextField()


class TeamMember(models.Model):
	user = models.ForeignKey(User)
	team = models.ForeignKey(Team, related_name="members")
	
