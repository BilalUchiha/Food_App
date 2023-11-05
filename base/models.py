from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, mobile, address, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, mobile=mobile, address=address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, mobile, address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, mobile, address, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='customuser_set',  # Add a related_name to avoid clashes
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_set',  # Add a related_name to avoid clashes
        related_query_name='user',
    )

    USERNAME_FIELD = 'username'  # Use username for authentication
    EMAIL_FIELD = 'email'  # Use email for email field
    REQUIRED_FIELDS = ['email', 'mobile', 'address']

    def __str__(self):


        return self.username
    
class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,unique=True)
    price = models.IntegerField()
    type = models.CharField(max_length=300)
    image = models.ImageField(max_length=900)


    def __str__(self):
        return self.name





class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    item = models.IntegerField()
    price = models.IntegerField()

    @property
    def total(self):
        return self.price * self.item

class Pay(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    discount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


    @property
    def balance(self):
        return self.amount - self.discount

    def __str__(self) -> str:
        return self.date