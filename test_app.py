from app import app 

def test_home():
    response= app.test_client().get("/")

    assert response.status_code ==200
    assert response.data == b"This is Ansar from IIITK and the Reg.no is 2024PHD21006"