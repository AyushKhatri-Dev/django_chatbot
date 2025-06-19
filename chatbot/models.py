from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat at {self.timestamp}"