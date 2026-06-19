from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Categoria, Prato, Mesa, Pedido
from .forms import PratoForm, MesaForm, PedidoForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'gestao/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    total_pratos = Prato.objects.count()
    total_mesas = Mesa.objects.count()
    pedidos_pendentes = Pedido.objects.filter(estado='pendente').count()
    return render(request, 'gestao/dashboard.html', {
        'total_pratos': total_pratos,
        'total_mesas': total_mesas,
        'pedidos_pendentes': pedidos_pendentes,
    })


# ── Pratos ──────────────────────────────────────────────
@login_required
def lista_pratos(request):
    query = request.GET.get('q', '')
    pratos = Prato.objects.filter(nome__icontains=query) if query else Prato.objects.all()
    return render(request, 'gestao/lista_pratos.html', {'pratos': pratos, 'query': query})


@login_required
def detalhe_prato(request, pk):
    prato = get_object_or_404(Prato, pk=pk)
    return render(request, 'gestao/detalhe_prato.html', {'prato': prato})


@login_required
def criar_prato(request):
    form = PratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Prato criado com sucesso!')
        return redirect('lista_pratos')
    return render(request, 'gestao/form_prato.html', {'form': form, 'titulo': 'Novo Prato'})


@login_required
def editar_prato(request, pk):
    prato = get_object_or_404(Prato, pk=pk)
    form = PratoForm(request.POST or None, instance=prato)
    if form.is_valid():
        form.save()
        messages.success(request, 'Prato atualizado!')
        return redirect('lista_pratos')
    return render(request, 'gestao/form_prato.html', {'form': form, 'titulo': 'Editar Prato'})


@login_required
def apagar_prato(request, pk):
    prato = get_object_or_404(Prato, pk=pk)
    if request.method == 'POST':
        prato.delete()
        messages.success(request, 'Prato apagado!')
        return redirect('lista_pratos')
    return render(request, 'gestao/confirmar_apagar.html', {'objeto': prato})


# ── Mesas ───────────────────────────────────────────────
@login_required
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestao/lista_mesas.html', {'mesas': mesas})


@login_required
def criar_mesa(request):
    form = MesaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mesa criada com sucesso!')
        return redirect('lista_mesas')
    return render(request, 'gestao/form_mesa.html', {'form': form, 'titulo': 'Nova Mesa'})


@login_required
def editar_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    form = MesaForm(request.POST or None, instance=mesa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mesa atualizada!')
        return redirect('lista_mesas')
    return render(request, 'gestao/form_mesa.html', {'form': form, 'titulo': 'Editar Mesa'})


@login_required
def apagar_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        mesa.delete()
        messages.success(request, 'Mesa apagada!')
        return redirect('lista_mesas')
    return render(request, 'gestao/confirmar_apagar.html', {'objeto': mesa})


# ── Pedidos ─────────────────────────────────────────────
@login_required
def lista_pedidos(request):
    estado = request.GET.get('estado', '')
    pedidos = Pedido.objects.filter(estado=estado) if estado else Pedido.objects.all()
    return render(request, 'gestao/lista_pedidos.html', {'pedidos': pedidos, 'estado': estado})


@login_required
def detalhe_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'gestao/detalhe_pedido.html', {'pedido': pedido})


@login_required
def criar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido criado com sucesso!')
        return redirect('lista_pedidos')
    return render(request, 'gestao/form_pedido.html', {'form': form, 'titulo': 'Novo Pedido'})


@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido atualizado!')
        return redirect('lista_pedidos')
    return render(request, 'gestao/form_pedido.html', {'form': form, 'titulo': 'Editar Pedido'})


@login_required
def apagar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido apagado!')
        return redirect('lista_pedidos')
    return render(request, 'gestao/confirmar_apagar.html', {'objeto': pedido})