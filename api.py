from models import app, Farm, Food, Season, get_or_create
from flask import jsonify, request
# from farm_crud import get_all_farms, get_farm, create_farm, update_farm, destroy_farm

@app.errorhandler(Exception)
def unhandled_exception(e):
  app.logger.error('Unhandled Exception: %s', (e))
  message_str = e.__str__()
  return jsonify(message=message_str.split(':')[0])

@app.route('/farms', methods=['GET', 'POST'])
def farm_index_create():
    if request.method == 'GET':
        return get_all_farms()
    if request.method == 'POST':
        return create_farm(
            name=request.form['name'],
            city=request.form['city']
        )

@app.route('/farms/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def farm_show_update_delete(id):
    if request.method == 'GET':
        return get_farm(id)
    if request.method == 'PUT':
        return update_user(
            id=id,
            name=request.form['name'],
            city=request.form['city']
        )
    if request.method == 'DELETE':
        return destroy_user(id)