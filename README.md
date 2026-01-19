# Тест автоизации saucedemo

Автоматизированные тесты проверки авторизации на сайте https://www.saucedemo.com/

## Стэк
- Python 3.10
- Playwright
- Pytest
- Allure
- Page Object Model

## Тесты
1. Успешный логин (standard_user)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин с performance_glitch_user (учитываются задержки)

## Инструкции по установке и запуску

```bash
# Сборка образа
docker build -t saucedemo-tests .

# Запуск тестов
docker run --rm saucedemo-tests
