# coding: utf8
if False:
    from gluon import *
    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    from gluon import *
    from db import *  #repeat for all models
    from menu import *
# 尝试
import datetime
now=datetime.date.today()
year=now.year
month=now.month
if int(month) in range(2,8):
    xueqi=2
    xuenian=str(int(year)-1-2000)
elif int(month)==1:
    xueqi=1
    xuenian=str(int(year)-1-2000)
else:
    xueqi=1
    xuenian=str(int(year)-2000)


@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def index(): return dict()

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def student_manage():
    form = SQLFORM.grid(db.auth_user)
    return dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)

def course_manage():
    form = SQLFORM.smartgrid(db.course,
            links=[dict(header='',body=lambda row:A('图文编辑',_href=URL('course_edit',args=row.id)))])
    return dict(form=form)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def keshi_manage():
    form = SQLFORM.smartgrid(db.keshi,
                             constraints={'keshi':(db.keshi.xuenian==xuenian)&(db.keshi.xueqi==xueqi)},
                             links=[dict(header='',body=lambda row:A('批改作业',_href=URL('pigai',args=row.id))),
                                    dict(header='',body=lambda row:A('添加练习',_href=URL('addwenti',args=row.id)))])
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

    

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def grade2():
    lastxs=db().select(db.zuoye.zuozhe).last().zuozhe
    banji=db.auth_user[lastxs].banji
    if len(request.args):
        banji=request.args[0]
    rows=db((db.keshi.xuenian==xuenian)&(db.keshi.xueqi==xueqi)&(db.keshi.nianji==2)).select(left=db.keshi.on(db.keshi.kecheng==db.course.id))
    return dict(rows=rows,banji=banji)

@auth.requires(request.client=='127.0.0.1' or auth.has_membership(role='teacher') , requires_login=False)
def grade1():
    lastxs=db().select(db.zuoye.zuozhe).last().zuozhe
    banji=db.auth_user[lastxs].banji
    if len(request.args):
        banji=request.args[0]
    rows=db((db.keshi.xuenian==xuenian)&(db.keshi.xueqi==xueqi)&(db.keshi.nianji==1)).select(left=db.keshi.on(db.keshi.kecheng==db.course.id))
    return dict(rows=rows,banji=banji)


def homeworks2():
    keshi_id=request.args[0]
    if month in range(1,8):
        jie2=int(year)+1-2000
    else:
        jie2=int(year)+2-2000
    banji=request.args[1]
    
    rows=db((db.auth_user.banji==banji)&
                (db.auth_user.jie==jie2)).select(
                                    db.auth_user.last_name,
                                    db.auth_user.first_name,
                                    db.zuoye.ALL,left=db.zuoye.on((db.auth_user.id==db.zuoye.zuozhe)&(db.zuoye.keshi==keshi_id)),
                                    orderby=db.auth_user.last_name)
    return dict(rows=rows,banji=banji)

def homeworksterm2():
    if month in range(1,8):
        jie2=int(year)+1-2000
    else:
        jie2=int(year)+2-2000
    
    rows=db((db.zuoye.keshi==db.keshi.id)& (db.zuoye.zuozhe==db.auth_user.id)& (db.keshi.xuenian==xuenian) & (db.keshi.xueqi==xueqi)&
                (db.auth_user.jie==jie2)).select(
                                    db.auth_user.banji,
                                    db.auth_user.last_name,
                                    db.auth_user.first_name,
                                    db.keshi.kecheng,
                                    db.zuoye.keshi,
                                    db.zuoye.wenjian,
                                    db.zuoye.defen,
                                    orderby=db.auth_user.banji|db.auth_user.last_name)
    return dict(rows=rows)

def homeworksterm1():
    if month in range(1,8):
        jie1=int(year)+2-2000
    else:
        jie1=int(year)+3-2000

    
    rows=db((db.zuoye.keshi==db.keshi.id)& (db.zuoye.zuozhe==db.auth_user.id)& (db.keshi.xuenian==xuenian) & (db.keshi.xueqi==xueqi)&
                (db.auth_user.jie==jie1)).select(
                                    db.auth_user.banji,
                                    db.auth_user.last_name,
                                    db.auth_user.first_name,
                                    db.keshi.kecheng,
                                    db.zuoye.keshi,
                                    db.zuoye.wenjian,
                                    db.zuoye.defen,
                                    orderby=db.auth_user.banji|db.auth_user.last_name)
    return dict(rows=rows)


def homeworks1():
    keshi_id=request.args[0]
    if month in range(1,8):
        jie1=int(year)+2-2000
    else:
        jie1=int(year)+3-2000
    banji=request.args[1]
    
    rows=db((db.auth_user.banji==banji)&
                (db.auth_user.jie==jie1)).select(
                                    db.auth_user.last_name,
                                    db.auth_user.first_name,
                                    db.zuoye.ALL,left=db.zuoye.on((db.auth_user.id==db.zuoye.zuozhe)&(db.zuoye.keshi==keshi_id)),
                                    orderby=db.auth_user.last_name)
    return dict(rows=rows,banji=banji)


def addwenti():
    keshi_id=request.args[0]
    keshi=db.keshi[keshi_id]
    course=keshi.kecheng
    timus=db(db.timu.course==course).select()
    for timu in timus:
        db.lianxi.update_or_insert(
                                   (db.lianxi.keshi==keshi_id)&
                                   (db.lianxi.timu==timu),
                                   keshi=keshi_id,
                                   timu=timu
                                   )
    lianxis=db(db.lianxi.keshi==keshi_id).select()
    return dict(timus=timus,lianxis=lianxis)
    
     
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

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
    url='http://'+request.env.http_host+'/'+request.application+'/static/images/'+str(db.title[id].weizhi)
    print url
    return dict(url=url,error=0)

def course_edit():
    course_id=request.args[0]
    row=db.course[course_id]
    form=FORM('edit',TEXTAREA(row.neirong,_id="textarea_id",_name="content" ,_style="width:700px;height:300px;"),
              INPUT(_type='submit'),
              next=URL('teacher','course_manage'))
    if form.process().accepted:
        response.write(form.vars)
        row.update_record(neirong= form.vars['content'])
        redirect(URL('teacher','course_manage'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form,req=form.vars)