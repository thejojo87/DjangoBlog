#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by thejojo at 2017/11/26

import xadmin
from .models import BlogInfo

class BlogInfoAdmin(object):
    list_display = ["book", "title", "click_num", "blog_brief",
                    "add_time", "blog_main"]


xadmin.site.register(BlogInfo, BlogInfoAdmin)
