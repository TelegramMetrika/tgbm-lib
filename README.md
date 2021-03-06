# tgbm-lib
---
### Simplifies sending logs from your bots to server.
---
## Install package from pip
```
pip install ...
```

Import and create instances
```python
from tgbm_lib import Logger, ServerSender
sender = ServerSender(
    token='metrika_token_here',    # <---
    server='metrika_url_here'      # <---
)
logger = Logger(sender)
```

Create StatMiddleware to logging every incoming message
```python
class StatMiddleware(middlewares.BaseMiddleware):
    def __init__(self):
        super(StatMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        await logger.write_logs(self._manager.bot.id, message, parse_text=True)

dp.middleware.setup(StatMiddleware())
```