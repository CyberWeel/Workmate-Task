from app.reports.base import BaseReport


class ClickbaitReport(BaseReport):
  name = "clickbait"

  def generate(self, data):
    filtered_metrics = [
      metric for metric in data
      if metric.ctr > 15 and metric.retention_rate < 40
    ]

    sorted_data = sorted(filtered_metrics, key = lambda x: x.ctr, reverse = True)

    return [
      {
        "title": metric.title,
        "ctr": metric.ctr,
        "retention_rate": metric.retention_rate,
      }
      for metric in sorted_data
    ]