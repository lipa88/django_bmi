# Generated by Django 2.1.4 on 2018-12-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('height', models.FloatField()),
                ('mass', models.FloatField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
