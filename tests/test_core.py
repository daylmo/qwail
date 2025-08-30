from qwail.core.config import Settings

settings = Settings()


def test_config():
    assert str(settings.DATABASE_URL)
