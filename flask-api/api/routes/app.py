from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from ..models import db, User
from .. import login_manager
from flask_login import logout_user

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/', methods = ['GET'])
def index():
    return 'Index'