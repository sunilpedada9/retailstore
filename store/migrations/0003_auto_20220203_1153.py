# Generated by Django 3.2.6 on 2022-02-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220120_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status_id', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'INACTIVE')], default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='rack',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='rack',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='store.product'),
            preserve_default=False,
        ),
    ]
