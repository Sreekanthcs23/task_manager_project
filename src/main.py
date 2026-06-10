from flask import Flask
from src.config import Config
from src.controllers.task_controller import task_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(task_bp)
    
    # TODO: Create a route map or patch handler for toggle_status! 
    # Currently, `task_service.toggle_status` remains entirely dead code.
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=Config.PORT, debug=Config.DEBUG)
