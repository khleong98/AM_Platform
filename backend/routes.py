from flask import Blueprint, jsonify, request

from models import User
from utils import generate_referral_tree


blueprint = Blueprint('main', __name__)

@blueprint.route('/email', methods=['GET'])
def email():
    email_option = [i.email for i in User.query.order_by(User.email.asc()).all()]
    if email_option:
        return jsonify({'email': email_option}), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'error': 'No available email.'}), 404, {'ContentType': 'application/json'}

@blueprint.route('/referral', methods=['GET'])
def referral():
    email_input = request.args.get('email')
    referral_tree = generate_referral_tree(email_input) if email_input else {}
    return jsonify({'referral': referral_tree}), 200, {'ContentType': 'application/json'}

@blueprint.route('/detail', methods=['POST'])
def detail():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    user_detail = {i.name: getattr(user, i.name) for i in user.__table__.columns if (i.name != 'email' and i.name != 'referrer_id')}
    return jsonify({'detail': user_detail}), 200, {'ContentType': 'application/json'}

@blueprint.route('/api/detail', methods=['POST'])
def detail_api():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        user_detail = {i.name: getattr(user, i.name) for i in user.__table__.columns if (i.name != 'email' and i.name != 'referrer_id')}
        return jsonify(user_detail), 200
    else:
        return jsonify({'error': 'Invalid email.'}), 404