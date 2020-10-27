from rpckit.rpc import RpcClient


class RpcFunction:

    _rpc_cache = {}

    def __init__(self, server_url, function_name):
        self.server_url = server_url
        self.function_name = function_name

    def __call__(self, fn):
        async def wrapper(*args, **kwargs):
            rpc = RpcFunction._get_rpc(self.server_url)
            fn(*args, **kwargs)
            return await rpc.f(self.function_name).call(*args)
        return wrapper

    @staticmethod
    def _get_rpc(server_url):
        if server_url in RpcFunction._rpc_cache:
            return RpcFunction._rpc_cache[server_url]
        else:
            rpc = RpcClient(server_url)
            RpcFunction._rpc_cache[server_url] = rpc
            return rpc


def rpc_function(server_url, function_name):
    def decorator(fn):
        async def wrapper(*args, **kwargs):
            rpc = RpcClient(server_url)
            fn(*args, **kwargs)
            return await rpc.f(function_name).call(*args)
        return wrapper
    return decorator
