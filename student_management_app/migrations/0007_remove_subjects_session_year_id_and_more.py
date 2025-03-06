# Generated by Django 5.0.7 on 2025-01-30 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_subjects_session_year_id_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='session_year_id',
        ),
        migrations.AddField(
            model_name='subjects',
            name='session_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel'),
        ),
    ]
