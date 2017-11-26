#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by thejojo at 2017/11/26

import xadmin
from .models import BlogInfo

class BlogInfoAdmin(object):
    list_display = ["book", "title", "click_num", "blog_brief",
                    "add_time", "blog_main"]
    # search_fields = ['name', ]
    # list_editable = ["is_hot", ]
    # list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
    #                "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    # style_fields = {"goods_desc": "ueditor"}

    # class GoodsImagesInline(object):
    #     model = GoodsImage
    #     exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [GoodsImagesInline]

xadmin.site.register(BlogInfo, BlogInfoAdmin)
