from flask import Flask, jsonify, request

app = Flask(__name__)


# repositorio temporal de datos
#esto no representa persistencia de datos

libros = {
    101: {
        "id": 101, "titulo": "Clean Code", "Autor": "Robert C. Martin", "disponible": True},
         102: {
        "id": 102, "titulo": "Python Crash", "Autor": "Erick Matthes", "disponible": True},
         103: {
        "id": 103, "titulo": "Architecture patterns", "Autor": "GoF", "disponible": False},
}
@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "API REST de Biblioteca Universitaria",
            "version": "1.0",
            "endpoints": [
                "GET/libros", #Muestra todos los libros
                "GET /libros/<id>", #Informacion de un libro
                "POST /libros", # Crear un libro
                "PUT /libros/<id>", #Modificar la disponibilidad
                "DELETE /libros/<id>" #Borrar un libro
            ]
        }
    )
@app.get("/libros")
def obtener_libros():
    return jsonify(list(libros.values()))


@app.get("/libros/<int:id>")
def obtener_libro(id):
    libro = libros.get(id)

    if libro:
        return jsonify(libro)
    
    return jsonify({"error": "Libro no encontrado"}), 404

@app.post("/libros")
def agregar_libro():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion"}), 400
    if "titulo" not in datos or "autor" not in datos or "disponible" not in datos:
        return jsonify({"error": "Los campos son requeridos"}), 400
    
    nuevo_id = max(libros.key())+1

    libros[nuevo_id] = {
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "disponible": datos["disponible"]
    }

    return jsonify({libros[nuevo_id]}), 201


if __name__ == "__main__":
    app.run(debug=True)

