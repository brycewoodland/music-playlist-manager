import firebase_admin
from firebase_admin import credentials, firestore

# Application Default Credentials 
cred = credentials.Certificate('service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_test_data():
    doc_ref = db.collection('testCollection').document('testDoc')
    doc_ref.set({
        'name': 'Test User',
        'age': 25,
        'email': 'testuser@example.com'
    })
    print('Data added successfully')

def get_test_data():
    doc_ref = db.collection('testCollection').document('testDoc')
    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
    else:
        print('No such document!')

add_test_data()
get_test_data()
