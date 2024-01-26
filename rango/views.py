"""Required modules"""
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from rango.models import Category, Page
from rango.forms import CategoryForm, ContactForm, PageForm
from rango.forms import UserForm, UserProfileForm


def index(request):
    """
    Query the database for a list of All categories currently stored.
    Order the categories by no. likes in descending order.
    Retrieve the top 5 only - of all if less than 5.
    Place the list in our context_dict dictionary
    that will be passed to the template engine.
    """
    category_list = Category.objects.order_by("-likes")  # [:5]
    page_list = Page.objects.order_by("-views")  # [:5]
#    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return contact_sucess(request)
    else:
        form = ContactForm()

    context_dict = {"categories": category_list, "pages": page_list, "form": form}

    return render(request, "rango/index.html", context=context_dict)


def smart_house(request):
    """Random Test context"""
    smart_house_ctx = {
        "smart_house": """Pametna kuća predstavlja inovativan
                       koncept modernog doma koji integrira napredne
                       tehnologije kako bi unaprijedila udobnost, sigurnost i
                       energetsku učinkovitost. Opremljena različitim pametnim
                       uređajima i senzorima, pametna kuća omogućuje
                       korisnicima daljinsko upravljanje i praćenje različitih
                       aspekata svakodnevnog života putem mobilnih uređaja ili
                       glasovnih naredbi.""",
    }
    return render(request, "rango/smart_house.html", context=smart_house_ctx)


def show_category(request, category_name_slug):
    """Create a context dictionary which we can pass to the template
    rendering engine."""
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
        context_dict["pages"] = pages

        # We also add the category object from the database to the context
        # dictionary. We'll use this in the template to verify that the
        # category exists.
        context_dict["category"] = category

    except ObjectDoesNotExist:
        # We get here if we didn't find the specified category. Don't do
        # anything the template will display the "no category" message for us.
        context_dict["category"] = None
        context_dict["pages"] = None

    return render(request, "rango/category.html", context_dict)


@login_required
def add_category(request):
    """add category view"""
    form = CategoryForm()

    # A HTTP POST?
    if request.method == "POST":
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            # form.save(commit=True)
            category = form.save(commit=True)
            print(category, category.slug)
            # Now that the category is saved
            # we could give a confirmatin message
            # But since the most recent category added is on the index page
            # then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contined errors
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error message (if any).
    return render(request, "rango/add_category.html", {"form": form})


def contact(request):
    """contact viev"""
    # form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return contact_sucess(request)
    else:
        form = ContactForm()

    return render(request, "rango/contact_form.html", {"form": form})


def contact_sucess(request):
    """Thx mesage"""
    return render(request, "rango/contact_sucess.html")


@login_required
def add_page(request, category_name_slug):
    """Add page enable from website"""
    try:
        category = Category.objects.get(slug=category_name_slug)
    except ObjectDoesNotExist:
        category = None

    form = PageForm()
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {"form": form, "category": category}
    return render(request, "rango/add_page.html", context_dict)


def about(request):
    """Retarded about function"""
    return render(request, "rango/about.html", {})


def register(request):
    """
    A boolean value for telling the template
    whether the registration was successful.
    Set to False initially. Code changes value to
    True when registration succeeds.
    """
    registered = False

    # If it's a HTTP Post, we're interested in processing form data.
    if request.method == "POST":
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set te user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # if so, we need to get it from the input form and
            # put it in the UserProfile model.
            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

                # Now save the UserProfile model instance.
                profile.save()

                # Update our variable to indicate that the template
                # registration was sucessful.
                registered = True
            else:
                # Invalid form or forms - mistakes or something else?
                # print problems to the terminal.
                print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, se we render out form using two ModelForm
        # instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Rendier te template depending on the contex.
    return render(request, "rango/register.html/",
                  {
                   "user_form": user_form,
                   "profile_form": profile_form,
                   "registered": registered
                   })


def user_login(request):
    """
    If the request is a HTTP POST, try to pull out the relevant
    information.
    """
    if request.method == "POST":
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no
        # user with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Smart-Relay.hr account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("""napravi login_error html povezi sa view
            user_login().""")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {})


@login_required
def restricted(request):
    """Check @login_required decorator"""
    return render(request, 'rango/restricted.html', {})


@login_required
def user_logout(request):
    """
    Use the login_required decorator to ensure only those logged in can
    acess the view
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))
