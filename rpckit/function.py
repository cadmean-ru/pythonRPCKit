from rpckit.exceptions import FunctionException


class FunctionCall:
    def __init__(self, *args, auth=""):
        self.args = args
        self.auth = auth


class FunctionOutput:
    def __init__(self, *, error, result, metaData):
        self.result = result
        self.error = error
        self.meta_data = metaData


class Function:

    def __init__(self, name, rpc):
        self.name = name
        self.rpc = rpc

    async def call(self, *args):
        c = FunctionCall(*args)
        data = self.rpc.config.codec.encode(c.__dict__)
        url = self.rpc.config.url_provider(self)
        ct = self.rpc.config.codec.content_type
        r = await self.rpc.config.transport.send(f"{self.rpc.server_url}/{url}", data, ct)
        output = FunctionOutput(**self.rpc.config.codec.decode(r))
        if output.error != 0:
            raise FunctionException(output.error)
        return output.result
