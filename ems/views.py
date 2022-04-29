from ast import Delete
from django.shortcuts import render
from django.http import HttpResponse
from ems.models import Customer

def view_employee(request):
    if request.method=='GET':
        resp=render(request,'ems/employee.html')
        return resp
    elif request.method=='POST':
        if 'btninsert' in request.POST:
            emp=Customer()
            emp.name=request.POST.get('txtName','NA')
            emp.age=int(request.POST.get('txtAge',0))
            emp.address=request.POST.get('txtAddress','NA')
            emp.year_of_exp=int(request.POST.get('txtExp',0))
            emp.contact=request.POST.get('txtNo','NA')
            emp.save()
            resp=HttpResponse("<h1>Record inserted successfully</h1>")
            return resp
        elif 'btnupdate' in request.POST:
            emp=Customer()
            emp.id=int(request.POST.get('txtid',0))
            if Customer.objects.filter(id=emp.id).exists(): #get has no attribute exists()
                emp.name=request.POST.get('txtName','NA')
                emp.age=int(request.POST.get('txtAge',0))
                emp.address=request.POST.get('txtAddress','NA')
                emp.year_of_exp=int(request.POST.get('txtExp',0))
                emp.contact=request.POST.get('txtNo','NA')
                emp.save()
                resp=HttpResponse("<h1>Record updated successfully in current id</h1>")
                return resp
                
            else:
                emp=Customer()
                emp.name=request.POST.get('txtName','NA')
                emp.age=int(request.POST.get('txtAge',0))
                emp.address=request.POST.get('txtAddress','NA')
                emp.year_of_exp=int(request.POST.get('txtExp',0))
                emp.contact=request.POST.get('txtNo','NA')
                emp.save()
                resp=HttpResponse("<h1>Record inserted successfully in new id</h1>")
                return resp
        elif 'btndelete' in request.POST:
            #emp=Customer()
            empid=int(request.POST.get('txtid',0))
            Customer.objects.get(id=empid).delete()
            resp=HttpResponse("<h1>Record deleted successfully</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            empid=int(request.POST.get('txtid',0)) 
            emp1=Customer.objects.get(id=empid)
            d={'emp1':emp1}
            resp=render(request,'ems/employee.html',context=d)
            return resp
        elif 'btnshow' in request.POST:
            allemp=Customer.objects.all()
            d={'allemp':allemp}
            resp=render(request,'ems/employee.html',context=d)
            return resp





# Create your views here.
