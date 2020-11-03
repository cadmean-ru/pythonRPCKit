from aiohttp import ClientSession
from aiohttp import ClientError

from rpckit.exceptions import RpcException
from rpckit.constants import RpcErrorCode
from rpckit.constants import SUPPORTED_RPC_VERSION


class HttpTransport:

    async def send(self, url, data, content_type):
        try:
            async with ClientSession() as session:
                headers = {
                    "Content-Type": content_type,
                    "Cadmean-RPC-Version": SUPPORTED_RPC_VERSION
                }
                async with session.post(url, data=data, headers=headers, timeout=10) as resp:
                    if resp.status != 200:
                        raise RpcException(RpcErrorCode.UnsuccessfulStatusCode,
                                           f"Server failed to respond with a success status code. "
                                           f"Actual status code: {resp.status}")
                    return await resp.read()
        except ClientError:
            raise RpcException(RpcErrorCode.FailedToSendCall, "Connection problem occurred")
