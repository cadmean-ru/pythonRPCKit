import aiohttp

from rpckit.exceptions import RpcException


class HttpTransport:

    async def send(self, url, data, content_type):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": content_type,
                "Cadmean-RPC-Version": "2"
            }
            async with session.post(url, data=data, headers=headers, timeout=10) as resp:
                if resp.status != 200:
                    raise RpcException(5, f"Server failed to respond with a success status code. "
                                          f"Actual status code: {resp.status}")
                return await resp.read()
