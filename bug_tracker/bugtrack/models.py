from django.db import models
import datetime

class Project(models.Model):
	project_name = models.CharField(max_length = 30)
	project_description = models.TextField()

	def __str__(self):
		return self.project_name

	class Meta:
		permissions = [
			("view_form", "Can view Project form")
		]

class BugTicket(models.Model):
	STATUS_CHOICES = [
		('O', 'Open'),
		('IP', 'In-Progress'),
		('C', 'Closed'),
	]

	bug_title = models.CharField(max_length = 30)
	bug_description = models.TextField()
	status = models.CharField(max_length = 2, choices = STATUS_CHOICES, default = STATUS_CHOICES[0])
	date_created = models.DateField(default=datetime.date.today)
	project = models.ForeignKey('Project', on_delete = models.CASCADE)

	class Meta:
		permissions = [
			("view_form", "Can view BugTicket form")
		]