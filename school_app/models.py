# -*-coding: UTF-8-*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from enum import Enum
from datetime import datetime

# Create your models here.

class Etablissement(models.Model):
  nom = models.CharField(max_length=150, null=False, blank=False)
  logo = models.ImageField(upload_to='photos')
  adresse = models.CharField(max_length=150)
  tel = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  class Meta:
    ordering = ['nom']

  def __str__(self):
    return f'{self.nom}'
    
class EmploiDuTemps(models.Model):
  dateDebut = models.DateTimeField(null=False, blank=False)
  dateFin = models.DateTimeField(null=False, blank=False)
  code = models.CharField(max_length=50)
  
  def clean(self) -> None:
    if self.dateDebut > self.dateFin:
      raise ValidationError(
          'La Date de Debut doit preceder la Date de Fin.\n Reprendre.'
          )

  class Meta:
    ordering=['dateDebut']

  def __str__(self):
    return f'{self.dateDebut} {self.dateFin}'


class Domaine(models.Model):
  libelle = models.CharField(max_length=100, null=False, blank=False, default=' ')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

class Filiere(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False, default=' ')
  #domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

class Parcours(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False)
  #filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle
  
class GradeScolaire(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False, default=' ')
  #parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE, blank=True, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

class Niveau(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False, default=' ')
  #gradeScolaire = models.ForeignKey(GradeScolaire, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle
  pass

class Cursus(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False, default=' ')
  #parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE, blank=True, null=False, related_name='models', related_query_name='model')
  niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')
  gradeScolaire = models.ForeignKey(GradeScolaire, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')
  parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE, blank=True, null=False, related_name='models', related_query_name='model')
  filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')
  domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

class  Matiere(models.Model):
  libelle = models.CharField(max_length=100, null=False, blank=False, default=' ')
  cursus = models.ManyToManyField(Cursus, related_name='models', through='MatiereCursus')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

class MatiereCursus(models.Model):
  matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE);
  cursus = models.ForeignKey(Cursus, on_delete=models.CASCADE);
  libelle= models.CharField(max_length=200, default=' ');
  duree = models.PositiveIntegerField(default=1, help_text='En heures');

  class Meta:
    ordering = ['libelle'];

  def __str__(self):
    return self.libelle

class AnneeScolaire(models.Model):
  dateDebut = models.DateTimeField(null=True, blank=True)
  dateFin = models.DateTimeField(null=True, blank=True)
  libelle = models.CharField(max_length=50, null=False, blank=False, default=' ')

  class Meta:
    ordering = ['libelle'];
  
  def clean(self) -> None:
    if self.dateDebut > self.dateFin:
      raise ValidationError(
          'La Date de Debut doit preceder la Date de Fin.\n Reprendre.'
          )

  def __str__(self):
    return f'{self.libelle}';

class MatCursusAnnee(models.Model):
  anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE);
  matiereCursus = models.ForeignKey(MatiereCursus, on_delete=models.CASCADE);
  libelle = models.CharField(max_length=50, null=True, blank=True, default=' ')

  class Meta:
    ordering = ['libelle'];

  def __str__(self):
    return f'{self.anneeScolaire.libelle} {self.matiereCursus.libelle}';


class Personne(models.Model):
  nom = models.CharField(max_length=150, null=False, blank=False)
  prenoms = models.CharField(max_length=150, null=False, blank=False)
  dateNais = models.DateTimeField()
  tel = models.CharField(max_length=50)
  profession = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  adresse = models.CharField(max_length=100)
  """
  SEXE_M = 'masculin'
  SEXE_F = 'feminin'
  SEXE_U = 'inconnu'
  SEXE_CHOICES = (
      (SEXE_M, 'Masculin'),
      (SEXE_F, 'Feminin'),
      (SEXE_U, 'Inconnu'),
      )
  """
  sexe_list = ['Masculin','Feminin','Inconnu']
  ALL_SEXE = sorted([(item, item) for item in sexe_list])

  sexe = models.CharField(
      max_length=15,
      choices=ALL_SEXE,
      #choices=SEXE_CHOICES,
      #default=SEXE_CHOICES.SEXE_M,
    )
  

  class Meta:
    ordering = ['nom', 'prenoms']
    abstract = True

  def __str__(self):
    return f'{self.nom} {self.prenoms}'
  
