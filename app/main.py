from aiohttp import web
import logging
from app.healthcheck import HealthcheckController
from app.product import create, find_by_id, find
from aiojobs.aiohttp import setup

async def init_app():
    healthcheck = HealthcheckController()
    app = web.Application()
    app.add_routes([web.get('/healthcheck', healthcheck.handle_get),
                    web.post('/api/v1/product', create),
                    web.get('/api/v1/products', find),
                    web.get('/api/v1/product/{id}', find_by_id)])
    setup(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
