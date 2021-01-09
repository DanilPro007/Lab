from django.contrib import admin
from .models import Plants,Irrigation,Firms,Worker,Decorator,Time


admin.site.register(Irrigation),
admin.site.register(Plants),
admin.site.register(Firms),
admin.site.register(Worker),
admin.site.register(Decorator),
admin.site.register(Time),