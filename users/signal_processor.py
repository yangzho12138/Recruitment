from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Resume
from jobs.producer import publish

@receiver(signal=post_save, sender=Resume, dispatch_uid="resume_post_save_dispatcher")
def post_save_callback(sender, instance=None, created=False, **kwargs):
    data = {
        'email': instance.email,
        'gender': instance.gender,
        'city': instance.city,
        'born_address': instance.born_address,
        'apply_position': instance.apply_position,
        'created_date': str(instance.created_date),
        'degree': instance.degree,
        'major': instance.major,
        'bachelor_school': instance.bachelor_school,
        'master_school': instance.master_school,
        'doctor_school': instance.doctor_school,
        'bachelor_GPA': instance.bachelor_GPA,
        'master_GPA': instance.master_GPA,
        'doctor_GPA': instance.doctor_GPA,
        'offer': False
    }
    publish("resume changed", data)