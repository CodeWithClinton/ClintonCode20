# Generated by Django 3.2.8 on 2022-08-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='yam.jpg', upload_to='img'),
        ),
    ]