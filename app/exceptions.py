class AppError(Exception):
  pass


class FileProcessingError(AppError):
  pass


class UnknownReportError(AppError):
  pass