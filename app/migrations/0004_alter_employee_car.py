# Generated by Django 3.2.17 on 2023-03-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='car',
            field=models.ManyToManyField(blank=True, to='app.EmployeeCarDetails'),
        ),
    ]