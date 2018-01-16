from django.db import models

# Create your models here.


class Server(models.Model):
    listen = models.CharField(max_length=256)
    server_name = models.CharField(max_length=256)
    root = models.CharField(max_length=256)
    ssl_certificate = models.CharField(max_length=256)
    ssl_certificate_key = models.CharField(max_length=256)
    ssl_session_cache = models.CharField(max_length=256)
    ssl_session_timeout = models.CharField(max_length=256)
    ssl_ciphers = models.CharField(max_length=256)
    ssl_prefer_server_ciphers = models.CharField(max_length=256)

    #        location / {
    #        }
    #
    #        error_page 404 /404.html;
    #            location = /40x.html {
    #        }
    #
    #        error_page 500 502 503 504 /50x.html;
    #            location = /50x.html {
