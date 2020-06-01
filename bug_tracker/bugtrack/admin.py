from django.contrib import admin
from .models import BugTicket, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('project_name', 'project_description')

@admin.register(BugTicket)
class BugAdmin(admin.ModelAdmin):
	list_display = ('bug_title', 'bug_description', 'status', 'date_created', 'project')

