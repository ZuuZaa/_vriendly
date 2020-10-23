# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from threading import Thread

# from account.models import Verification
# from account.tasks import send_verification_mail

# @receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='create_auth_token')
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Verification.objects.create(user=instance)

# @receiver(post_save, sender=Verification, dispatch_uid='send_mail')
# def send_mail(sender, instance=None, created=False, **kwargs):
#     if created:
#         link = f"localhost:8000/confirm/{instance.token}/{instance.user.id}"
#         print('verification --------')
#         print(link)
#         print(instance.user.email)
#         task = Thread(target=send_verification_mail, args=(instance.user.email, link))
#         task.start()
#         return(link)




