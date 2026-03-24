from unittest.mock import Mock


class MockBegin:
    async def __aenter__(self):
        return None

    async def __aexit__(self, exc_type, exc, tb):
        pass


class MockSession:
    def __init__(self):
        self.add = Mock()

    def begin(self):
        return MockBegin()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass
