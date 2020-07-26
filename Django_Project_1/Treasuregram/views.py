""" *
    *   render is used to render templates.
    *
    *   we will be returning the http response.
    * """
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Treasure


# Create your views here.
""" *
    *   a view is simply a python function that takes in a web request and returns a web reponse.
    *
    *   we will create a function that returns the http response
    *   we need to map this view to url to run it
    *   consider you want url/index to go to index view we just wrote.
    *   django has url dispatcher whose job is to map a URL to its corresponding view
    *   so what it will look like localhost:port 8000/index
    *   the URL dispatcher will map the URL to the corresponding view (Treasuregram/urls.py), 
    *   and then the view will return the http response , Hello Explorers (Treasuregram.views.index)
    *   the url dispatcher is inside the project's urls.py file
    * """
# def index(request):
#     return HttpResponse('<h1>Hello Explorers!</h1>')


""" *
    *   now we are going to render our template so we don't the httpresponse any more
    *   we will return a render object that takes in a request and a string that contains
    *   the name of our template index.html
    * """

# def index(request):
#     return render(request, 'index.html')

""" *
    *   first we want to send the data from our view to our template
    *   second we want to access the data inside our template
    *   
    *   we will create some data
    *   we will wrap the variables inside the context, which is a dictionary that maps variable names to Python 
    *   objects then we can pass this context as the third parameter to our render function
    * """
# def index(request):
#     name = 'Gold Nugget'
#     value = 1000.00
#     context = {'treasure_name': name,
#                'treasure_val': value}
#     return render(request, 'index.html', context)

""" *
    *   we are putting the context directly instead of creating the context variable first.
    * """
# def index(request):
#     return render(request, 'index.html', {'treasures':treasures})
#
#
# class Treasure:
#     def __init__(self, name, value, material, locaation):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = locaation
#
#
# treasures = [Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
#              Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
#              Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')
#              ]


""" *
    *
    * """
def index(request):
    # here we need to get all of Treasure's objects
    # we need to get all the value from database in variable
    treasure = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasure})