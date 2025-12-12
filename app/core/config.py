import os

def _env(nom: str, defaut: str = "") -> str:
    return os.getenv(nom, defaut)

class Configuration:
    bd_hote: str = _env("BD_HOTE", "localhost")
    bd_port: str = _env("BD_PORT", "5432")
    bd_nom: str = _env("BD_NOM", "ecommerce")
    bd_utilisateur: str = _env("BD_UTILISATEUR", "postgres")
    bd_mot_de_passe: str = _env("BD_MOT_DE_PASSE", "admin")

    jwt_secret: str = _env("JWT_SECRET", "change_moi")
    jwt_algo: str = _env("JWT_ALGO", "HS256")
    jwt_duree_minutes: int = int(_env("JWT_DUREE_MINUTES", "60"))

    mode: str = _env("MODE", "dev")

    @property
    def url_bdd_async(self) -> str:
        return (
            f"postgresql+asyncpg://{self.bd_utilisateur}:{self.bd_mot_de_passe}"
            f"@{self.bd_hote}:{self.bd_port}/{self.bd_nom}"
        )

config = Configuration()
