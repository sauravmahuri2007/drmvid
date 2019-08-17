from django_rq import enqueue

from video_encoding.tasks import convert_all_videos

# Signals Helper Functions
def signal_convert_video(sender, instance, **kwargs):
    enqueue(convert_all_videos,
            instance._meta.app_label,
            instance._meta.model_name,
            instance.pk)