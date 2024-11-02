from django.db import models # type: ignore

class aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    curso = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome