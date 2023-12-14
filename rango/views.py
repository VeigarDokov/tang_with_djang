from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Nudim sve vezano za elektro instalacije!",
                    'malamaca': "Otpornici, releji, elektronika...",
                    }
    return render(request, 'rango/index.html', context=context_dict)


def smart_house(request):
    smart_house_ctx = {'smart_house': """Pametna kuća predstavlja inovativan
                       koncept modernog doma koji integrira napredne
                       tehnologije kako bi unaprijedila udobnost, sigurnost i
                       energetsku učinkovitost. Opremljena različitim pametnim
                       uređajima i senzorima, pametna kuća omogućuje
                       korisnicima daljinsko upravljanje i praćenje različitih
                       aspekata svakodnevnog života putem mobilnih uređaja ili
                       glasovnih naredbi.""", }
    return render(request, 'rango/smart_house.html', context=smart_house_ctx)
