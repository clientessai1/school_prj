from django.contrib import admin
from school_app.models import *
# Register your models here.

class FiliereAdmin(admin.ModelAdmin):
    #list_display = ('libelle') # Affiche les deux colonnes en Page Admin
    #list_display = ('nom', 'domaine') # Affiche les deux colonnes en Page Admin
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    #list_filter = ('domaine',) # Affiche un champ de filtre sur les domaines

"""
class FiliereInline(admin.TabularInline):
     model = Filiere
"""
class DomaineAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    #inlines = (FiliereInline,)
    pass

class EtablissementAdmin(admin.ModelAdmin):
    pass

#class DomaineAdmin(admin.ModelAdmin):
#    pass
#
#class FiliereAdmin(admin.ModelAdmin):
#    pass

class LieuAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class ParcoursAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class GradeScolaireAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class NiveauAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class CursusAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    list_display = ('libelle', 'domaine', 'parcours','gradeScolaire') # Affiche les deux colonnes en Page Admin
    list_filter = ('domaine', 'parcours', 'filiere', 'gradeScolaire') # Affiche un champ de filtre sur les domaines
    pass

class MatiereAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class MatiereCursusAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    list_filter = ('cursus',) # Affiche un champ de filtre sur les domaines
    pass

class AnneeScolaireAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'dateDebut', 'dateFin') # Affiche les deux colonnes en Page Admin
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class MatCursusAnneeAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class PersonneAdmin(admin.ModelAdmin):
    pass

class GradeEnseignantAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class EnseignantAdmin(admin.ModelAdmin):
    search_fields = ('nom', 'prenoms') #Faire apparaître le champ de recherche de 'nomf'
    pass

class EnseignementAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    list_filter = ('enseignant',) # Affiche un champ de filtre sur les domaines
    pass

class SalleAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class SeanceCoursAdmin(admin.ModelAdmin):
    search_fields = ('lieu',) #Faire apparaître le champ de recherche de 'nomf'
    list_display = ('enseignement', 'lieu', 'date', 'salle',) # Affiche les deux colonnes en Page Admin
    pass

class SeanceCoursInline(admin.TabularInline):
     model = SeanceCours

class EmploiDuTempsAdmin(admin.ModelAdmin):
    inlines = (SeanceCoursInline,)
    pass
#
class EquipementAdmin(admin.ModelAdmin):
    search_fields = ('libelle',) #Faire apparaître le champ de recherche de 'nomf'
    pass

class LogistiqueAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Domaine, DomaineAdmin)
#admin.site.register(Domaine, DomaineAdmin)
#admin.site.register(Filiere, FiliereAdmin)

admin.site.register(Etablissement, EtablissementAdmin)
admin.site.register(EmploiDuTemps, EmploiDuTempsAdmin)
admin.site.register(Domaine, DomaineAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Parcours, ParcoursAdmin)
admin.site.register(Lieu, LieuAdmin)
admin.site.register(GradeScolaire, GradeScolaireAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Cursus, CursusAdmin)
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(MatiereCursus, MatiereCursusAdmin)
admin.site.register(AnneeScolaire, AnneeScolaireAdmin)
admin.site.register(MatCursusAnnee, MatCursusAnneeAdmin)
#admin.site.register(Personne, PersonneAdmin)
admin.site.register(GradeEnseignant, GradeEnseignantAdmin)
admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Enseignement, EnseignementAdmin)
admin.site.register(Salle, SalleAdmin)
admin.site.register(SeanceCours, SeanceCoursAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Logistique, LogistiqueAdmin)

