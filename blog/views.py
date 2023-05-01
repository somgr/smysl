from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
    <title>Сайт Блог!</title>
    <h1>Денис</h1>
    </html>""")
