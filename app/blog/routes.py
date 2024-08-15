"""Blog routes."""
from flask import render_template

from app.blog import bp


@bp.route('/blog-one')
def blog_one():
    return render_template('blog/blog_one.html')


@bp.route('/blog-two')
def blog_two():
    return render_template('blog/blog_two.html')


@bp.route('/everyday-makeup')
def blog_everyday():
    return render_template('blog/blog_everyday.html')

@bp.route('/evening-makeup')
def blog_evening():
    return render_template('blog/blog_evening.html')


@bp.route('/lifting-makeup')
def blog_lifting():
    return render_template('blog/blog_lifting.html')


@bp.route('/bridal-makeup')
def blog_bridal():
    return render_template('blog/blog_bridal.html')


@bp.route('/photoshoot')
def blog_photoshoot():
    return render_template('blog/blog_photoshoot.html')


@bp.route('/publications-journals')
def blog_magazines():
    return render_template('blog/blog_magazines.html')
