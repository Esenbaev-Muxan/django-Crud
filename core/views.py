from django.shortcuts import render
from .models import Pessoa
from django.shortcuts import redirect

# Create your views here.
def home(request):
    pessoans = Pessoa.objects.all()
    return render(request, "index.html", {"pessoans": pessoans })

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoans = Pessoa.objects.all()
    return render(request, "index.html", {"pessoans": pessoans})
    
def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)  

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)  