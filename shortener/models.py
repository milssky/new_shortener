from django.db import models


class Url(models.Model):
    full_url = models.URLField(
        verbose_name="Сокращаемая ссылка",
        help_text="Вставьте ссылку и чудо произойдет"
    )
    nums_of_visits = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_url[:30]}. Visits: {self.nums_of_visits}"

