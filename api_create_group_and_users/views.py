from rest_framework.response import Response;
from rest_framework.decorators import api_view;
from django.http import HttpResponseBadRequest;
from django.shortcuts import HttpResponse;
from django.shortcuts import render;
import json;
from django.contrib.auth.models import User, Group, Permission;
from django.contrib.contenttypes.models import ContentType;
from school_app.models import Filiere;
from school_app.models import Domaine;



@api_view(['GET'])
def createGroupAndUsers(request):
#    newGroup = Group();
#    newGroup.name = 'New Group';
#    newGroup.save();
    
    """
    #Delete all permissions
    for perm in Permission.objects.all():
        perm.delete();
    """
    #print(Permission.objects.get(codename='add_filiere02').delete());
    
    #for perm in Permission.objects.get(codename='add_filiere02'):
        #perm.delete();
    
    
    group_domaine_view, created_domaine_view = Group.objects.get_or_create(name = 'group_domaine_view'); 
    """
    #group_domaine_view

    Must Access:
     #Details form
     - Details' Form link (or details button)
     - Details' Form 
        - Without Modify's button/link
           - Because it's decorator requires Modify's Permission
        - Without Delete's button/link
           - Because it's decorator requires Delete's Permission
    

    List of [domaine] :
     > with(+) [details' button] 
     > minus(-) [add's button], [modify's button], [delete's button]

    Why ? Because : 
     - Add_Button showing is conditioned by the decorator the require Add_Permission
     - Modify_Button showing is conditioned by the decorator the require Modify_Permission
     - Delete_Button showing is conditioned by the decorator the require Delete_Permission

     Note #1: Will not have access to Add_form because: 
        - the display of the form is conditioned by the decorator that requires Add's Permission
        - Therefore [will not also access] the link that leads to the Add's form neither, as :
            - this link's display is under a decorator that requires Add's Persmision

     Note #2: Will not have access to Modify_form because: 
        - This form's display is conditioned by the decorator that requires Modify's Permission
        - Therefore [will not also access] the link that leads to the Modify's form also, as :
            - this link's display is under a decorator that requires Modify's Persmision
    """

    #List, detail, Add_form, Add_button, Add_method,
    group_domaine_add, created_domaine_add = Group.objects.get_or_create(name = 'group_domaine_add'); 
    """
    #group_domaine_add

    Must Access:
     #Add form
     - Add's Form link (if there is)
     - Add's Form
     - Add's Button
     - Add's Method

     #Details form
     - Details' Form link (or details button)
     - Details' Form 
        - Without Modify's button/link
           - Because it's decorator requires Modify's Permission
        - Without Delete's button/link
           - Because it's decorator requires Delete's Permission
    

    List of [domaine] :
     > with(+) [details' button] 
     > minus(-) [modify's button], [delete's button]

    Why ? Because : 
     - Modify_Button showing is conditioned by the decorator the require Modify_Permission
     - Delete_Button showing is conditioned by the decorator the require Delete_Permission

     Note #1: Will not have access to Modify_form because: 
        - This form's display is conditioned by the decorator that requires Modify's Permission
        - Therefore [will not also access] the link that leads to the Modify's form also, as :
            - this link's display is under a decorator that requires Modify's Persmision
    """

    #List, detail, Modif_form, Modif_button, Modif_method,
    group_domaine_modif, created_domaine_modif = Group.objects.get_or_create(name = 'group_domaine_modif');
    """
    #group_domaine_modif

    Must Access:
     #Modif form
     - Modif's Form link (if there is)
     - Modif's Form
     - Modif's Button
     - Modif's Method

     #Details form
     - Details' Form link (or details button)
     - Details' Form 
        - With Modify's button/link
           - Because it's decorator requires Modify's Permission
        - Without Delete's button/link
           - Because it's decorator requires Delete's Permission
    

    List of [domaine] :
     > with(+) [details' button] 
     > with(+) [modify's button]
     > minus(-) [delete's button]

    Why ? Because : 
     - Modify_Button showing is conditioned by the decorator the require Modify_Permission
     - Delete_Button showing is conditioned by the decorator the require Delete_Permission

    """
    #List, detail, Modif_form, Modif_button, Modif_method,
    group_domaine_add_modif, created_add_modif = Group.objects.get_or_create(name = 'group_domaine_add_modif');
    group_domaine_delete, created_domaine_delete = Group.objects.get_or_create(name = 'group_domaine_delete');
    group_domaine_all, created_domaine_all = Group.objects.get_or_create(name = 'group_domaine_all');
    #print(group_tech);
    #print(created);
    
    filiere_content_type = ContentType.objects.get_for_model(Filiere);
    domaine_content_type = ContentType.objects.get_for_model(Domaine);
    permissions_vector = (

            #Permission filiere
            [   { 'codename':"add_filiere", 'name':"Can Add a Filiere ", 'content_type':filiere_content_type}, #[0][0]
                { 'codename':"modify_filiere", 'name':"Can modify a Filiere ", 'content_type':filiere_content_type},#[0][1]
                { 'codename':"delete_filiere", 'name':"Can delete a Filiere ", 'content_type':filiere_content_type} ,#[0][2]
                { 'codename':"view_filiere", 'name':"Can view a Filiere ", 'content_type':filiere_content_type} ],#[0][3]

            #Permission domaine
            [   { 'codename':"add_domaine", 'name':"Can Add a Domaine ", 'content_type':domaine_content_type},#[1][0]
                { 'codename':"modify_domaine", 'name':"Can modify a Domaine ", 'content_type':domaine_content_type},#[1][1]
                { 'codename':"delete_domaine", 'name':"Can delete a Domaine ", 'content_type':domaine_content_type} ,#[1][2]
                { 'codename':"view_domaine", 'name':"Can view a Domaine ", 'content_type':domaine_content_type} ]#[1][3]

    );

    nb_model_permission = len(permissions_vector); 
    print("Nb MOdel Permission : {}".format(nb_model_permission));
    nb_permission_per_model = len(permissions_vector[0]);
    print("Nb Permission Per Model : {}".format(nb_permission_per_model));
    print(permissions_vector[1][1]);

    #Create user
    user_john = None;
    #user_view, user_add, user_modif, user_add_modif, user_delete, user_all = None;
    new_username = 'John';
    if (User.objects.filter(username=new_username).exists()):
        user_john = User.objects.get(username=new_username);
    else:
        user_john = User.objects.create_user(username=new_username, email='john@jn.com', password='pass');

   # user_john.groups.add(group_domaine_view);
    group_domaine_view.user_set.add(user_john);

    #Delete first
    for i in range(nb_model_permission):
        model_permissions = permissions_vector[i];
        for permission_dictionnary in model_permissions:
            #print(permission_dictionnary['codename']);
            code_name = permission_dictionnary['codename'];

            if (Permission.objects.filter(codename=code_name).exists()):
                Permission.objects.get(codename=code_name).delete();

            print("- - -{} Deleted - - -".format(code_name));
        pass;

    """
    #Create later
    for i in range(nb_model_permission):
        model_permissions = permissions_vector[i];
        for permission_dictionnary in model_permissions:
            #print(permission_dictionnary['codename']);
            code_name = permission_dictionnary['codename'];
            name = permission_dictionnary['name'];
            content_type = permission_dictionnary['content_type'];
            new_permission = Permission.objects.create(codename=code_name, name=name, content_type=content_type);
            group_tech.permissions.add(new_permission);
            print("{} created ".format(code_name));
        pass;
    """
    def createAPermission(permission_dictionnary):
        new_code_name = permission_dictionnary['codename'];
        new_name = permission_dictionnary['name'];
        new_content_type = permission_dictionnary['content_type'];
        new_permission = None;
        if (Permission.objects.filter(codename=new_code_name).exists()):
            new_permission = Permission.objects.get(codename=new_code_name);
        else:
            new_permission = Permission.objects.create(codename=new_code_name, name=new_name, content_type=new_content_type);
        return new_permission;

    #group_domaine_view
    group_domaine_view.permissions.add(createAPermission(permissions_vector[1][3])); #domain view

    #group_domaine_add
    group_domaine_add.permissions.add(createAPermission(permissions_vector[1][3])); #domain view
    group_domaine_add.permissions.add(createAPermission(permissions_vector[1][0])); #domain add

    #group_domaine_modif
    group_domaine_modif.permissions.add(createAPermission(permissions_vector[1][3])); #domain view
    group_domaine_modif.permissions.add(createAPermission(permissions_vector[1][1])); #domain modif

    #group_domaine_add_modif
    group_domaine_add_modif.permissions.add(createAPermission(permissions_vector[1][3])); #domain view
    group_domaine_add_modif.permissions.add(createAPermission(permissions_vector[1][1])); #domain modif
    group_domaine_add_modif.permissions.add(createAPermission(permissions_vector[1][0])); #domain add

    #group_domaine_delete
    group_domaine_delete.permissions.add(createAPermission(permissions_vector[1][3])); #domain view
    group_domaine_delete.permissions.add(createAPermission(permissions_vector[1][2])); #domain delete

    #group_domaine_all
    group_domaine_all.permissions.add(createAPermission(permissions_vector[1][3])); #domain view
    group_domaine_all.permissions.add(createAPermission(permissions_vector[1][1])); #domain modif
    group_domaine_all.permissions.add(createAPermission(permissions_vector[1][0])); #domain add
    group_domaine_all.permissions.add(createAPermission(permissions_vector[1][2])); #domain delete

    """
    group_domaine_view
    group_domaine_add
    group_domaine_modif
    group_domaine_add_modif
    group_domaine_delete
    group_domaine_all
    """
    #Create user
    user_all = None;
    #user_view, user_add, user_modif, user_add_modif, user_delete, user_all = None;
    new_username = 'user_all';
    if (User.objects.filter(username=new_username).exists()):
        user_all = User.objects.get(username=new_username);
    else:
        user_all = User.objects.create_user(username=new_username, email='uall@al.com', password='pass');
    
    user_all.groups.add(group_domaine_all);
    print(" - - -UserAll Groups Permissions - - - ");
    print(user_all.get_group_permissions());
    print(" - - - - - - ");

   # user_john.groups.add(group_domaine_view);
   request.session.modified = True;


    print(" - - -User John Groups Permissions - - - ");
    print(user_john.get_group_permissions());
    print(" - - - - - - ");
    user_john_groups = user_john.groups;
    user_john_permissions = Permission.objects.filter(user=user_john);
    print("User");
    print(user_john);
    print(user_john_groups);
    #print(len(user_john_groups));
    print(user_john_permissions);
    print(len(user_john_permissions));
    #print(user_john_permissions[0]);

    """
    permission = Permission.objects.create(
            codename="add_filiere03", name="Can Add a Filiere 03", content_type=filiere_content_type
            );
    group_tech.permissions.add(permission);
    """


#    group_tech.remove();
    
    return HttpResponse(f'createGroupAndUsers!');
