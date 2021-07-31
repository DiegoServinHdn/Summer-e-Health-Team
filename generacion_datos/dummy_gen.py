from dataclasses import asdict, dataclass, field
from faker import Faker
import pandas as pd

# Instancia de faker para crear dummy data
faker = Faker()

# dataclass de usuarios
@dataclass
class Usuarios:
    nombre_usuario: str = field(default_factory=faker.name)
    email: str = field(default_factory=faker.email)
    contrasenia: str = field(default_factory=faker.sha256)
    fecha_nacimiento: str = field(default_factory=faker.date)
    direccion: str = field(default_factory=faker.street_address)
    codigo_postal: str = field(default_factory=faker.postcode)

    @classmethod
    def generar(cls, generaciones):
        """! Genera datos dummy de usuarios
        @param generaciones numero de genera
        @return lista con datos de usuarios generados
        """
        return [cls() for _ in range(generaciones)]


if __name__ == '__main__':
    # Ejemplo genracion usuarios
    usuario_df = pd.DataFrame(Usuarios.generar(100))
    usuario_df.to_csv("usuarios_dummy.csv")
    print(usuario_df.head())