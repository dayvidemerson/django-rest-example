from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    date = models.DateField('data')
    name = models.CharField('nome', max_length=255)
    description = models.TextField('descrição')

    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'
        ordering = ['-date']

    def __str__(self):
        return self.name
