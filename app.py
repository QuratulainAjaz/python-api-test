from flask import Flask, request, jsonify

app = Flask(__name__)


guestbook = {}
current_id = 1  


#GET all names
@app.route("/names", methods=["GET"])
def get_names():
    return jsonify(guestbook), 200


#POST add new name
@app.route("/add-name", methods=["POST"])
def add_name():
    global current_id
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    guestbook[current_id] = data["name"]
    response = {
        "id": current_id,
        "name": data["name"]
    }

    current_id += 1
    return jsonify(response), 201  # 201 Created


#DELETE name by ID
@app.route("/delete-name/<int:name_id>", methods=["DELETE"])
def delete_name(name_id):
    if name_id not in guestbook:
        return jsonify({"error": "Name ID not found"}), 404

    deleted_name = guestbook.pop(name_id)
    return jsonify({
        "message": "Deleted successfully",
        "deleted": deleted_name
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

