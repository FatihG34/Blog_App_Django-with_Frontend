# Generated by Django 4.1.2 on 2022-10-15 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogApp", "0003_alter_blogpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="author",
            field=models.ForeignKey(
                default="Anonymous User",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="post_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="comment_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="post_like",
                to="blogApp.blogpost",
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liked_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="view",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="viewed_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
