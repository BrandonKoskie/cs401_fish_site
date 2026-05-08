"""
Database models for the Hawaii Seafood Guide application.

This module defines the SQLAlchemy ORM models representing the core data
entities: Overfished Areas, Imported Species, Fishing Methods, and Consumer
Guides. Each model maps to a corresponding database table.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OverfishedArea(db.Model):
    """
    Represents a Hawaii marine area experiencing overfishing pressure.
    
    Attributes:
        id (int): Primary key.
        area (str): Name of the geographic area.
        overfishing_status (str): Current status (e.g., 'High pressure / Declining').
        main_reasons (str): Primary causes of overfishing in this area.
        source_link (str, optional): Reference source for the data.
    """
    __tablename__ = "overfished_areas"

    id                 = db.Column(db.Integer,     primary_key=True)
    area               = db.Column(db.String(200), nullable=False)
    overfishing_status = db.Column(db.String(100), nullable=False)
    main_reasons       = db.Column(db.Text,        nullable=False)
    source_link        = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        """
        Convert the OverfishedArea instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the model.
        """
        return {
            "id":                 self.id,
            "area":               self.area,
            "overfishing_status": self.overfishing_status,
            "main_reasons":       self.main_reasons,
            "source_link":        self.source_link,
        }


class ImportedSpecies(db.Model):
    """
    Represents a seafood species commonly imported to Hawaii.
    
    Attributes:
        id (int): Primary key.
        species (str): Common name of the imported species.
        annual_import_volume (str): Approximate import volume (e.g., 'High').
        main_reason (str): Primary reason for importing this species.
        source_link (str, optional): Reference source for the data.
    """
    __tablename__ = "imported_species"

    id                   = db.Column(db.Integer,     primary_key=True)
    species              = db.Column(db.String(200), nullable=False)
    annual_import_volume = db.Column(db.String(100), nullable=False)
    main_reason          = db.Column(db.Text,        nullable=False)
    source_link          = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        """
        Convert the ImportedSpecies instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the model.
        """
        return {
            "id":                   self.id,
            "species":              self.species,
            "annual_import_volume": self.annual_import_volume,
            "main_reason":          self.main_reason,
            "source_link":          self.source_link,
        }


class FishingMethod(db.Model):
    """
    Represents a fishing method used in Hawaii with sustainability information.
    
    Attributes:
        id (int): Primary key.
        method (str): Name of the fishing method.
        description (str): Brief description of how the method works.
        sustainability_rank (str): Sustainability rating.
        key_reasons (str): Key factors affecting the sustainability score.
        source_link (str, optional): Reference source for the data.
    """
    __tablename__ = "fishing_methods"

    id                  = db.Column(db.Integer,     primary_key=True)
    method              = db.Column(db.String(200), nullable=False)
    description         = db.Column(db.Text,        nullable=False)
    sustainability_rank = db.Column(db.String(100), nullable=False)
    key_reasons         = db.Column(db.Text,        nullable=False)
    source_link         = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        """
        Convert the FishingMethod instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the model.
        """
        return {
            "id":                  self.id,
            "method":              self.method,
            "description":         self.description,
            "sustainability_rank": self.sustainability_rank,
            "key_reasons":         self.key_reasons,
            "source_link":         self.source_link,
        }

class ConsumerGuide(db.Model):
    """
    Represents a consumer guide for seafood selection in Hawaii.
    
    Attributes:
        id (int): Primary key.
        guide_name (str): Title of the guide.
        description (str): Brief summary of the guide's purpose.
        content (str): HTML content of the guide.
        filters (str, optional): Comma-separated filter tags.
        resources (str, optional): Reference sources for the guide.
    """
    __tablename__ = "consumer_guides"

    id          = db.Column(db.Integer,     primary_key=True)
    guide_name  = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text,        nullable=False)
    content     = db.Column(db.Text,        nullable=False)
    filters     = db.Column(db.String(300), nullable=True)
    resources   = db.Column(db.Text,        nullable=True)

    def to_dict(self):
        """
        Convert the ConsumerGuide instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the model.
        """
        return {
            "id":          self.id,
            "guide_name":  self.guide_name,
            "description": self.description,
            "content":     self.content,
            "filters":     self.filters,
            "resources":   self.resources,
        }
