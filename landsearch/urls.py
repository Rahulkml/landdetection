from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('cards/', views.card_list, name='cards'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('customers/', views.member_list, name='customers'),
    path('customers/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('revenue/', views.RevenueListView.as_view(), name='revenue'),
    path('logout', views.logout, name='log-out'),
    path('search/', views.search_view, name="search"),
    path('find/<int:pk>', views.land_search, name="find"),
    path('verify/', views.verify_view, name="verify"),
    path('notifications/', views.notification_view, name="notifications"),
    path('disable/<int:pk>', views.disable, name="disable"),
]