# Generated by Django 3.0.6 on 2020-05-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chaussure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(default=' ')),
                ('img', models.ImageField(upload_to='post_img/')),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]