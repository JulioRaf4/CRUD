# Generated by Django 4.1.3 on 2023-03-15 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_remove_registro_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='email',
        ),
    ]
