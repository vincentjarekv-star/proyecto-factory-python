
from abc import ABC, abstractmethod


#1. Producto Abstracto

class Notificacion(ABC):

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


#2. Producto Concreto

class NotificacionEmail(Notificacion):

    def enviar(self, mensaje: str) -> None:
        print(f"Enviando correo: {mensaje}")


class NotificacionSMS(Notificacion):

    def enviar(self, mensaje: str) -> None:
        print(f"Enviando SMS: {mensaje}")


class NotificacionTelegram(Notificacion):

    def enviar(self, mensaje: str) -> None:
        print(f"Enviando Telegram: {mensaje}")


#3. Abstracto

class FabricaNotificacion(ABC):

    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass


#4. Concreto

class FabricaEmail(FabricaNotificacion):

    def crear_notificacion(self) -> Notificacion:
        return NotificacionEmail()


class FabricaSMS(FabricaNotificacion):

    def crear_notificacion(self) -> Notificacion:
        return NotificacionSMS()


class FabricaTelegram(FabricaNotificacion):

    def crear_notificacion(self) -> Notificacion:
        return NotificacionTelegram()


#5. Funcion del programa

def main() -> None:

    print("=== PATRON FACTORY METHOD ===")

    fabrica_email = FabricaEmail()
    notificacion_email = fabrica_email.crear_notificacion()
    notificacion_email.enviar("Bienvenido al sistema")

    fabrica_sms = FabricaSMS()
    notificacion_sms = fabrica_sms.crear_notificacion()
    notificacion_sms.enviar("Su codigo de verificacion es 1234")

    fabrica_telegram = FabricaTelegram()
    notificacion_telegram = fabrica_telegram.crear_notificacion()
    notificacion_telegram.enviar("Notificacion enviada desde Telegram")


if __name__ == "__main__":
    main()
