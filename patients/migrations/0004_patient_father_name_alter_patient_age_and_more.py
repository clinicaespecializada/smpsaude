# Generated by Django 5.1.1 on 2024-09-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_rename_education_patient_mother_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='father_name',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Nome do pai'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(verbose_name='idade'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=155, verbose_name='genero'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mother_name',
            field=models.CharField(max_length=155, verbose_name='Nome da mae'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=155, verbose_name='nome'),
        ),
    ]
