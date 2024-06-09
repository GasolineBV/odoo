import logging
from odoo import http

_logger = logging.getLogger(__name__)

class FastAPIController(http.Controller):

    @http.route('/fastapi_test', type='http', auth='public', methods=['GET'], csrf=False)
    def fastapi_entrypoint(self, **kwargs):
        try:
            from ..fastapi.app import app
            import uvicorn
            _logger.info("Imports successful")
            config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
            server = uvicorn.Server(config)
            _logger.info("Starting FastAPI server...")
            server.run()
            return "FastAPI server running"
        except Exception as e:
            _logger.error(f"Error starting FastAPI server: {e}")
            return http.Response(f"Internal server error: {e}", status=500)
