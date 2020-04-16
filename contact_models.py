import pyrebase


class Contact():
    
    def GuardarGenerador(self,name,lastname,phone,email,password):
        config = {
            "apiKey": "AIzaSyD9piMgrWxDzmjDzKiFuITa1VnCw3D-Oko",
            "authDomain": "recytech-de6d5.firebaseapp.com",
            "databaseURL": "https://recytech-de6d5.firebaseio.com",
            "projectId": "recytech-de6d5",
            "storageBucket": "recytech-de6d5.appspot.com",
            "messagingSenderId": "977394626490",
            "appId": "1:977394626490:web:df434ab45173d5f05f7783",
            "measurementId": "G-MB6N22C296"
        }
        firebase = pyrebase.initialize_app(config)
    
        data = {"name":name,
                "lastname": lastname,
                "phone": phone,
                "email": email,
                "password":password
                }
        db = firebase.database()
        db.child("generator").push(data)


    def GuardarRecolector(self,name,lastname,phone,email,password):
        config = {
            "apiKey": "AIzaSyD9piMgrWxDzmjDzKiFuITa1VnCw3D-Oko",
            "authDomain": "recytech-de6d5.firebaseapp.com",
            "databaseURL": "https://recytech-de6d5.firebaseio.com",
            "projectId": "recytech-de6d5",
            "storageBucket": "recytech-de6d5.appspot.com",
            "messagingSenderId": "977394626490",
            "appId": "1:977394626490:web:df434ab45173d5f05f7783",
            "measurementId": "G-MB6N22C296"
        }
        firebase = pyrebase.initialize_app(config)
    
        data = {"name":name,
                "lastname": lastname,
                "phone": phone,
                "email": email,
                "password":password
                }
        db = firebase.database()
        db.child("collector").push(data)


    def Get(self):
        config = {
            "apiKey": "AIzaSyD9piMgrWxDzmjDzKiFuITa1VnCw3D-Oko",
            "authDomain": "recytech-de6d5.firebaseapp.com",
            "databaseURL": "https://recytech-de6d5.firebaseio.com",
            "projectId": "recytech-de6d5",
            "storageBucket": "recytech-de6d5.appspot.com",
            "messagingSenderId": "977394626490",
            "appId": "1:977394626490:web:df434ab45173d5f05f7783",
            "measurementId": "G-MB6N22C296"
        }
        firebase = pyrebase.initialize_app(config)
    
        db = firebase.database()
        all_users = db.child("generator").get()
        lista = ["lista de generadores"]
        print(lista)
        for user in all_users.each():
            a= user.val()
            for key,val in a.items():
                lista.append(val)

        print(lista)
            

if __name__ == "__main__":
    objeto = Contact()
    objeto.Get()
