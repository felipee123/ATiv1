from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from. models import aluno
def ver_escola(request):
    if request.method == "GET":
     nome = 'felipe'
     return render(request, 'cadastrado_aulo.html' ,{'nome': nome})
    elif request .method == "POST":
       nome = request.POST.get('nome')
       sobrenome = request.POST.get('sobrenome')
       email = request.POST.get('email')
       curso = request.POST.get('curso')

       Aluno = aluno(nome=nome, sobrenome=sobrenome, email=email, curso=curso)
       Aluno.save()
       return HttpResponse('dados cadrastrados com sucesso')

