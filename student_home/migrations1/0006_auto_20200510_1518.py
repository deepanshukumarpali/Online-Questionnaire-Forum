# Generated by Django 3.0.6 on 2020-05-10 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_home', '0005_remove_question_q_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='a_question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student_home.Question'),
        ),
    ]