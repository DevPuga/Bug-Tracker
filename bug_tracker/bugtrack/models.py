from django.db import models

class project(models.Model):
	project_name = models.CharField(max_length = 30)
	project_description = models.TextField()
	
