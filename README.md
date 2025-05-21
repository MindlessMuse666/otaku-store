# Otaku Store 🛒

[![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Современный MVP интернет-магазин аниме-мерча на Django + Tailwind CSS.

![Otaku Store Screenshot](media/readme_screenshot.png)

---

## 🚀 Features

- Каталог товаров с фильтрацией по категориям (футболки, кружки, постеры)
- Детальные страницы товаров
- Корзина и оформление заказа
- Регистрация, авторизация, сброс пароля
- Современный адаптивный интерфейс (Tailwind CSS)
- Sticky header и удобная навигация
- Загрузка и отображение изображений товаров
- Docker и PostgreSQL для продакшн-развёртывания

---

## 🖥️ Demo

> _Скриншоты и демо появятся после деплоя проекта._

---

## ⚡ Быстрый старт

```bash
git clone https://github.com/MindlessMuse666/otaku-store.git
cd otaku-store
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Откройте [http://127.0.0.1:8000/](http://127.0.0.1:8000/) в браузере.

---

## 🐳 Docker

Для запуска в Docker:
```bash
docker-compose up --build
```

---

## 🛠️ Технологии

- Python 3.10+
- Django 5+
- Tailwind CSS (CDN)
- PostgreSQL
- Docker

---

## 🤝 Contributing

Pull requests и предложения приветствуются!  
Для крупных изменений, пожалуйста, сначала откройте issue для обсуждения.

---

## 📄 License

Этот проект распространяется под лицензией MIT.  
См. файл [LICENSE](LICENSE) для подробностей.

---

## 📬 Контакты

- Автор: [MindlessMuse666](https://github.com/MindlessMuse666)
- Telegram: [@mindless_muse](t.me/mindless_muse)
- Email: mindlessmuse.666@gmail.com

---

> Проект создан в учебных целях для демонстрации архитектуры интернет-магазина на Django.