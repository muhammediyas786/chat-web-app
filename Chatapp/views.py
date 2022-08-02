from datetime import datetime
from urllib import request
from django.contrib import messages
from .models import E_Group, Group, Message
from django.db.models import Q
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required(login_url='login')
def home(request):
    groups_obj = E_Group.objects.all()
    j = 0
    for i in groups_obj:
        if i.e_maker == request.user.username:
            j = j + 1
    print(j)
    if j <= 0:
        message = 'please join/create any Groups'
        return render(request,'index.html',{'groupnames':groups_obj,'len':message})
    else:
        return render(request,'index.html',{'groupnames':groups_obj})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalied !')
            return redirect('login')
    else:
        return render(request,'login.html')





@login_required(login_url='login')
def search(request):
    user_input = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        user_input = Group.objects.all().filter(Q(name__contains=query))
        if query == '':
            return redirect('/')
    return render (request, 'search.html',{'output':user_input})


@login_required(login_url='login')
def exist_group(request):
    if request.method == 'POST':
        group_names = request.POST['gruop_name']
        
        


        if Group.objects.filter(name=group_names).exists():
            exist_obj = E_Group.objects.create(e_name=group_names,e_maker=request.user.username)
            
            exist_obj.save()

            return redirect('/')
        else:
            messages.info(request, 'This Group Corrently unavailable !')
            return redirect('search')
    else:
        return redirect('search')
        

@login_required(login_url='login')
def create_group(request):
    if request.method == 'POST':
        print('hai')
        groupname=request.POST['gruop_name']
        if Group.objects.filter(name=groupname).exists():
            messages.info(request, 'Group Name already exist!')
            return redirect('group')
        else:
            new_group = Group.objects.create(name=groupname)
            new_group.save()
            exist_group(request)

            return redirect('/')
    else:
        return render(request, 'group.html')


@login_required(login_url='login')
def Inner_group(request,pk):
    group_obj = Group.objects.filter(name=pk)
    message_obj = Message.objects.filter(group=pk)
    date = datetime.now().date()
    return render(request, 'inner_group.html',{'date':date, 'group_obj':group_obj,'message_obj':message_obj})

@login_required(login_url='login')
def message_senting(request, pk):
    if request.method == 'POST':
        senter = pk
        msg = request.POST['text']
        group = request.POST['group']

        new_msg = Message.objects.create(senter=senter, msg=msg, group=group)
        new_msg.save()

        group_obj = Group.objects.filter(name=group)
        message_obj = Message.objects.filter(group=group)
        date = datetime.now().date()
        return render(request, 'inner_group.html',{'date':date, 'group_obj':group_obj,'message_obj':message_obj})


    else:
        return redirect('Inner_group')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if request.POST['username'] and request.POST['email']  and request.POST['password'] and  request.POST['password1']   :

            if password == password1:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username already taken ! ")
                    return redirect('signup')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.info(request,"email already taken ! ")
                        return redirect('signup')
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email)
                        user.save()

                        auth.login(request, user)

                        return redirect('/')
            else:
                messages.info(request,"passwoword dosn't match ! ")
                return redirect('signup')
           
        else:
            messages.info(request, 'please fill all fields !')
            return redirect('signup')
    else:
        return render(request, 'signup.html')



def logout(request):
    auth.logout(request)
    return redirect('login')