from flask import Blueprint

main = Blueprint('main', __name__)

from . import user_views, admin_view
