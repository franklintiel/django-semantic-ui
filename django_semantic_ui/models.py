import os
from django.conf import settings
from .exceptions import StaticFolderException, SemanticUIException


class SemanticUI(object):

    def __init__(self, semantic_folder='semantic'):
        try:
            self.gulp_version = settings.GULP_VERSION
        except:
            self.gulp_version = '3.9.1'
        try:
            self.semantic_ui_version = settings.SEMANTIC_UI_VERSION
        except:
            self.semantic_ui_version = 'latest'
        self.semantic_folder = semantic_folder if semantic_folder else 'semantic'
        try:
            self.static_folder_path = '{0}'.format(settings.STATIC_ROOT)
            if not os.path.exists(self.static_folder_path):
                raise StaticFolderException("[ERROR] Static folder not exists.")
            print "Static Folder: {0}".format(self.static_folder_path)
        except:
            raise SemanticUIException("[ERROR] STATIC_ROOT constant not defined on the settings.py.")


    def install(self):
        """
        Install Gulp and Semantic UI Framework on a django project
        :return:
        """
        print "Installing started..."
        try:
            print "Moving to static folder..."
            os.chdir(self.static_folder_path)
            package_json_path = '{0}/package.json'.format(self.static_folder_path)
            file_exists = os.path.isfile(package_json_path)
            if not file_exists:
                print "Generationg the package.json file..."
                os.system('npm init')
                print "Package.json file has been generated successfully!."
            print "Installing gulp..."
            os.system('npm install gulp@{0} --save-dev'.format(self.gulp_version))
            print "Gulp module has been installed successfully (Version installed {0})".format(
                self.gulp_version)
            print "Installing semantic-ui module..."
            os.system('npm install semantic-ui@{0} --save'.format(self.semantic_ui_version))
            print "Semantic-ui module has been installed successfully (Version installed {0}).".format(
                self.semantic_ui_version)
            print "Semantic UI  has been installed successfully..."
        except:
            raise SemanticUIException("[ERROR] Installing failed cannot move to static folder.")

    def uninstall(self):
        """
        Uninstall Gulp and Semantic UI framework from the django project.
        :return:
        """
        print "Uninstalling started..."
        try:
            print "Moving to Static folder..."
            os.chdir(self.static_folder_path)
            print "Uninstalling Semantic UI module..."
            os.system('npm uninstall semantic-ui --save')
            print "Semantic UI module has been removed successfully!."
            print "Uninstalling Gulp module..."
            os.system('npm uninstall gulp --save-dev')
            print "Gulp module has been removed successfully!."
            print "Deleting semantic folder..."
            try:
                os.system('rm -rf {0}'.format(self.semantic_folder))
                print "Semantic folder has been removed successfully."
                print "Deleting semantic.json file..."
                try:
                    os.system('rm -f semantic.json')
                    print "semantic.json file has been removed..."
                    print "Semantic UI has been removed successfully!"
                except:
                    raise SemanticUIException("[ERROR] Semantic JSON file not exists.")
            except:
                raise SemanticUIException("[ERROR] Semantic folder not exists.")
        except:
            raise SemanticUIException("[ERROR] Uninstalling failed cannot move to static folder.")

    def build(self):
        """
        Running Gulp build command inside semantic folder.
        :return:
        """
        print "Gulp Build command started..."
        print "Moving to Static folder..."
        os.chdir(self.static_folder_path)
        semantic_path = '{0}/{1}'.format(self.static_folder_path, self.semantic_folder)
        try:
            print "Moving to Semantic folder..."
            os.chdir(semantic_path)
            print "Gulp build command executing..."
            os.system('gulp build')
            print "Gulp build command completed successfully."
        except:
            raise SemanticUIException(
                "[ERROR] Gulp build command failed, the semantic folder not exists or the name is incorrect.")
