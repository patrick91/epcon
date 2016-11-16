from pytest_django.live_server_helper import LiveServer


class DebugabbleLiveServer(LiveServer):
    def __init__(self, *args, **kwargs):
        super(DebugabbleLiveServer, self).__init__(*args, **kwargs)

        from django.conf import settings
        settings.DEBUG = True

