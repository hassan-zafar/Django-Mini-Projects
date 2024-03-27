from django.db import models
from django.core.validators import RegexValidator

class Note(models.Model):
    alphanumeric_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    title = models.CharField(max_length=100,validators=[alphanumeric_validator])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
