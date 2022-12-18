from django.contrib import admin
from jobs.models import Job

# Register your models here.

# Job Model 的管理类
class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date') # 在创建页面将这些属性隐藏起来，创建时默认为null，需要利用save_model方法
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date') # 在列表页面显示的字段
    # 在模型保存前进行一些操作
    def save_model(self, request, obj, form, change):
        obj.creator = request.user # 将创建人指定为当前登陆的用户
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)