class GradeEnseignant(models.Model):
  libelle = models.CharField(max_length=100, blank=False, null=False)
  #parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE, blank=True, null=False, related_name='models', related_query_name='model')

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle


class Enseignant(Personne):
  gradeEnseignant = models.ForeignKey(GradeEnseignant, on_delete=models.CASCADE, blank=False, null=False, related_name='models', related_query_name='model')
  matCursusAnnee = models.ManyToManyField(MatCursusAnnee, related_name='models', through='Enseignement')

  dateIndispoDebut = models.DateField(null=True, blank=True)
  dateIndispoFin = models.DateField(null=True, blank=True)


  class Meta:
    ordering = ['nom', 'prenoms']

  def __str__(self):
    return f'{self.gradeEnseignant.libelle} {self.nom} {self.prenoms}'
  
class Enseignement(models.Model):
  enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
  matCursusAnnee = models.ForeignKey(MatCursusAnnee, on_delete=models.CASCADE)
  libelle = models.CharField(max_length=150, null=True, blank=True)

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return f'{self.matCursusAnnee} > {self.enseignant}'


class Lieu(models.Model):
  libelle = models.CharField(max_length=99, null=False, blank=False, default=' ')
  localisation = models.CharField(max_length=100, null=True, blank=True)


  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return self.libelle

def getDefaultLieu():
  return Lieu.objects.get(id=1)


class Salle(models.Model):
  libelle = models.CharField(max_length=50, null=False, blank=False, default=' ')
  capacite = models.PositiveIntegerField(default=0)
  numero = models.CharField(max_length=50)
  enseignement = models.ManyToManyField(Enseignement, related_name='models', through='SeanceCours')


  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return f'{self.libelle}'

class SeanceCours(models.Model):

  """
  class StatutChoices(Enum):
    Fait = 'fait'
    NonFait = 'non fait'
    statut_list = ['Fait', 'Non Fait']
    
    @classmethod
    def choices(cls):
      #return tuple((i.name, i.value) for i in cls)
      return sorted([(item, item) for item in statut_list])
    """
  salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
  enseignement = models.ForeignKey(Enseignement, on_delete=models.CASCADE)
  date = models.DateField(null=False, blank=False)
  emploiDuTemps = models.ForeignKey(EmploiDuTemps, on_delete=models.CASCADE)
  heureDebut = models.TimeField(null=False, blank=False, default=datetime.now())
  heureFin = models.TimeField(null=False, blank=False, default=datetime.now())
  lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, default=getDefaultLieu, blank=True, null=False, related_name='models', related_query_name='model')

  statut_list = ['Fait', 'Non Fait']
  ALL_STATUT = sorted([(item, item) for item in statut_list])

  statut = models.CharField(
      max_length=15,
      choices=ALL_STATUT,
      default=statut_list[1],
    )

  type_list = ['TD','TP','Cours']
  ALL_TYPE = sorted([(item, item) for item in type_list])

  typeSeance = models.CharField(
      max_length=15,
      choices=ALL_TYPE,
    )
 
  def clean(self) -> None:
    if self.enseignement.enseignant.dateIndispoDebut <= self.date and self.date <= self.enseignement.enseignant.dateIndispoFin :
      raise ValidationError(
          'Cet Enseignant est indisponible dans cette Période. Prière le programmer à une autre date.'
          )

  

  def __str__(self):
    return f'SeanceCours {self.enseignement}-{self.salle.libelle}'

class Equipement(models.Model):
  libelle = models.CharField(max_length=50, null=False, blank=False, default=' ')
  quantite = models.PositiveIntegerField(default=0)
  seanceCours = models.ManyToManyField(SeanceCours, related_name='models', through='Logistique');

  class Meta:
    ordering = ['libelle']

  def __str__(self):
    return '{self.libelle}'


class Logistique(models.Model):
  seanceCours = models.ForeignKey(SeanceCours, on_delete=models.CASCADE)
  equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

  def __str__(self):
    return f'Logistique {self.seanceCours.date}-{self.seanceCours.salle.libelle} - {self.equipement.libelle}'


