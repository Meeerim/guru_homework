
- Аргументы запуска. Собираем фикстуры, марки, и другую полезную информацию для отладки
  - --co
  - -k
  - -m
  - --markers
  - --fixtures
  - --durations=10
  - -v
  - -l (--showlocals)
  - --setup-plan

- Марки. Пропускаем тесты правильно
  - skip
  - xfail
  - usefixtures

- Параметризация. На тесте, на фикстуре. Переопределение параметров
  - pytest.mark.parametrize на тесте. Использование нескольких параметров
  - параметризация фикстуры. 
  - indirect параметризация

  
- ДЗ - github.com в мобильном и десктопном варианте. 
- Реализовать автотест для github.com, который заходит на страницу, ищет кнопку Sign In, и тыкает на нее (авторизоваться не нужно)
- Нужно параметризовать тест различным размером окна браузера.
- Обратите внимание, что тест на мобильную версию будет отличаться из-за изменения структуры локаторов.
- Сделайте три варианта пропуска неподходящих параметров и тестов
  1. Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
  2. Переопределите параметр с помощью indirect
  3. Сделайте разные фикстуры для каждого теста
В чем преимущества и недостатки каждого из подходов?
