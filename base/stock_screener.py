from utils import get_headers_from_investing_screener


class Screener():
    def __init__(self) -> None:
        self._base_url = ""
        self._headers = get_headers_from_investing_screener()
        self._params = dict()

    def filter(self):
        pass