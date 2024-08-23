from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, WorkExperience, Education, Certification
from .forms import ProjectForm
@login_required

def profile_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')

        user = request.user
        user.first_name, user.last_name = name.split(' ', 1)
        user.email = email


        profile, created = ProjectForm.objects.get_or_create(user=user)
        profile.bio = bio
        profile.linkedin = linkedin
        profile.github = github
        profile.save()

        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('list_projects')

    # For GET requests, show the profile edit form
    user = request.user
    profile, created = Project.objects.get_or_create(user=user)

    return render(request, 'portfolio/profile.html', {
        'user': user,
        'profile': profile
    })
@login_required
def profile_create(request):
    user = request.user

    # Fetch all relevant objects for the logged-in user
    projects = Project.objects.filter(user=user)
    work_experiences = WorkExperience.objects.filter(user=user)
    educations = Education.objects.filter(user=user)
    certifications = Certification.objects.filter(user=user)

    # Render the profile page with the fetched data
    return render(request, 'portfolio/profile.html', {
        'user': user,
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
        'certifications': certifications,
    })

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_profile.html', {'form': form})
@login_required
def edit_project(request, project_id):
    # Implement form handling to edit a project
    pass

@login_required
def delete_project(request, project_id):
    # Implement functionality to delete a project
    pass


@login_required
def list_projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'portfolio/project_list.html', {'projects': projects})

@login_required
def list_work_experience(request):
    work_experience = WorkExperience.objects.filter(user=request.user)
    return render(request, 'portfolio/work_experience_list.html', {'work_experience': work_experience})

@login_required
def list_education(request):
    education = Education.objects.filter(user=request.user)
    return render(request, 'portfolio/education_list.html', {'education': education})

@login_required
def list_certifications(request):
    certifications = Certification.objects.filter(user=request.user)
    return render(request, 'portfolio/certifications_list.html', {'certifications': certifications})

def project(request):
    return render(request,'portfolio/index.html')

