from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class N2Pnl(BaseModel):
    """N2 Profit & Loss"""
    __tablename__ = "n2_pnl"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, unique=True, index=True)
    period_start = Column(Date)
    period_end = Column(Date)
    total_revenue = Column(Float)
    total_cost = Column(Float)
    total_profit = Column(Float)

class N2PnlAdvertising(BaseModel):
    """N2 PnL Advertising"""
    __tablename__ = "n2_pnl_advertising"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    ad_spend = Column(Float)
    ad_revenue = Column(Float)
    ad_profit = Column(Float)

class N2PnlCollect(BaseModel):
    """N2 PnL Collect"""
    __tablename__ = "n2_pnl_collect"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    collection_type = Column(String)
    amount = Column(Float)
    collection_date = Column(DateTime)

class N2PnlFbaReimbursements(BaseModel):
    """N2 PnL FBA Reimbursements"""
    __tablename__ = "n2_pnl_fba_reimbursements"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    reimbursement_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    reimbursement_amount = Column(Float)
    reimbursement_reason = Column(String)

class N2PnlFbaReplacements(BaseModel):
    """N2 PnL FBA Replacements"""
    __tablename__ = "n2_pnl_fba_replacements"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    replacement_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    replacement_cost = Column(Float)
    replacement_reason = Column(String)

class N2PnlFbaReturns(BaseModel):
    """N2 PnL FBA Returns"""
    __tablename__ = "n2_pnl_fba_returns"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    return_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    return_cost = Column(Float)
    return_reason = Column(String)

class N2PnlFbmShippingNonAmzn(BaseModel):
    """N2 PnL FBM Shipping Non-Amazon"""
    __tablename__ = "n2_pnl_fbm_shipping_non_amzn"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    order_id = Column(String, index=True)
    shipping_cost = Column(Float)
    shipping_carrier = Column(String)
    shipping_method = Column(String)

class N2PnlSettlement(BaseModel):
    """N2 PnL Settlement"""
    __tablename__ = "n2_pnl_settlement"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    settlement_id = Column(String, unique=True, index=True)
    settlement_amount = Column(Float)
    settlement_date = Column(DateTime)

class N2PnlSettlementCogs(BaseModel):
    """N2 PnL Settlement COGS"""
    __tablename__ = "n2_pnl_settlement_cogs"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    cogs_amount = Column(Float)
    cogs_type = Column(String)

class N2PnlSettlementCustomerReturn(BaseModel):
    """N2 PnL Settlement Customer Return"""
    __tablename__ = "n2_pnl_settlement_customer_return"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    return_id = Column(String, unique=True, index=True)
    return_amount = Column(Float)
    return_reason = Column(String)

class N2PnlSettlementFbaInbound(BaseModel):
    """N2 PnL Settlement FBA Inbound"""
    __tablename__ = "n2_pnl_settlement_fba_inbound"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    shipment_id = Column(String, index=True)
    inbound_cost = Column(Float)
    inbound_type = Column(String)

class N2PnlSettlementPickPack(BaseModel):
    """N2 PnL Settlement Pick & Pack"""
    __tablename__ = "n2_pnl_settlement_pick_pack"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    order_id = Column(String, index=True)
    pick_pack_fee = Column(Float)
    weight_handling = Column(Float)

class N2PnlSettlementPlacement(BaseModel):
    """N2 PnL Settlement Placement"""
    __tablename__ = "n2_pnl_settlement_placement"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    placement_fee = Column(Float)
    placement_type = Column(String)

class N2PnlSettlementRemovalOrders(BaseModel):
    """N2 PnL Settlement Removal Orders"""
    __tablename__ = "n2_pnl_settlement_removal_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    removal_order_id = Column(String, unique=True, index=True)
    removal_cost = Column(Float)
    removal_type = Column(String)

class N2PnlSettlementSkuNoSku(BaseModel):
    """N2 PnL Settlement SKU No SKU"""
    __tablename__ = "n2_pnl_settlement_sku_no_sku"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    sku_status = Column(String)
    adjustment_amount = Column(Float)

class N2PnlSettlementStorageLongTerm(BaseModel):
    """N2 PnL Settlement Storage Long Term"""
    __tablename__ = "n2_pnl_settlement_storage_long_term"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    long_term_storage_fee = Column(Float)
    storage_period = Column(String)

class N2PnlSettlementStorageMonthly(BaseModel):
    """N2 PnL Settlement Storage Monthly"""
    __tablename__ = "n2_pnl_settlement_storage_monthly"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    monthly_storage_fee = Column(Float)
    storage_month = Column(Date)

class N2PnlSponsoredBrand(BaseModel):
    """N2 PnL Sponsored Brand"""
    __tablename__ = "n2_pnl_sponsored_brand"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    sponsored_brand_spend = Column(Float)
    sponsored_brand_revenue = Column(Float)

class N2PnlSponsoredDisplay(BaseModel):
    """N2 PnL Sponsored Display"""
    __tablename__ = "n2_pnl_sponsored_display"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    sponsored_display_spend = Column(Float)
    sponsored_display_revenue = Column(Float)

class N2PnlUnsettledOrders(BaseModel):
    """N2 PnL Unsettled Orders"""
    __tablename__ = "n2_pnl_unsettled_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    order_id = Column(String, unique=True, index=True)
    unsettled_amount = Column(Float)
    order_status = Column(String) 