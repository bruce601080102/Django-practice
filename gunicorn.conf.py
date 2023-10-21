# gunicorn.conf.py

# 綁定的ip和端口。這裡綁定到'localhost'的'8000'端口。
bind = '127.0.0.1:8000'

# 使用的工作進程類型。常用的是'sync'，但你還可以使用'gevent'等其他選項。
worker_class = 'sync'

# 指定工作進程的數量。
workers = 4

# 設置日誌文件的位置。
accesslog = 'access.log'
errorlog = 'error.log'

# 如果你想有更多的日誌輸出，可以將日誌級別設定為'debug'。
loglevel = 'info'
