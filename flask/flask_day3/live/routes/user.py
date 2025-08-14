from flask import blueprints, render_template, Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


#라우터정의
@user_bp.route('/<username>')
def profile(username):
    return render_template('username.html',username=username)