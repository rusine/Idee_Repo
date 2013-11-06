from django import forms
from main.models import Idea

class IdeaForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'content'}))
 
    def is_valid(self):
        form = super(IdeaForm, self).is_valid()
        for f in self.errors.iterkeys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error content'})
        return form
 
    class Meta:
        model = Idea
        exclude = ('user',)