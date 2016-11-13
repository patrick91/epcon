from pytest_django.live_server_helper import LiveServer


class DebugableLiveServer(LiveServer):
    def __init__(self, *args, **kwargs):
        super(DebugableLiveServer, self).__init__(*args, **kwargs)

        from django.conf import settings
        settings.DEBUG = True

