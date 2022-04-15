from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import basicmodel

def basicView(request):
    all_basic=basicmodel.objects.all()
    return render(request,'basic.html',
    {'all_items':all_basic})

def addbasic(request):
    new_item=basicmodel(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/proj/')

def deletebasic(request,proj_id):
    item_to_delete=basicmodel.objects.get(id=proj_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/proj/')

def deletebasic(request,proj_id):
    item_to_delete=basicmodel.objects.get(id=proj_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/proj/')


    







    




