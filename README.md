# 🔥 Calories-Calculator

> A Flask web app that estimates a user's **daily caloric needs** based on personal stats (weight, height, age) **and the live outdoor temperature** of their city — colder cities = more calories needed.

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![Flask](https://img.shields.io/badge/framework-Flask-black)]()
[![WTForms](https://img.shields.io/badge/forms-WTForms-grey)]()

---

## 📌 Overview

Most calorie calculators ignore environment. This one takes a small step in the right direction by **scraping the current temperature for the user's city** (via `selectorlib` + a `temperature.yaml` rule file) and feeding it into a simplified Mifflin-St Jeor-inspired formula.

The formula in `calorie.py`:

```
calories = 10·weight + 6.5·height + 5 − 10·temperature
```

Cooler cities → higher calorie estimate. Warmer cities → lower.

> ⚠️ **Educational use only.** This is not a clinically validated nutrition formula — it's a programming exercise built on top of a Flask form, a web scraper, and class-based views.

## 🧱 Architecture

```
┌──────────────┐
│   Browser    │   GET /        ──▶  HomePage
└──────┬───────┘   GET /calories_form ──▶ CaloriesFormPage (form)
       │           POST /calories_form ─▶ CaloriesFormPage (result)
       ▼
┌─────────────────────────┐
│  Flask + WTForms        │
│  MethodView controllers │
└──────┬──────────────────┘
       │
       ├─▶ Temperature(country, city).get()
       │       │
       │       ▼   selectorlib + temperature.yaml
       │   scrapes current temperature from the web
       │
       └─▶ Calories(weight, height, age, temperature).calculate()
                  │
                  ▼
             10·w + 6.5·h + 5 − 10·t
```

## 🗂️ Project Structure

```
Calories-Calculator/
├── main.py                   # Flask app + MethodView routes
├── calorie.py                # Calories class — formula
├── temperature.py            # Temperature class — scrapes city temp
├── temperature.yaml          # selectorlib scraping rules
├── requirements.txt
├── static/
│   ├── main.css
│   ├── photo.jpg
│   └── photo.png
└── templates/
    ├── index.html
    └── calories_form_page.html
```

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python main.py
```
Flask will start on **http://127.0.0.1:5000** in debug mode.

### 3. Use it
1. Open the home page → click through to `/calories_form`
2. Fill in:
   - **Weight** (kg) — default 80
   - **Height** (cm) — default 180
   - **Age** — default 28
   - **Country** — default `Italy`
   - **City** — default `Firenze`
3. Submit → see your estimated daily calories

## 🧩 Core Classes

### `Calories` (`calorie.py`)
```python
Calories(weight=80, height=180, age=28, temperature=15).calculate()
# → 10*80 + 6.5*180 + 5 - 10*15  =  800 + 1170 + 5 - 150  =  1825
```

### `Temperature` (`temperature.py`)
Wraps `selectorlib` to extract the temperature value from a weather page using rules defined in `temperature.yaml`. Constructed as:
```python
Temperature(country='Italy', city='Firenze').get()
```

### Flask views (`main.py`)
- `HomePage` — `GET /`
- `CaloriesFormPage` — `GET /calories_form` (renders the form), `POST /calories_form` (renders the form + result)

## 📦 Key Dependencies

```
Flask==1.1.2
WTForms==2.3.3
selectorlib==0.16.0
PyYAML==5.3.1
requests==2.25.1
```

## 💡 Possible Extensions

- Switch the scraper to a real weather API (OpenWeatherMap)
- Use a clinically validated formula (Mifflin-St Jeor, Harris-Benedict)
- Account for **activity level** and **sex**
- Persist results per user (login + history chart)
- Containerize with Docker and deploy to Heroku / Render / Fly.io

## 👤 Author

**Denis Vreshtazi** — [GitHub](https://github.com/denisvreshtazi)
