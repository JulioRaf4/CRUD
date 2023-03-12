# Generated by Django 4.1.3 on 2023-03-09 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_pessoa_lname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='age',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='email',
        ),
    ]