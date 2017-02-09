from django.contrib import admin

from jobs.models import Job


class JobsModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",

    ]

    class Meta:
        model = Job


admin.site.register(Job, JobsModelAdmin)
