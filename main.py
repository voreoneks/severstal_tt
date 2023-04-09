import json
import os
from datetime import datetime
from glob import glob
from threading import Thread

from redis import Redis

from app.core import config
from app.core.logging import app_logger
from app.db.dependencies import get_repository
from app.db.repositories.pictures import PicturesRepository
from app.models.pictures import PictureModel

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=0,
    password=config.REDIS_PASS
)

redis.delete('queue')

def producer_tasks():
    app_logger.info('Producer thread started.')

    pictures = glob(config.PICTURES_FOLDER + '/*')
    length = len(pictures)
    app_logger.info(f'{length} pictures are found.')

    redis.rpush('length', length)
    data = dict()

    for picture in pictures:
        size = os.stat(picture).st_size
        with open(picture, 'rb') as file:
            file_bytes = file.read()
            data.update({
                'file_bytes': file_bytes,
                'size': size
            })
            redis.lpush('queue', json.dumps(data))


async def consumer_tasks():
    app_logger.info('Consumer thread started.')
    
    length = int(redis.rpop('length'))
    while length:
        json_bytes = redis.rpop('queue')
        if json_bytes:
            data = json.loads(json_bytes)
            picture = PictureModel(
                size=data.get('size'),
                created_at=datetime.utcnow()
            )
            repository:PicturesRepository = get_repository(PicturesRepository)
            await repository.create(picture)

            length -= 1

    app_logger.info('All done. Check database.')


producer_thread = Thread(target=producer_tasks, name='producer', daemon=False)
consumer_thread = Thread(target=consumer_tasks, name='consumer', daemon=False)

if __name__ == '__main__':
    producer_thread.start()
    consumer_thread.start()
