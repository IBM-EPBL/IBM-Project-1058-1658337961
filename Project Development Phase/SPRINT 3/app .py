import uuid
from flask import Flask

instance_id = uuid.uuid4().hex
app = Flask(__name__)


@app.route("/")
def get_instance_id():
    return f"<b style='font-size:30px;color:red;'>Instance ID:crn:v1:bluemix:public:dashdb-for-transactions:eu-gb:a/5303d70427d747c9b8fde97327e3cd78:0115708c-6b18-486d-984e-0b3b10679d21 {instance_id}</b>"



if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")