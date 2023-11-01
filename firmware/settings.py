# Scrapy settings for firmware project

BOT_NAME = 'firmware'

SPIDER_MODULES = ['firmware.spiders']
NEWSPIDER_MODULE = 'firmware.spiders'

FILES_STORE = 'firmware_files/'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOAD_TIMEOUT = 320

LOG_LEVEL = 'DEBUG'

FTP_USER = 'anonymous'
FTP_PASSWORD = 'guest'

DOWNLOAD_HANDLERS = {
    'ftp': 'firmware.handlers.FTPHandler'
}

DOWNLOADER_MIDDLEWARES = {
    'firmware.middlewares.FirmwareDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
    'firmware.pipelines.HpPipeline': 300,
    'firmware.pipelines.AsusPipeline': 300,
    'firmware.pipelines.AvmPipeline': 1,
    'firmware.pipelines.LinksysPipeline': 1,
}

# Enable to run with Selenium. Set to the driver executable path
SELENIUM_DRIVER_EXECUTABLE_PATH = '/usr/local/bin/geckodriver'
