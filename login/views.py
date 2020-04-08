from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title'		: 'Login | Taman Safari Indonesia',
    
  }
  return render(request, 'login/index.html', context)
