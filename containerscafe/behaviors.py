from containerscafe.common.process_connector import CommandError


class ContainerBehavior(object):

    def __init__(self, container_type):
        self.container_type = container_type

    def __enter__(self):
        self.container_type.create()
        self.container_type.wait(self.container_type.STOPPED)
        self.container_type.start()
        self.container_type.wait(self.container_type.RUNNING)
        return self.container_type

    def __exit__(self, container_type):
        if container_type is not None:
            pass

        self.container_type.stop()
        self.container_type.wait(self.container_type.STOPPED)
        self.container_type.destroy()
        self.container_type.clean()

    @property
    def get_context(self):
        return self.container_type
