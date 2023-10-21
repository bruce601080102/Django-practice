from django.shortcuts import render, redirect
from myapp.samples.profiles_test.signals import ProfileForm
from myapp.samples.profiles_test.models import save_profile


def create_profile(request):
    # profile = Profile.objects.all()
    # for i in profile:
    #     print(i.name)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        # name = form.data['name']
        # print(name)
        # if form.is_valid():
        #     form.save()
        #     return redirect('profile_created')
        name = form.data['name']
        email = form.data['email']
        res = save_profile(name, email)
        if res:
            return redirect('profile_created')
        
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})


def profile_created(request):
    return render(request, 'profile_created.html')
