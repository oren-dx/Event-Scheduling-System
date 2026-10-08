from django.db import models
from django.contrib.auth.models import AbstractUser

class EventUserModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=15,null=True)

    def __str__(self):
        return f'{self.full_name}-{self.phone}'
    
class EventModel(models.Model):
    EVENT_TYPES =[
        ('Conference','Conference'),
        ('Concert','Concert'),
        ('Wedding','Wedding'),
    ]
    STATUS_TYPES =[
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ]
    user = models.ForeignKey(
        EventUserModel,
        on_delete=models.CASCADE,
        related_name='events'
    )
    event_title = models.CharField(max_length=100,null=True)
    event_type = models.CharField(choices=EVENT_TYPES,max_length=20,null=True)
    event_description = models.TextField(max_length=100,null=True)
    event_date = models.DateField(null=True)
    status = models.CharField(choices=STATUS_TYPES,max_length=20,null=True)
    location = models.CharField(max_length=200,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.event_title}'




        

        
    


