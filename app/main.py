import argparse
import sys
from tabulate import tabulate

from app.reader import read_csv_files
from app.reports.registry import get_report
from app.exceptions import AppError


# Поддержка кириллицы
sys.stdout.reconfigure(encoding = "utf-8")


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--files", nargs = "+", required = True)
  parser.add_argument("--report", required = True)

  return parser.parse_args()


def main():
  args = parse_args()

  try:
    data = read_csv_files(args.files)
    report = get_report(args.report)

    result = report.generate(data)

    if not result:
      print("No data for report")
      return

    print(tabulate(result, headers="keys", tablefmt="grid"))

  except AppError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()