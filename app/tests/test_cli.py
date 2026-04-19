import subprocess


def test_main_runs():
  result = subprocess.run(
    ["python", "-m", "app.main", "--files", "uploads/stats1.csv", "--report", "clickbait"],
    capture_output = True,
    text = True,
    encoding = "utf-8",
    errors = "replace",
  )

  assert result.returncode == 0
  assert "title" in result.stdout