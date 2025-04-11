def apply_middleware(app):
    @app.before_request
    def log_request():
        print("Request received")
