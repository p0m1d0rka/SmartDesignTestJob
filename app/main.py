from aiohttp import web
import logging
from app.healthcheck import Healthcheck


async def init_app(argv):
    healthcheck = Healthcheck()
    app = web.Application()
    app.add_routes([web.get('/healthcheck', healthcheck.handle_get)])
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
