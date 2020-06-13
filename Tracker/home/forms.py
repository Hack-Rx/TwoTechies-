from django.forms import ModelForm
from .models import Users

class EntryForm(ModelForm):
    class Meta:
        model = Users
        fields = ('name','contact','address','symptoms' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control ng-untouched ng-pristine ng-valid', 'placeholder' : 'enter your name','type':'text','id':'inputname'})
        self.fields['contact'].widget.attrs.update({'class' : 'form-control ng-untouched ng-pristine ng-invalid', 'placeholder' : 'What\'s your contact number','type':'text'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control ng-untouched ng-pristine ng-valid', 'placeholder' : 'What\s your Address','type':'text'})
        self.fields['symptoms'].widget.attrs.update({'class' : 'form-control ng-untouched ng-pristine ng-valid', 'placeholder' : 'What kind of Symptoms you are facing?','type':'text'})
