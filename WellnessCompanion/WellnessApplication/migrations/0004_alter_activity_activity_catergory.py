# Generated by Django 3.2.7 on 2021-09-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WellnessApplication', '0003_auto_20210911_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_catergory',
            field=models.CharField(choices=[('Mindfulness and Stress Managment', 'Mindfulness and Stress Managment'), ('Physical Health', 'Physical Health'), ('Nutrition', 'Nutrition')], max_length=40),
        ),
    ]
