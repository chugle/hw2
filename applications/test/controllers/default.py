# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
from html import FORM, TEXTAREA
from http import redirect

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    row=db(content.html).select().last()
    form=FORM('html',TEXTAREA(row.html,_id="textarea_id",_name="content" ,_style="width:700px;height:300px;"),
              INPUT(_type='submit'),
              next=URL('default','index'))
    if form.process().accepted:
        session.flash = form.vars
        content.insert(html= form.vars['content'])
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form,req=form.vars)


def upload_json():
    path=os.path.join(request.folder,'static','images')
    f=request.vars['imgFile']
    if hasattr(f, 'file'):
        (source_file, original_filename) = (f.file, f.filename)
    elif isinstance(f, (str, unicode)):
        ### do not know why this happens, it should not
        (source_file, original_filename) = \
            (cStringIO.StringIO(f), 'file.txt')
    id=db.title.insert(weizhi=db.title.weizhi.store(source_file, original_filename))
    #newfilename = field.store(source_file, original_filename,
    #                         field.uploadfolder)
    # this line was for backward compatibility but problematic
    # self.vars['%s_newfilename' % fieldname] = newfilename
    url='http://localhost:8000/test/static/images/'+str(db.title[id].weizhi)
    return dict(url=url,error=0)

def file_manager_json():
    return dect(request=request)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
