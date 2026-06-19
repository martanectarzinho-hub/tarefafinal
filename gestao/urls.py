from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registar/', views.registar_view, name='registar'),

    # Pratos
    path('pratos/', views.lista_pratos, name='lista_pratos'),
    path('pratos/<int:pk>/', views.detalhe_prato, name='detalhe_prato'),
    path('pratos/novo/', views.criar_prato, name='criar_prato'),
    path('pratos/<int:pk>/editar/', views.editar_prato, name='editar_prato'),
    path('pratos/<int:pk>/apagar/', views.apagar_prato, name='apagar_prato'),

    # Mesas
    path('mesas/', views.lista_mesas, name='lista_mesas'),
    path('mesas/nova/', views.criar_mesa, name='criar_mesa'),
    path('mesas/<int:pk>/editar/', views.editar_mesa, name='editar_mesa'),
    path('mesas/<int:pk>/apagar/', views.apagar_mesa, name='apagar_mesa'),

    # Pedidos
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', views.detalhe_pedido, name='detalhe_pedido'),
    path('pedidos/novo/', views.criar_pedido, name='criar_pedido'),
    path('pedidos/<int:pk>/editar/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/<int:pk>/apagar/', views.apagar_pedido, name='apagar_pedido'),
]