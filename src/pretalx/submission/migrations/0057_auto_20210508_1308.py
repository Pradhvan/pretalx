# Generated by Django 3.1.8 on 2021-05-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0056_reviewscorecategory_is_independent"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="question_required",
            field=models.CharField(default="none", max_length=13),
        ),
    ]
