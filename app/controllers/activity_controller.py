__author__ = 'zhaojm'

from flask import Blueprint, render_template, request, redirect, url_for, current_app

from app.models import Activity
from app.database import db_session


activity_controller = Blueprint('activity_controller', __name__, url_prefix='/activity')

@activity_controller.route('/')
def list():
    cur = Activity.query.all()
    # activites = cur
    activites = []
    for c in cur:
        a = {}
        a['id'] = c.id
        a['title'] = c.title
        a['description'] = c.description
        activites.append(a)
    # print(activites)

    current_app.logger.debug("current_app log")


    return render_template('activity/list.html', activites=activites)

@activity_controller.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        a = Activity(request.form['title'], request.form['description'])
        db_session.add(a)
        db_session.commit()
        return redirect(url_for('.detail', id=a.id))
    else:
        return render_template('activity/post.html')

@activity_controller.route('/delete/<id>')
def delete(id):
    Activity.query.filter(Activity.id==id).delete()
    return redirect(url_for('.list'))

@activity_controller.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    activity = Activity.query.filter(Activity.id==id).first()
    if request.method == 'POST':
        db_session.query(Activity).filter(Activity.id==id).update({'title': request.form['title'], 'description': request.form['description']})
        # activity.update({'title': request.form['title'], 'description': request.form['description']})
        db_session.commit()
        return redirect(url_for('.detail', id=id))

    else:
        a = {}
        a['id'] = activity.id
        a['title'] = activity.title
        a['description'] = activity.description

        return render_template('activity/edit.html', activity=a)

@activity_controller.route('/detail/<id>')
def detail(id):
    activity = Activity.query.filter(Activity.id==id).first()

    a = {}
    a['id'] = activity.id
    a['title'] = activity.title
    a['description'] = activity.description

    return render_template('activity/detail.html', activity=a)