#!/usr/bin/env python3

import abc
import asyncio
import inspect
import random
import re
import string
import sys


def check_class(cls, base):
    return (inspect.isclass(cls) and issubclass(cls, base) and
            not inspect.isabstract(cls))


def safecall(handler, *args):
    try:
        if handler:
            handler(*args)
    except Exception:
        pass


def str2bytes(s):
    return s.encode('utf-8', errors='replace')


def random_split(message):
    i = 0

    while i < len(message):
        n = random.randint(1, len(message) - i)
        yield message[i:i + n]
        i += n


class Generator:
    @staticmethod
    def word(min_length=8, max_length=32,
             abc=string.ascii_letters + string.digits):
        return ''.join(random.choice(abc)
                       for _ in range(random.randint(min_length, max_length)))

    @staticmethod
    def text(min_length=2048, max_length=8192):
        return [Generator.word()
                for _ in range(random.randint(min_length, max_length))]


class Graph:
    LINE_RE = re.compile(r'([^:]+):\s+"(.*?)"\s+(.*)')

    def __init__(self, filename):
        self._pages = {}
        def pgname(name):
            name = name.strip()
            return name if name != '*' else ''

        with open(filename) as f:
            for line in f:
                match = Graph.LINE_RE.match(line)
                if not match:
                    continue

                pagename, flag, next_pages = match.groups()

                page = Generator.text()
                if flag:
                    page.insert(random.randrange(len(page)), flag)

                for np in next_pages.split():
                    page.insert(random.randrange(len(page)),
                                '"{}"'.format(pgname(np)))

                page = ' '.join(page)
                self._pages[pgname(pagename)] = page


    def __getitem__(self, name):
        return self._pages.get(name, None)


class CommandBase(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def do(self, params, connection, graph):
        pass


class CommandHelp(CommandBase):
    MESSAGE = """Help
====

Available commands:
    help
    exit
    fetch <page>"""

    @property
    def name(self):
        return "help"

    def do(self, params, conn, graph):
        conn.send(self.MESSAGE)
        conn.close()


class CommandExit(CommandBase):
    @property
    def name(self):
        return "exit"

    def do(self, params, conn, graph):
        conn.close()


class CommandFetch(CommandBase):
    @staticmethod
    def make_packet(data):
        data = str2bytes(data)
        return b'\n'.join((str2bytes(str(len(data))), data))

    @property
    def name(self):
        return "fetch"

    def do(self, params, conn, graph):
        page = graph[params]
        if page is None:
            conn.send("Wrong page")
            conn.close()

        conn.READ_TIMEOUT = 60.0
        conn.send(self.make_packet(page))


class Connection:
    READ_TIMEOUT = 1.0

    def __init__(self, reader, writer):
        self._reader = reader
        self._writer = writer

    def send(self, msg):
        if isinstance(msg, bytes):
            for part in random_split(msg):
                self._writer.write(part)
        elif isinstance(msg, str):
            self.send(str2bytes(msg))
        else:
            self.send(str(msg))

    def at_eof(self):
        return self._reader.at_eof()

    def close(self):
        self._writer.close()

    async def readline(self):
        try:
            line = await asyncio.wait_for(self._reader.readline(),
                                          self.READ_TIMEOUT)
            print (line)
            return line.decode('utf-8', errors='replace')
        except asyncio.TimeoutError:
            self.close()
            return 'close becouse of asyncio.TimeoutError'


class _TCPServer:
    def __init__(self, port, data_handler=None):
        self._data_handler = data_handler
        self._port = port

    async def _accept(self, reader, writer):
        connection = Connection(reader, writer)

        while not connection.at_eof():
            line = (await connection.readline()).strip()
            # print('185', line)
            if line:
                safecall(self._data_handler, line, connection)

    async def run(self):
        server = await asyncio.start_server(self._accept, '0.0.0.0', self._port)

        try:
            async with server:
                print('Ready. Go!')
                await server.serve_forever()
        except KeyboardInterrupt:
            pass


class Server:
    PORT = 13000
    commands = {}

    def __init__(self, graph, tcp_server=_TCPServer, port=PORT):
        if not isinstance(graph, Graph):
            raise TypeError('graph')

        if not issubclass(tcp_server, _TCPServer):
            raise TypeError('tcp_server')

        self._graph = graph
        self._server = tcp_server(port, data_handler=self._handle)

    @classmethod
    def register_handler(cls, handler):
        if not check_class(handler, CommandBase):
            raise TypeError('handler')

        handler = handler()
        cls.commands[handler.name] = handler

    def run(self):
        asyncio.run(self._server.run())

    def _handle(self, data, connection):
        cmd, *args = data.split(' ', 1)
        print(cmd, *args)
        if cmd not in self.commands:
            connection.send("Wrong command.\n")
            connection.close()
            return

        # try:
        self.commands[cmd].do(''.join(args), connection, self._graph)
        # except Exception as e:
        #     print(e)
        #     pass



def main(args):
    for command in CommandBase.__subclasses__():
        Server.register_handler(command)

    Server(Graph(args[0])).run()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
