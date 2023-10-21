from django.db.models.signals import post_save
from django.db.models.signals import Signal
from django.dispatch import receiver
from django.db import models
from django.db import IntegrityError
from django.shortcuts import redirect

profile_save_failed = Signal()


class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()


@receiver(post_save, sender=Profile)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"Welcome {instance.name}! A welcome email would be sent to {instance.email}.")


# 连接保存失败的接收器
@receiver(profile_save_failed)
def handle_profile_save_failure(sender, instance, **kwargs):
    print(f"Failed to save profile with name: {instance.name}. This name might already exist.")
    

def save_profile(name, email):
    profile = Profile(name=name, email=email)
    try:
        profile.save()
        return True

    except IntegrityError as e:
        print("Caught an integrity error:", e)
        profile_save_failed.send(sender=Profile, instance=profile)
        return False

# 測試
# save_profile("John", "john@example.com")
# save_profile("John", "john2@example.com") 
