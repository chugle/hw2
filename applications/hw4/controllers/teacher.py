# coding: utf8
# 尝试
import datetime
now=datetime.date.today()
year=now.year
month=now.month
jie = auth.user.jie   
if int(month) in range(2,8):
    xueqi=2
    nianji=int(year)-2000-int(jie)+4
    xuenian=str(int(year)-1-2000)
else:
    xueqi=1
    nianji=int(year)-2000-int(jie)+3
    xuenian=str(int(year)-2000)


@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def index(): return dict()

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
    form = SQLFORM.smartgrid(db.keshi,
                             constraints={db.keshi:(db.keshi.xuenian==xuenian)&(db.keshi.xueqi==xueqi)},
                             links=[dict(header='',body=lambda row:A('批改作业',_href=URL('pigai',args=row.id)))])
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

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def pigai():
    keshi_id=request.args[0]
    row=db((db.zuoye.keshi==keshi_id)&(db.zuoye.defen==None)).select().first()
    if row:
        form=SQLFORM(db.zuoye,row.id,upload=URL('download'))
        vals=None
        if form.process().accepted:
            vals=response.url
            redirect(request.url)

        return dict(form=form,vals=vals)
    else:
        return dict(error=H3('没有可以批改的作业'))
    
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)