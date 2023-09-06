from django.db import models


class ScrapingResult(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
