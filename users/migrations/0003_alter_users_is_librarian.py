# Generated by Django 3.2.12 on 2022-04-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_is_librarian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_librarian',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Librarian'),
        ),
    ]
