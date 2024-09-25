from django.urls import path
from uae_visa import views


urlpatterns = [
    path('visa_info/', views.visa_info, name='visa_info'),
    # path('visa_app_v2/<str:serial_no>/', views.visa_app_v2, name='visa_app_v2'),
    path('edit/<str:serial_no>/',views.edit,name='edit'),
    path('edit_visa_info/<int:serial_id>/',views.edit_visa_info,name='edit_visa_info'),

    # path('visa_app/', views.visa_app, name='visa_app'),
    
    # path('visa_app_update/<str:serial_no>', views.visa_app_update, name='visa_app_update'),
    

    path('form_1_list/', views.form_1_list, name='form_1_list'),
    path('form_2_list/', views.form_2_list, name='form_2_list'),

    path('form_1_search/', views.form_1_search, name='form_1_search'),
    path('form_2_search/', views.form_2_search, name='form_2_search'),

    path('pdf_for_visa_info/<int:serial_id>/', views.pdf_for_visa_info, name="pdf_for_visa_info"),
    path('pdf_application/<str:serial_no>/', views.pdf_application, name='pdf_application'),
    path('pdf_fly_air/<str:serial_no>/', views.pdf_fly_air, name="pdf_fly_air"),
    path('pdf_for_agreement/<str:serial_no>/', views.pdf_for_agreement, name="pdf_for_agreement"),

    
    
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'), 
]
