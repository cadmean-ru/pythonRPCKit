from rpckit.codec import JsonCodec
from rpckit.function import Function
from rpckit.transport import HttpTransport


def provide_function_url(f):
    return f"api/rpc/{f.name}"


class RpcConfig:

    def __init__(self, codec=JsonCodec(), transport=HttpTransport(), url_provider=provide_function_url):
        self.codec = codec
        self.transport = transport
        self.url_provider = url_provider


class RpcClient:

    def __init__(self, server_url, config=RpcConfig()):
        self.server_url = server_url
        self.config = config

    def f(self, name):
        return Function(name, self)
