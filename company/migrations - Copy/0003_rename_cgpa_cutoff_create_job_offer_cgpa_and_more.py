# Generated by Django 4.2.7 on 2023-11-23 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_create_job_profile_create_job_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_job_offer',
            old_name='cgpa_cutoff',
            new_name='cgpa',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='CIVIL',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='CSE',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='ECE',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='EEE',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='ISE',
        ),
        migrations.RemoveField(
            model_name='create_job_offer',
            name='MECH',
        ),
    ]
