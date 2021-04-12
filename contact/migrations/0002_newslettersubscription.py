# Generated by Django 3.1.7 on 2021-04-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Newsletter Subscriptions',
            },
        ),
    ]