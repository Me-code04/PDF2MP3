import os
from django.shortcuts import render
from .forms import PDFUploadForm
from django.conf import settings
from PyPDF2 import PdfReader
from gtts import gTTS

def index(request):
    context = {}

    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            language = form.cleaned_data['language']
            start_page = form.cleaned_data.get('start_page')
            end_page = form.cleaned_data.get('end_page')

            reader = PdfReader(pdf_file)
            total_pages = len(reader.pages)
            start = start_page - 1 if start_page else 0
            end = end_page if end_page else total_pages

            text = ""
            for page_num in range(start, min(end, total_pages)):
                page = reader.pages[page_num]
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

            tts = gTTS(text=text, lang='en' if language == 'en-uk' else language, tld='co.uk' if language == 'en-uk' else 'com')
            filename = f"output_{request.user.id if request.user.is_authenticated else 'anon'}.mp3"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            tts.save(filepath)

            context['audio_file'] = settings.MEDIA_URL + filename

    else:
        form = PDFUploadForm()

    context['form'] = form
    return render(request, 'pdf_app/index.html', context)
