# Generated by Django 4.2.2 on 2023-09-17 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_email_student_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Field_of_study',
            new_name='field_of_study',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='GPA',
            new_name='gpa',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_No',
            new_name='student_number',
        ),
    ]
