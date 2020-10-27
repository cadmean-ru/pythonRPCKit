class RpcException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class FunctionException(RpcException):

    def __init__(self, error):
        super.__init__(error, f"Function call finished with an error: {error}")
