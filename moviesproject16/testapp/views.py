from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import MoviesInformation

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit==True)
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})
def list_movie_view(request):
    movies_list=MoviesInformation.objects.all()
    return render(request,'testapp/listmovies.html',{'movies_list':movies_list})
