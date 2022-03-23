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
                 token: str,
                 server: str) -> None:
        self.token = token
        self.server = server

        try:
            print()
            # ping server
        except Exception as e:
            logging.error(f'Metrika server offline: {str(e)}')

    def parse_data(self, data: dict) -> dict:
        # ...
        return data

    async def write_message(self, data) -> None:
        data = self.parse_data(data)
        # self.token
        # send data
        print(data)
