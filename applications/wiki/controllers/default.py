# -*- coding: utf-8 -*-
def index():
     """ this controller returns a dictionary rendered by the view
         it lists all wiki pages
     >>> index().has_key('pages')
     True
     """
     pages = db().select(db.page.id,db.page.title,orderby=db.page.title)
     return dict(pages=pages)

@auth.requires_login()
def create():
     "creates a new empty wiki page"
     form = crud.create(db.page, next=URL('index'))
     return dict(form=form)
     
     
from gluon.contrib.markdown import WIKI
def show():
     "shows a wiki page"
     this_page = db.page(request.args(0)) or redirect(URL('index'))
     db.comment.page_id.default = this_page.id
     form = crud.create(db.comment) if auth.user else None
     pagecomments = db(db.comment.page_id==this_page.id).select()
     return dict(page=this_page, comments=pagecomments, form=form)

@auth.requires_login()
def edit():
     "edit an existing wiki page"
     this_page = db.page(request.args(0)) or redirect(URL('index'))
     form = crud.update(db.page, this_page,
                        next=URL('show',args=request.args))
     return dict(form=form)

@auth.requires_login()
def documents():
     "browser, edit all documents attached to a certain page"
     page = db.page(request.args(0)) or redirect(URL('index'))
     db.document.page_id.default = page.id
     db.document.page_id.writable = False
     grid = SQLFORM.grid(db.document.page_id==page.id,args=[page.id])
     return dict(page=page, grid=grid)

def user():
     return dict(form=auth())

def download():
     "allows downloading of documents"
     return response.download(request, db)

def search():
     "an ajax wiki search page"
     return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
              _onkeyup="ajax('callback', ['keyword'], 'target');")),
              target_div=DIV(_id='target'))

def callback():
     "an ajax callback that returns a <ul> of links to wiki pages"
     query = db.page.title.contains(request.vars.keyword)
     pages = db(query).select(orderby=db.page.title)
     links = [A(p.title, _href=URL('show',args=p.id)) for p in pages]
     return UL(*links)


def news():
    "generates rss feed form the wiki pages"
    reponse.generic_patterns = ['.rss']
    pages = db().select(db.page.ALL, orderby=db.page.title)
    return dict(
       title = 'mywiki rss feed',
       link = 'http://127.0.0.1:8000/mywiki/default/index',
       description = 'mywiki news',
       created_on = request.now,
       items = [
          dict(title = row.title,
               link = URL('show', args=row.id),
               description = MARKMIN(row.body).xml(),
               created_on = row.created_on
               ) for row in pages])
