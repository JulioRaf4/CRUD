from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Pessoa
from django.contrib import messages
# Create your views here.


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html")


def classe(request):
    pessoas = Pessoa.objects.all()
    return render(request, "classe.html", {'pessoas': pessoas})


def salvar(request):
    vname = request.POST.get("name")
    vemail = request.POST.get("email")
    vdate = request.POST.get("bornDate")
    vcpf = request.POST.get("cpf")
    if vname and vemail and vdate and vcpf:
        Pessoa.objects.create(name=vname, email=vemail, bornDate=vdate, cpf=vcpf)
        pessoas = Pessoa.objects.all()
        return render(request, "classe.html", {'pessoas': pessoas})
    else:
        messages.error(request, "Erro ao criar form")
        return redirect(home)

def edit(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "edit.html", {'pessoa': pessoa})


def update(request, id):
    vname = request.POST.get("name")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.name = vname
    pessoa.save()
    return redirect(classe)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(classe)
