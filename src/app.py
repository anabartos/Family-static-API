"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
   
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    if member is not None:
        return jsonify({
            "id": member.get("id"),
            "name": member.get("name"),
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers")
        }), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 404

@app.route('/member', methods=['POST'])
def add_member():

    # this is how you can use the Family datastructure by calling its methods
    member = request.json
    jackson_family.add_member(member)
    return jsonify({"message": "Miembro añadido correctamente", "member": member}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    return jsonify({"done": True, "message": "Miembro con ID {id} eliminado correctamente"}), 200
    # this is how you can use the Family datastructure by calling its methods
    # if jackson_family.get_member(id):
    #     jackson_family.delete_member(id)
    #     return jsonify({"done": True, "message": "Miembro con ID {id} eliminado correctamente"}), 200
    # else:
    #     return jsonify({"done": False, "error": "Miembro no encontrado"}), 404









        

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

