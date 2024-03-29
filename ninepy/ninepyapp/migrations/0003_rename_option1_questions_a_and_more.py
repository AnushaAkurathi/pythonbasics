# Generated by Django 4.0.6 on 2022-07-23 05:58

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('ninepyapp', '0002_questions_explanation_alter_questions_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='option1',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='option2',
            new_name='b',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='option3',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='option4',
            new_name='d',
        ),
        migrations.AddField(
            model_name='questions',
            name='e',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
