from django.contrib.auth.models import Group;
newGroup = Group();
newGroup.name = 'New Group';
newGroup.save();
