from app.db import instance
from umongo import Document
from umongo import fields
from aiohttp import web
from aiojobs.aiohttp import atomic
from marshmallow.exceptions import ValidationError
from json.decoder import JSONDecodeError
from bson import ObjectId
from bson.errors import InvalidId


@instance.register
class Product(Document):
    title = fields.StrField(required=False)
    description = fields.StrField()
    params = fields.DictField()


@atomic
async def create(request):
    try:
        body = await request.json()
        p = Product(**body)
        await p.commit()
        return web.json_response(p.dump(), status=200)
    except JSONDecodeError as e:
        return web.json_response({"error:": "JSONDecodeError", "message": str(e)}, status=422)
    except ValidationError as e:
        return web.json_response({"error:": "ValidationError", "message": str(e)}, status=422)
    except Exception as e:
        return web.json_response({"error:": "Exception", "message": str(e)}, status=500)


async def find_by_id(request):
    id = request.match_info.get('id')
    print(id)
    try:
        product = await Product.find_one({"_id": ObjectId(id)})
        if product:
            return web.json_response(product.dump())
        else:
            return web.json_response({})
    except InvalidId as e:
        return web.json_response({"error:": "InvalidId", "message": str(e)}, status=422)


async def find(request):
    try:
        body = await request.json()
        sort_by = body.get("sort_by", ["title", 1])
        f = body.get("filter", {})
        products_cursor = Product.find(f).sort([(sort_by[0], sort_by[1])])
        result = []
        async for product in products_cursor:
            result.append(product.dump())
        return web.json_response(result, status=200)
    except JSONDecodeError as e:
        return web.json_response({"error:": "JSONDecodeError", "message": str(e)}, status=422)
    except Exception as e:
        return web.json_response({"error:": "Exception", "message": str(e)}, status=500)
