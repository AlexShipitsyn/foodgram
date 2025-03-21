from django.forms import ModelForm

from recipes.models import Import


class ImportForm(ModelForm):
    class Meta:
        model = Import
        fields = ('csv_file',)
