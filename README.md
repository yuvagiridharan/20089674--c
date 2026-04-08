This project contains 4 programming tasks completed as part of  Tasks 1 and 2 are written in C# and Tasks 3 and 4 are written in Python.

## Task 1 — Churros Food Truck App (C#)
A food truck ordering system where the stall owner places and delivers churros orders using a Queue (FIFO).

**Run:**
```bash
cd que01/churrosapp
dotnet run
```
**Files:** `Program.cs` `churros.cs` `order.cs` `OrderTests.cs`

**Menu options:** Press `1` to place order → Press `2` to deliver order → Press `0` to exit

**Unit Tests:** 5 tests for `pay_bill()` method — single item, multiple quantity, zero price, negative price exception, return value check

---

## Task 2 — Periodic Table Lookup (C#)
Look up any of the first 30 elements by entering an atomic number. Uses `Dictionary<int, Element>` for fast O(1) lookup.

**Run:**
```bash
cd que02/Periodictable
dotnet run
```
**Files:** `Program.cs` `Element.cs`

**Example:**
```
Hi there! Happy to help!
Provide atomic number (1-30): 1
Atomic Number : 1  |  Name : Hydrogen  |  Symbol : H  |  Class : Nonmetal
Do you want to know more elements [y/n]?
```

---

## Task 3 — EasyDrive Car Rental (Python)
TCP client-server app. Client collects customer details and sends to server. Server saves to TinyDB database and returns a unique registration number.

**Install:**
```bash
cd que03/rentalcar
python3 -m venv venv && source venv/bin/activate
pip install tinydb rich questionary
```
**Terminal 1 — server first:**
```bash
python3 que03_server.py
```
**Terminal 2 — then client:**
```bash
python3 que03_client.py
```
**Files:** `que03_server.py` `que03_client.py`

**Customer fields:** Full Name · Home Address · PPS Number (1234567A) · Driving Licence Number

---

## Task 4 — Books Web Scraper (Python)
Scrapes book titles, ratings and prices from a website, saves to CSV, then reads and displays CSV data in terminal.

**Install:**
```bash
cd que04/webscrub
python3 -m venv venv && source venv/bin/activate
pip install requests beautifulsoup4
```
**Run:**
```bash
python3 que04.py
```
**Files:** `que04.py` `books.csv`

**URL:** https://books.toscrape.com/catalogue/category/books/travel_2/index.html

---

## Folder Structure
```
20089674/
├── que01/churrosapp/      → Task 1 C# Churros App
├── que02/Periodictable/   → Task 2 C# Periodic Table
├── que03/rentalcar/       → Task 3 Python EasyDrive
├── que04/webscrub/        → Task 4 Python Web Scraper
└── .github/workflows/     → CI/CD Pipeline
```

---

## CI/CD — GitHub Actions
Every push triggers automatic build and test for all 4 tasks. See **Actions** tab on GitHub.

| Task | Language | Libraries |
|------|----------|-----------|
| Task 1 | C# .NET 8 | System.Collections.Generic |
| Task 2 | C# .NET 8 | System.Collections.Generic |
| Task 3 | Python 3.11 | tinydb, socket, json, uuid |
| Task 4 | Python 3.11 | requests, beautifulsoup4, csv |

---
