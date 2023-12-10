from django.contrib import admin
from django.urls import path
from core.views import query_examples, query_exercise1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste1/',query_examples),
    path('teste2/',query_exercise1),
]
