# from django.db import models
# from django.contrib.auth.models import AbstractUser,Group,Permission

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     # username

# class User(AbstractUser):
#     # ... other fields ...
#     groups = models.ManyToManyField(Group, related_name='custom_user_groups')
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='custom_user_permissions'
#     )
from django.db import models
from django.contrib.auth.models import User, Group, Permission,AbstractUser

class User_groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'group')

class User_user_permissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'permission')


