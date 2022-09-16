from datetime import datetime

class Usuario:

    def __int__(self,cedula: int,nombre: str,apellido: str,celular: int):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular

    def registrar_usuario(self, cedula, nombre) -> bool:

        if self.buscar_usuario(cedula) is None:
            usuario = Usuario(cedula, nombre)
            self.usuarios[cedula] = usuario
            return True
        else:
            return False

    def eliminar_usuario(self) -> bool:
        pass

    def actualizar_usuario(self) -> bool:
        pass


class Vehiculo:

    def __int__(self, matricula: str,tipo_vehiculo: str,hora_entrada: datetime.now(),
                hora_salida: datetime.now(), fecha: datetime):
        self.matricula = matricula
        self.tipo_vehiculo = tipo_vehiculo
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.fecha = fecha

    def ingreso_vehiculo(self) -> bool:
        pass

    def salida_vehiculo(self) -> bool:
        pass

class Tarifa:

    def __int__(self,tipo_tarifa: str, cod_tarifa:int):
        self.tipo_tarifa = tipo_tarifa
        self.cod_tarifa = cod_tarifa

    def cobro(self):
        pass

class Ticked:

    def __int__(self,hora_entrada: datetime.now(),hora_salida: datetime.now(), fecha: datetime, valor: int):
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.fecha = fecha
        self.valor = valor

    def comprobante(self):
        pass

class Reporte:

    def __int__(self, id_reporte: int):
        self.id_reporte = id_reporte

    def informacion(self):
        pass

class Estacionamineto:

    def __int__(self):
        pass