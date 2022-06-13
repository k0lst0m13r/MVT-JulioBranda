# Generated by Django 4.0.5 on 2022-06-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentezco', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('especie', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
