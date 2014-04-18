import os

from containerscafe.common.states import State


class BaseContainerClient(object):

    STOPPED = 'value not set'
    RUNNING = 'value not set'

    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.rc_file = None
        self._state = State(State.INITIAL)
        self._requires_destroy = False
        self.cmd_delay = 0

    def _run(self, cmd):
        raise NotImplementedError

    def _check_states(self, *valid_states):
        raise NotImplementedError

    def set_option(self, option, *values):
        raise NotImplementedError

    def create(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def execute(self, user_cmd):
        raise NotImplementedError

    def wait(self, states):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def clean(self):
        raise NotImplementedError

    @classmethod
    def write_cfg(cls, path, config, filename='config', open_func=open):
        rc_file = os.path.join(path, filename)

        with open_func(rc_file, 'w') as cfg_out:
            for cfg_key in config:
                value = config[cfg_key]

                # Is the object iterable?
                if not isinstance(value, str):
                    if hasattr(value, '__contains__'):
                        str_val = ', '.join(value)
                    else:
                        raise TypeError('Expected string or iterable value')
                else:
                    str_val = value

                cfg_out.write('{} = {}\n'.format(cfg_key, str_val))
        return rc_file

    @classmethod
    def get_cfg(cls, rc_file, open_func=open):
        with open_func(rc_file, "r") as cfg_file:
            cfg = cfg_file.readlines()
        return cfg_file
