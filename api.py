from flask import Flask, request, jsonify
import json

app = Flask(__name__) #Se almacena Flask

DATA_FILE = 'tareas.json'

def load_tareas():#cargar tareas 
    try:
        with open(DATA_FILE,'r',encoding='utf-8') as f: #abre el archivo en modo de lectura
            return json.load(f) #esto pasa el archivo json a una lista de python para poder usarlos en los except mas adelante
        
    except FileNotFoundError: #archivo no encontradp
        return[]
    except json.JSONDecodeError: #archivo mal formateado
        return[]
    
def save_tareas(tareas):
    with open(DATA_FILE,'w',encoding='utf-8') as f:
        json.dump(tareas,f)#convierte la lista de python en JSON y la escribe en el archivo


#ENPOINTS DEL API DE API
#ENDPOINT DE LEER/OBTENER NOTAS
@app.route('/tareas',methods=['GET'])
def get_tareas():
    tareas=load_tareas()
    status_filter=request.args.get('status')
    if status_filter:
        tareas=[n for n in tareas if n.get('status') == status_filter] #voy a scambiar este for por algo mas sencillo 
    return jsonify(tareas),200 #codigo de exito


#Endpoint de creacion de tareas
@app.route('/tareas',methods=['POST'])
def create_tareas():
    data=request.get_json()
    if not data:
        return jsonify({'error': 'JSON invalido o body vacio'}),400

#se empizan las validaciones [id, titulo, descripcion, estado]

    if 'id'not in data:
        return jsonify({'error':'Falta el identificador (id)'}),400
    if 'titulo'not in data or not str(data.get('titulo')).strip():
        return jsonify({'Error': 'Falta el titulo'})
    if 'descripcion' not in data or not str(data.get('descripcion')).strip():
        return jsonify({'Error': "Falta agregar la descripcion"}),400
    allowed_statuses =['por hacer', 'en progreso', 'completada']
    if 'status' not in data or data.get('status') not in allowed_statuses:
        return jsonify({'Error': f"Estado invalido. Valores permitidos: {allowed_statuses}"}),400
    tareas =load_tareas()
    if any(n.get('id')== data['id'] for n in tareas):
        return jsonify({'Error': 'ID ya existente'}),400
    
    tareas.append({
        'id':data['id'],
        'titulo':data['titulo'],
        'descripcion':data['descripcion'],
        'status':data['status']
    })
    save_tareas(tareas)
    return jsonify({'Mensjae': 'Nota creada con exito'}),201

@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def update_tarea(tarea_id):
    data = request.get_json()
    if not data:
        return jsonify({'Error': 'JSON vacío o inválido'}), 400

    tareas = load_tareas()
    allowed_statuses = ['por hacer', 'en progreso', 'completada']

    for tarea in tareas:
        if tarea['id'] == tarea_id:
            if 'status' in data and data['status'] not in allowed_statuses:
                return jsonify({'Error': f"Estado inválido. Valores permitidos: {allowed_statuses}"}), 400

            # Actualizar solo los campos que vienen
            if 'titulo' in data:
                tarea['titulo'] = data['titulo']
            if 'descripcion' in data:
                tarea['descripcion'] = data['descripcion']
            if 'status' in data:
                tarea['status'] = data['status']

            save_tareas(tareas)
            return jsonify({'Mensaje': 'Tarea actualizada', 'tarea': tarea}), 200

    return jsonify({'Error': 'Tarea no encontrada'}), 404

#Enpoint para eliminar la tarea
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def delete_tarea(tarea_id):
    tareas = load_tareas()

    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tareas.remove(tarea)
            save_tareas(tareas)
            return jsonify({'Mensaje': 'Tarea eliminada correctamente'}), 200

    return jsonify({'Error': 'Tarea no encontrada'}), 404

    
if __name__ == '__main__':
    app.run(host='localhost',debug=True)