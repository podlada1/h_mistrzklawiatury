# h_mistrzklawiatury — Mistrzyni klawiatury

Prosta gra po polsku dla pięciolatki. Przyjazny kotek, duże znaki,
podpowiedź na ekranowej klawiaturze i gwiazdki za sukcesy.
Bez limitu czasu, reklam, internetu i kar za pomyłki.

## Uruchomienie

Potrzebny jest Python 3 z Tkinterem (standardowy instalator Pythona dla Windows
zwykle go zawiera). Nie trzeba instalować pakietów przez pip.

W folderze z grą uruchom:

```console
python mistrz_klawiatury.py
```

Na Windows można też użyć `py mistrz_klawiatury.py` lub dwukrotnie kliknąć plik,
jeśli pliki `.py` są powiązane z Pythonem.

Na Ubuntu/Debian, jeśli brakuje Tkintera: `sudo apt install python3-tk`,
a następnie `python3 mistrz_klawiatury.py`. W środowisku bez pulpitu gra wymaga
serwera wyświetlania; na Windows najprościej uruchomić ją windowsowym Pythonem,
nie w terminalu WSL.

## Zabawa

- **Litery** — znajdź i naciśnij pokazaną literę; nie trzeba używać Shift.
- **Cyferki** — znajdź cyfrę, również na klawiaturze numerycznej z włączonym Num Lock.
- **Słowa** — przepisuj krótkie słowa po jednej literze.
- Żółty klawisz na rysunku pokazuje, czego teraz szukać na prawdziwej klawiaturze.
- Za każdą literę, cyfrę lub całe słowo jest gwiazdka. Co 10 sukcesów kotek świętuje.
- **Od początku** zeruje wynik; zmiana trybu również rozpoczyna nową zabawę.
- **F11** przełącza pełny ekran, **Esc** wraca do okna.

Najlepiej zacząć od kilku minut wspólnej zabawy w trybie „Litery”.
Gra ćwiczy podstawowe litery A–Z; polskie znaki i skróty klawiaturowe zostawiamy na później.

## Independent project

This folder is a complete, independent project. It does not need `h_pokemon`
or the original `5yearsold` folder. The game code is in `mistrz_klawiatury.py`.
No pip dependencies or build step are required.

**This is a desktop application, not a website.** Run it on a computer with a
graphical desktop. Docker, a web server, and Kubernetes are not needed to play.

## Basic checks

From this folder, run:

```sh
python3 -m compileall -q mistrz_klawiatury.py
```

This checks Python syntax, not gameplay. After editing, launch the game and
try Litery, Cyferki, Słowa, reset, and fullscreen.

## Use with GitHub

Create an **empty** GitHub repository named `h_mistrzklawiatury` (no README).
From this folder, replace `YOUR_USERNAME` and run:

```sh
git init -b main
git add .
git commit -m "Initial standalone keyboard game"
git remote add origin https://github.com/YOUR_USERNAME/h_mistrzklawiatury.git
git push -u origin main
```

The workflow in `.github/workflows/ci.yml` checks syntax and imports on every
push and pull request. It does not open a window or publish an installer.
Check results in GitHub's **Actions** tab.
