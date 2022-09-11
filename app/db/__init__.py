import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tenacity import after, before, retry, stop, wait

from app.core import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 3},
)
SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


# TODO: logger system
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@retry(
    stop=(stop.stop_after_delay(10) | stop.stop_after_attempt(3)),
    wait=wait.wait_fixed(1),
    before=before.before_log(logger, logging.INFO),
    after=after.after_log(logger, logging.WARN),
)
def check_db_connection() -> None:
    try:
        with engine.connect() as connection:
            logger.info(engine)
            connection.close()
    except Exception as e:
        logger.error(str(e))
        raise e


check_db_connection()
