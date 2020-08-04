from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from app.models import Student, Adminlogin


def show(request):
    return render(request,"index.html")


def slogin(request):
    return render(request,"slogin.html")


def sregester(request):
    return render(request,"sregister.html")


def forgetpassword(request):
    return render(request,"forgetpassword.html")


def admin(request):
    return render(request,'admin.html')


def register(request):
    n = request.POST.get("t1")
    a = request.POST.get('t2')
    c = request.POST.get('t3')
    g = request.POST.get('t4')
    u = request.POST.get('t5')
    p = request.POST.get("t6")
    Student(name=n,age=a,contactno=c,gender=g,username=u,password=p).save()
    messages.success(request,'ok')
    return redirect('sregester')


def login(request):
    u = request.POST.get("t1")
    p = request.POST.get("t2")

    try:
        Student.objects.get(username=u, password=p)




        return render(request, "logi.html",{"user":u})
    except Student.DoesNotExist:
        return render(request,"slogin.html",{"d1":"login fail"})


def slogout(request):
    logout(request)
    return redirect('/')




def viewprofile(request):
    st1=request.GET.get("un")
    stu=Student.objects.get(username=st1)
    return render(request,"viewprofile.html",{"data":stu})


def smodify(request):
    s=request.GET.get('un')
    d=Student.objects.get(username=s)
    return render(request,'data.html',{"data":d})


def update(request):
    s=request.GET.get('un')
    n=request.POST.get('t1')
    a=request.POST.get('t2')
    p=request.POST.get('t3')
    c=request.POST.get('t4')
    Student.objects.filter(username=s).update(name=n,age=a,password=p,contactno=c)
    return HttpResponse("successfuly updated")


def password(request):
    n=request.POST.get("t1")
    cno=request.POST.get('t2')
    p1=request.POST.get('t3')
    p2=request.POST.get('t4')
    try:
        Student.objects.get(contactno=cno)
        if p1 == p2:
            Student.objects.filter(contactno=cno).update(password=p1)

            msg="succes"
        else:
            msg="p1 not euals to p2"
    except Student.DoesNotExist:

        msg="contact number does not match"
    return render(request,"forgetpassword.html",{"msg":msg})


def adlogin(request):
    an=request.POST["t1"]
    ps=request.POST["t2"]
    try:
        Adminlogin.objects.get(username=admin,password=admin)
        return render(request,'adminlogin.html')
    except Adminlogin.DoesNotExist:

        return render(request,"admin.html",{"msg":"login faill"})

def alogout(request):
    logout(request)
    return  redirect('/')

def adhome(request):
    return render(request,'adminlogin.html')

def viewdeatils(request):
    a = Student.objects.all()


    return render(request, "showingdeatiles.html", {"res": a})


def sdelete(request):
    a = Student.objects.all()


    return render(request, "sdelete.html", {"res": a})


def delete(request):
    p=request.POST["cno"]
    Student.objects.filter(contactno=p).delete()
    a = Student.objects.all()
    return render(request,"sdelete.html",{"msg":"success","res": a})
