from django.conf import settings # 画像を表示する設定
from django.conf.urls.static import static # 画像を表示する設定
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]

"""画像を表示する設定 settingsがDEBUGの場合、MEDIA_URLとMEDIA_ROOTをurlpatternsに保存する"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
