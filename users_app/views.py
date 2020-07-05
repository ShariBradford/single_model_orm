from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "user_list": User.objects.all() 
    }
    return render(request, 'index.html', context)

def validate(request):
    new_user = request.POST
    User.objects.create(first_name=new_user["first_name"], last_name=new_user["last_name"],email_address=new_user["email_address"], age=new_user["age"])
    return redirect('/')