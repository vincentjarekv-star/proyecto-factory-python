
from abc import ABC, abstractmethod


# 1. Producto abstracto
class Notificacion(ABC):

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


# 2. Productos concretos
class NotificacionEmail(Notificacion):

    def enviar(self, mensaje: str) -> None:
        print(f"Enviando correo: {mensaje}")


class NotificacionSMS(Notificacion):

    def enviar(self, mensaje: str) -> None:
        print(f"Enviando SMS: {mensaje}")


# 3. Creador abstracto
class FabricaNotificacion(ABC):

    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass


# 4. Creadores concretos
class FabricaEmail(FabricaNotificacion):

    def crear_notificacion(self) -> Notificacion:
        return NotificacionEmail()


class FabricaSMS(FabricaNotificacion):

    def crear_notificacion(self) -> Notificacion:
        return NotificacionSMS()


# 5. Funcionamiento del programa
def main() -> None:

    print("=== PATRON FACTORY METHOD ===")

    fabrica_email = FabricaEmail()
    notificacion_email = fabrica_email.crear_notificacion()
    notificacion_email.enviar("Bienvenido al sistema")

    fabrica_sms = FabricaSMS()
    notificacion_sms = fabrica_sms.crear_notificacion()
    notificacion_sms.enviar("Su codigo de verificacion es 1234")


if __name__ == "__main__":
    main()
