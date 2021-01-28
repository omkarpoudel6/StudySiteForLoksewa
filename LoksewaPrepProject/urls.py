
from django.contrib import admin
from django.urls import path
# from Loksewa.views import test,questions,category
from . import settings

from Loksewa import views
from django.contrib.staticfiles.urls import static
from Users.views import Login,Signup,Logout,Home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',Login,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout/',Logout,name='logout'),

    path('',Home,name='home'),

    path('test/',views.test,name='test'),
    path('questions/',views.questions,name='questions'),
    path('category/<int:id>/',views.category,name='category')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
