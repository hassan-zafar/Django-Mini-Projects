from django.urls import path
from .views import NoteDetail, NoteListCreate

urlpatterns = [
    path('', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),

]
