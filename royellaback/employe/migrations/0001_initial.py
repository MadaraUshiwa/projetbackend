# Generated by Django 5.0.4 on 2024-05-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('poste', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='images/')),
                ('citation', models.TextField()),
            ],
        ),
    ]
