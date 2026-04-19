from abc import ABC, abstractmethod

from app.models import VideoMetric


class BaseReport(ABC):
  name: str

  @abstractmethod
  def generate(self, data: list[VideoMetric]) -> list[dict]:
    pass