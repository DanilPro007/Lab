from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.time_home, name='tm'),
    path('decorator/', views.decorator_home, name='dcr'),
    path('worker/', views.worker_home, name='wrk'),
    path('firms/', views.firms_home, name='frm'),
    path('irrigation/', views.irrigation_home, name='irr'),
    path('plants/',views.plants_home,name='plt'),
    path("plants/create",views.createpl,name='createpl'),
    path ('plants/<int:pk>/update', views.plantsUpdateView.as_view(),name='upd'),
    path ('plants/<int:pk>/delete', views.plantsDeleteView.as_view(),name='del'),
    path("irrigation/create",views.createir,name='createir'),
    path ('irrigation/<int:pk>/update', views.irrigationUpdateView.as_view(),name='updir'),
    path ('irrigation/<int:pk>/delete', views.irrigationDeleteView.as_view(),name='delir'),
    path ('firms/<int:pk>/update', views.firmsUpdateView.as_view(),name='updfrm'),
    path ('firms/<int:pk>/delete', views.firmsDeleteView.as_view(),name='delfrm'),
    path("firms/create",views.createfrm,name='createfrm'),
    path ('worker/<int:pk>/update', views.workerUpdateView.as_view(),name='updwrk'),
    path ('worker/<int:pk>/delete', views.workerDeleteView.as_view(),name='delwrk'),
    path("worker/create",views.createwrk,name='createwrk'),
    path ('decorator/<int:pk>/update', views.decoratorUpdateView.as_view(),name='upddcr'),
    path ('decorator/<int:pk>/delete', views.decoratorDeleteView.as_view(),name='deldcr'),
    path("decorator/create",views.createdcr,name='createdcr'),
    path ('time/<int:pk>/update', views.timeUpdateView.as_view(),name='updtm'),
    path ('time/<int:pk>/delete', views.timeDeleteView.as_view(),name='deltm'),
    path("time/create",views.createtm,name='createtm'),
]

