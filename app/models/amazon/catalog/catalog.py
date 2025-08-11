from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class N2Asins(BaseModel):
    """N2 ASINs"""
    __tablename__ = "n2_asins"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, unique=True, index=True)
    product_name = Column(String)
    brand = Column(String)
    category = Column(String)
    is_active = Column(Boolean, default=True)

class N2CatalogAliasMap(BaseModel):
    """N2 Catalog Alias Map"""
    __tablename__ = "n2_catalog_alias_map"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    alias_id = Column(String, unique=True, index=True)
    primary_asin = Column(String, index=True)
    alias_asin = Column(String, index=True)
    alias_type = Column(String)

class N2CatalogKits(BaseModel):
    """N2 Catalog Kits"""
    __tablename__ = "n2_catalog_kits"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    kit_id = Column(String, unique=True, index=True)
    kit_name = Column(String)
    kit_asin = Column(String, index=True)
    component_asin = Column(String, index=True)
    quantity = Column(Integer)

class N2CatalogPrimary(BaseModel):
    """N2 Catalog Primary"""
    __tablename__ = "n2_catalog_primary"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, unique=True, index=True)
    product_name = Column(String)
    brand = Column(String)
    category = Column(String)
    is_primary = Column(Boolean, default=True) 