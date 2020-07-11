# Generated by Django 3.0.8 on 2020-07-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
                ('compleated', models.BooleanField(default=False)),
            ],
        ),
    ]
