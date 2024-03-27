from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import Word
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from math import log10


class UploadFileView(View):
    def get(self, request):
        return render(request, 'app/upload.html')

    def post(self, request):
        if request.FILES['file']:
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            Word.objects.all().delete()

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            word_counts = {}
            words = text.split()
            total_words = len(words)

            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            top_words = []

            for word, tf in sorted_words[:50]:
                idf = log10(total_words / word_counts[word])  # Расчет IDF по формуле
                top_words.append(Word(word=word, tf=tf, idf=round(idf, 2)))  # IDF в данном случае не используется

            Word.objects.bulk_create(top_words)
            top_words_from_db = Word.objects.order_by('-tf')[:50]
            os.remove(file_path)

            return render(request, 'app/result.html', {'words': top_words_from_db})

        return JsonResponse({'success': False})
