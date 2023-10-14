from django.urls import path

from . import views

app_name = 'caps'

urlpatterns = [
	path('donate/', views.donate, name='donate'),
	path('add_deposit/', views.add_deposit, name='add_deposit'),
	path('deposits/<int:donation_id>/', views.deposits, name='deposits'),
	path('wait_for_vol/<int:donation_id>/', views.wait_for_vol, name='wait_for_vol'),
	path('not_wait_for_vol/<int:donation_id>/', views.not_wait_for_vol, name='not_wait_for_vol'),
    path('donations/', views.donations, name='donations'),
	path('donation_approval/<int:donation_id>/', views.donation_approval, name='donation_approval'),
	path('deposit_approval/<int:deposit_id>/<int:acceptation_id>/', views.deposit_approval, name='deposit_approval'),
	path('notifications/', views.notifications, name='notifications'),
    path('donation_accept/<int:acceptation_id>/', views.donation_accept, name='donation_accept'),
    path('donation_reject/<int:acceptation_id>/', views.donation_reject, name='donation_reject'),
    path('deposit_accept/<int:acceptation_id>/', views.deposit_accept, name='deposit_accept'),
    path('deposit_reject/<int:acceptation_id>/', views.deposit_reject, name='deposit_reject'),
	path('choose_deposit/<int:acceptation_id>/', views.choose_deposit, name='choose_deposit'),
    path('my_donations/', views.my_donations, name='my_donations'),
    path('donation/<int:donation_id>/', views.donation, name='donation'),
    path('my_deposits/', views.my_deposits, name='my_deposits'),
    path('deposit/<int:deposit_id>/', views.deposit, name='deposit'),
]