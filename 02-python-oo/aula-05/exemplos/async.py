import aiohttp
import asyncio


async def request(url, verbose=False):
    with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)

            if verbose:
                print(await response.text())


if __name__ == '__main__':
    import sys
    verbose = '-v' in sys.argv

    loop = asyncio.get_event_loop()
    requests = [asyncio.ensure_future(request('http://httpbin.org/get', verbose))
                for _ in range(25)]
    loop.run_until_complete(asyncio.wait(requests))
    loop.close()
