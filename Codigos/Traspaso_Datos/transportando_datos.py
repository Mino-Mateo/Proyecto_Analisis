import pymongo
import couchdb

# Estableciendo conexion con Mongodb
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['Proyecto_analisis']  
mongo_collection = mongo_db['Bases_datos_json']  

# Estableciendo conexion con Couchdb 
couch = couchdb.Server('http://admin:admin@localhost:5984')  # Modificando el url y agregando nuestras credenciales
couch_db = couch['servidor_principal']

# Exportando los datos de Mongodb
documents = mongo_collection.find({})  

# Tranfireindo los documentos a CouchDB
for document in documents:
    # Ya que en Mongodb nos crea un id, este debemos borrarla para que no nos cree ningun problema en Couchdb
    if '_id' in document:
        del document['_id']

    # Agregar el documento a CouchDB
    couch_db.save(document)


mongo_client.close()
