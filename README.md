# PKP Tracker – Mapa Podróży

Aplikacja webowa typu Full-Stack MVP służąca do rejestrowania, analizy i wizualizacji odbytych podróży kolejowych. Projekt zrealizowany w ramach zadania rekrutacyjnego.

🎥 **Demo aplikacji:** Nagranie prezentujące działanie aplikacji znajduje się w repozytorium pod nazwą `demo.mp4`.

---

## 1. Opis aplikacji i funkcjonalności

PKP Tracker pozwala użytkownikowi prowadzić cyfrowy dziennik przejazdów kolejowych i automatycznie przekształca wprowadzone dane w wizualne statystyki.

**Główne funkcjonalności:**
* **Zarządzanie przejazdami (CRUD):** Dodawanie nowych tras (stacja początkowa, stacja końcowa, data przejazdu, typ pociągu, ocena w skali 1–5), wyświetlanie pełnej historii relacji oraz usuwanie wybranych wpisów.
* **Interaktywna mapa połączeń:** Wizualizacja dostępnej siatki stacji kolejowych w Polsce oraz dynamiczne rysowanie odbytych podróży na mapie.
* **Moduł statystyk:** Automatyczne wyliczanie łącznej liczby przejazdów, średniej oceny podróży oraz najczęściej wybieranego typu pociągu (np. EIP, IC, TLK, REGIO).
* **Creative Twist – Wyzwanie Transsyberyjskie:** System grywalizacji, który na podstawie współrzędnych geograficznych oblicza rzeczywisty dystans przebytych tras w kilometrach i porównuje go na animowanym pasku postępu do całkowitej długości Kolei Transsyberyjskiej (9 289 km).

---

## 2. Opis techniczny i ciekawe rozwiązania

### Wykorzystane technologie
* **Backend:** Python 3.11, FastAPI, SQLModel (SQLAlchemy + Pydantic), Uvicorn.
* **Baza danych:** SQLite (lokalna baza plikowa generowana automatycznie).
* **Frontend:** HTML5, Vanilla JavaScript (Fetch API), TailwindCSS (CDN), Leaflet.js (biblioteka mapowa).

### Rozwiązania architektoniczne i UX
* **Obliczanie dystansu (Wzór Haversine'a):** Zamiast przechowywać sztywne odległości w bazie danych, aplikacja wylicza realny dystans w linii prostej pomiędzy współrzędnymi miast bezpośrednio po stronie klienta.
* **Dwuwarstwowa mapa (`L.layerGroup`):** Rozdzielono warstwę statycznej siatki możliwych połączeń (szare tło) od warstwy odbytych podróży (zielone linie). Zastosowano również niestandardowy renderer SVG z rozszerzonym marginesem (`padding: 1.0`), co eliminuje problem znikających linii podczas przesuwania mapy.
* **Walidacja i Defensive Programming:** 
  * Pola wyboru stacji wykorzystują natywny mechanizm `<datalist>` (wyszukiwanie z podpowiedziami) połączony z walidacją słownikową w JavaScript, co uniemożliwia wysłanie formularza z literówką lub nieobsługiwaną stacją.
  * Pole daty zostało ograniczone atrybutami zakresu (`1900–2026`).
  * Funkcje renderujące widok i mapę zostały zabezpieczone przed niekompletnymi danymi (np. wartościami `null`), co chroni aplikację przed błędami `TypeError`.

---

## 3. Instrukcja uruchomienia projektu lokalnie

### Krok 1: Pobranie repozytorium
* Sklonuj repozytorium: `git clone https://github.com/oskik/pkp-tracker`
* Wejdź do katalogu projektu

### Krok 2: Uruchomienie Backend API
1. Utwórz i aktywuj środowisko wirtualne (np. za pomocą Condy):
   * `conda create -n pkp-tracker python=3.11 -y`
   * `conda activate pkp-tracker`
2. Zainstaluj wymagane biblioteki:
   * `pip install fastapi uvicorn sqlmodel`
3. Uruchom serwer deweloperski FastAPI (z głównego katalogu projektu):
   * `uvicorn backend.main:app --reload`
   * Serwer API uruchomi się pod adresem `http://localhost:8000` (dokumentacja Swagger UI: `http://localhost:8000/docs`).

### Krok 3: Uruchomienie Frontendu
Aplikacja frontendowa nie wymaga osobnego procesu budowania (Node.js/npm):
1. Upewnij się, że serwer backendowy działa w tle na porcie `8000`.
2. Otwórz plik `frontend/index.html` bezpośrednio w dowolnej przeglądarce internetowej (np. klikając na niego dwukrotnie lub używając rozszerzenia Live Server w VS Code).

---

## 4. Wykorzystanie narzędzi AI

W procesie tworzenia aplikacji wspierałem się narzędziami AI (model Gemini oraz rozszerzenie Continue w VS Code) jako asystentem programistycznym (pair programming):
* **Architektura i Boilerplate API:** Wygenerowanie startowej struktury projektu w FastAPI, definicji modelu bazy danych w SQLModel, konfiguracji middleware CORS oraz podstawowych endpointów CRUD (`GET`, `POST`, `DELETE`).
* **Szablon UI i stylowanie:** Przygotowanie responsywnego układu strony w TailwindCSS, w tym kart statystyk oraz animowanego paska postępu dla „Wyzwania Transsyberyjskiego”.
* **Debugowanie i refaktoryzacja:** Analiza błędów konsoli, ujednolicenie mapowania danych w komunikacji `fetch` pomiędzy formularzem a API oraz zabezpieczenie kodu JavaScript przed błędami parsowania danych.

Przygotowany przeze mnie prompt systemowy definiujący wymagania dla agenta AI znajduje się w repozytorium w pliku z instrukcjami.