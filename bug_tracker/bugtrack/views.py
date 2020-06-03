from django.shortcuts import render, redirect
from django.http import HttpResponse
from bugtrack.models import BugTicket, Project
from .forms import ProjectForm, BugForm

def home(request):
	bug_tickets = BugTicket.objects.all()
	projects = Project.objects.all()

	project_form = ProjectForm()
	bug_form = BugForm()

	if request.method == "POST":
		if 'project' in request.POST:
			project_form = ProjectForm(request.POST)

			if project_form.is_valid():
				name = project_form.cleaned_data["project_name"]
				description = project_form.cleaned_data["project_description"]

				t = Project(project_name=name, project_description = description)
				t.save()

				return redirect('/')

		if 'bug' in request.POST:
			bug_form = BugForm(request.POST)

			if bug_form.is_valid():
				bug_name = bug_form.cleaned_data["bug_name"]
				description = bug_form.cleaned_data["bug_description"]
				bug_project = bug_form.cleaned_data["project"]

				t = BugTicket(bug_title=bug_name, bug_description=description, status = BugTicket.STATUS_CHOICES[0], project=bug_project)
				t.save()

				return redirect('/')

	context = {
		"tickets" : bug_tickets,
		"projects" : projects,
		"projectf" : project_form,
		"bugf" : bug_form,
	}

	return render(request, 'bugtrack/home.html', {'data' : context})
