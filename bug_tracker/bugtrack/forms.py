from django import forms
from .models import Project

class ProjectForm(forms.Form):
	project_name = forms.CharField(label='Project Name', max_length=30)
	project_description = forms.CharField(label='Project Description', widget=forms.Textarea)

class BugForm(forms.Form):
	bug_name = forms.CharField(label='Bug Name')
	bug_description = forms.CharField(widget=forms.Textarea)
	project = forms.ModelChoiceField(queryset=Project.objects.all())