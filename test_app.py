from app import register_user

def test_register_user():
    assert register_user("Nidhi") == "User Nidhi registered successfully"
