# Generated by Django 5.1.3 on 2024-11-12 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_testimonial_company_testimonial_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Designation',
            new_name='designation',
        ),
    ]
