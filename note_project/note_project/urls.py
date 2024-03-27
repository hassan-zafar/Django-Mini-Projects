from django.urls import include, path

urlpatterns = [
    path('', include('notes.urls'))
]