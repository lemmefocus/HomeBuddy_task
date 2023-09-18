# Техническое тестовое задание для HomeBuddy

## Описание

Develop several (at least 3) UI autotests for https://hb-autotests.stage.sirenltd.dev/hvac

### Use scenario:

* zip code 10001
* answer the questions on the form
* enter the first and last name
* enter an email
* enter the phone number
* (if necessary) confirm the phone number
* get a "thank you" page.
Feel free to choose the checks yourself.
Use "py test" + "selenium"

Please note that your solution must be in Pull Request (PR) format. 

## Пример запуска:
```
pytest .\tests\test_hvac_estimation_navigate_to_other_services.py
```
