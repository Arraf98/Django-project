# Generated by Django 4.2.3 on 2024-01-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_admin_blogpost_contact_message_order_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user_image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
