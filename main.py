from avilla.core import Avilla, Context, MessageReceived
from avilla.console.protocol import ConsoleProtocol

avilla = Avilla()
avilla.apply_protocols(ConsoleProtocol())


@avilla.listen(MessageReceived)
async def on_message_received(cx: Context):
    await cx.scene.send_message("Hello, Avilla!")


avilla.launch()