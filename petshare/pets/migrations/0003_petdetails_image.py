# Generated by Django 4.0.2 on 2022-02-18 10:01

from django.db import migrations, models
import pets.models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_petdetails_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='petdetails',
            name='image',
            field=models.ImageField(default=1, upload_to=pets.models.imgupload),
            preserve_default=False,
        ),
    ]