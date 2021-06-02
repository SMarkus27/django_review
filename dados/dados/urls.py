from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create_task),
    path('task/<id>', views.one_task, name='task'),
    path('task/<id>/update', views.update_task, name='task-update'),
    path('task<id>/delete', views.delete_task, name='task-delete'),
    path('grafico/', views.grafico),
    path('tinymce/', include('tinymce.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
