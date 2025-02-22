# Generated by Django 5.1.5 on 2025-01-25 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('submission_file', models.FileField(max_length=400, upload_to='submissions/')),
                ('status', models.CharField(default='waiting', max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('prob_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.problemfile')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
