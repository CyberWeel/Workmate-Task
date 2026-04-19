from app.reports.clickbait import ClickbaitReport
from app.exceptions import UnknownReportError


REPORTS = {
  ClickbaitReport.name: ClickbaitReport,
}


def get_report(name: str):
  if name not in REPORTS:
    raise UnknownReportError(f"Неизвестный отчёт: {name}")

  return REPORTS[name]()