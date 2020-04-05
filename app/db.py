from umongo import Instance
import motor.motor_asyncio

db = motor.motor_asyncio.AsyncIOMotorClient()["test_db"]

instance = Instance(db)
