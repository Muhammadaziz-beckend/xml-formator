from django.urls import path, include

from .views import *
from .ysge import swagger

urlpatterns = [
    path("upload-excel/", UpdateDataAPIView.as_view(), name="upload-excel"),
    path("export-excel/", ExportExcelView.as_view(), name="export-excel"),
    path("html/", html,name='upload_excel'),
]

urlpatterns += swagger
