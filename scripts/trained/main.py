from model import Plant_Disease_Model
import torchvision.transforms as transforms
import torch
from urllib import request
from PIL import Image
import firebase_admin
from firebase_admin import db

transform = transforms.Compose(
    [transforms.Resize(size=128),
     transforms.ToTensor()])

cred_object = firebase_admin.credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred_object, {
	    'apiKey': "AIzaSyAUVkAhNCBmKf0KQYiKf_Ow7eN5kDc8ZKA",
        'authDomain': "plantdiseasedetection-83796.firebaseapp.com",
        'databaseURL': "https://plantdiseasedetection-83796-default-rtdb.firebaseio.com",
        'projectId': "plantdiseasedetection-83796",
        'storageBucket': "plantdiseasedetection-83796.appspot.com",
        'messagingSenderId': "276736650865",
        'appId': "1:276736650865:web:92faee319c78b7a35df5d0"
	})

labels = [('Apple','Scab'),('Apple','Black Rot'), ('Apple','Cedar Apple Rust'),('Apple',''),('Blueberry',''),
    ('Cherry','Powdery Mildew'),('Cherry',''),('Corn','Cercospora /Grey Leaf Spot'),
    ('Corn','Common Rust'),('Corn','Northern Leaf Blight'),('Corn',''), ('Grape','Black Rot'),('Grape','Esca'),
    ('Grape','Leaf Blight'), ('Grape',''), ('Orange','Haunglongbing'), ('Peach','Bacterial Spot'), ('Peach',''),
    ('Pepper','Bacterial Spot'),('Pepper',''),('Potato','Early Blight'),('Potato','Late Blight'),
    ('Potato',''),('Raspberry',''),('Soybean',''),('Squash','Powdery Mildew'),('Strawberry','Leaf Scorch'),
    ('Strawberry',''),('Tomato','Bacterial Spot',''),('Tomato','Early Blight'),('Tomato','Late Blight'),
    ('Tomato','Leaf Mould'),('Tomato','Septoria Leaf Spot'),('Tomato','Spider Mites'),('Tomato','Target Spot'),
    ('Tomato','Yellow Leaf Curl Virus'),('Tomato','Mosaic Virus'),('Tomato','')]

def ignore_first_call(fn):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            return fn(*args, **kwargs)
        else:
            called = True
            return None
    return wrapper

def processImage(post_id,url):
    url_response = request.urlopen(url)
    img_pil = Image.open(url_response)
    tensor = transform(img_pil)
    xb = tensor.unsqueeze(0)
    yb = model(xb)
    _, preds = torch.max(yb, dim=1)
    result = labels[preds[0].item()]
    db_ref.child(post_id).update({"status": 2,'plant':result[0],'disease':result[1]})

@ignore_first_call
def plantDiseaseDetectionListener(message):
    try:
        if(message is not None and type(message.data) == dict and "url" in message.data.keys()):
            post_id = message.path.split("/")[-1].strip()
            url = message.data["url"].strip()
            print("\nPOST ID: ",post_id)
            print("URL: ",url)
            processImage(post_id,url) 
    except Exception as e:
        print("Handled exception for event")
        print(e)

if __name__ == '__main__':
    model = Plant_Disease_Model()
    model.load_state_dict(torch.load('./plantDisease-resnet34.pth', map_location=torch.device('cpu')))
    model.eval()
    db_ref = db.reference('/plant-images')
    db_ref.listen(plantDiseaseDetectionListener)
