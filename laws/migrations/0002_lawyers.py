# Generated by Django 5.0.3 on 2024-09-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lawyers')),
                ('name', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]