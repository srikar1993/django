from django.shortcuts import render
from testApp import forms
from testApp.models import Movie

# Create your views here.

def welcome_view(request):
    return render(request, 'testApp/index.html')

def addmovie(request):
    if request.method == 'GET':
        form = forms.MovieForm()
        return render(request, 'testApp/addmovie.html', {'form': form})
    
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # my_dict = {'form': form, 'name': form.cleaned_data['name'], 'release_date': form.cleaned_data['release_date'], 'hero': form.cleaned_data['hero'], 'heroin': form.cleaned_data['heroin']}
            return render(request, 'testApp/index.html')
    # return render(request, 'testApp/index.html', {'form': form})

def movielist(request):
    movie_list = Movie.objects.all()
    return render(request, 'testApp/movielist.html', {'movie_list': movie_list})
