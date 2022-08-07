# Generated by Django 4.1 on 2022-08-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_video_categoria_alter_video_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='privado',
            new_name='gratis',
        ),
        migrations.AlterField(
            model_name='video',
            name='descricao',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
