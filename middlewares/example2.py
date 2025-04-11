def apply_middleware(app):
    @app.after_request
    def log_response(res):
        print("response sent")
        return res  # ← Don't forget this!
