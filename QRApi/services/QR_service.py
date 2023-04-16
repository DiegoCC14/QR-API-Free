import qrcode, string, random, os, time


def generar_qr(cadena_qr, dir_img_guardado):

    img = qrcode.make(cadena_qr)
    nameQr = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
    img.save(str(dir_img_guardado / f"{nameQr}.png"))
    return f"{nameQr}.png"


def borra_archivos_limite_time(dir_folder, limite_time=600):
    archivos = os.listdir(dir_folder)
    ahora = time.time()
    for archivo in archivos:
        ruta_archivo = os.path.join(dir_folder, archivo)
        fecha_creacion = os.path.getctime(ruta_archivo)
        diferencia = ahora - fecha_creacion
        if diferencia > limite_time:  # 600 == 10 minutos
            os.remove(ruta_archivo)
