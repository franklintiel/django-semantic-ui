# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django_semantic_ui.models import SemanticUI


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('subcommand', choices=['install', 'uninstall', 'gulp_build'])

    def handle(self, *args, **options):
        if 'subcommand' in options:
            object = SemanticUI()
            if options.get('subcommand') == 'install':
                object.install()
            elif options.get('subcommand') == 'uninstall':
                object.uninstall()
            elif options.get('subcommand') == 'gulp_build':
                object.build()
            else:
                print self.help
