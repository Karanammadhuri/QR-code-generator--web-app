# Generated by Django 4.2.7 on 2024-02-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCodeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
