from django.core.management.base import BaseCommand
from django_semantic_ui.models import SemanticUI
from django_semantic_ui.exceptions import SemanticUIException


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('subcommand', choices=['install', 'uninstall', 'gulp_build'])
        parser.add_argument('--semantic_folder', type=str, nargs='?')

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
