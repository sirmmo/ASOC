from django.db import models

from core.models import *


class LessonDefinition(models.Model):
	sequence_number = models.IntegerField()

#USIAMO I CUSTOMFORMS!!! YAY!!!


class LessonClosure(models.Model):
	team = models.ForeignKey(Team)
	lesson = models.ForeignKey(LessonDefinition)


class LessonClosureAttachment(models.Model):
	lc = models.ForeignKey(LessonClosure)
	the_file = models.FileField()

