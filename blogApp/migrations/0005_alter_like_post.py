# Generated by Django 4.1.2 on 2022-10-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blogApp", "0004_alter_blogpost_author_alter_comment_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_like",
                to="blogApp.blogpost",
            ),
        ),
    ]
