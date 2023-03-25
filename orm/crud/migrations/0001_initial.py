# Generated by Django 3.2.16 on 2023-03-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='online course', max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=30)),
                ('last_name', models.CharField(default='Doe', max_length=30)),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crud.user')),
                ('full_time', models.BooleanField(default=True)),
                ('total_learners', models.IntegerField()),
            ],
            bases=('crud.user',),
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crud.user')),
                ('occupation', models.CharField(choices=[('student', 'Student'), ('developer', 'Developer'), ('data_scientist', 'Data Scientist'), ('dba', 'Database Admin')], default='student', max_length=20)),
                ('social_link', models.URLField()),
            ],
            bases=('crud.user',),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(auto_now_add=True)),
                ('mode', models.CharField(choices=[('audit', 'Audit'), ('honor', 'Honor')], default='audit', max_length=5)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.course')),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.learner')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Learners',
            field=models.ManyToManyField(through='crud.Enrollment', to='crud.Learner'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='crud.Instructor'),
        ),
    ]
