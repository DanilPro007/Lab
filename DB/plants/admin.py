from django.contrib import admin
from .models import Articles,Irrigation,Firms,Worker,Decorator,Time


admin.site.register(Irrigation),
admin.site.register(Articles),
admin.site.register(Firms),
admin.site.register(Worker),
admin.site.register(Decorator),
admin.site.register(Time),