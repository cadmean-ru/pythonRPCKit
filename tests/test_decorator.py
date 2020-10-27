from aiounittest import AsyncTestCase

from rpckit.decorators import rpc_function
from rpckit.decorators import RpcFunction


@rpc_function("http://localhost:5000", "test.addInt")
def add_int(a, b):
    print(f"Calling rpc function that adds {a}+{b}")


@RpcFunction("http://localhost:5000", "test.concatString")
def concat(s1, s2):
    print(f"Calling rpc function that concats {s1}+{s2}")


@RpcFunction("http://localhost:5000", "test.squareDouble")
def square(d):
    print(f"Calling rpc function that squares {d}")


class DecoratorsTestCase(AsyncTestCase):

    async def test_add_int_with_decorator(self):
        expected = 42
        a = b = 21
        actual = await add_int(a, b)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_concat_with_decorator_class(self):
        expected = "Hello, Cadmean!"
        s1 = "Hello,"
        s2 = " Cadmean!"
        actual = await concat(s1, s2)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_square_with_decorator_class(self):
        expected = 0.09
        a = 0.3
        actual = await square(a)
        print(actual)
        self.assertEqual(expected, actual)
