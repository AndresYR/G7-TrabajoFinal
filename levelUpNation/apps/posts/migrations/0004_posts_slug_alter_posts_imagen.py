# Generated by Django 5.1.1 on 2024-10-17 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_fecha_comentarios_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
