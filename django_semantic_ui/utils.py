# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.conf import settings


class Constant:
    JQUERY_URL = 'https://code.jquery.com/jquery-3.1.1.min.js'
    GULP_VERSION = '3.9.1'
    SEMANTIC_UI_VERSION = 'latest'
    SEMANTIC_DIRNAME = 'semantic'
    JAVASCRIPT_FILE = '/dist/semantic.min.js'
    STYLESHEET_FILE = '/dist/semantic.min.css'
    PACKAGE_NAME = 'dsu'
    STATIC_URL = '/static/'


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def get_static_folder():
        try:
            static_url = settings.STATIC_URL
        except:
            static_url = Constant.STATIC_URL
        return static_url

    @staticmethod
    def get_semantic_javascript_url(semantic_folder=Constant.SEMANTIC_DIRNAME):
        return '{0}{1}/{2}{3}'.format(
            Utils.get_static_folder(), Constant.PACKAGE_NAME,
            semantic_folder, Constant.JAVASCRIPT_FILE)

    @staticmethod
    def get_semantic_stylesheet_url(semantic_folder=Constant.SEMANTIC_DIRNAME):
        return '{0}{1}/{2}{3}'.format(
            Utils.get_static_folder(), Constant.PACKAGE_NAME,
            semantic_folder, Constant.STYLESHEET_FILE)

    @staticmethod
    def get_text_value(value):
        return force_text(value) if value else ''

    @staticmethod
    def get_attrs_formatted(attrs=None):
        return mark_safe(flatatt(attrs=attrs)) if attrs else ''


    @staticmethod
    def render_tag(tag, attrs=None, content=None, close=True):
        content_formatted = Utils.get_text_value(value=content)
        attrs_formatted = Utils.get_attrs_formatted(attrs=attrs)
        html = "<{0} {1}>{2}".format(tag, attrs_formatted, content_formatted)
        html += "</{0}>".format(tag) if close or content else ""
        return format_html(
            format_string=html,
            tag=tag,
            attrs=attrs_formatted,
            content=content_formatted)
