from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings  # ✅ ADD THIS
from django.conf.urls.static import static  # ✅ ADD THIS
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("receipes/", receipes, name="receipes"),
    path('delete_receipe/<id>/' , delete_receipe, name="delete_receipe"),
    path('update_receipe/<id>/' , update_receipe, name="update_receipe"),
    path("", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path('success_page/', success_page, name="success_page"),
    path('admin/', admin.site.urls),
]

# ✅ Correct usage of `settings.DEBUG`
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
