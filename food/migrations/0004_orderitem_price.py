# Generated by Django 4.1.13 on 2024-03-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_foodcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
