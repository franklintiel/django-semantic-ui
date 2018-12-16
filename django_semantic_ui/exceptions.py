class StaticFolderException(Exception):
    """
    Exception displayed when the static folder not exists.
    """
    pass


class SemanticUIException(Exception):
    """
    Exception displayed during the install/uninstall/gulp build commands
    """
    pass