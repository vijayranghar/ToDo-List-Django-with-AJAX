# Create your views here.
import json
from django.shortcuts import render_to_response,HttpResponse,redirect
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404
from django.forms import ModelForm
from .forms import todoModelForm
from todoApp.models import todoModel
from django.contrib import messages
from django.core import serializers


def home(request):
	todo=todoModel.objects.all()
	form = todoModelForm()
	return render(request,'index.html',{'form':form,'todo':todo})

def todoPost(request):
	if request.method == 'POST' and request.is_ajax():  #if the form has been submitted
		form = todoModelForm(request.POST)
		if form.is_valid():
			form.save()
		todo_json = serializers.serialize('json',todoModel.objects.order_by('-pk'))
		return HttpResponse(json.dumps(todo_json),content_type="application/json")
	return HttpResponse("status")

		
def delete(request,id):
	if request.method == "POST" and request.is_ajax:
		print "ajax"
		del_object = get_object_or_404(todoModel ,pk = id)
		del_object.delete()
		todo_json = serializers.serialize('json',todoModel.objects.order_by('-pk'))
		return HttpResponse(json.dumps(todo_json),content_type="application/json")
	return HttpResponse("status")
	