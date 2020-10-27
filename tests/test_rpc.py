from aiounittest import AsyncTestCase

from rpckit.rpc import RpcClient


class TestRpcClient(AsyncTestCase):

    def setUp(self):
        self.rpc = RpcClient("http://localhost:5000")

    async def test_callAddInt(self):
        expected = 3
        result = await self.rpc.f("test.addInt").call(1, 2)
        print(result)
        self.assertEqual(expected, result)

    async def test_callSquareDouble(self):
        expected = 0.09
        actual = await self.rpc.f("test.squareDouble").call(0.3)
        print(actual)
        self.assertEqual(expected, actual)

    async def test_concatString(self):
        expected = "bruh"
        actual = await self.rpc.f("test.concatString").call("br", "uh")
        print(actual)
        self.assertEqual(expected, actual)
