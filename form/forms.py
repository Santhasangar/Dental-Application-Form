from . models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('Name', 'Phone','Email','Date','Comments','Doctor')

    def __init__(self, *args, **kwargs):
        super(AppointmentForm,self).__init__(*args, **kwargs)
        self.fields['Doctor'].empty_label = "Select Field"
        self.fields['Email'].required = False
        self.fields['Comments'].required = False