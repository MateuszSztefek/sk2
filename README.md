# Prosty serwer i klient usługi FTP

Klient może się połączyć z serwerem, zobczyć jakie są pliki w folderze gdzie jest serwer i pobrać jakiś. Serwer może obsługiwać kilku klientów na raz (każdy klient jest obsługiwany w innym wątku). Serwer po uruchomieniu wypisuje na konsoli takie informacje jak kto się podłączył, ile aktualnie jest połączeń i jakie komendy zostały użyte przez poszczególnych klientów

Wysyłanie komend z klienta do serwera działa w ten sposób, że najpierw jest wysyłana domyślna wiadomość długości 64B, która określa jak długa będzie docelowa wiadomość, która jest wysyłana w następnej kolejności. Serwer odczytuje jaką komendę otrzymał (możliwe komendy to: !SHOW, !GET <filename>, !DISCONNECT). Plik jest przesyłany w ten sposób, że serwer sprawdza czy ma taki plik, jeżeli tak to wysyła najpiew nazwę pliku, a później cały plik do klienta. Koniec pliku jest zaznaczany poprzez dodanie "\<END\>" na końcu, dzięki czemu klient wie gdzie kończy się plik.

Przykład działania serwera:

![image](https://github.com/MateuszSztefek/sk2/assets/88203590/09cf5de2-b6c8-4a06-8f8f-4c8e54b817c3)

Przykład działania klienta:

![image](https://github.com/MateuszSztefek/sk2/assets/88203590/43514123-3e55-4338-819f-ea8f8525768b)
