from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
# Create your views here.
translator = Translator()

def tarjima(request):
	if request.method == 'GET':
		eng = request.GET.get('q','')
		print(eng)
		b = translator.translate(eng, dest='uz').text
		print(b)
		
	return render(request,'base.html',{'b':b,'a':eng})