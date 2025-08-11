from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from sqlalchemy import DECIMAL
from sqlalchemy.dialects.postgresql import JSONB
from app.models.base import BaseModel

class ScCatalog(BaseModel):
    """SellerCloud Catalog across all channels and marketplaces"""
    __tablename__ = "sc_catalog"

    sc_catalog_id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Product identification
    id = Column(Text)  # SKU / product id
    asin = Column(Text)
    manufacturer_sku = Column(Text)
    upc = Column(Text)
    main_product_id = Column(Text)
    shadow_of = Column(Text)

    # Product details
    product_name = Column(Text)
    brand_name = Column(Text)
    product_type = Column(Text)
    image_url = Column(Text)
    amazon_condition = Column(Text)
    product_condition_name = Column(Text)

    # Pricing / costs
    average_cost = Column(DECIMAL)
    list_price = Column(DECIMAL)
    sale_price = Column(DECIMAL)
    map_price = Column(DECIMAL)
    amazon_price = Column(DECIMAL)
    site_price = Column(DECIMAL)
    site_cost = Column(DECIMAL)
    last_cost = Column(DECIMAL)
    vendor_price = Column(DECIMAL)
    order_reserve_total = Column(DECIMAL)
    shipping_cost = Column(DECIMAL)

    # Inventory / quantities
    aggregate_physical_qty_fba = Column(Integer)
    aggregate_physical_qty = Column(Integer)
    aggregate_qty = Column(Integer)
    physical_qty = Column(Integer)
    reserved_qty = Column(Integer)
    warehouse_physical_qty = Column(Integer)
    aggregated_qty = Column(Integer)
    aggregate_physical_sellable_qty_including_physical_value = Column(Integer)
    aggregate_non_sellable_qty = Column(Integer)
    inventory_available_qty = Column(Integer)
    on_order = Column(Integer)
    on_back_order = Column(Integer)
    replacement_qty = Column(Integer)

    # Inventory values
    warehouse_physical_qty_value = Column(DECIMAL)
    warehouse_reserved_qty_value = Column(DECIMAL)
    reserve_qty_total_value = Column(DECIMAL)

    # Sales history
    qty_sold_15 = Column(Integer)
    qty_sold_30 = Column(Integer)
    qty_sold_60 = Column(Integer)
    qty_sold_90 = Column(Integer)
    qty_sold_180 = Column(Integer)
    qty_sold_365 = Column(Integer)
    qty_sold_ytd = Column(Integer)

    # Weights / shipping
    weight = Column(DECIMAL)
    shipping_weight = Column(DECIMAL)
    weight_oz = Column(DECIMAL)
    weight_lbs = Column(DECIMAL)
    package_weight_lbs = Column(DECIMAL)
    package_weight_oz = Column(DECIMAL)
    location_notes = Column(Text)

    # Kit / matrix
    is_kit = Column(Boolean)
    is_matrix_parent = Column(Boolean)
    inventory_dependant_option = Column(Integer)
    deduct_from_item_cost_type = Column(Text)

    # Marketplace / channel
    amazon_market_place_id = Column(Text)
    amazon_marketplace = Column(Text)
    fulfilled_by = Column(Text)
    enabled_on_channels = Column(Text)
    web_enabled = Column(Boolean)
    drop_ship_mode = Column(Text)

    # Vendor / company
    default_vendor = Column(Text)
    vendor_of_product = Column(Text)
    vendor_id = Column(Integer)
    vendor_visible = Column(Boolean)
    company_name = Column(Text)
    company_id = Column(Integer)
    buyer = Column(Text)

    # Status / misc
    active_status = Column(Text)
    status = Column(Text)
    is_sell_able = Column(Boolean)
    back_order_visible = Column(Boolean)
    sales_rank = Column(Integer)
    notes_count = Column(Integer)
    warehouse_count = Column(Integer)
    warehouse_name = Column(Text)
    country = Column(Text)

    # Timestamps
    last_aggregate_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    date_created = Column(DateTime)

    # Processing metadata
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class ScCatalogChild(BaseModel):
    """Supply Chain Catalog Child"""
    __tablename__ = "sc_catalog_child"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    parent_product_id = Column(String, index=True)
    child_product_id = Column(String, index=True)
    relationship_type = Column(String)
    quantity = Column(Integer)

class ScOrders(BaseModel):
    """SellerCloud Orders across all channels and marketplaces"""
    __tablename__ = "sc_orders"

    orders_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    # SellerCloud and source identifiers
    id = Column(Integer, index=True)  # SellerCloud internal id
    order_source_order_id = Column(Text)
    order_source = Column(Integer)  # marketplace/source id (e.g., 20=Amazon)
    purchase_order_id = Column(Integer)

    # Order status/payment/shipping flags
    shipping_status = Column(Integer)
    payment_status = Column(Integer)
    status_code = Column(Integer)
    picked = Column(Integer)
    dropship = Column(Integer)
    is_blacklisted = Column(Boolean)
    is_replacement_order = Column(Boolean)

    # Customer information
    first_name = Column(Text)
    last_name = Column(Text)
    company_name = Column(Text)

    # Timing
    time_of_order = Column(DateTime)
    created_on = Column(DateTime)
    ship_date = Column(DateTime)
    order_shipping_promise_date = Column(DateTime)
    last_updated = Column(DateTime)

    # Financials
    grand_total = Column(DECIMAL)
    final_value_total = Column(DECIMAL)
    shipping_total = Column(DECIMAL)
    order_discounts_total = Column(DECIMAL)
    shipping_discounts_total = Column(DECIMAL)
    insurance_total = Column(DECIMAL)
    handling_fee = Column(DECIMAL)
    final_shipping_fee = Column(DECIMAL)

    # Location / shipping info
    country = Column(Text)
    destination_state = Column(Text)
    destination_country = Column(Text)
    shipping_address_state_name = Column(Text)
    shipping_address_country_code = Column(Text)
    shipping_carrier = Column(Text)
    shipping_service = Column(Text)

    # Amazon-specific
    amazon_marketplace_id = Column(Text)
    amazon_marketplace = Column(Text)

    # Delivery
    estimated_delivery_date = Column(Text)
    delivery_status_string = Column(Text)

    # Processing/job metadata
    shipped_by = Column(Integer)
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class ScOrderItems(BaseModel):
    """Supply Chain Order Items"""
    __tablename__ = "sc_order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    order_id = Column(String, index=True)
    product_id = Column(String, index=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)

class ScProductGroup(BaseModel):
    """Supply Chain Product Group"""
    __tablename__ = "sc_product_group"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    group_id = Column(String, unique=True, index=True)
    group_name = Column(String)
    group_type = Column(String)
    description = Column(String)

class N2ScCogs(BaseModel):
    """N2 Supply Chain Cost of Goods Sold"""
    __tablename__ = "n2_sc_cogs"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    product_id = Column(String, index=True)
    cogs_amount = Column(Float)
    cogs_type = Column(String)
    cogs_date = Column(DateTime)

class TableSettings(BaseModel):
    """Table Settings"""
    __tablename__ = "table_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    table_name = Column(String, unique=True, index=True)
    setting_key = Column(String)
    setting_value = Column(String)
    setting_type = Column(String) 