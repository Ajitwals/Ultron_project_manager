from django.db import models

# Create your models here.


class Project(models.Model):
    name_of_project= models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name_of_project

class Project_timelines(models.Model):
    project_name = models.ForeignKey(Project,on_delete=models.SET_DEFAULT,null=True,default=None)
    project_deadline = models.DateTimeField()

    def __str__(self) :
        return str(self.project_deadline)


class Employee(models.Model):
    name_of_employee = models.CharField(max_length=1600)

    def __str__(self) :
        return self.name_of_employee

class Task(models.Model):
    Name_of_project = models.ForeignKey(Project,on_delete=models.SET_DEFAULT,null=True,default=None)
    task_title = models.CharField(max_length=150000)
    employee_name = models.ForeignKey(Employee,on_delete=models.SET_DEFAULT,null=True,default=None)
    task_details = models.TextField(blank=True)
    task_created_on = models.DateTimeField(auto_now=True)
    task_started = models.BooleanField(default=False)
    task_in_progress = models.BooleanField(default=False)
    task_completed = models.BooleanField(default=False)
    project_submission_date = models.ForeignKey(Project_timelines,on_delete=models.SET_DEFAULT,null=True,default=None)
