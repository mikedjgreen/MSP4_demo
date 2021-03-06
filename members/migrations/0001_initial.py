# Generated by Django 3.1.5 on 2021-02-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('created', models.DateTimeField()),
                ('bio', models.CharField(max_length=254)),
                ('admin_id', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
        ),
    ]
