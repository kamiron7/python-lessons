
## 🚀 Запуск тестов


### 1. Запуск тестов с формированием отчета

Чтобы собрать отчет Allure, выполните команду:

```bash
pytest --alluredir=allure-results 
```
Если возникли ошибки, попробуйте очистить старые результаты:

```bash

rm -rf allure-results/
pytest --alluredir=allure-results
```
----------

## 📊 Просмотр отчета Allure

### 1. Автоматический запуск сервера отчета

Выполните команду:

```bash
allure serve allure-results
```
Эта команда запустит локальный сервер и откроет отчет в браузере.

### 2. Генерация отчета вручную

Если команда `allure serve` не работает, попробуйте сгенерировать отчет:

```bash
allure generate allure-results --clean -o allure-report
```
Затем откройте отчет:

```bash
allure open allure-report
```