from loguru import logger
logger.info('hello word')

logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#输出文件add()
logger.add('a.log',format='{time:YYYY-MM-DD at HH:mm:ss} | {level} |{message}',level='DEBUG')
logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
