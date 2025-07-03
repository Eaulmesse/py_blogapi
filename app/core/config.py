from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Exemple de variable de configuration
    APP_NAME: str = "py_BlogAPI"
    SECRET_KEY: str = "your-secret-key-here-change-in-production" # La clé secrète pour JWT
    DATABASE_URL: str = "mysql+pymysql://root@localhost:3306/blog_db" # Valeur par défaut pour le développement

    # Configure Pydantic pour charger les variables depuis un fichier .env
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()


