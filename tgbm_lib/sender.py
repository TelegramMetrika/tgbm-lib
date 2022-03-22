import logging

class Sender:
    """
    Interface for sender class
    """
    def __init__(self) -> None:
        pass

    async def write_message(self, data: dict) -> None:
        """
        Upload message to db

        Args:
            data (dict): data from logger class
        """
        pass


class ServerSender(Sender):
    def __init__(self,
                 token: str) -> None:
        self.token = token

        try:
            print()
            # ping server
        except Exception as e:
            logging.error(f'error: {str(e)}')

    def parse_data(self, data: dict) -> dict:
        _data = {
            'measurement': 'bot',
            'time': data.get('datetime'),
            'fields': {
                "event": 1
            },
            'tags': {
                'user': str(data.get('user_id')),
                'bot_id': str(data.get('bot_id'))
            }
        }

        if data.get('is_command'):
            _data['tags'].update({
                'command': data.get('text')
            })
        if data.get('text'):
            _data['fields'].update({
                'text': data.get('text')
            })
        return _data

    async def write_message(self, data) -> None:
        data = self.parse_data(data)
        print(data)
