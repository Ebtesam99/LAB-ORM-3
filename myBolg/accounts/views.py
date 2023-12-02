from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registerPage(request: HttpRequest):

    if request.method == "POST":
      
      newUser = User.objects.create_user(username = request.POST["username"], first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = request.POST["password"])
      newUser.save()
      return redirect("accounts:loginUser")
    
    return render(request, "accounts/register.html")

def loginUser(request: HttpRequest):
   
   message = None

   if request.method == "POST":
       
       user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
       
       if user:
           login(request, user)
           return redirect("blog:displayBlog")
       
       else:
           message = "Please provide correct username and password"
   return render(request, "accounts/signIn.html", {"message" : message})


def logoutUser(request: HttpRequest):

   if request.user.is_authenticated:
        logout(request)    

   return redirect("accounts:loginUser") 
