class Response:
    def __init__(
        self,
        data,
        error=False,
        success=True,
    ):
        self.success = success
        self.error = error
        self.data = data
