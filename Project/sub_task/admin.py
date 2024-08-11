from django.contrib import admin
from .models import Project,Task,Employee,Project_timelines
# Register your models here.

class Employee_data(admin.ModelAdmin):
    list_display = ('name_of_employee',)
    search_fields = ('name_of_employee',)
admin.site.register(Employee,Employee_data)


class Project_time(admin.ModelAdmin):
    list_display = ('project_name','project_deadline',)
    search_fields = ('project_name',)

admin.site.register(Project_timelines,Project_time)

class Project_data(admin.ModelAdmin):
    list_display = ('name_of_project','description','date_created')
    search_fields = ('name_of_project',)
    list_per_page = 5
admin.site.register(Project,Project_data)



class Task_data(admin.ModelAdmin):
    list_display = ('task_title','Name_of_project','task_created_on','task_started','task_in_progress','task_completed',)
    search_fields = ('task_title',)
    list_filter = ('task_completed','task_started')
    list_per_page = 5
admin.site.register(Task,Task_data)