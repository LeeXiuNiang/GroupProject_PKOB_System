from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('report/', views.index, name='report'), #CRUD
    path('reportrequest/', views.index2, name='reportrequest'),  # CRUD
    path('reportdecline/', views.index3, name='reportdecline'),  # CRUD
    path('reportreceive/', views.index4, name='reportreceive'),
    path('<str:ic_no>', views.victim_detail, name="victim_detail"),
    path('viewreceive/<str:ic_no>', views.viewreceive_detail, name="viewreceive_detail"),
    path('view/<str:ic_no>', views.request_detail, name="request_detail"), #personal
    path('add/', views.add_detail, name="add_detail"),  # add
    path('request/', views.request, name="request"),  # add
    path('edit_detail/<str:ic_no>', views.edit_detail, name="edit_detail"), #edit
    path('receivereq_detail/<str:ic_no>', views.receivereq_detail, name="receivereq_detail"),
    path('detail_decline/<str:ic_no>', views.viewdecline_detail, name="detail_decline"),#edit
    path('acceptreq_detail/<str:ic_no>', views.acceptreq_detail, name="acceptreq_detail"), #edit
    path('notacceptreq_detail/<str:ic_no>', views.notacceptreq_detail, name="notacceptreq_detail"), #edit
    path('update_detail/<str:ic_no>', views.update_detail, name="update_detail"),  # update
    path('updatereq_detail/<str:ic_no>', views.updatereq_detail, name="updatereq_detail"),  # update
    path('declinereq_detail/<str:ic_no>', views.declinereq_detail, name="declinereq_detail"),
    path('receive_detail/<str:ic_no>', views.receive_detail, name="receive_detail"),
    path('delete_detail/<str:ic_no>', views.delete_detail, name="delete_detail"), #delete
    path('delete_request/<str:ic_no>', views.delete_request, name="delete_request"), #delete
    path('deletereq_detail/<str:ic_no>', views.deletereq_detail, name="deletereq_detail"), #delete
]

