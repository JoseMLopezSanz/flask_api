from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "A store with name {} already existis".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store"}, 500

        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {"message": "An error occurred while deleting the store"}, 500

        return {"message": "Store {} has been deleted".format(name)}

class StoreList(Resource):
    def get(self):
        return {"message": [x.json() for x in StoreModel.query.all()]}
