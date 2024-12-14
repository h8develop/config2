# Dependency Visualizer

## Описание проекта
Этот проект предназначен для анализа зависимостей Python-пакетов и их визуализации с использованием PlantUML. Основная цель — упростить анализ и представление транзитивных связей между библиотеками в проекте. Включает функции для определения зависимостей, генерации графов и юнит-тестов.

## Структура репозитория

### Файлы
- **`requirements.txt`**: Содержит список зависимостей для установки.
- **`tests/test_visualizer.py`**: Тесты для проверки работы функций анализа зависимостей.
- **`visualizer.py`**: Основной скрипт, реализующий анализ и генерацию графов зависимостей.

---

## Основной функционал

1. **`get_dependencies(package_name)`**:
   - Рекурсивно определяет зависимости указанного пакета.
   - Возвращает словарь, где ключ — имя пакета, значение — список зависимостей.

2. **`generate_plantuml(dependencies)`**:
   - Преобразует зависимости в код для PlantUML.
   - Создаёт граф с узлами (пакетами) и их связями (зависимостями).

3. **CLI-команды**:
   - Запуск через командную строку:
     ```bash
     python visualizer.py path_to_program package_name output_file repository_url
     ```
   - Аргументы:
     - `path_to_program` — путь к программе.
     - `package_name` — имя анализируемого пакета.
     - `output_file` — файл для сохранения PlantUML-кода.
     - `repository_url` — URL репозитория.

---

## Установка

1. Убедитесь, что установлен Python 3.9+.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

---

## Использование

### Анализ зависимостей пакета

Пример вызова команды для анализа пакета `requests`:
```bash
python visualizer.py . requests output.puml https://github.com/psf/requests
```
- Результат (`output.puml`) можно загрузить на [PlantUML](https://plantuml.com/) для визуализации.

---

## Пример файла PlantUML

Для пакета `requests` сгенерированный граф может выглядеть так:
```plaintext
@startuml
requests --> certifi
requests --> urllib3
requests --> idna
requests --> charset-normalizer
@enduml
```

---

## Тестирование

Запустите тесты с помощью команды:
```bash
python -m unittest discover -s tests -p "*.py"
```

Пример теста из `tests/test_visualizer.py`:
```python
class TestDependencyVisualizer(unittest.TestCase):
    def test_get_dependencies(self):
        dependencies = get_dependencies('requests')
        self.assertIn('urllib3', dependencies['requests'])
```

---

## Примечания

- **Ограничения**:
  - Используется `pkg_resources`, который устарел, для анализа зависимостей. Возможно обновление на `importlib.metadata`.
  - Зависимости корректно анализируются только для установленных пакетов.

- **Возможные улучшения**:
  - Добавить поддержку необработанных ошибок.
  - Реализовать поддержку неустановленных пакетов через PyPI API.

--- 

## Автор

Создан для демонстрации анализа зависимостей Python-пакетов. Для вопросов и предложений обратитесь через репозиторий GitHub.