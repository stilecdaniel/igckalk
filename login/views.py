from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def product_detail(request, product):
    return render(request, "objednavky/product_detail.html", {"product":product.replace("-"," ")})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'objednavky/change_password.html', {
        'form': form
    })

def profile_info(request):
    return render(request, "objednavky/profile.html")

@login_required()
def home(request):
    user = request.user
    print(user)
    if user.is_active:
        return render(request, "objednavky/home.html" )
    return render(request, "pending_auth.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            userEmail = form.cleaned_data["email"]
            user.save()

            send_mail(
                subject="Potvrdenie používateľa",
                message="Vážení zákazník firmy I.G.C.Strojal s.r.o., \nVaša registrácia bola úspešná, po prihlásení na stránke www.XXXX.sk si možete vytvárať cenové ponuky a objednávky našich komínoých systémov.\nV prípade akýchkoľvek otázok ohľadom používania systému, vytvárania cenových ponúk, odosielania objednávok, kontaktujte Ing. Lenku Klottonovú, mailovú adresa: klottonova.igc@gmail.com, tel.č. 0907968 769.\nVprípade technických a obchodných otázok ohľadom komínových systémov, kontaktujte Bc. Gabriela Klottona, mailová adresa: klotton@igc.sk, tel.č.: 0903 711 469.\n\nTešíme sa na spoluprácu,\n\nTím I.G.C.Strojal s.r.o.",
                from_email="testigc88@gmail.com",
                recipient_list=[userEmail],
                fail_silently=False,
                )

        return redirect("auth")
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form":form})

def auth(request):
    return render(request, "pending_auth.html")

def contact(request):
    return render(request, "contacts.html")