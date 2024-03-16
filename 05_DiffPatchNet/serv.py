import asyncio
import cowsay

COMMANDS = ['who', 'cows', 'login', 'say', 'yield', 'quit']

clients = {}
nicknames = {}

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me)
    clients[me] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                msng = q.result().decode().strip() + ' '
                if msng.split()[0] not in COMMANDS:
                    await clients[me].put("SERVER: UNKNOWN COMMAND")
                    continue
                if me not in nicknames.keys():
                    if msng.split()[0] not in ['login', 'cows']:
                        await clients[me].put("SERVER: LOGIN FIRSTLY")
                    elif msng.split()[0] == 'login':
                        if msng[msng.index(' ') + 1:-1] not in nicknames.values():
                            if ' ' not in msng[msng.index(' ') + 1:-1]:
                                nicknames[me] = msng[msng.index(' ') + 1:-1]
                                await clients[me].put("SERVER: LOGIN SUCCESSFULLY")
                                print(f'{me} logged in as {nicknames[me]}')
                            else:
                                await clients[me].put("SERVER: LOGIN ERROR, NICKNAME SHOULDN'T CONTAIN SPACE")
                        else:
                            await clients[me].put("SERVER: NICKNAME ALREADY USED")
                    else:
                        if nicknames == {}:
                            await clients[me].put(f"SERVER: ANY")
                        else:
                            await clients[me].put(f"SERVER: ANY EXCEPT {', '.join(list(nicknames.values()))}")
                else:
                    match msng.split()[0]:
                        case "who":
                            await clients[me].put(f"SERVER: {', '.join(list(nicknames.values()))}")
                        case "cows":
                            if nicknames == {}:
                                await clients[me].put(f"SERVER: ANY")
                            else:
                                await clients[me].put(f"SERVER: ANY EXCEPT {', '.join(list(nicknames.values()))}")
                        case "login":
                            await clients[me].put("ALREADY LOGGED IN")
                        case "say":
                            if len(msng.split()) > 2:
                                if msng.split()[1] in nicknames.values():
                                    await clients[list(nicknames.keys())[list(nicknames.values()).index(msng.split()[1])]].put(cowsay.cowsay(f"{nicknames[me]} -> {msng.split()[1]} : {' '.join(msng.split()[2:])}"))
                                else:
                                    await clients[me].put("SERVER: RECEPIENT IS NOT ONLINE")
                            else:
                                await clients[me].put("SERVER: CHOOSE RECEPIENT")
                        case "yield":
                            for out in clients.values():
                                if out is not clients[me]:
                                    await out.put(cowsay.cowsay(f"{nicknames[me]} -> *ALL* : {' '.join(msng.split()[1:])}"))
                        case "quit":
                            del nicknames[me]
                            print(f'{me} logged out')
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
