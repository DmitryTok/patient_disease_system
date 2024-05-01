# Система обліку хвороб

### Встановити віртуальне оточення
Windows
```bash
python -m venv venv
```
Linux/MacOS
```bash
python3 -m venv venv
```

### Активувати віртуальне оточення
Windows
```bash
source venv\Scripts\activate
```
Linux/MacOS
```bash
source venv/bin/activate
```

### Встановити необхідні бібліотеки та залежності
```bash
pip install -r requirements.txt
```

### Перейти в директорію де знаходиться 'manage.py' файл.
```
cd disease_system
```

### Створити структуру бази даних
```
python manage.py makemigrations
```

### Створити базу даних із необхідною структурою полів та колонок
```
python manage.py migrate
```

### Створити суперюзера
```
python manage.py createsuperuser
```

### Запустити тестовий сервер
```
python manage.py runserver
```