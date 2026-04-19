from dataclasses import dataclass


@dataclass
class VideoMetric:
  title: str
  ctr: float
  retention_rate: float
  views: int
  likes: int
  avg_watch_time: float