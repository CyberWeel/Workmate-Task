from app.reports.clickbait import ClickbaitReport
from app.models import VideoMetric


def test_clickbait_filtering():
  data = [
    VideoMetric("ok", 16, 30, 0, 0, 0),
    VideoMetric("bad_ctr", 10, 30, 0, 0, 0),
    VideoMetric("bad_retention", 20, 50, 0, 0, 0),
  ]

  report = ClickbaitReport()
  result = report.generate(data)

  assert len(result) == 1
  assert result[0]["title"] == "ok"