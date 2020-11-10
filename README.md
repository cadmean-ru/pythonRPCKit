# cadRPC client library for Python

cadRPC is an easy-to-use RPC technology. It's goal is to simplify the communication with your web API, hiding all the HTTP and JSON poppycock.

## Installation

Install the ```cadrpc``` package:

```pip install cadrpc```

## How to use

An example is worth a thousand words. Note, you can run the examples yourself, as 
they call functions of the example server at testrpc.cadmean.ru.

The easiest way to call an RPC funcfion is using a decorator:

```python
import asyncio
from rpckit.decorators import RpcFunction

RpcFunction.default_server_url = "http://testrpc.cadmean.ru"  # You need to set this only once in your program


@RpcFunction("sum")
def rpc_sum(a, b):
    print(f"Calling rpc function that adds {a}+{b}") # or just pass


async def main():
    result = await rpc_sum(1, 68)
    print(result)


if __name__ == '__main__':
    # run asyncronous function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
