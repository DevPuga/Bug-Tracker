from django.shortcuts import render
from django.http import HttpResponse
from bugtrack.models import BugTicket, Project

def home(request):
	bug_tickets = BugTicket.objects.all()
	projects = Project.objects.all()

	context = {
		"tickets" : bug_tickets,
		"projects" : projects,
	}

	return render(request, 'bugtrack/home.html',{'data' : context})
