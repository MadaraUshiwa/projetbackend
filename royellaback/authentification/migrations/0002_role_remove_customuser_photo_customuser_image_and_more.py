# Generated by Django 5.0.4 on 2024-05-23 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='photo',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='authentification.role'),
        ),
    ]
