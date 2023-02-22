from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from tabledata.models import tabledata
from tabledata.models import helps



def home (request):
    return render(request,"index.html")
def insert(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            city=request.POST.get('city')
            data=tabledata(name=name,phone_no=phone,city=city)
            data.save()
    except:
        pass
    return render(request,"insert.html")
def viewall(request):
    all_data=tabledata.objects.all()
    data={
        'alldata':all_data
    }
    return render(request,"viewall.html",data)
def delete(request):
    all_data=tabledata.objects.all()
    data={
        'alldata':all_data
    }
    return render(request,"delte.html",data)
def delete1(request,uid):
    get_id=tabledata.objects.get(id=uid)
    get_id.delete()
    url="/delete/"
    return  HttpResponseRedirect(url)
def update(request,uid):
            get_id=tabledata.objects.get(id=uid)
            data={
                "data1":get_id
            }
            try:
                if request.method=="POST":
                    name=request.POST.get ('name')
                    phone=request.POST.get('phone')
                    city=request.POST.get('city')
                    data=tabledata(id=uid,name=name,phone_no=phone,city=city)
                    data.save()
                    url="/delete/"
                    return  HttpResponseRedirect(url)
            except:
                pass
            return render(request,"update.html",data)

def help(request):
            try:
                if request.method=="POST":
                    name=request.POST.get ('name')
                    phone=request.POST.get('phone')
                    mess=request.POST.get('mess')
                    data=helps(name=name,phone_no=phone,mess=mess)
                    data.save()
            except:
                pass
    
            return render(request,"help.html")