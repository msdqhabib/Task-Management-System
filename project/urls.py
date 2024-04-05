from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication app
    path('', include("core.urls")),
    path('', include("tasks.urls")),
    path('', include("authentication.urls")),
]
