from flask import Flask, request, jsonify
from db import PgManager
from repositories import UserRepository, CarRepository, RentalRepository

app = Flask(__name__)

db_manager = PgManager(
    db_name  = "Lyfter",
    user     = "postgres",
    password = "josexxx01",
    host     = "localhost"
)

users_repo   = UserRepository(db_manager)
cars_repo    = CarRepository(db_manager)
rentals_repo = RentalRepository(db_manager)

@app.route("/users", methods=["POST"])
def create_user():
    body = request.json
    result = users_repo.create(
        full_name = body["full_name"],
        email     = body["email"],
        username  = body["username"],
        password  = body["password"],
        birthdate = body["birthdate"],
        status    = body["status"]
    )
    if result:
        return jsonify({"message": "Usuario creado exitosamente"}), 201
    return jsonify({"message": "Error creando usuario"}), 500

@app.route("/users", methods=["GET"])
def get_users():
    filters = request.args.to_dict() or None
    result  = users_repo.get_all(filters)
    return jsonify(result), 200

@app.route("/users/<int:id>/status", methods=["PATCH"])
def update_user_status(id):
    body   = request.json
    result = users_repo.update_status(id, body["status"])
    if result:
        return jsonify({"message": "Estado actualizado"}), 200
    return jsonify({"message": "Error actualizando estado"}), 500


@app.route("/users/<int:id>/delinquent", methods=["PATCH"])
def flag_delinquent(id):
    result = users_repo.flag_as_delinquent(id)
    if result:
        return jsonify({"message": "Usuario flaggeado como moroso"}), 200
    return jsonify({"message": "Error flaggeando usuario"}), 500


@app.route("/cars", methods=["POST"])
def create_car():
    body   = request.json
    result = cars_repo.create(
        brand  = body["brand"],
        model  = body["model"],
        year   = body["year"],
        status = body["status"]
    )
    if result:
        return jsonify({"message": "Auto creado exitosamente"}), 201
    return jsonify({"message": "Error creando auto"}), 500


@app.route("/cars", methods=["GET"])
def get_cars():
    filters = request.args.to_dict() or None
    result  = cars_repo.get_all(filters)
    return jsonify(result), 200


@app.route("/cars/<int:id>/status", methods=["PATCH"])
def update_car_status(id):
    body   = request.json
    result = cars_repo.update_status(id, body["status"])
    if result:
        return jsonify({"message": "Estado actualizado"}), 200
    return jsonify({"message": "Error actualizando estado"}), 500


@app.route("/rentals", methods=["POST"])
def create_rental():
    body   = request.json
    result = rentals_repo.create(
        user_id = body["user_id"],
        car_id  = body["car_id"]
    )
    if result:
        return jsonify({"message": "Alquiler creado exitosamente"}), 201
    return jsonify({"message": "Error creando alquiler"}), 500


@app.route("/rentals", methods=["GET"])
def get_rentals():
    filters = request.args.to_dict() or None
    result  = rentals_repo.get_all(filters)
    return jsonify(result), 200


@app.route("/rentals/<int:id>/complete", methods=["PATCH"])
def complete_rental(id):
    body   = request.json
    result = rentals_repo.complete(id, body["car_id"])
    if result:
        return jsonify({"message": "Alquiler completado exitosamente"}), 200
    return jsonify({"message": "Error completando alquiler"}), 500


@app.route("/rentals/<int:id>/status", methods=["PATCH"])
def update_rental_status(id):
    body   = request.json
    result = rentals_repo.update_status(id, body["status"])
    if result:
        return jsonify({"message": "Estado actualizado"}), 200
    return jsonify({"message": "Error actualizando estado"}), 500


if __name__ == "__main__":
    app.run(debug=True)