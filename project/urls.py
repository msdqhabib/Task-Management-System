from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path('', include("core.urls")),
    path('', include("tasks.urls")),
    path('', include("teams.urls")),
    path('', include("authentication.urls")),
]
