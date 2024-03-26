from django.shortcuts import render,redirect,get_object_or_404
from .form import ItemForm
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form=ItemForm()
    return render(request,'productcreate.html',{'form':form})

def update(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    if request.method == 'POST':
        form=ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form=ItemForm(instance=item)
    return render(request,'productcreate.html',{'form':form})

def delete(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('view')
    return render(request,'productdelete.html',{"items":item})

def view(request):
    formdetails=Item.objects.all()
    return render(request,'viewfile.html',{"items":formdetails})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not (username and email and password):
            return render(request,"signup.html",{'error':'All fields are required'})
        if User.objects.filter(username = username).exists():
            return render(request,"signup.html",{'error':'Username already exists'})
        saving = User.objects.create_user(username = username, email = email, password = password)
        auth_login(request,saving)
        return redirect('create')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('create')
        else:
            return render(request,'login.html',{'error':'Invalid credentials'})
    return render(request,'login.html')