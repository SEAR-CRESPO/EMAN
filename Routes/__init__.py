from .administrador import administrador_bp
from .cliente import cliente_bp
from .compra import compra_bp
from .domicilio import domicilio_bp
from .pago import pago_bp
from .persona import persona_bp
from .producto import producto_bp
from .tipo_genero import tipo_genero_bp
from .ubicacion import ubicacion_bp

def loadRoutes(app):
    app.register_blueprint(administrador_bp, url_prefix="/administrador")
    app.register_blueprint(cliente_bp, url_prefix="/cliente")
    app.register_blueprint(compra_bp, url_prefix="/compra")
    app.register_blueprint(domicilio_bp, url_prefix="/domicilio")
    app.register_blueprint(pago_bp, url_prefix="/pago")
    app.register_blueprint(persona_bp, url_prefix="/persona")
    app.register_blueprint(producto_bp, url_prefix="/producto")
    app.register_blueprint(tipo_genero_bp, url_prefix="/tipo_genero")
    app.register_blueprint(ubicacion_bp, url_prefix="/ubicacion")