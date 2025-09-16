from django.db import models

# Create your models here.
# 기사데이터를 긁어오겠노라
class NewData(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)