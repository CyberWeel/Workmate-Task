from app.reader import read_csv_files


def test_read_csv_files():
  data = read_csv_files(["uploads/stats1.csv"])

  assert len(data) > 0
  assert data[0].title is not None