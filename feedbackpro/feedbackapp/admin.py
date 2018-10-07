from django.contrib import admin
from . models import EmpFeedBack


class AdminEmpFeedback(admin.ModelAdmin):
    list_display = ['eid', 'fbeid', 'rating', 'feedback']


admin.site.register(EmpFeedBack, AdminEmpFeedback)
