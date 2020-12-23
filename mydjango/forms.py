from django import forms

from students.models import Students, Schools


class SchoolsForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = "__all__"


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

class UploafImages(forms.Form):
    class Meta:
        models = Students
        fiels = "__all__"
    file = forms.FileField(required=True)