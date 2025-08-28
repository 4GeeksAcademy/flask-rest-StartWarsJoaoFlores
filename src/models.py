
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    subscripción: Mapped[str] = mapped_column(String(120), nullable=False)

    favoritos: Mapped["Favorito"] = relationship(back_populates="username")
    planeta: Mapped[list["Planetas"]] = relationship(back_populates="username")
    personajes: Mapped[list["Personaje"]] = relationship(back_populates="username")
    vehiculos: Mapped[list["Vehiculos"]] = relationship(back_populates="username")

    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname
            # do not serialize the password, its a security breach
        }

class Favorito(db.Model):
    __tablename__ = "Favorito"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    username: Mapped["User"] = relationship(back_populates="favoritos")
    personajes: Mapped[list["Personaje"]] = relationship(back_populates="favoritos")
    vehiculos: Mapped[list["Vehiculos"]] = relationship(back_populates="favoritos")

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name
        }

class Planetas(db.Model):
    __tablename__ = "Planetas"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    diametro: Mapped[str] = mapped_column(String(120), nullable=False)
    gravedad: Mapped[str] = mapped_column(String(120), nullable=False)
    superficieagua: Mapped[str] = mapped_column(String(120), nullable=False)

    username: Mapped["User"] = relationship(back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diametro": self.diametro,
            "gravedad": self.gravedad,
            "superficieagua": self.superficieagua
        }


class Personaje(db.Model):
    __tablename__ = "Personajes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    genero: Mapped[str] = mapped_column(String(120), nullable=False)
    dateBirth: Mapped[str] = mapped_column(String(120),nullable=False)

    username: Mapped["User"] = relationship(back_populates="Personajes")
    vehiculos : Mapped["Vehiculos"] = relationship(back_populates ="personaje")
    especie: Mapped["Especies"] = relationship(back_populates= "personaje")
    favortios: Mapped["Favorito"] = relationship(back_populates= "personajes")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "genero": self.genero,
        }

class Especies (db.Model):
    __tablename__ = "Especies"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    classificacion: Mapped[str] = mapped_column(String(120), nullable=False)
    lenguaje: Mapped[str] = mapped_column(String(120), nullable=False)

    personaje: Mapped["Personaje"] = relationship(back_populates="especie")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classificacion": self.classificacion,
            "lenguaje": self.lenguaje
        }

class Vehiculos (db.Model):
    __tablename__ = "Vehiculos"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    modelo: Mapped[str] = mapped_column(String(120), nullable=False)
    crew: Mapped[str] = mapped_column(String(120), nullable=False)
    length: Mapped[str] = mapped_column(String(120), nullable=False)

    personaje : Mapped["Personaje"] = relationship(back_populates= "vehiculos")
    favoritos: Mapped["Favorito"] = relationship(back_populates="vehiculos")
    username : Mapped["User"] = relationship(back_populates="vehiculos")

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "modelo": self.modelo,
            "crew": self.crew,
            "length": self.length
        }