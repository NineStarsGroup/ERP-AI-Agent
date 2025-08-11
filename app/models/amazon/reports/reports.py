from sqlalchemy import Column, Integer, String, Float, DateTime, Text, DECIMAL, Date
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from app.models.base import BaseModel

class AmznLedgerDetailViewData(BaseModel):
    """FBA Inventory Ledger Detail View: inventory movements/adjustments across FCs"""
    __tablename__ = "amzn_ledger_detail_view_data"

    ledger_detail_view_data_id = Column(Integer, primary_key=True, index=True)
    # Product identification
    date = Column(Date, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text)
    msku = Column(Text)
    title = Column(Text)
    # Event and reference
    event_type = Column(Text)
    reference_id = Column(Text)
    # Quantity
    quantity = Column(Integer)
    reconciled_quantity = Column(Integer)
    unreconciled_quantity = Column(Integer)
    # Location and disposition
    fulfillment_center = Column(Text)
    disposition = Column(Text)
    reason = Column(Text)
    country = Column(Text)
    # Timestamps
    date_and_time = Column(DateTime)
    # Processing
    grouped_rows_count = Column(Integer)
    previous_row_ids = Column(ARRAY(Integer))
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznLedgerDetailViewDataCollect(BaseModel):
    """Amazon Ledger Detail View Data Collect"""
    __tablename__ = "amzn_ledger_detail_view_data_collect"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    ledger_id = Column(String, unique=True, index=True)
    transaction_type = Column(String)
    amount = Column(Float)
    currency = Column(String)
    transaction_date = Column(DateTime)
    description = Column(String)
    collection_status = Column(String)

class AmznLedgerDetailViewDataProcess(BaseModel):
    """Amazon Ledger Detail View Data Process"""
    __tablename__ = "amzn_ledger_detail_view_data_process"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    ledger_id = Column(String, unique=True, index=True)
    transaction_type = Column(String)
    amount = Column(Float)
    currency = Column(String)
    transaction_date = Column(DateTime)
    description = Column(String)
    processing_status = Column(String)

class AmznMerchantListingsAllData(BaseModel):
    """Amazon Merchant Listings All data: product listings across marketplaces with pricing, quantities, and status"""
    __tablename__ = "amzn_merchant_listings_all_data"

    merchant_listings_all_data_id = Column(Integer, primary_key=True, index=True)

    # Product identification/details
    item_name = Column(Text)
    item_description = Column(Text)
    listing_id = Column(Text)
    seller_sku = Column(Text, index=True)
    product_id = Column(Text)
    product_id_type = Column(Integer)
    item_condition = Column(Text)
    item_note = Column(Text)
    image_url = Column(Text)
    open_date = Column(Text)

    # Pricing/financial
    price = Column(DECIMAL(12, 2))
    zshop_shipping_fee = Column(DECIMAL(12, 2))
    bid_for_featured_placement = Column(Text)

    # Quantities / inventory
    quantity = Column(Integer)
    pending_quantity = Column(Integer)
    add_delete = Column(Text)

    # ASINs
    asin1 = Column(Text, index=True)
    asin2 = Column(Text)
    asin3 = Column(Text)

    # Marketplace/channel
    marketplace = Column(Text)
    fulfillment_channel = Column(Text)
    merchant_shipping_group = Column(Text)
    status = Column(Text)

    # Z-Shop specifics
    item_is_marketplace = Column(Text)
    zshop_category1 = Column(Text)
    zshop_browse_path = Column(Text)
    zshop_storefront_feature = Column(Text)
    zshop_boldface = Column(Text)

    # Shipping
    will_ship_internationally = Column(Text)
    expedited_shipping = Column(Text)

    # Processing
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznMerchantListingsAllDataCollect(BaseModel):
    """Amazon Merchant Listings All Data Collect"""
    __tablename__ = "amzn_merchant_listings_all_data_collect"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, index=True)
    sku = Column(String, index=True)
    product_name = Column(String)
    listing_price = Column(Float)
    quantity = Column(Integer)
    fulfillment_channel = Column(String)
    collection_status = Column(String)

class AmznMerchantListingsAllDataProcess(BaseModel):
    """Amazon Merchant Listings All Data Process"""
    __tablename__ = "amzn_merchant_listings_all_data_process"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, index=True)
    sku = Column(String, index=True)
    product_name = Column(String)
    listing_price = Column(Float)
    quantity = Column(Integer)
    fulfillment_channel = Column(String)
    processing_status = Column(String)

class ManualAmzFbaPlacementFee(BaseModel):
    """Manual Amazon FBA Placement Fee"""
    __tablename__ = "manual_amz_fba_placement_fee"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, index=True)
    fee_amount = Column(Float)
    fee_type = Column(String)
    placement_date = Column(DateTime)
    notes = Column(String) 