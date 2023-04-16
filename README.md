# QR API Free - Diego Rinaldo Cazon Condori

1. Link Servicio: https://qrservicefree.diegocazon.repl.co/generate_qr/
2. Example Data:
    - data = { "cadena":"www.google.com" }
    - data = { "cadena":"Texto Codificado" }
    - data = { "cadena":"Nombre" }
3. Response Example:
    - { url: "https://qrservicefree.diegocazon.repl.co/static/qr/htttanh.png","limit_time":"10 minute" }
    limit_time = time limit the url valid.

#Example AJAX: <br>
$.ajax({
<br>    url:"https://qrservicefree.diegocazon.repl.co/generate_qr/",
<br>    data:{ "cadena": "eve.holt@reqres.in" },
<br>    beforeSend:BeforeSend,
<br>    complete:OnComplete,
<br>    success:OnSuccess,
<br>    error:OnError });