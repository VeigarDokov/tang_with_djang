"""Required modules"""
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
# from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    """
    Query the database for a list of All categories currently stored.
    Order the categories by no. likes in descending order.
    Retrieve the top 5 only - of all if less than 5.
    Place the list in our context_dict dictionary
    that will be passed to the template engine.
    """
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
#    context_dict = {'boldmessage': "Nudim sve vezano za elektro instalacije!",
#                    'malamaca': "Otpornici, releji, elektronika...",
#                    }
#   return render(request, 'rango/index.html', context=context_dict)

    return render(request, 'rango/index.html', context=context_dict)


def smart_house(request):
    """Random Test context"""
    smart_house_ctx = {'smart_house': """Pametna kuća predstavlja inovativan
                       koncept modernog doma koji integrira napredne
                       tehnologije kako bi unaprijedila udobnost, sigurnost i
                       energetsku učinkovitost. Opremljena različitim pametnim
                       uređajima i senzorima, pametna kuća omogućuje
                       korisnicima daljinsko upravljanje i praćenje različitih
                       aspekata svakodnevnog života putem mobilnih uređaja ili
                       glasovnih naredbi.""", }
    return render(request, 'rango/smart_house.html', context=smart_house_ctx)


def show_category(request, category_name_slug):
    """ Create a context dictionary which we can pass to the template
    rendering engine.  """
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an
        # exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all the associated pages.
        # Note that filter() will return a list of page objects or an empty
        # list.
        pages = Page.objects.filter(category=category)

        # Adds our result list to te template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from the database to the context
        # dictionary. We'll use this in the template to verify that the
        # category exists.
        context_dict['category'] = category

    except ObjectDoesNotExist:
        # We get here if we didn't find the specified category. Don't do
        # anything the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
