# coding: utf8
# 尝试
@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def index(): return dict(message="hello from teacher.py")

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def student_manage():
    form = SQLFORM.grid(db.auth_user)
    return dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def course_manage():
    form = SQLFORM.smartgrid(db.course)
    return dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def keshi_manage():
    form = SQLFORM.smartgrid(db.keshi)
    return dict(form=form)   

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def timu_manage():
    form = SQLFORM.smartgrid(db.timu)
    return dict(form=form)      
 
@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def lianxi_manage():
    form = SQLFORM.smartgrid(db.lianxi)
    return dict(form=form)      

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def zuoti_manage():
    form = SQLFORM.smartgrid(db.zuoti)
    return  dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def zuoye_manage():
    form = SQLFORM.smartgrid(db.zuoye)
    return  dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def defen_manage():
    form = SQLFORM.smartgrid(db.defen)
    return  dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def wangpan_manage():
    form = SQLFORM.smartgrid(db.wangpan)
    return  dict(form=form)
