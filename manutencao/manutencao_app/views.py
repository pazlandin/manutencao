from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from .models import Escada
from .forms import EscadaForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EscadaSerializer


# =========================
# 🔐 AUTENTICAÇÃO
# =========================

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next') or request.GET.get('next')

            if next_url == request.path:
                next_url = None

            if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)

            return redirect('home')

        else:
            messages.error(request, "Usuário ou senha inválidos")

    return render(request, 'manutencao_app/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# 🏠 HOME
# =========================

@login_required
def home(request):
    return render(request, 'manutencao_app/home.html')


# =========================
# 📋 ESCADAS (CRUD)
# =========================

@login_required
def lista_escadas(request):
    escadas = Escada.objects.all().order_by('-data_envio')

    busca = request.GET.get('q')
    modelo = request.GET.get('modelo')
    data = request.GET.get('data')

    if busca:
        escadas = escadas.filter(
            Q(codigo__icontains=busca) |
            Q(modelo__icontains=busca)
        )

    if modelo:
        escadas = escadas.filter(modelo=modelo)

    if data:
        escadas = escadas.filter(data_envio=data)

    return render(request, 'manutencao_app/lista_escadas.html', {'escadas': escadas})


@login_required
def criar_escada(request):
    if request.method == 'POST':
        form = EscadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_escadas')
    else:
        form = EscadaForm()

    return render(request, 'manutencao_app/criar_escada.html', {'form': form})


@login_required
def detalhe_escada(request, id):
    escada = get_object_or_404(Escada, id=id)
    return render(request, 'manutencao_app/detalhe_escada.html', {'escada': escada})


@login_required
def deletar_escada(request, id):
    escada = get_object_or_404(Escada, id=id)

    if request.method == 'POST':
        escada.delete()
        return redirect('lista_escadas')

    return render(request, 'manutencao_app/confirmar_delete.html', {'escada': escada})


# =========================
# ⚙️ AÇÕES / STATUS
# =========================

@login_required
def status_escadas(request):
    escadas = Escada.objects.exclude(status='concluida')
    return render(request, 'manutencao_app/status_escadas.html', {'escadas': escadas})


@login_required
def atualizar_status(request, id):
    escada = get_object_or_404(Escada, id=id)

    if request.method == 'POST':
        escada.status = request.POST.get('status')
        escada.save()

    return redirect('lista_escadas')


@login_required
def concluir_escada(request, id):
    escada = get_object_or_404(Escada, id=id)
    escada.status = 'concluida'
    escada.save()
    return redirect('detalhe_escada', escada.id)


# =========================
# 🔌 API
# =========================

@login_required
@api_view(['GET'])
def api_lista_escadas(request):
    escadas = Escada.objects.all()
    serializer = EscadaSerializer(escadas, many=True)
    return Response(serializer.data)