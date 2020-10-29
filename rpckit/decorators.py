from rpckit.rpc import RpcClient
from rpckit.exceptions import RpcException


class RpcFunction:

    default_server_url = None

    _rpc_cache = {}

    def __init__(self, function_name, server_url=None):
        self.server_url = server_url
        self.function_name = function_name

    def __call__(self, fn):
        async def wrapper(*args, **kwargs):
            u = self._get_url()
            rpc = RpcFunction._get_rpc(u)
            fn(*args, **kwargs)
            return await rpc.f(self.function_name).call(*args)
        return wrapper

    def _get_url(self):
        if self.server_url is not None:
            return self.server_url

        if RpcFunction.default_server_url is not None:
            return RpcFunction.default_server_url

        raise RpcException(7, "No server url specified")

    @staticmethod
    def _get_rpc(server_url):
        if server_url in RpcFunction._rpc_cache:
            return RpcFunction._rpc_cache[server_url]
        else:
            rpc = RpcClient(server_url)
            RpcFunction._rpc_cache[server_url] = rpc
            return rpc

    @staticmethod
    def clear_cache():
        RpcFunction._rpc_cache = {}


def rpc_function(server_url, function_name):
    def decorator(fn):
        async def wrapper(*args, **kwargs):
            rpc = RpcClient(server_url)
            fn(*args, **kwargs)
            return await rpc.f(function_name).call(*args)
        return wrapper
    return decorator
