from django.db import models

class Search(models.Model):
    city = models.CharField(max_length=100)
    result_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} @ {self.created_at:%Y-%m-%d %H:%M}"
