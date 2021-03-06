from django.shortcuts import redirect,render
from app.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app.models import account_profile

# Create your views here.
@login_required(login_url="signin")
def home(request):
    return render(request,"index.html")

def sign_up(request):      
    if request.method=="POST":
        username=request.POST["username"]
        email =request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
    

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already registered")
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already registered")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #create profile for newusers

                user_model=User.objects.get(username=username)
                profile=account_profile.objects.create(user=user_model,id_user=user_model.id)
                profile.save()
                return redirect('signin')   
        else:
            messages.info(request,"password  is mismatch") 
            return redirect('signup')


    else:
        return render (request,"signup.html") 

# @login_required(login_url="signin")
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"user and password does'not exist")
            return redirect('signup')


             

    else:
        return render(request,"signin.html")

def user_bio(request):
    if request.method=="POST":

        if request.FILES.get('image')==None:
            image=account_profile.profile_image
            bio=request.POST['bio']
            location=request.POST['location']

            account_profile.bio=bio
            account_profile.profile_image=image
            account_profile.location=location
            account_profile.save()

        if request.FILES.get('image')!=None:
            image=account_profile.profile_image
            bio=request.POST['bio']
            location=request.POST['location']

            account_profile.bio=bio
            account_profile.profile_image=image
            account_profile.location=location
            account_profile.save()    

    return render(request,"setting.html")

@login_required(login_url="signin")
def logout(request):
     auth.logout(request)
     return redirect('signin')















