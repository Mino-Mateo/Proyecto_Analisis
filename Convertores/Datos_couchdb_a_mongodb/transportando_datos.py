import pymongo
import couchdb

# Conectarse a MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['Proyecto_analisis']  # Reemplaza 'nombre_de_tu_base_de_datos' con el nombre de tu base de datos en MongoDB
mongo_collection = mongo_db['Bases_datos_json']  # Reemplaza 'nombre_de_tu_coleccion' con el nombre de tu colección en MongoDB

# Conectarse a CouchDB
couch = couchdb.Server('http://admin:admin@localhost:5984')  # Reemplaza la URL y las credenciales de CouchDB si es necesario
couch_db = couch['servidor_principal']  # Reemplaza 'nombre_de_tu_base_de_datos_en_couchdb' con el nombre de tu base de datos en CouchDB

# Obtener los documentos de MongoDB
documents = mongo_collection.find({})  # Puedes agregar una consulta (query) aquí si deseas obtener documentos específicos

# Transferir los documentos a CouchDB
for document in documents:
    # Eliminar la clave '_id' del documento para evitar errores al guardar en CouchDB
    if '_id' in document:
        del document['_id']

    # Agregar el documento a CouchDB
    couch_db.save(document)

# Cerrar las conexiones (opcional, pero buena práctica)
mongo_client.close()
