from django.core.management.base import BaseCommand
from django_semantic_ui.models import SemanticUI
from django_semantic_ui.exceptions import SemanticUIException


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('subcommand', choices=['install', 'uninstall', 'gulp_build'])
        parser.add_argument('--semantic_folder', type=str, nargs='?')

    def handle(self, *args, **options):
        if 'subcommand' in options:
            if options.get('subcommand') == 'install':
                object = SemanticUI()
                object.install()
            elif options.get('subcommand') == 'uninstall':
                if not options.get('semantic_folder'):
                    raise SemanticUIException("""
                    ERROR: Uninstalling failed, you need to pass the argument --semantic_folder
                    By example:
                    $ python manage.py semanticui uninstall --semantic_folder=semantic
                    {0}
                    """.format(self.help))
                else:
                    object = SemanticUI(semantic_folder=options.get('semantic_folder'))
                    object.uninstall()
            elif options.get('subcommand') == 'gulp_build':
                if not options.get('semantic_folder'):
                    raise SemanticUIException("""
                    ERROR: Gulp Build command failed, you need to pass the argument --semantic_folder
                    By example:
                    $ python manage.py semanticui gulp_build --semantic_folder=semantic
                    {0}
                    """.format(self.help))
                else:
                    object = SemanticUI(semantic_folder=options.get('semantic_folder'))
                    object.build()
            else:
                print self.help
