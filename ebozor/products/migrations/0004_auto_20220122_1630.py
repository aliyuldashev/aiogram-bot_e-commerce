# Generated by Django 3.2.9 on 2022-01-22 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_buyurtma_m_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Second_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='manzil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Rasm file_id'),
        ),
        migrations.CreateModel(
            name='oshxonalar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('delivary_payment', models.BigIntegerField(default=0, verbose_name='dastavka narxi')),
                ('delivary_zero', models.BigIntegerField(default=0, verbose_name='dastavka limit')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.product', verbose_name='Maxsulotlar')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='first_tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='products.first_tag', verbose_name='Birinchi Turini'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='second_tag',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.second_tag', verbose_name='Ikkinchi turini:'),
        ),
        migrations.AddField(
            model_name='user',
            name='oshxona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='products.oshxonalar', verbose_name='Oshxona'),
            preserve_default=False,
        ),
    ]
