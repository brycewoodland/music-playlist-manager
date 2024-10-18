from flasgger import Swagger

def configure_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Music Playlist Manager API",
            "description": "API documentation for the Music Playlist Manager application",
            "version": "1.1.0",
            "termsOfService": "",
            "contact": {
                "email": "support@example.com"
            },
            "license": {
                "name": "MIT",
                "url": "https://opensource.org/licenses/MIT"
            }
        },
        "host": "127.0.0.1:5000",  
        "basePath": "/",  # Base path for the endpoints
        "schemes": [
            "http",
            "https"
        ],
        "securityDefinitions": {
            "APIKeyHeader": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        }
    }

    Swagger(app, config=swagger_config, template=swagger_template)