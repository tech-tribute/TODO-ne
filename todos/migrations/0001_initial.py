# Generated by Django 5.0 on 2023-12-15 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_complete', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='lists.list')),
            ],
            options={
                'ordering': ['-create_date'],
                'indexes': [models.Index(fields=['-create_date'], name='todos_todo_create__1662cb_idx')],
            },
        ),
    ]
