import asyncio

COMMANDS = ['who', 'cows', 'login', 'say', 'yeild', 'quit']

clients = {}
nicknames = {}

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    logged_in = False
    print(me)
    clients[me] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                msng = q.result().decode().strip()
                if msng.split()[0] not in COMMANDS:
                    await clients[me].put("SERVER: UNKNOWN COMMAND")
                    continue
                if not logged_in and msng.split()[0] not in ['login', 'cows']:
                    await clients[me].put("SERVER: LOGIN FIRSTLY")
                    continue
                else:
                    if msng[msng.index(' ') + 1:] not in nicknames.values():
                        nicknames[me] = msng[msng.index(' ') + 1:]
                        logged_in = True
                        await clients[me].put("SERVER: LOGIN SUCCESSFULLY")
                        continue
                    else:
                        await clients[me].put("SERVER: NICKNAME ALREADY USED")
                        continue
                for out in clients.values():
                    if out is not clients[me]:
                        await out.put(f"{me} {msng[msng.index(' ') + 1:]}")
            elif q is receive:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
