from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Task(models.Model):
    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=256)
    done = models.BooleanField(_('done?'), default=False)

    create_at = models.DateTimeField(_('create at?'), auto_now_add=True)
    updated_at = models.DateTimeField(_('update at?'), auto_now=True)

    def __str__(self):
        return self.title    