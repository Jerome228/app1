from django.shortcuts import render

# Home view.
def home(request):
    return render(request, 'users/home.html')
