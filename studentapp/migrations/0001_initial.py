# Generated by Django 4.1.7 on 2023-03-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Joining_date', models.DateField()),
                ('Qualification', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Mobile_number', models.IntegerField()),
            ],
        ),
    ]