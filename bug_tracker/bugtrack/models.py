from django.db import models

class Project(models.Model):
	project_name = models.CharField(max_length = 30)
	project_description = models.TextField()

	def __str__(self):
		return self.project_name

class BugTicket(models.Model):
	STATUS_CHOICES = [
		('O', 'Open'),
		('IP', 'In-Progress'),
		('C', 'Closed'),
	]

	bug_title = models.CharField(max_length = 30)
	bug_description = models.TextField()
	status = models.CharField(max_length = 2, choices = STATUS_CHOICES, default = STATUS_CHOICES[0])
	date_created = models.DateField()
	project = models.ForeignKey('Project', on_delete = models.CASCADE)
