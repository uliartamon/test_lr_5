# Selenium Smoke Testing

## Описание проекта

Проект представляет собой автоматизированное дымовое тестирование веб-сервиса с использованием Selenium WebDriver и Python.

В качестве тестируемого сервиса используется страница:

https://demoqa.com/text-box

Автоматизированный тест проверяет базовую работоспособность веб-формы и выполняет основные пользовательские действия.

---

## Используемые технологии

- Python 3.12
- Selenium WebDriver
- Pytest
- ChromeDriver
- webdriver-manager

---

## Реализованный функционал

Автотест выполняет:

- открытие веб-страницы;
- заполнение полей ввода;
- поиск элементов по локаторам;
- автоматический скролл страницы;
- нажатие кнопки Submit;
- проверку отображения результата;
- создание скриншотов до и после отправки формы.

---

## Структура проекта

```text
selenium_smoke_test/
│
├── screenshots/
│   ├── before_submit.png
│   └── after_submit.png
│
├── tests/
│   └── test_demoqa_textbox.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Установка проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/selenium-smoke-test.git
cd selenium-smoke-test
```

---

### 2. Создание виртуального окружения

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Запуск тестов

```bash
pytest tests/test_demoqa_textbox.py -v
```

---

## Тестируемый сценарий

В ходе smoke-тестирования проверяется следующий пользовательский сценарий:

1. Открытие страницы DemoQA.
2. Заполнение формы:
   - Full Name
   - Email
   - Current Address
   - Permanent Address
3. Скролл страницы до кнопки Submit.
4. Создание скриншота заполненной формы.
5. Нажатие кнопки Submit.
6. Проверка отображения результата.
7. Создание итогового скриншота.

---

## Используемые локаторы

| Элемент | Локатор |
|---|---|
| Full Name | By.ID("userName") |
| Email | By.ID("userEmail") |
| Current Address | By.ID("currentAddress") |
| Permanent Address | By.ID("permanentAddress") |
| Submit | By.ID("submit") |
| Output | By.ID("output") |

---

## Скриншоты

После выполнения теста автоматически создаются:

- `before_submit.png`
- `after_submit.png`

Скриншоты сохраняются в папке:

```text
screenshots/
```

---

## Тип тестирования

Данный проект реализует:

- автоматизированное тестирование;
- UI testing;
- smoke testing веб-приложения.

---

## Автор

Ульяна
