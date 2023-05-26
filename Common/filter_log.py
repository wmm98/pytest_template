import logging
import sys
# 创建日志器logger并将其日志级别设置为DEBUG
logger = logging.getLogger("python_config_logger")
logger.setLevel(logging.DEBUG)
# 创建一个流处理器handler并将其日志级别设置为DEBU
err_handler = logging.FileHandler("./err.txt", encoding='utf-8')
err_handler.setLevel(logging.DEBUG)
# 创建一个格式化器formatter并将其添加到处理器handler中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
err_handler.setFormatter()

# 为日志器logger添加上面创建好的处理器handler
logger.addHandler(err_handler)

# 添加handler的过滤器,只输出errlog; 也可添加logger的过滤器
non_error_filter = logging.Filter()
non_error_filter.filter = lambda record: logging.WARNING < record.levelno < logging.CRITICAL
err_handler.addFilter(non_error_filter)


# 将日志打印在控制台
logger.debug('打印日志级别：debug')
logger.info('打印日志级别：info')
logger.warning('打印日志级别：warning')
logger.error('打印日志级别：error')
logger.critical('打印日志级别：critical')

logger.removeHandler(err_handler)
