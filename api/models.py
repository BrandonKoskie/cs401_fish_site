from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OverfishedArea(db.Model):
    __tablename__ = "overfished_areas"

    id                 = db.Column(db.Integer,     primary_key=True)
    area               = db.Column(db.String(200), nullable=False)
    overfishing_status = db.Column(db.String(100), nullable=False)
    main_reasons       = db.Column(db.Text,        nullable=False)
    source_link        = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        return {
            "id":                 self.id,
            "area":               self.area,
            "overfishing_status": self.overfishing_status,
            "main_reasons":       self.main_reasons,
            "source_link":        self.source_link,
        }


class ImportedSpecies(db.Model):
    __tablename__ = "imported_species"

    id                   = db.Column(db.Integer,     primary_key=True)
    species              = db.Column(db.String(200), nullable=False)
    annual_import_volume = db.Column(db.String(100), nullable=False)
    main_reason          = db.Column(db.Text,        nullable=False)
    source_link          = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        return {
            "id":                   self.id,
            "species":              self.species,
            "annual_import_volume": self.annual_import_volume,
            "main_reason":          self.main_reason,
            "source_link":          self.source_link,
        }


class FishingMethod(db.Model):
    __tablename__ = "fishing_methods"

    id                  = db.Column(db.Integer,     primary_key=True)
    method              = db.Column(db.String(200), nullable=False)
    description         = db.Column(db.Text,        nullable=False)
    sustainability_rank = db.Column(db.String(100), nullable=False)
    key_reasons         = db.Column(db.Text,        nullable=False)
    source_link         = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        return {
            "id":                  self.id,
            "method":              self.method,
            "description":         self.description,
            "sustainability_rank": self.sustainability_rank,
            "key_reasons":         self.key_reasons,
            "source_link":         self.source_link,
        }
