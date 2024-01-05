from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *


def form_read(request):
    farmat = Form.objects.all()
    context = {'farmat':farmat}
    return HttpResponse('Formni ichidagi narsalar')

def form_create(request):
    format = Form.objects.create(phone = "+998999999999")
    format = Form.objects.create(title = "Dasturchi")
    format = Form.objects.create(adres = "Farg`ona")
    return HttpResponse('Data yaratildi')

def form_update(request):
    update = Form.objects.get(id=1)
    update.body='Alijonov Azamat Shuxratuvich'
    update.name='Axror'
    update.email='axrorber@gmail.com'
    update.save()
    return HttpResponse("Ma'lumot yangilandi")

def form_delete(request):
    delete_user = Form.objects.get(id = 2)
    delete_user.delete()
    return HttpResponse("Ma'lumot o'chirildi")
    
def education_read(request):
    farmat = Education.objects.all()
    context = {'farmat':farmat}
    return HttpResponse('Education ichidagi narsalar')

def education_create(request):
    format = Education.objects.create(phone = "+998999999999")
    format = Education.objects.create(name = "Axmadjon")
    format = Education.objects.create(body = "Yilning eng yomon proecti")
    return HttpResponse('Data yaratildi')


def education_update(request):
    update = Education.objects.get(id=1)
    update.body='Alijonov Azamat Shuxratuvich'
    update.name='Axror'
    update.title='axrorber@gmail.com'
    update.save()
    return HttpResponse("Ma'lumot yangilandi")

def education_delete(request):
    delete_user = Education.objects.get(name = "Axror")
    delete_user.delete()
    return HttpResponse("Ma'lumot o'chirildi")
    
def login_read(request):
    farmat = Loggin.objects.all()
    context = {'farmat':farmat}
    return HttpResponse('Education ichidagi narsalar')

def login_create(request):
    format = Loggin.objects.create(phone = "+998991912345")
    format = Loggin.objects.create(name = "Jabbor")
    format = Loggin.objects.create(body = "Shootlar :")
    format = Loggin.objects.create(surname = "Ganiyev")
    return HttpResponse('Data yaratildi')


def login_update(request):
    update = Loggin.objects.get(id=1)
    update.body='Alijonov Azamat Shuxratuvich'
    update.name='Axror'
    update.email='axrorber@gmail.com'
    update.save()
    return HttpResponse("Ma'lumot yangilandi")

def login_delete(request):
    delete_user = Loggin.objects.get(id = 7)
    delete_user.delete()
    return HttpResponse("Ma'lumot o'chirildi")