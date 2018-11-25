import time
import requests
import json

inicio = 0 
fim = 0
c2 = 0
js = {
    "email":"eduardojvr10@gmail.com", 
    "segunda":"12:00 ~ 13:00 ",
    "terca":"12:00 ~ 13:00",
    "quarta":"12:00 ~ 13:00",
    "quinta":"12:00 ~ 13:00",
    "sexta":"12:00 ~ 13:00",
    "sabado":"12:00 ~ 13:00",
    "domingo":"12:00 ~ 13:00"
}
js = json.dumps(js)

while True:
    req = requests.post('https://notificamais.herokuapp.com/notifyEvent/data_mensage',js)
    if req.status_code == 200: 
        print(req)
        if c2 == 1:
            break
    elif (req.status_code != 200 and c2 == 0):
        c2 = 1
        inicio = time.time()
    else:
        print("Erro interno do servidor! ", req.status_code)
fim = time.time()

print(fim-inicio)
