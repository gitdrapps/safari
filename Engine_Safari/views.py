from django.shortcuts import render 
from django.http import HttpResponseRedirect


def index(request):
  context = {
    'title'		: 'Portal | Taman Safari Indonesia',
    'info'		: 'Admin website Taman Safari Bogor harap update konten',
  }
  return render(request, 'index.html', context)
