"""Required modules"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project_tang_wit_djang.settings")

import django

django.setup()

from rango.models import Category, Page


def populate():
    """this function will be executed if this file is run as scrypt"""
    # First we will create list of dictionaries containing the pages
    # we want to add into each category.
    # Then ew will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allow us to iterate
    # trougheach data structure, and add the data to our models.

    python_pages = [
        {
            "title": "Official Python Tutorial",
            "url": "http://docs.python.org/2/tutorial/",
        },
        {
            "title": "How to think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/",
        },
        {
            "title": "Learn Python in 10 Minutes",
            "url": "https://www.stavros.io/tutorials/python/",
        },
    ]

    el_insatalacije_pages = [
        {
            "title": "Poslovne i kućne električne instalacije",
            "url": "https://bs.wikipedia.org/wiki/Električne_instalacije",
        },
        {
            "title": "Industrijske električne instalacije",
            "url": "https://hr.wikipedia.org/wiki/Elektrane_i_elektroenergetske_mreže",
        },
    ]
    odrzavanje_inspekcija_pages = [
        {
            "title": "Održavanje",
            "url": "https://hr.wikipedia.org/wiki/Održavanje",
        },
        {
            "title": "Automatizacija i kontrola",
            "url": "https://hr.wikipedia.org/wiki/Pametna_zgrada",
        },
    ]

    django_pages = [
        {
            "title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
        },
        {
            "title": "Django Rocks",
            "url": "http://www.djangorocks.com/"
        },
        {
            "title": "How to Tango with Django",
            "url": "http://www.tangowithdjango.com/"
        },
    ]

    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org"},
    ]

    cats = {
        "Montaža električnih instalacija": {"pages": el_insatalacije_pages},
        "Održavanje i inspekcija": {"pages": odrzavanje_inspekcija_pages},
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages},
    }

    # If you want to add more categorues or pages,
    # ad them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # if you are using python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out ctategories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c} - {p}")


def add_page(cat, title, url, views=10):
    """populate page objects in database"""
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    """populate category objects in database"""
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()
