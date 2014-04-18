import commands

class LocalHostClient(object):

    def execute(cmd):
        return commands.getoutput(cmd=cmd)
