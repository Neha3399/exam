from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, sellerRegister, coustmerRegister, blogform
from new_app.models import seller, blog


# Create your views here.
def Log(request):
    return render(request,"Login.html")

def sellerR(request):
    form1 = LoginRegister()
    form2=sellerRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = sellerRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_seller=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"seller_register.html",{"form1":form1,"form2":form2} )



def coustmerR(request):
    form1 = LoginRegister()
    form2=  coustmerRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = coustmerRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_coustmer=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"coustmer_register.html",{"form1":form1,"form2":form2} )

def land(request):
    return render(request,"index.html")
def dash(request):
    return render(request,"index1.html")


def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('uname')
        password= request.POST.get('password')
        print(username)
        print(password)
        user= authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("ok")
            if user.is_staff:
                print("admin")
                return redirect('dash')
            elif user.is_seller:
                print("admin")
                return redirect('dash')
            elif user.is_coustmer:
                print("admin")
                return redirect('dash')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,"Login.html")

def blog_posting(request):
    data=blogform()
    user1=request.user
    print(user1)
    rcvr=seller.objects.get(user=user1)
    print(rcvr.id)
    if request.method == "POST":
        rname = blogform(request.POST,request.FILES)
        if rname.is_valid():
            print("ok")
            obj=rname.save(commit=False)
            obj.sellerName=rcvr
            obj.save()
    return render(request,"blog.html",{"form":data})

def view(request):
    data=blog.objects.all()
    return render(request, "blog_view.html",{'data':data} )

def remove(request,id):
    data = blog.objects.get(id=id)
    data.delete()
    return redirect("view")

def update(request,id):
    data= blog.objects.get(id=id)
    form= blogform(instance=data)
    if request.method == "POST":
        Blo=blogform(request.POST,instance=data)
        if Blo.is_valid():
           Blo.save()
           return redirect("view")
    return render(request,"update.html",{"form":form})
