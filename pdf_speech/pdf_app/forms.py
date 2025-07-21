from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label="Select PDF")
    language = forms.ChoiceField(
        choices=[
            ('en', 'English'),
            ('en-uk', 'English (UK)'),
            ('fr', 'French')
        ],
        label="Language"
    )
    start_page = forms.IntegerField(min_value=1, required=False, label="Start Page")
    end_page = forms.IntegerField(min_value=1, required=False, label="End Page")
