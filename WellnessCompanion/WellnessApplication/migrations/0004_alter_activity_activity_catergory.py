# Generated by Django 3.2.7 on 2021-09-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WellnessApplication', '0003_auto_20210912_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_catergory',
            field=models.CharField(choices=[('Mindfulness and Stress Management', 'Mindfulness and Stress Management'), ('Physical Health', 'Physical Health'), ('Nutrition', 'Nutrition')], default='Mindfulness and Stress Management', max_length=40),
        ),
    ]
