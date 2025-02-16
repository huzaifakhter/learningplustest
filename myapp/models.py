from django.db import models

class TextEntry(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Show first 50 characters in admin panel
