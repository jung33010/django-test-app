from django.shortcuts import render
from datetime import datetime

context = {
    'name': 'Django',
    'age': 13,
    'num': 1,
    'hobby': ['coding', 'reading', 'traveling'],
    'today': datetime.now(),
    'is_authenticated': True,
    'fruits': ['apple', 'banana', 'cherry'],
    'users': [
        {'id': 1234, 'name': 'Alice', 'age': 24, 'married': True},
        {'id': 2345, 'name': 'Bob', 'age': 34, 'married': False},
        {'id': 3456, 'name': 'Charlie', 'age': 25, 'married': True},
    ],
    'users': [],
}

def index(request):
  return render(request, 'app/index.html')

def variables_filters(request):
  return render(request, 'app/01_variables_filters.html', context)

def tags(request):
  return render(request, 'app/02_tags.html', context)

def layout(request):
  return render(request, 'app/03_child.html')   

def staticfiles(request):
  return render(request, 'app/04_staticfiles.html')

def urls(request):
  return render(request, 'app/05_urls.html')

def article(request, id: int): 
  """
  Args:
      request: The HTTP request object.
      id (int): The ID of the article to retrieve.
  """
  print(f'Article ID: {id}')
  
  # DB article 테이블에서 id가 id인 데이터를 로드

  return render(request, 'app/05_urls.html', {"id": id})

def search(request):
  print(request) # <WSGIRequest: GET '/app/search?q=AI&lang=en'>
  print(request.GET) # <QueryDict: {'q': ['AI'], 'lang': ['en']}>

  q = request.GET.get('q')
  lang = request.GET.get('lang')
  mode = request.GET.get('mode', 'view')
  return render(request, 'app/05_urls.html', {'q': q, 'lang': lang, 'mode': mode})


def bootstrap(request):
  return render(request, 'app/06_bootstrap.html')
