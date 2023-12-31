# Generated by Django 4.2.7 on 2023-11-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0010_alter_artwork_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('events', models.BooleanField(blank=True, null=True)),
                ('newsletter', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
