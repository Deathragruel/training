from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """ Signifies a blog post. """
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        text = self.text if len(self.text) < 50 else self.text[:50] + "..."
        return f"{self.title}:-\n\n{text}"
