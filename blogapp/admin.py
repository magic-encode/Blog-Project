from django.contrib import admin

from .models import Blog
from .models import Catagory
from .models import Comments


admin.site.register(Blog)
admin.site.register(Catagory)
admin.site.register(Comments)





