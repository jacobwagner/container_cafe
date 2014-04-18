from containerscafe.common.states import State
from containerscafe.containers.container_base_client import BaseContainerClient


class HostContainerClient(BaseContainerClient):

    STOPPED = 'N/A'
    RUNNING = 'N/A'

    def __init__(self, name, connection, clean=False):
        super(HostContainerClient, self).__init__(
            name=name, connection=connection)
        self._state = State(State.RUNNING)
        self._requires_destroy = clean

    def execute(self, user_command, **kwargs):
        return self.connection.execute(user_command, **kwargs)

    def clean(self):
        self.connection.close()
