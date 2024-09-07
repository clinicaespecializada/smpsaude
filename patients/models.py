from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=155, verbose_name='nome')
    birth_date = models.IntegerField(verbose_name='data de nascimento')
    gender = models.CharField(max_length=155, verbose_name='genero')
    mother_name = models.CharField(max_length=155, verbose_name='Nome da mae')
    father_name = models.CharField(max_length=155, verbose_name='Nome do pai', blank=True, null=True)
    cpf = models.CharField(max_length=155)


    def __str__(self) -> str:
        return self.name