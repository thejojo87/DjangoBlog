#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by thejojo at 2017/11/26

import xadmin
from .models import BookInfo

class BookInfoAdmin(object):
    list_display = ["name"]


xadmin.site.register(BookInfo, BookInfoAdmin)









