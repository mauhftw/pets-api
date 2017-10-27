from flask import Flask, jsonify, request
from flask_restful import reqparse
from flask_jwt import JWT, jwt_required, current_identity
from models.pet import Pet
from security import authenticate, identity 
import database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

jwt = JWT(app, authenticate, identity)

#GET /hello
@app.route("/hello")
def hello():
    return "hello world!"


#GET /pet
@app.route("/pet")
@jwt_required()
def get_pets():

	pets = Pet.all()
	if pets is None:
		return jsonify({'message': 'there aren\'t pets stored'}),404
	return pets.to_json()

#GET /pet/{id}
@app.route("/pet/<int:id>")
@jwt_required()
def get_pet(id):

	pet = Pet.find(id)
	if pet is None:
		return jsonify({'message': 'pet is not present'}),404
	return pet.to_json()

#POST /pet
@app.route("/pet", methods=['POST'])
@jwt_required()
def store_pet():
	#check = reqparse.RequestParser()	#checks are missing
	data = request.get_json()
	pet = Pet()

	exists = Pet.where('name','=',data['name'])
	if exists.__getattr__ is None:
		return jsonify({'message': 'pet is already stored'}),404

	pet.name = data['name']
	pet.type = data['type']
	pet.age = data['age']
	pet.specie = data['specie']
	if pet.save():
		return jsonify(data)
	return jsonify({'message': 'oops! something went wrong'}),500


#PATCH /pet/{id}
@app.route("/pet/<int:id>", methods=['PATCH'])
@jwt_required()
def update_pet(id):
	#check = reqparse.RequestParser()	#checks are missing
	data = request.get_json()
	pet = Pet.find(id)

	if pet is None:
		return jsonify({'message': 'pet doesn\'t exist'}),404

	pet.name = data['name']
	pet.type = data['type']
	pet.age = data['age']
	pet.specie = data['specie']
	if pet.update():
		return jsonify({'message': 'pet has been successfully updated'}),200
	return jsonify({'message': 'oops! something went wrong'}),500


#DELETE /pet/{id}
@app.route("/pet/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_pet(id):

	pet = Pet.find(id)
	if pet is None:
		return jsonify({'message': 'pet doesn\'t exist'}),404

	if pet.delete():
		return jsonify({'message': 'pet has been successfully deleted'}),200
	return jsonify({'message': 'oops! something went wrong'}),500


#app.run(host='0.0.0.0',port=5000)
