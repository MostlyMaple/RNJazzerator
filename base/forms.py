from django.forms import ModelForm
from .models import AudioFile

class AudioForm(ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'