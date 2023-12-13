from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Nudim sve vezano za elektro instalacije!",
                    'malamaca': "Otpornici, releji, elektronika...",
                    }
    return render(request, 'rango/index.html', context=context_dict)


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
