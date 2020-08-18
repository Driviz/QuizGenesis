from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if extra_fields.get('is_superuser') is True:
            self.is_superuser_eligible(**extra_fields)

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_teacher', True)
        
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_teacher') is not True:
        #     raise ValueError(('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(('Superuser must have is_superuser=True.'))
        self.is_superuser_eligible(**extra_fields)
        # user = self.create_user(username, email, password)
        # user.is_superuser = True
        # user.is_staff = True
        # user.is_teacher = True
        # user.save()

        return self.create_user(username, email, password, **extra_fields)

    def is_superuser_eligible(self, **extra_fields):
        if extra_fields.get('is_staff') is not True:
            raise TypeError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_teacher') is not True:
        #     raise TypeError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise TypeError('Superuser must have is_superuser=True.')