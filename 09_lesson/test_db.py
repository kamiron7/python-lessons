import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/homework"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, nullable=False)


@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()


def test_create_subject(db_session):
    new_subject = Subject(subject_id=20, subject_title="Serbian")
    db_session.add(new_subject)
    db_session.commit()

    subject_in_db = db_session.query(Subject).filter_by(
        subject_title="Serbian"
        ).first()
    assert subject_in_db is not None

    db_session.delete(subject_in_db)
    db_session.commit()


def test_update_subject(db_session):
    subject = Subject(subject_id=20, subject_title="Serbian")
    db_session.add(subject)
    db_session.commit()

    subject.subject_title = "Dutch"
    db_session.commit()

    updated_subject = (
        db_session.query(Subject).filter_by(
            subject_id=subject.subject_id
            ).first()
    )
    assert updated_subject.subject_title == "Dutch"

    db_session.delete(updated_subject)
    db_session.commit()


def test_delete_subject(db_session):
    subject = Subject(subject_id=20, subject_title="Dutch")
    db_session.add(subject)
    db_session.commit()

    subject_in_db = db_session.query(Subject).filter_by(
        subject_id=20
        ).first()
    assert subject_in_db is not None

    db_session.delete(subject_in_db)
    db_session.commit()

    deleted_subject = db_session.query(Subject).filter_by(
        subject_id=20
        ).first()
    assert deleted_subject is None
