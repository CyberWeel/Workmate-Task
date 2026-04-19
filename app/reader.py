import csv
from pathlib import Path

from app.models import VideoMetric
from app.exceptions import FileProcessingError


def read_csv_files(file_paths: list[str]) -> list[VideoMetric]:
  result: list[VideoMetric] = []

  for file_path in file_paths:
    path = Path(file_path)

    if not path.exists():
      raise FileProcessingError(f"Файл не существует: {file_path}")

    with path.open(encoding = "utf-8") as f:
      reader = csv.DictReader(f)

      for row in reader:
        result.append(
          VideoMetric(
            title = row["title"],
            ctr = float(row["ctr"]),
            retention_rate = float(row["retention_rate"]),
            views = int(row["views"]),
            likes = int(row["likes"]),
            avg_watch_time = float(row["avg_watch_time"]),
          )
        )

  return result