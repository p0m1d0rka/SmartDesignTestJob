from aiohttp import web


class HealthcheckController:

    def __init__(self):
        pass

    async def handle_get(self, request):
        response = {"code": 200, "status": "ok"}
        return web.json_response(response)
