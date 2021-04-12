# Generated by Django 3.1.7 on 2021-04-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Blog Post'},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='article',
            new_name='section_one',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='url',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='original_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='section_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='section_two',
            field=models.TextField(blank=True, null=True),
        ),
    ]