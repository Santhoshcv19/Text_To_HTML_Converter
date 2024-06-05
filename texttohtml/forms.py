from django import forms
from ckeditor.widgets import CKEditorWidget

class TexttoHTMLForm(forms.Form):
    input_text = forms.CharField(widget=CKEditorWidget(), label="Enter your text here...")