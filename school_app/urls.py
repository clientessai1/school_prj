from django.urls import path;
from . import views; #Import from the current directory

"""
from . import scaffolding; #
#from scaffolding import scaffolding.DomaineCrudManager; #
DomaineCrudManager = scaffolding.DomaineCrudManager;
domain_crud = DomaineCrudManager();

CursusCrudManager = scaffolding.CursusCrudManager;
cursus_crud = CursusCrudManager();
"""

urlpatterns = [
        path('', views.home, name='home'),
        #path('homeold', views.homeold, name='homeold'),
];

"""
urlpatterns += domain_crud.get_url_patterns();

urlpatterns += cursus_crud.get_url_patterns();
"""

"""
urlpatterns = [
        path('', views.home, name='home'),
];
"""

#urlpatterns += domain_crud.get_url_patterns()
