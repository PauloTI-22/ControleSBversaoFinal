# Generated by Django 4.0.1 on 2022-01-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_rename_orcamento01_task_orçamento01_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='orçamento01',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='orçamento02',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='orçamento03',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
