import sys
sys.path.insert(0, '.')
import pytest
from api.app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            from api.models import db
            db.create_all()
        yield client

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200

def test_basics_page(client):
    """Test that the seafood basics page loads successfully."""
    response = client.get('/basics')
    assert response.status_code == 200

def test_fish_page(client):
    """Test that the fish species page loads successfully."""
    response = client.get('/fish')
    assert response.status_code == 200

def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200

def test_guides_page(client):
    """Test that the consumer guides page loads successfully."""
    response = client.get('/guides')
    assert response.status_code == 200

def test_overfished_areas_api(client):
    """Test the overfished areas API endpoint returns valid JSON."""
    response = client.get('/api/overfished-areas')
    assert response.status_code == 200
    data = response.get_json()
    assert 'overfished_areas' in data
    assert 'total' in data
    assert isinstance(data['overfished_areas'], list)

def test_imported_species_api(client):
    """Test the imported species API endpoint returns valid JSON."""
    response = client.get('/api/imported-species')
    assert response.status_code == 200
    data = response.get_json()
    assert 'imported_species' in data
    assert 'total' in data
    assert isinstance(data['imported_species'], list)

def test_fishing_methods_api(client):
    """Test the fishing methods API endpoint returns valid JSON."""
    response = client.get('/api/fishing-methods')
    assert response.status_code == 200
    data = response.get_json()
    assert 'fishing_methods' in data
    assert 'total' in data
    assert isinstance(data['fishing_methods'], list)

def test_fish_api(client):
    """Test the fish species API endpoint returns valid JSON."""
    response = client.get('/api/fish')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_consumer_guides_api(client):
    """Test the consumer guides API endpoint returns valid JSON."""
    response = client.get('/api/consumer-guides')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
