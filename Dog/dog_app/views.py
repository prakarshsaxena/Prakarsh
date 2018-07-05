from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import HttpResponse
from .models import Dog
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import DogForm, RegistrationForm
from django.core.mail import EmailMessage
from django.conf import settings


def index(request):
    form = DogForm()
    dogs = Dog.objects.all()
    context = {'dogs': dogs}
    return render(request, 'dog_app/index.html', {'form': form, 'dogs' : dogs})


def create(request):
    print(request.POST)
    dog = Dog(name=request.POST.get('name', ""), breed=request.POST.get('breed', ""))
    dog.save()
    return redirect('/')


def edit(request, dog_id):

    dog = Dog.objects.get(pk=dog_id)
    context = {'dog' : dog}
    return render(request, 'dog_app/edit.html', context)


def update(request, id):
    dog = Dog.objects.get(pk=id)
    dog.name = request.POST['name']
    dog.breed = request.POST['breed']
    dog.save()
    return redirect('/')


def delete(request, dog_id):
    Dog.objects.get(pk=dog_id).delete()

    return redirect('/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': settings.BASE_URL,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            username = form.cleaned_data['email']
            email = EmailMessage(
                        mail_subject, message, 'prakarshsaxena31@gmail.com', to=[username]
            )
            email.content_subtype = "html"
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            #password = form.cleaned_data['password1']
            #form.save()

            #user = authenticate(username=username, password=password)


            #if user:
             #   login(request, user)


            #return redirect('index')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('email_or_mobile')
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        return redirect('index')

    else:
        return render(request, 'registration/login.html')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("Hi")
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active= True
        user.save()
        username, password = user.username, 'pass1234'
        u = authenticate(username = username, password = password)
        login(request, u)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



"""
def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
"""