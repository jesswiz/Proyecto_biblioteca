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


if __name__ == "__main__":
    app.run(debug=True)

