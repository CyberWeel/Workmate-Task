# Отчёты по метрике YouTube
Простое CLI-приложение для анализа CSV-файлов с данными по YouTube-видео.

## Возможности
- Поддержка нескольких файлов
- Расширяемая система отчётов
- Текущий отчёт (единственный):
  - clickbait (CTR > 15 и retention < 40)

## Пример запуска
```bash
python -m app.main --files uploads/stats1.csv uploads/stats2.csv --report clickbait
```

[Скриншот](https://github.com/CyberWeel/Workmate-Task/blob/master/example.png)
[Пример запуска тестов](https://github.com/CyberWeel/Workmate-Task/blob/master/tests.png)