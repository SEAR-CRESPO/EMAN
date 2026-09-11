from .administrador  import administrador_bp
from .cliente        import cliente_bp
from .compra         import compra_bp
from .domicilio      import domicilio_bp
from .pago           import pago_bp
from .persona        import persona_bp
from .producto       import producto_bp
from .tipo_genero    import tipo_genero_bp
from .ubicacion      import ubicacion_bp
from .carrito_compra import carrito_compra_bp
from .dom_contacto   import dom_contacto_bp
from .per_contacto   import per_contacto_bp
from .produ_compr    import produ_compr_bp
from .produc_carri   import produc_carri_bp
from .documentacion  import documentacion_bp

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
    app.register_blueprint(carrito_compra_bp, url_prefix="/carrito_compra")
    app.register_blueprint(dom_contacto_bp, url_prefix="/dom_contacto")
    app.register_blueprint(per_contacto_bp, url_prefix="/per_contacto")
    app.register_blueprint(produ_compr_bp, url_prefix="/produ_compr")
    app.register_blueprint(produc_carri_bp, url_prefix="/produ_carri")
    app.register_blueprint(documentacion_bp, url_prefix="/documentacion")