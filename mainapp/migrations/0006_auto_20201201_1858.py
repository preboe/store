# Generated by Django 3.1.3 on 2020-12-01 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_delete_base_soap'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='baby_soap',
            new_name='cosmetics',
        ),
        migrations.RenameModel(
            old_name='natural_parfume',
            new_name='perfume',
        ),
        migrations.RenameModel(
            old_name='care_soap',
            new_name='soap',
        ),
        migrations.RemoveField(
            model_name='bar_soap',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cream_soap',
            name='category',
        ),
        migrations.RemoveField(
            model_name='scrub',
            name='category',
        ),
        migrations.RemoveField(
            model_name='scrub_soap',
            name='category',
        ),
        migrations.RemoveField(
            model_name='soap_from_scratch',
            name='category',
        ),
        migrations.RemoveField(
            model_name='souvenir_soap',
            name='category',
        ),
        migrations.DeleteModel(
            name='bacterial_soap',
        ),
        migrations.DeleteModel(
            name='Bar_soap',
        ),
        migrations.DeleteModel(
            name='cream_soap',
        ),
        migrations.DeleteModel(
            name='scrub',
        ),
        migrations.DeleteModel(
            name='scrub_soap',
        ),
        migrations.DeleteModel(
            name='soap_from_scratch',
        ),
        migrations.DeleteModel(
            name='souvenir_soap',
        ),
    ]