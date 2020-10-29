import dateutil.parser
from aiounittest import AsyncTestCase

from rpckit.rpc import RpcClient


class TestRpcClient(AsyncTestCase):

    def setUp(self):
        self.rpc = RpcClient("http://testrpc.cadmean.ru")

    async def test_call_sum(self):
        expected = 3
        a = 1
        b = 2
        result = await self.rpc.f("sum").call(a, b)
        print(result)
        self.assertEqual(expected, result)

    async def test_call_square(self):
        expected = 0.09
        actual = await self.rpc.f("square").call(0.3)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_call_concat(self):
        expected = "Hello, world!"
        actual = await self.rpc.f("concat").call("Hello", ", ", "world!")
        print(actual)
        self.assertEqual(expected, actual)

    async def test_call_get_date(self):
        actual = await self.rpc.f("getDate").call()
        d = dateutil.parser.parse(actual)
        print(d.strftime("%A, %d. %B %Y %I:%M%p"))

    async def test_call_authorized_function(self):
        actual = await self.rpc.f("auth").call("email@example.com", "password")
        print(actual)
        self.assertIsNotNone(self.rpc.config.auth_ticket_holder.get_ticket())
        actual = await self.rpc.f("user.get").call()
        print(actual)
        self.assertIsNotNone(actual)
