from microdot_asyncio import Microdot
import uasyncio


app = Microdot()

htmldoc = '''<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from Microdot!</p>
            <p><a href="/shutdown">Click to shutdown the server</a></p>
        </div>
    </body>
</html>
'''

async def loop():
    while True:
        print("hey")
        await uasyncio.sleep(1)

@app.route('/')
async def hello(request):
    return htmldoc, 200, {'Content-Type': 'text/html'}


@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

async def main():
    uasyncio.create_task(loop())
    uasyncio.create_task(app.run(debug=True))

uasyncio.run(main())
