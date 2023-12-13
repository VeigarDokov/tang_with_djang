from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    var = """
        <html>
          <body>
            <h1>
            Smart-relay d.o.o</br>
            <a href='/rango/about/'>About</a>
            </h1>
          </body>
        </html>"""
    return HttpResponse(var)


def about(request):
    var = """
        <html>
          <body>
            <h1>
            <a href='/rango/'>Home</a></br>
            Web page under development!</br></br>
            Smart-relay d.o.o
            </h1>
          </body>
        </html>"""
    return HttpResponse(var)
