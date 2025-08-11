from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Date, DECIMAL
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from app.models.base import BaseModel

class AmznFlatFileAllOrdersDataByLastUpdateGeneral(BaseModel):
    """Amazon All Orders Data by Last Update (FBA/FBM) with pricing, taxes, shipping and status updates"""
    __tablename__ = "amzn_flat_file_all_orders_data_by_last_update_general"

    flat_file_all_orders_data_by_last_update_id = Column(Integer, primary_key=True, index=True)

    # Order identification
    amazon_order_id = Column(Text, index=True)
    merchant_order_id = Column(Text)
    purchase_date = Column(DateTime)
    last_updated_date = Column(DateTime)
    order_status = Column(Text)

    # Channel and fulfillment
    fulfillment_channel = Column(Text)
    sales_channel = Column(Text)
    order_channel = Column(Text)
    ship_service_level = Column(Text)

    # Product info
    product_name = Column(Text)
    sku = Column(Text, index=True)
    asin = Column(Text)
    item_status = Column(Text)
    quantity = Column(Integer)

    # Pricing
    currency = Column(Text)
    item_price = Column(DECIMAL(12, 2))
    item_tax = Column(DECIMAL(12, 2))
    shipping_price = Column(DECIMAL(12, 2))
    shipping_tax = Column(DECIMAL(12, 2))
    gift_wrap_price = Column(DECIMAL(12, 2))
    gift_wrap_tax = Column(DECIMAL(12, 2))
    item_promotion_discount = Column(DECIMAL(12, 2))
    ship_promotion_discount = Column(DECIMAL(12, 2))

    # Shipping address
    ship_city = Column(Text)
    ship_state = Column(Text)
    ship_postal_code = Column(Text)
    ship_country = Column(Text)

    # Other order details
    promotion_ids = Column(Text)
    cpf = Column(Text)
    is_business_order = Column(Text)
    purchase_order_number = Column(Text)
    price_designation = Column(Text)
    buyer_company_name = Column(Text)
    is_replacement_order = Column(Text)
    original_order_id = Column(Text)
    is_buyer_requested_cancellation = Column(Text)
    buyer_requested_cancel_reason = Column(Text)
    signature_confirmation_recommended = Column(Text)

    # Processing info
    order_first_fetched_at = Column(DateTime(timezone=True))
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFlatFileReturnsDataByReturnDate(BaseModel):
    """Amazon FBM Returns Data by Return Date (non-FBA)"""
    __tablename__ = "amzn_flat_file_returns_data_by_return_date"

    flat_file_returns_data_by_return_date_id = Column(Integer, primary_key=True, index=True)

    # Order and return identification
    order_id = Column(Text, index=True)
    order_date = Column(Text)
    return_request_date = Column(Text)
    return_request_status = Column(Text)
    amazon_rma_id = Column(Text)
    merchant_rma_id = Column(Text)

    # Shipping and logistics
    label_type = Column(Text)
    label_cost = Column(DECIMAL(12, 2))
    currency_code = Column(Text)
    return_carrier = Column(Text)
    tracking_id = Column(Text)
    label_to_be_paid_by = Column(Text)
    a_to_z_claim = Column(Text)
    is_prime = Column(Text)

    # Product information
    asin = Column(Text, index=True)
    merchant_sku = Column(Text, index=True)
    item_name = Column(Text)
    return_quantity = Column(Integer)
    order_quantity = Column(Integer)

    # Return details
    return_reason = Column(Text)
    in_policy = Column(Text)
    return_type = Column(Text)
    resolution = Column(Text)
    return_delivery_date = Column(Text)
    invoice_number = Column(Text)

    # Financials
    order_amount = Column(DECIMAL(12, 2))
    refunded_amount = Column(DECIMAL(12, 2))

    # Safe-T claims
    safe_t_action_reason = Column(Text)
    safe_t_claim_id = Column(Text)
    safe_t_claim_state = Column(Text)
    safe_t_claim_creation_time = Column(Text)
    safe_t_claim_reimbursement_amount = Column(DECIMAL(12, 2))

    # Processing metadata
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFlatFileReturnsDataByReturnDateCollect(BaseModel):
    """Amazon Returns Data by Return Date Collect"""
    __tablename__ = "amzn_flat_file_returns_data_by_return_date_collect"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    return_id = Column(String, unique=True, index=True)
    order_id = Column(String, index=True)
    return_date = Column(DateTime)
    return_reason = Column(String)
    refund_amount = Column(Float)
    asin = Column(String, index=True)
    collection_status = Column(String)

class AmznFlatFileReturnsDataByReturnDateDelete(BaseModel):
    """Amazon Returns Data by Return Date Delete"""
    __tablename__ = "amzn_flat_file_returns_data_by_return_date_delete"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    return_id = Column(String, unique=True, index=True)
    order_id = Column(String, index=True)
    return_date = Column(DateTime)
    return_reason = Column(String)
    refund_amount = Column(Float)
    asin = Column(String, index=True)
    deletion_status = Column(String) 


# Note: The canonical model for 'amzn_ledger_detail_view_data' lives under
# app/models/amazon/reports/reports.py. Removed duplicate definition here to avoid
# SQLAlchemy table redefinition errors.