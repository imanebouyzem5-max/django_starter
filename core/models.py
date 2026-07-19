from django.db import models


class Task(models.Model):
    """Exemple de modele - a adapter selon le vrai projet."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
