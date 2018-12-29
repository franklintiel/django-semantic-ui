# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.conf import settings
from .exceptions import FolderNotFoundException, SemanticUIException
from .utils import Constant


class SemanticUI(object):

    def __init__(self):
        self.project_folder_path = os.path.dirname(__file__)
        try:
            self.jquery_url = settings.DSU_JQUERY_URL
        except:
            self.jquery_url = Constant.JQUERY_URL
        try:
            self.gulp_version = settings.GULP_VERSION
        except:
            self.gulp_version = Constant.GULP_VERSION
        try:
            self.semantic_ui_version = settings.SEMANTIC_UI_VERSION
        except:
            self.semantic_ui_version = Constant.SEMANTIC_UI_VERSION
        try:
            self.semantic_folder = settings.SEMANTIC_DIRNAME
        except:
            self.semantic_folder = Constant.SEMANTIC_DIRNAME
        try:
            if not os.path.exists(self.project_folder_path):
                raise FolderNotFoundException("[ERROR] Project folder not found. PATH: {0}".format(
                    self.project_folder_path))
            else:
                self.static_folder_path = '{0}/static'.format(self.project_folder_path)
                if not os.path.exists(self.static_folder_path):
                    print "Creating the Static folder on PATH: {0}".format(self.static_folder_path)
                    os.mkdir(self.static_folder_path)
                try:
                    os.chdir(self.static_folder_path)
                    self.semantic_files_path = '{0}/dsu'.format(self.static_folder_path)
                    if not os.path.exists(self.semantic_files_path):
                        print "Creating the django_semantic_ui folder on PATH: {0}".format(self.semantic_files_path)
                        os.mkdir(self.semantic_files_path)
                    print "Semantic UI Folder: {0}".format(self.semantic_files_path)
                except Exception as e:
                    raise SemanticUIException(e.message)
        except Exception as e:
            raise SemanticUIException(e.message)

    def install(self):
        """
        Install Gulp and Semantic UI Framework on a django project
        :return:
        """
        print "Installing started..."
        try:
            print "Moving to static folder..."
            os.chdir(self.semantic_files_path)
            package_json_path = '{0}/package.json'.format(self.semantic_files_path)
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
            os.chdir(self.semantic_files_path)
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
                    print "Deleting package.json file..."
                    try:
                        os.system('rm -f package*')
                        print "package.json file has been removed..."
                        node_modules_path = '{0}/node_modules'.format(self.semantic_files_path)
                        if not os.path.exists(node_modules_path):
                            raise FolderNotFoundException("[ERROR] node_modules folder not found. PATH: {0}".format(
                                node_modules_path))
                        else:
                            os.system("rm -rf node_modules")
                        print "Removing Semantic folder..."
                        os.rmdir(self.semantic_files_path)
                        print "Semantic folder removed."
                        print "Removing static folder..."
                        os.rmdir(self.static_folder_path)
                        print "Static folder removed."
                        print "Semantic UI has been removed successfully!"
                    except:
                        raise SemanticUIException("[ERROR] Semantic JSON file not exists.")
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
        print "Moving to Semantic files folder..."
        semantic_path = '{0}/{1}'.format(self.semantic_files_path, self.semantic_folder)
        try:
            print "Moving to Semantic folder..."
            os.chdir(semantic_path)
            print "Gulp build command executing..."
            os.system('gulp build')
            print "Gulp build command completed successfully."
        except:
            raise SemanticUIException(
                "[ERROR] Gulp build command failed, the semantic folder not exists or the name is incorrect.")
