# Generated by Django 3.2.15 on 2023-01-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application_amcgh', '0005_auto_20230118_0454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('department_name',)},
        ),
        migrations.AlterModelOptions(
            name='department_slug',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.FileField(default='User-avatar.png', upload_to='Doctor_Profile_Pic'),
        ),
    ]
