from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import render, redirect




@login_required
def profile_view(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')

    return render(request, 'profiles/profile.html', {'form': form})
def hom(request):
    return render(request,'profiles/hom.html')
def about_view(request):
    return render(request,'profiles/about.html')

def project(request):
    return render(request,'profiles/index.html')