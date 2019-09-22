from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .forms import ProjectProposalForm
from .models import ProjectModel
from user.models import Profile
import datetime

# home page
@login_required(login_url='/login/')
def home(request):
    projectList = ProjectModel.objects.filter(supervisor1 = request.user)
    return render(request, 'home.html', {'projectList':projectList})

def project_list_undergrad(request):
    all_projects = ProjectModel.objects.filter(draft=False, viewable=True, approved=True)
    context = {
        'all_projects' : all_projects
    }
    return render(request, 'project_list_undergrad.html', context=context)

#def project_list_postgrad(request):
#    all_projects = ProjectModel.objects.filter(postgraduate=True, draft=False, viewable=True, approved=True)
#    context = {
#        'all_projects' : all_projects
#    }
#    return render(request, 'project_list_postgrad.html', context=context)

def project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    user = request.user.username
    creator = project.supervisor1.id
    supervisor = Profile.objects.get(user_id=creator)

    strUser = str(user)
    strSupervisor = str(supervisor.user)

    if project.draft is True and strUser != strSupervisor: 
        return render(request, 'denied.html')

    else:
        prereqs = project.prerequisites.split(",")
        tags = project.projectTags.split(", ")
        context = {
            'project' : project,
            'supervisor' : supervisor,
            'prereqs' : prereqs,
            'tags' : tags,
        }
    return render(request, 'project_detail.html', context=context)

@login_required(login_url='/login/')
def project_registration(request):
    if request.method == 'POST':
        form = ProjectProposalForm(request.POST)
        if form.is_valid():
            formData = ProjectModel()
            formData.supervisor1 = request.user
            formData.supervisor2Title = form.cleaned_data['supervisor2Title']
            formData.supervisor2FirstName = form.cleaned_data['supervisor2FirstName']
            formData.supervisor2LastName = form.cleaned_data['supervisor2LastName']
            formData.supervisor3Title = form.cleaned_data['supervisor3Title']
            formData.supervisor3FirstName = form.cleaned_data['supervisor3FirstName']
            formData.supervisor3LastName = form.cleaned_data['supervisor3LastName']
            formData.title = form.cleaned_data['title']
            formData.description = form.cleaned_data['description']
            formData.noOfStudents = form.cleaned_data['noOfStudents']
            formData.prerequisites = form.cleaned_data['prerequisites']
            formData.projectTags = form.cleaned_data['projectTags']
            formData.IP = form.cleaned_data['IP']
            # checkboxes
            formData.chemical = form.cleaned_data['chemical']
            formData.civil = form.cleaned_data['civil']
            formData.elec = form.cleaned_data['elec']
            formData.envir = form.cleaned_data['envir']
            formData.materials = form.cleaned_data['materials']
            formData.mechanical = form.cleaned_data['mechanical']
            formData.mechatronic = form.cleaned_data['mechatronic']
            formData.mining = form.cleaned_data['mining']
            formData.oilGas = form.cleaned_data['oilGas']
            formData.petroleum = form.cleaned_data['petroleum']
            formData.software = form.cleaned_data['software']
            formData.other = form.cleaned_data['other']
            # admin fields
            formData.creationDate = datetime.date
            formData.draft = form.cleaned_data['draft']
            formData.save()

            title = form.cleaned_data.get('title')
            messages.success(request, f'Project Proposal named {title} was created!')
            return redirect('home-page')
    else:
        form = ProjectProposalForm()
    return render(request, 'project_registration.html', {'form':form})

#def dashboard(request):
#    projectList = ProjectModel.objects.filter(supervisor1 = request.user)
#    return render(request, 'dashboard.html', {'projectList':projectList})

@login_required(login_url='/login/')
def projectEdit(request, pk):
    try:
        project = ProjectModel.objects.get(projectID= pk)
    except ProjectModel.DoesNotExist:
        raise Http404('Project Does Not Exist')

    if request.method == 'POST':
        form = ProjectProposalForm(request.POST)
        if form.is_valid():
            form.save()
            
            title = form.cleaned_data.get('title')
            messages.success(request, f'Project Proposal Named {title} was updated!')
            return redirect('dashboard')
    else:
        form = ProjectProposalForm(project)
        return render(request, 'project-edit.html', context={'form': form})