from generic_scaffold import CrudManager;
from . import models;

class DomaineCrudManager(CrudManager):
    model = models.Domaine
    prefix = 'domaines/'

class CursusCrudManager(CrudManager):
    model = models.Cursus;
    prefix = 'cursuss/';
"""
    def get_url_patterns(self):
        CrudManager.get_url_patterns
        """
