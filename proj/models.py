from django.db import models

class basicmodel(models.Model):
    content=models.TextField()

    def __str__(self):
        return self.content
    


