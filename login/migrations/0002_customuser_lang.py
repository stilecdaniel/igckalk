# Generated by Django 4.2.3 on 2023-12-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lang',
            field=models.CharField(choices=[('sk', 'Slovak'), ('en', 'English'), ('hu', 'Hungarian'), ('cs', 'Czech')], default='sk', max_length=10, verbose_name='Jazyk'),
        ),
    ]
