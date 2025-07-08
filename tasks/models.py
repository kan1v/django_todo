from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

class CompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(is_completed=True)

class Task(models.Model):
    class Status(models.TextChoices):
        HIGH_PRIORITY = 'HPR', 'Высокий приоритет'
        MIDDLE_PRIORITY = 'MPR', 'Средний приоритет'
        LOW_PRIORITY = 'LPR', 'Низкий приоритет'
        
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=3,
                                choices=Status.choices,
                                default=Status.MIDDLE_PRIORITY)
    
    created_at = models.DateTimeField(auto_now_add=True)
    due_date =  models.DateTimeField()    

    user_from = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='user_tasks')
    
    objects = models.Manager()
    completed_tasks = CompletedManager()
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Task.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)