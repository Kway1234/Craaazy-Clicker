# 🖱️💥 Craaazy-Clicker

> *Klick. Klick. Klick. KLICK. Warum ist mein Cursor jetzt ein Lama?*

**Craaazy-Clicker** ist ein Browser-Idle-Game, bei dem du mit einem einzigen Klick anfängst und am Ende ein ganzes Multiversum aus völlig absurden Klick-Maschinen regierst. Klingt normal? Ist es nicht. Alle paar Minuten passiert ein **Crazy Event**, das die Regeln des Spiels komplett auf den Kopf stellt.

---

## 📖 Inhalt

- [Worum geht's?](#-worums-gehts)
- [Features](#-features)
- [Crazy Events](#-crazy-events)
- [Upgrades & Gebäude](#-upgrades--gebäude)
- [Installation](#-installation)
- [Steuerung](#-steuerung)
- [Projektstruktur](#-projektstruktur)
- [Roadmap](#-roadmap)
- [Mitmachen](#-mitmachen)
- [Lizenz](#-lizenz)

---

## 🤔 Worum geht's?

Im Zentrum des Bildschirms liegt der **Große Rote Knopf**. Jeder Klick bringt dir **Craaazies** (🌀) – die offizielle Währung des Spiels. Mit Craaazies kaufst du Helfer, die für dich klicken, Upgrades, die jeden Klick wertvoller machen, und Gebäude, die Craaazies produzieren, während du schläfst.

Der Haken: Der Knopf hat seinen eigenen Kopf. Er läuft weg, wird größer, kleiner, teilt sich in fünf Knöpfe auf oder verlangt, dass du ihm ein Kompliment machst. Wer am verrücktesten mitspielt, gewinnt am meisten.

---

## ✨ Features

- 🖱️ **Klassisches Klick-Gameplay** – einfach zu lernen, unmöglich wieder aufzuhören
- 🌀 **Crazy Events** – zufällige Ereignisse, die das Spiel für 30–60 Sekunden komplett verändern
- 🏭 **15+ Gebäude** – vom Hamster im Laufrad bis zur Quanten-Klick-Fabrik
- 🔁 **Prestige-System „Reboot the Universe"** – setz alles zurück und erhalte dauerhafte *Chaos-Kristalle* 💎
- 🏆 **Über 100 Achievements** – darunter „Hast du überhaupt einen Job?" (1 Mio. Klicks)
- 💾 **Auto-Save** im Browser (LocalStorage) plus Export/Import als Text-Code
- 🌙 **Offline-Fortschritt** – deine Gebäude arbeiten weiter, wenn der Tab zu ist
- 🎨 **Skins** für Knopf und Cursor (Lama, Toaster, Gummiente, …)
- 📱 **Läuft auf Desktop und Handy** – Tippen zählt auch als Klicken

---

## 🌪️ Crazy Events

Alle 2–5 Minuten wird gewürfelt. Hier ein paar Beispiele:

| Event | Was passiert |
|---|---|
| 🏃 **Fluchtknopf** | Der Knopf rennt vor deinem Cursor weg. Erwischst du ihn, gibt's 10× Craaazies. |
| 🪞 **Spiegelwelt** | Die Maus ist invertiert. Links ist rechts. Oben ist unten. Viel Glück. |
| 🐌 **Schneckentempo** | Alles läuft halb so schnell – aber jeder Klick zählt dreifach. |
| 🎉 **Konfetti-Sturm** | Konfetti regnet vom Himmel. Jedes angeklickte Stück ist ein Bonus. |
| 🧨 **Knopf-Explosion** | Der Knopf zerfällt in 8 Mini-Knöpfe. Klick sie alle, bevor sie verschwinden! |
| 🦙 **Lama-Invasion** | Lamas laufen über den Bildschirm und klauen Craaazies. Klick sie weg! |
| 🤫 **Pssst** | Klicken ist verboten. Wer 20 Sekunden widersteht, wird belohnt. |
| 🎰 **Doppelt oder nichts** | Setz die Hälfte deiner Craaazies. Münzwurf. Kein Zurück. |

---

## 🏗️ Upgrades & Gebäude

Ein kleiner Auszug aus dem Shop:

| Gebäude | Preis (Start) | Produktion |
|---|---|---|
| 🐹 Hamster im Laufrad | 15 🌀 | 0,1 🌀/s |
| 👵 Oma mit Maus | 100 🌀 | 1 🌀/s |
| 🤖 Klick-Roboter | 1.100 🌀 | 8 🌀/s |
| 🐒 Affen-Callcenter | 12.000 🌀 | 47 🌀/s |
| 🍞 Toaster-Farm | 130.000 🌀 | 260 🌀/s |
| 🌋 Vulkan-Klicker | 1,4 Mio. 🌀 | 1.400 🌀/s |
| ⚛️ Quanten-Klick-Fabrik | 20 Mio. 🌀 | 7.800 🌀/s |
| 🕳️ Schwarzes Loch (klickt sich selbst) | 330 Mio. 🌀 | 44.000 🌀/s |

Jedes Gebäude wird beim Kauf **15 % teurer**. Ab 25, 50 und 100 Stück gibt es Spezial-Upgrades, die die Produktion verdoppeln.

---

## 🚀 Installation

### Voraussetzungen

- [Node.js](https://nodejs.org/) **18** oder neuer
- npm (kommt mit Node.js)

### Lokal starten

```bash
# Repository klonen
git clone https://github.com/Kway1234/Craaazy-Clicker.git
cd Craaazy-Clicker

# Abhängigkeiten installieren
npm install

# Dev-Server starten
npm run dev
```

Danach im Browser **http://localhost:5173** öffnen und loslegen.

### Build für Produktion

```bash
npm run build     # erstellt den Ordner dist/
npm run preview   # testet den Build lokal
```

Der Inhalt von `dist/` kann auf jedem statischen Hoster (GitHub Pages, Netlify, …) veröffentlicht werden.

---

## 🎮 Steuerung

| Eingabe | Aktion |
|---|---|
| **Linksklick / Tippen** | Knopf drücken |
| **Leertaste** | Auch Knopf drücken (für Profis) |
| **B** | Shop öffnen / schließen |
| **A** | Achievements anzeigen |
| **S** | Spiel manuell speichern |
| **M** | Sound an / aus |
| **Esc** | Pause-Menü |

> ⚠️ Auto-Clicker sind erlaubt – aber der Knopf merkt es. Und er ist nachtragend.

---

## 📁 Projektstruktur

```
Craaazy-Clicker/
├── public/            # Bilder, Sounds, Icons
├── src/
│   ├── main.js        # Einstiegspunkt
│   ├── game/
│   │   ├── state.js       # Spielstand & Speichern/Laden
│   │   ├── buildings.js   # Gebäude-Definitionen
│   │   ├── upgrades.js    # Upgrades
│   │   ├── events.js      # Crazy Events
│   │   └── prestige.js    # Reboot the Universe
│   ├── ui/            # Komponenten für Knopf, Shop, Popups
│   └── styles/        # CSS
├── index.html
├── package.json
└── README.md
```

---

## 🗺️ Roadmap

- [x] Idee haben
- [x] README schreiben
- [ ] Großer Roter Knopf
- [ ] Shop & erste 8 Gebäude
- [ ] Crazy-Event-System
- [ ] Prestige „Reboot the Universe"
- [ ] Achievements
- [ ] Soundeffekte (sehr viele, sehr laute)
- [ ] Online-Bestenliste
- [ ] Multiplayer-Modus „Klick-Krieg" ⚔️

---

## 🤝 Mitmachen

Ideen für neue Crazy Events, Gebäude oder Skins sind immer willkommen!

1. Repository forken
2. Neuen Branch erstellen: `git checkout -b feature/mein-verruecktes-event`
3. Änderungen committen: `git commit -m "Neues Event: Gravitation aus"`
4. Branch pushen: `git push origin feature/mein-verruecktes-event`
5. Pull Request öffnen

Bugs oder Vorschläge bitte als [Issue](https://github.com/Kway1234/Craaazy-Clicker/issues) melden.

---

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** – mach damit, was du willst, aber gib dem Knopf ab und zu eine Pause.

---

<p align="center">
  Gemacht mit 🌀 und viel zu vielen Klicks.
</p>

Keine ahnung wer das geschrieben hat hat nichts mit dem repo zutun
