from django.shortcuts import render
from pc_manage import models


# Create your views here.
def index(request):
    data = models.User.objects.all()
    return render(request, 'index.html', {'data': data})
