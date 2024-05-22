from django.contrib import admin
from django.urls import path
from ChatBotApi.views import getbotresponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getbotresponse', getbotresponse, name = "getbotresponse")
]
