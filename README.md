# פרויקט בדיקות אוטומציה - Sauce Demo

## תיאור כללי

פרויקט זה הוא מסגרת בדיקות אוטומציה מקיפה המיועדת לבדיקת אתר הדמו [Sauce Demo](https://www.saucedemo.com/). הפרויקט כולל בדיקות UI (ממשק משתמש) ומוכן להרחבה עם בדיקות API, תוך שימוש בטכנולוגיות מתקדמות כמו Playwright ו-Pytest.

## 🚀 תכונות עיקריות

- ✅ **בדיקות UI אוטומטיות** - בדיקת ממשק המשתמש באמצעות Playwright
- 🏗️ **Page Object Model (POM)** - ארכיטקטורה נקייה וניתנת לתחזוקה
- 📊 **דיווחי Allure** - דיווחים מפורטים ויפים
- 🎥 **הקלטות וצילומי מסך** - תיעוד אוטומטי של בדיקות כושלות
- 🔧 **תצורה גמישה** - הגדרות מותאמות אישית עם pytest.ini
- 🌐 **תמיכה מרובת דפדפנים** - Chrome, Firefox, Safari

## 🛠️ התקנה והגדרה

### דרישות מקדימות

- Python 3.8+
- Git

### שלבי התקנה

1. **שכפול הפרויקט**
   ```bash
   git clone <repository-url>
   cd final-winnerit-project-jun-25
   ```

2. **יצירת סביבה וירטואלית (מומלץ)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **התקנת התלויות**
   ```bash
   pip install -r requirements.txt
   ```

4. **התקנת דפדפני Playwright**
   ```bash
   playwright install
   ```

## 📁 מבנה הפרויקט

```
final-winnerit-project-jun-25/
├── 📂 pages/                      # Page Object Model - דפי האובייקטים
│   ├── __init__.py
│   ├── login_page.py              # דף הלוגין
│   └── items_page.py              # דף הפריטים (בפיתוח)
├── 📂 tests/                      # תיקיית הבדיקות
│   ├── __init__.py
│   ├── conftest.py                # הגדרות והכנות לבדיקות
│   ├── 📂 ui/                     # בדיקות ממשק משתמש
│   │   ├── __init__.py
│   │   ├── test_login_negative.py  # בדיקות לוגין שליליות
│   │   └── test_e2e_buy_items.py  # בדיקת קנייה אנד-טו-אנד
│   └── 📂 api/                    # בדיקות API (מוכן להרחבה)
│       └── __init__.py
├── 📂 api_requests/               # בקשות API (מוכן להרחבה)
│   └── __init__.py
├── 📂 allure-results/             # תוצאות דיווחי Allure
├── 📂 test-results/               # הקלטות ווידאו וצילומי מסך
├── pytest.ini                    # הגדרות Pytest
├── requirements.txt               # רשימת התלויות
└── README.md                      # המדריך הזה
```

## 🧪 הרצת בדיקות

### הרצת כל הבדיקות
```bash
pytest
```

### הרצת בדיקות UI בלבד
```bash
pytest tests/ui/
```

### הרצת בדיקה ספציפית
```bash
pytest tests/ui/test_login_negative.py::test_example_1 -v
```

### הרצה עם פרמטרים נוספים
```bash
# הרצה עם דפדפן ספציפי
pytest --browser firefox

# הרצה במצב headless
pytest --headed=false

# הרצה עם מהירות רגילה (ללא האטה)
pytest --slowmo 0
```

## 📊 דיווחים

### יצירת דיווח Allure
```bash
# יצירת דיווח (אחרי הרצת בדיקות)
allure serve allure-results
```

הדיווח ייפתח אוטומטיות בדפדפן ויכלול:
- ✅ סטטוס בדיקות
- 📸 צילומי מסך של שגיאות
- 🎥 הקלטות וידאו
- 📈 גרפים וסטטיסטיקות
- 📋 לוגים מפורטים

## 🎯 בדיקות קיימות

### בדיקות UI

#### `test_login_negative.py`
- **test_example_1**: בדיקת התחברות עם משתמש חסום
- **test_example_2**: בדיקת התחברות עם נתונים שגויים

#### `test_e2e_buy_items.py`
- **test_example**: בדיקת תהליך קנייה מלא מהתחברות ועד לסיום ההזמנה

### מאפייני הבדיקות
- 🔐 **בדיקות אבטחה** - התחברות עם משתמשים שונים
- 🛒 **בדיקות עסקיות** - תהליך קנייה מלא
- ❌ **בדיקות שליליות** - טיפול בשגיאות
- 📱 **בדיקות רספונסיביות** - תמיכה במכשירים שונים

## 🏗️ ארכיטקטורה

### Page Object Model (POM)

הפרויקט משתמש בדפוס Page Object Model לארגון הקוד:

#### `LoginPage` (pages/login_page.py)
```python
class LoginPage:
    # Locators - מאתרי אלמנטים
    # Methods - פעולות בדף
    # Assertions - בדיקות ציפייה
```

**פונקציות עיקריות:**
- `navigate()` - ניווט לדף
- `type_username()` - הקלדת שם משתמש
- `fill_password()` - מילוי סיסמה
- `click_login_button()` - לחיצה על כפתור התחברות
- `expect_error_message()` - בדיקת הודעת שגיאה

### הגדרות Pytest

קובץ `pytest.ini` כולל הגדרות מתקדמות:
```ini
[pytest]
addopts = -v --browser-channel chrome --screenshot on --full-page-screenshot --slowmo 500 --video on --tracing retain-on-failure --alluredir allure-results
```

**הסבר הפרמטרים:**
- `--browser-channel chrome` - שימוש בכרום
- `--screenshot on` - צילום מסך אוטומטי
- `--slowmo 500` - האטה של 500ms בין פעולות
- `--video on` - הקלטת וידאו
- `--tracing retain-on-failure` - שמירת מעקב בכשלונות
- `--alluredir` - תיקיית דיווחי Allure

## 🔧 התלויות העיקריות

| ספרייה | גרסה | תיאור |
|--------|------|--------|
| **playwright** | 1.53.0 | מנוע האוטומציה הראשי |
| **pytest** | 8.4.1 | מסגרת הבדיקות |
| **allure-pytest** | 2.14.3 | דיווחים מתקדמים |
| **pytest-playwright** | 0.7.0 | אינטגרציה Pytest-Playwright |
| **requests** | 2.32.4 | בקשות HTTP (לעתיד) |
| **Faker** | 37.4.0 | יצירת נתונים מזויפים |

## 🚧 תכניות להרחבה

### בדיקות API
- תיקיות `api_requests/` ו-`tests/api/` מוכנות להרחבה
- אינטגרציה עם ספריית `requests`
- בדיקות CRUD מלאות

### דפי אובייקטים נוספים
- `ItemsPage` - דף המוצרים
- `CartPage` - דף העגלה
- `CheckoutPage` - דף התשלום

### תכונות נוספות
- 🐳 **Docker** - הרצה בקונטיינרים
- 🔄 **CI/CD** - אינטגרציה רציפה
- 🌍 **Parallel Testing** - בדיקות מקבילות
- 📱 **Mobile Testing** - בדיקות מובייל

## 🤝 תרומה לפרויקט

### הוספת בדיקה חדשה
1. צור קובץ בדיקה ב-`tests/ui/` או `tests/api/`
2. ייבא את הדפים הנדרשים מ-`pages/`
3. השתמש ב-fixtures מ-`conftest.py`
4. הוסף דקורטורים של Allure לתיעוד

### הוספת דף אובייקטים חדש
1. צור קובץ חדש ב-`pages/`
2. הגדר locators עם תיאורים
3. ייצא methods לפעולות
4. הוסף assertions עם Allure steps

## 📞 תמיכה

לשאלות או בעיות:
- 📖 עיין בדוקומנטציה של [Playwright](https://playwright.dev/python/)
- 🔍 בדוק את [Pytest Docs](https://docs.pytest.org/)
- 📊 למד על [Allure Reports](https://docs.qameta.io/allure/)

---

**בהצלחה עם הבדיקות! 🎯**
