# Generated by Django 4.1.3 on 2023-03-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0006_remove_registro_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
