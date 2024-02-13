from django.shortcuts import render
from googletrans import Translator

def translation(request):
    return render(request,'translation.html')

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text :',text,'lang :',lang)
    
    
    #Connect the language
    translation = Translator()
    
    #detect Language
    dt = translation.detect(text)
    dt2 = dt.lang
    #translate text
    translated = translation.translate(text,lang)
    tr= translated.text
    return render(request,'translated.html',{'translated':tr,'u_lang':dt2,'t_lang':lang})
