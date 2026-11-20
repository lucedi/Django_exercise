from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('profile_list')
        
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})