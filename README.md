# Отчёты по метрике YouTube
Простое CLI-приложение для анализа CSV-файлов с данными по YouTube-видео.

## Возможности
- Поддержка нескольких файлов
- Расширяемая система отчётов
- Текущий отчёт (единственный):
  - clickbait (CTR > 15 и retention < 40)

## Пример запуска
```bash
python -m app.main --files stats1.csv stats2.csv --report clickbait