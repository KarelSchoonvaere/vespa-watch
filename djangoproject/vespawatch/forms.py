from django.forms import ModelForm, ImageField, ClearableFileInput
from .models import ManagementAction, Observation

class PublicObservationForm(ModelForm):
    file_field = ImageField(required=False, widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Observation
        fields = ['species', 'individual_count', 'behaviour', 'subject', 'location', 'latitude', 'longitude',
                  'inaturalist_id', 'observation_time', 'comments',
                  'observer_title', 'observer_last_name', 'observer_first_name', 'observer_email', 'observer_phone',
                  'observer_is_beekeeper', 'observer_approve_data_process', 'observer_approve_display',
                  'observer_approve_data_distribution'
        ]


class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = ['species', 'individual_count', 'behaviour', 'subject', 'location', 'latitude', 'longitude',
                  'inaturalist_id', 'observation_time', 'comments'
        ]


class ManagementActionForm(ModelForm):
    class Meta:
        model = ManagementAction
        fields = ['observation', 'outcome', 'action_time', 'person_name']