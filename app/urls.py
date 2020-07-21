from django.urls import path
from .views import validateNumber ,withdrawmoney ,cardpageshow,balancemoney,resetpin,debitmoney,depositmoney,updatepinmoney

urlpatterns = [
    path('',validateNumber),
    path('withdraw',withdrawmoney),
    path('balance/<str:name>',balancemoney),
    path('debit/<str:name>',debitmoney),
    path('deposit/<str:name>',depositmoney),
    path('update_pin/<str:name>',updatepinmoney),
    path('reset/',resetpin),
    path('cardpage/',cardpageshow),
    path('cardpage/reset/',resetpin),
]
