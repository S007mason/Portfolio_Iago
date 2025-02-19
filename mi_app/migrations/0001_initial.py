# Generated by Django 4.2.6 on 2025-02-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(default='Sin descripción', max_length=255)),
                ('git', models.URLField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='proyectos/')),
            ],
        ),
    ]
