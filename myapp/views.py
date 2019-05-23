from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']    #home, result 이어주는 코드
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            # add do dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full':text, 'total': len(words), 'dictionary': word_dictionary.items()})
  
내 
이름은
 효진 
 네
  이름은
   석호
    네
     이름은 
     현욱
{내 :1, 이름은 :2, 효진;1, 네 :1, 석호 ; 1  }     
