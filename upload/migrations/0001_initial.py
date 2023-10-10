# Generated by Django 4.2.6 on 2023-10-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('date_uploaded', models.DateField()),
                ('file', models.FileField(default=None, upload_to='uploaded_files')),
            ],
        ),
    ]
