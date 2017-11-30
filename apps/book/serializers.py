#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by thejojo at 2017/11/26

from rest_framework import serializers
from book.models import BookInfo

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"
