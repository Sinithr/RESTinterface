# RESTinterface
Plik interface.py uruchomić za pomocą python3.4.

Żądania należy wysyłać analogicznie do przykładu:
curl -i -H "Content-Type: application/json" -X PUT -d '{"km_radius": 2.0, "location": [37.760503, -122.433883]}' http://localhost:5000/interface

Oprócz podstawowej funkcjonalności dodano proste sortowanie i podstawowe zabezpieczenie w przypadku niewysłania danych.
