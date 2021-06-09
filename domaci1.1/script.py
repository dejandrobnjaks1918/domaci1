import requests

url = 'https://getpantry.cloud/apiv1/pantry/140478cb-7f41-4868-bf72-b57668433dfb/basket/testBasket'
data = {
   "id":"asd123",
   "ime":"asdasd",
   "prezime":"asdasd",
   "smer":"it",
   "predmet":[
      "PWA",
      "RISO",
      "WSIT"
   ],
   "prosek":7.7,
   "kontakt":{
      "adresa":"asd 123",
      "mesto":"beograd",
      "telefon":"123456789"
   }
}
r = requests.post(url, data)
print(r)