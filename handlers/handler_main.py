from handlers.handler_com import HandlerCommands


class HandlerMain:

    def __init__(self, bot):
        self.bot = bot
        self.handler_commnds = HandlerCommands(self.bot)

    def handle(self):
        self.handler_commnds.handle()
