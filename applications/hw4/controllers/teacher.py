# coding: utf8
# 尝试
@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def index(): return dict(message="hello from teacher.py")

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def student_manage():
    form = SQLFORM.grid(db.auth_user)
    return dict(form=form)

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def course_manage():
    form = SQLFORM.smartgrid(db.course)
    return dict(form=form)

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def keshi_manage():
    form = SQLFORM.smartgrid(db.keshi)
    return dict(form=form)   

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def timu_manage():
    form = SQLFORM.smartgrid(db.timu)
    return dict(form=form)      
 
@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def lianxi_manage():
    form = SQLFORM.smartgrid(db.lianxi)
    return dict(form=form)      

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def zuoti_manage():
    form = SQLFORM.smartgrid(db.zuoti)
    return  dict(form=form)

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def zuoye_manage():
    form = SQLFORM.smartgrid(db.zuoye)
    return  dict(form=form)

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def defen_manage():
    form = SQLFORM.smartgrid(db.defen)
    return  dict(form=form)

@auth.requires(auth.user_id==5 or request.client=='127.0.0.1', requires_login=True)
def wangpan_manage():
    form = SQLFORM.smartgrid(db.wangpan)
    return  dict(form=form)
