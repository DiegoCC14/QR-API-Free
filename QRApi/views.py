import pathlib , os
from .services.QR_service import generar_qr, borra_archivos_limite_time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.templatetags.static import static

DIR_ACTUAL = pathlib.Path(__file__).parent.absolute()  #La direccion actual


class QR(View):
    def get(self, request):

        request_data = request.GET.dict()
        borra_archivos_limite_time(
            DIR_ACTUAL / "static/qr",
            600)  #600=10 minutos, se borran archivos limite
        name_qr = generar_qr(request_data["cadena"], DIR_ACTUAL / "static/qr")
        print(
            f"https://qrservicefree.diegocazon.repl.co/{static(f'qr/{name_qr}')}"
        )
        return JsonResponse({
            "url":
            f"https://qrservicefree.diegocazon.repl.co/{static(f'qr/{name_qr}')}",
            "limit_time": "10 minutos"
        })
