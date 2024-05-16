from models import Referral, User


def generate_referral_tree(referrer_email):
    referral_tree = {referrer_email: []}
    referral = Referral.query.filter_by(referrer_id=User.query.filter_by(email=referrer_email).first().id).all()
    
    for referree in referral:
        referree_email = User.query.filter_by(id=referree.referree_id).first().email
        referral_tree[referrer_email].append(generate_referral_tree(referree_email))
    
    return referral_tree