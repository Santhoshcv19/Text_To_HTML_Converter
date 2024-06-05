from django.shortcuts import render
from django.utils.html import escape
from .forms import TexttoHTMLForm

def convert_text_to_html(request):
    if request.method == 'POST':
        form = TexttoHTMLForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            return render(request, 'texttohtml/result.html', {'html_output': input_text})
    else:
        form = TexttoHTMLForm()
    return render(request, 'texttohtml/index.html', {'form': form})