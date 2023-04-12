from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
def home(request):
    form=ResumeForm()
    candidates = Resume.objects.all()
    return render(request,'home.html',{'candidates':candidates ,'form':form})
# Create your views here.
