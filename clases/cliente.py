# cliente.py

class Cliente:
    def __init__(self,
                 id_cliente, nombre, cuit,
                 clave_fiscal=None, clave_ciudad=None, clave_arba=None, clave_sec=None,
                 clave_faecys=None, clave_inacap=None, clave_osecac=None,
                 clave_rubrica_digital_caba=None, clave_estudio_one_web=None,
                 registro_de_empleadores=None, otros_datos=None, domicilio=None,
                 carpeta=None, ptovta=None, nombase=None, ruta_base=None, rutabackup=None):
        
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.cuit = cuit

        self.clave_fiscal = clave_fiscal
        self.clave_ciudad = clave_ciudad
        self.clave_arba = clave_arba
        self.clave_sec = clave_sec
        self.clave_faecys = clave_faecys
        self.clave_inacap = clave_inacap
        self.clave_osecac = clave_osecac
        self.clave_rubrica_digital_caba = clave_rubrica_digital_caba
        self.clave_estudio_one_web = clave_estudio_one_web
        self.registro_de_empleadores = registro_de_empleadores
        self.otros_datos = otros_datos
        self.domicilio = domicilio

        self.carpeta = carpeta
        self.ptovta = ptovta
        self.nombase = nombase
        self.ruta_base = ruta_base
        self.rutabackup = rutabackup
    
    def mostrar_resumen(self):
        return f"""
        **CUIT**: {self.cuit}	
        **Clave ARCA**: {self.clave_fiscal}  
        **Clave Ciudad**: {self.clave_ciudad}  
        **Domicilio**: {self.domicilio}
        """

    def validar_cuit(self):
        return self.cuit.isdigit() and len(self.cuit) == 11

    def a_dict(self):
        return self.__dict__

    @classmethod
    def desde_dict(cls, data):
        return cls(**data)
