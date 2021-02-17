from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return render_template(
        'errors/404.html'), 404  # default status quo in flask is 200 so need 404 as second return value


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html'), 500

# we dnt use errorhandler instead of app_errorhandler because we want our handlers to work across our entire app, not just this blueprint
