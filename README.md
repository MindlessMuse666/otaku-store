# Otaku Store 🛒

[![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Современный MVP интернет-магазин аниме-мерча на Django + Tailwind CSS.

![Otaku Store](https://github.com/user-attachments/assets/9224822b-5b07-4ebe-95e9-d34f773eef92)

## 🚀 Features

- Каталог товаров с фильтрацией по категориям (футболки, кружки, постеры)
- Детальные страницы товаров
- Корзина и оформление заказа
- Регистрация, авторизация, сброс пароля
- Современный адаптивный интерфейс (Tailwind CSS)
- Sticky header и удобная навигация
- Загрузка и отображение изображений товаров
- Docker и PostgreSQL для продакшн-развёртывания

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

## 🐳 Docker

Для запуска в Docker:
```bash
docker-compose up --build
```

## 🛠️ Технологии

- Python 3.10+
- Django 5+
- Tailwind CSS (CDN)
- PostgreSQL
- Docker

## 📸 Скриншоты

### Главная страница
![Главная страница](https://github.com/user-attachments/assets/9224822b-5b07-4ebe-95e9-d34f773eef92)
*Удобный и аккуратный интерфейс главной страницы*

### Список категорий товаров
![Категории товаров](https://github.com/user-attachments/assets/348dcbcd-b3af-433b-8c00-47cecf401fd2)
*Страница со списком категорий товаров магазина, включая фильтрацию по категориям*

### Страница логина
![Логин](https://github.com/user-attachments/assets/703608fa-086c-4c04-b010-09042a7610d5)
*Страница входа в систему*

### Страница регистрации
![Регистрация](https://github.com/user-attachments/assets/7f753b64-bbff-4b44-aea2-d0bba9005163)
*Страница регистрации нового пользователя*

### Страница сброса пароля
![Сброс пароля](https://github.com/user-attachments/assets/7cc18bc8-cccd-455e-8cb6-56fb123a17b7)
*Страница сброса пароля пользователя*

## 🤝 Вклад в проект

Pull requests и предложения приветствуются!  
Для крупных изменений, пожалуйста, сначала откройте issue для обсуждения.

## 📄 Лицензия

Этот проект распространяется под лицензией MIT.  
См. файл [LICENSE](LICENSE) для подробностей.

## 📬 Контакты

- Автор: [MindlessMuse666](https://github.com/MindlessMuse666)
- Telegram: [@mindless_muse](t.me/mindless_muse)
- Email: mindlessmuse.666@gmail.com

---

> Проект создан в учебных целях для демонстрации архитектуры интернет-магазина на Django.
