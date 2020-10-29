import dateutil.parser
from aiounittest import AsyncTestCase

from rpckit.decorators import rpc_function
from rpckit.decorators import RpcFunction


RpcFunction.default_server_url = "http://testrpc.cadmean.ru"


@rpc_function("http://testrpc.cadmean.ru", "sum")
def add_int(a, b):
    print(f"Calling rpc function that adds {a}+{b}")


@RpcFunction("concat")
def concat(s1, s2):
    print(f"Calling rpc function that concats {s1}+{s2}")


@RpcFunction("square")
def square(d):
    print(f"Calling rpc function that squares {d}")


@RpcFunction("getDate")
def get_date():
    pass


@RpcFunction("auth")
def auth(email, password):
    pass


@RpcFunction("user.get")
def get_user():
    pass


class DecoratorsTestCase(AsyncTestCase):

    def setUp(self):
        RpcFunction.default_server_url = "http://testrpc.cadmean.ru"

    async def test_call_sum_with_decorator(self):
        expected = 42
        a = b = 21
        actual = await add_int(a, b)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_call_concat_with_decorator_class(self):
        expected = "Hello, Cadmean!"
        s1 = "Hello,"
        s2 = " Cadmean!"
        actual = await concat(s1, s2)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_call_square_with_decorator_class(self):
        expected = 0.09
        a = 0.3
        actual = await square(a)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_call_get_date_with_decorator_class(self):
        actual = await get_date()
        d = dateutil.parser.parse(actual)
        print(d.strftime("%A, %d. %B %Y %I:%M%p"))

    async def test_call_authorized_function_with_decorator_class(self):
        actual = await auth("email@example.com", "password")
        print(actual)
        actual = await get_user()
        print(actual)
        self.assertIsNotNone(actual)
