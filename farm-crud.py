from flask import jsonify, redirect
from models import db, Farm

def error(err_locale, error):
    print("ERROR in", err_locale, ":", error)
    return jsonify(error='Server Error')

def get_all_farms():
    try: 
        all_farms = Farm.query.all()
        results = [farm.as_dict() for farm in all_farms]
        return jsonify(results)
    except Exception as error:
        return error('getting all farms', error)

def get_farm(id):
    try: 
        farm = Farm.query.get(id)
        if farm:
            return jsonify(farm.as_dict())
        else:
            raise Exception('Error in getting one farm', id)
    except Exception as error:
        return error('getting one farm', error)

def create_farm(name, city):
    try: 
        new_farm = Farm(name=name, city=city)
        db.session.add(new_farm)
        db.session.commit()
        return jsonify(new_farm.as_dict())
    except Exception as error:
        return error('creating a farm', error)

def update_farm(id, name, city):
    try:
        farm = Farm.query.get(id)
        if farm:
            farm.city = city or farm.city
            farm.name = name or farm.name
            db.session.commit()
            return jsonify(farm.as_dict())
        else:
            return error('updating a farm', error)


def destroy_farm(id):
    try:
        farm = Farm.query.get(id)
        db.session.delete(farm)
        db.session.commit()
        return redirect('/farms')
    except Exception as error: 
        return error('deleting a farm', error)