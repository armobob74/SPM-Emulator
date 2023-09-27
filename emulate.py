from parse_logfile import parseLogfile
import asyncio
import serial
import serial_asyncio
import sys
import time


class AsyncSerialProtocol(asyncio.Protocol):
    """
    handles all async communications stuff
    takes in serial comms and returns what it hopes the spm normally would
    """
    def connection_made(self, transport):
        self.transport = transport
        print("Port opened")

    def data_received(self, data):
        s = data.decode('utf-8')
        print("Data received:", data.decode())
        #answer_pattern = r"/0(.)(.*)\x03\r"
        if len(s) > 512:
            status_code = 'O' # means buffer overflow error
        else:
            status_code = '@' # means busy -- no error
        response = f'/0{status_code}\x03\r'.encode()
        print("first response ",response)
        self.transport.write(response)

        if status_code == "@":
            asyncio.create_task(self.send_ready_response_after_delay())

    async def send_ready_response_after_delay(self):
        await asyncio.sleep(4)
        response = f'/0`\x03\r'.encode()  # ready response
        print("next response", response)
        self.transport.write(response)


    def connection_lost(self, exc):
        print("Port closed")
        self.transport.loop.stop()


async def main(port_name):
    loop = asyncio.get_event_loop()
    coro = serial_asyncio.create_serial_connection(loop, AsyncSerialProtocol, port_name, baudrate=9600)
    await coro
    await asyncio.sleep(float('Inf')) # this infinite sleep keeps the event loop running

if __name__ == "__main__":
    ports = parseLogfile()
    print('Have SPM on:',ports[0])
    print('Have emulator on:',ports[1])
    asyncio.run(main(ports[1]))
