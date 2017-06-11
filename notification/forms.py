from django import forms
from .models import DeviceToken


class CertFileUploadForm(forms.Form):
    cert_file = forms.FileField()
    target = forms.ChoiceField(choices=((0, 'Develop'), (1, 'Distribute')), required=True, widget=forms.RadioSelect)


class NotificationSendForm(forms.Form):

    target = forms.ChoiceField(choices=((0, 'Develop'), (1, 'Distribute')),
                               required=True,
                               widget=forms.RadioSelect,
                               initial=0)
    device_token = forms.ModelMultipleChoiceField(label='Device Token',
                                                  queryset=DeviceToken.objects.all().values_list('device_token',
                                                                                                 flat=True)
                                                  )
    title = forms.CharField(required=True)
    subtitle = forms.CharField()
    body = forms.CharField()
    sound = forms.CharField(initial='default', required=True)
    badge = forms.IntegerField(initial=1, required=True)
    content_available = forms.BooleanField(initial=False)
    mutable_content = forms.BooleanField(initial=False)
    extra = forms.CharField(widget=forms.Textarea)