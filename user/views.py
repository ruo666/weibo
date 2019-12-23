from flask import Blueprint
from flask import request
from flask import render_template
from models import  User

user_bp=Blueprint('user',__name__)
user_bp.template_folder = './templates'
user_bp.static_folder = './static'


@user_bp.route('/')
def home():
	return render_template('base.html')



@user_bp.route('/register',methods=['GET','POST'])
def register():
	if request.method=='GET':
		return render_template('')
	else:
		return render_template('')


@user_bp.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('')
	else:
		return render_template('')


@user_bp.route('/show',methods=['GET','POST'])
def show():
	if request.method=='GET':
		return render_template('')
	else:
		return render_template('')

@user_bp.route('/post',methods=['GET','POST'])
def post():
	if request.method=='GET':
		return render_template('')
	else:
		return render_template('')


