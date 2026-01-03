"""
Navigator - Benefits & Assistance Hub
HearthMind LLC
"""

from flask import Flask
import yaml
from pathlib import Path

def create_app():
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    config_path = Path(__file__).parent.parent / 'config'
    
    with open(config_path / 'benefits.yaml', 'r') as f:
        app.config['BENEFITS'] = yaml.safe_load(f) or {}
    
    with open(config_path / 'resources.yaml', 'r') as f:
        app.config['RESOURCES'] = yaml.safe_load(f) or {}
    
    with open(config_path / 'local_resources.yaml', 'r') as f:
        app.config['LOCAL_RESOURCES'] = yaml.safe_load(f) or {}
    
    import routes
    app.register_blueprint(routes.bp)
    
    return app
