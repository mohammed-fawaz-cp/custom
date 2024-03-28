# create urls for views
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

# create a url for the views
urlpatterns = [
    path('', views.BikeViewSet.as_view()),
    path('upload/', views.UploadData.as_view()),
    path('delete/<int:pk>/', views.DeleteData.as_view()),
    path('update/<int:pk>/', views.Update.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)