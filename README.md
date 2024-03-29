# cadRPC client library for Python

cadRPC is an easy-to-use RPC technology. It's goal is to simplify the communication with your web API, hiding all the HTTP and JSON poppycock.

## Installation

Install the ```cadmean-rpckit``` package:

```pip install cadmean-rpckit```

## How to use

An example is worth a thousand words. 
Note, you can run the examples yourself, as 
they call functions of the 
[example server](https://github.com/cadmean-ru/ExampleRpcServer) 
at testrpc.cadmean.ru.

The easiest way to call an RPC function is using a decorator.

Synchronous example:

```python
from rpckit.decorators import RpcFunction

# You need to set this url only once in your program
RpcFunction.default_server_url = "http://testrpc.cadmean.ru"

@RpcFunction("sum")
def rpc_sum(a, b):
    print(f"Calling rpc function that calculates {a}+{b}")

print(rpc_sum(5, 64))
```

Async/await example:

```python
import asyncio
from rpckit.decorators import RpcFunction

# You need to set this url only once in your program
RpcFunction.default_server_url = "http://testrpc.cadmean.ru"

@RpcFunction("sum", async_call=True)
def rpc_sum(a, b):
    print(f"Calling rpc function that calculates {a}+{b}")

async def main():
    print(await rpc_sum(5, 64))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

So, all you need to do to call an RPC function from python, 
is to define a regular function with parameters, 
that will match the ones of the remote function 
and than decorate it with ```@RpcFunction```, that takes 
remote function name as parameter.

You can add ```async_call=True``` to the decorator, than 
function call will be asynchronous, and you 
will be able to use your function with ```async/await```.

In the above examples we are calling the "sum" function at testrpc.cadmean.ru, 
that takes two integers and returns an integer.

## Error handling

cadRPC function may return an error code instead of a result. 
In this case this library rises ```FunctionException```.
It can be a system error or user defined error, 
that you return from RPC function in your server.
You would probably want to handle these errors in your program:

```python
from rpckit.decorators import RpcFunction
from rpckit.exceptions import FunctionException
from rpckit.constants import RpcErrorCode

RpcFunction.default_server_url = "http://testrpc.cadmean.ru"

@RpcFunction("notExistingFunction")
def not_existing_function():
    pass

try:
    not_existing_function()
except FunctionException as ex:
    print(ex)
    if ex.code == RpcErrorCode.FunctionNotFound:
        print("Ok. We expected that.")
    else:
        print("Something bad happened.")
```

## Authorization

adRPC simplifies authorization process in your web API. 
You just call a function on your RPC server, 
that will authenticate the user and return a JWT authorization 
ticket(access and refresh token). 
The client will store this ticket for you and will authorize 
further calls with the access token. 
Note, that you need to setup authorization on your server 
(see [this readme](https://github.com/cadmean-ru/csharpRPCKit/tree/master/Cadmean.RPC.ASP)).

Here is an example:

```python
from rpckit.decorators import RpcFunction

RpcFunction.default_server_url = "http://testrpc.cadmean.ru"

@RpcFunction("auth")
def auth(email, password):
    pass

@RpcFunction("user.get")
def get_user():
    pass

auth("email@example.com", "password") # Call the authentication function, that returns the JWT tokens
user = get_user() # Call the function that requires authorization after obtaining JWT tokens

print(user)
```

## Contributing

Feel free to submit issues or create pull requests following fork-and-pull git workflow.

## See also

* [C# client and server library](https://github.com/cadmean-ru/csharpRPCKit)
* [Android client library](https://github.com/cadmean-ru/androidRPCKit)
* [Example server](https://github.com/cadmean-ru/ExampleRpcServer)
* [Dart client library](https://github.com/cadmean-ru/cadmean_rpc_dart)
