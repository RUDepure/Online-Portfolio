# Generated by Django 4.1.7 on 2023-06-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_or_project',
            field=models.CharField(blank=True, choices=[('Job', 'Job'), ('Project', 'Project')], default=None, max_length=10, null=True),
        ),
    ]