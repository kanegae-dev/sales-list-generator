import os


def get_env_variable(name: str) -> str:
    """
    環境変数を取得する。
    未設定の場合はエラーを出す。
    """
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"{name} is not set in environment variables.")
    return value


# Google Maps API Key
GOOGLE_MAPS_API_KEY = get_env_variable("GOOGLE_MAPS_API_KEY")
