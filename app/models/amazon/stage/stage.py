from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

# Stage models for data collection and processing
class StageAmznFlatFileReturnsDataByReturnDateCollect(BaseModel):
    """Stage Amazon Flat File Returns Data by Return Date Collect"""
    __tablename__ = "stage_amzn_flat_file_returns_data_by_return_date_collect"
    
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

class StageAmznFlatFileReturnsDataByReturnDateDelete(BaseModel):
    """Stage Amazon Flat File Returns Data by Return Date Delete"""
    __tablename__ = "stage_amzn_flat_file_returns_data_by_return_date_delete"
    
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

class StageAmznLedgerDetailViewDataCollect(BaseModel):
    """Stage Amazon Ledger Detail View Data Collect"""
    __tablename__ = "stage_amzn_ledger_detail_view_data_collect"
    
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

class StageAmznLedgerDetailViewDataProcess(BaseModel):
    """Stage Amazon Ledger Detail View Data Process"""
    __tablename__ = "stage_amzn_ledger_detail_view_data_process"
    
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

class StageAmznMerchantListingsAllDataCollect(BaseModel):
    """Stage Amazon Merchant Listings All Data Collect"""
    __tablename__ = "stage_amzn_merchant_listings_all_data_collect"
    
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

class StageAmznMerchantListingsAllDataProcess(BaseModel):
    """Stage Amazon Merchant Listings All Data Process"""
    __tablename__ = "stage_amzn_merchant_listings_all_data_process"
    
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

class StageAmznSettlementReportDataV2(BaseModel):
    """Stage Amazon Settlement Report Data V2"""
    __tablename__ = "stage_amzn_settlement_report_data_v2"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    settlement_id = Column(String, unique=True, index=True)
    settlement_start_date = Column(Date)
    settlement_end_date = Column(Date)
    total_amount = Column(Float)
    currency = Column(String)
    stage_status = Column(String)

class StageN2AmznSettlementSummary(BaseModel):
    """Stage N2 Amazon Settlement Summary"""
    __tablename__ = "stage_n2_amzn_settlement_summary"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    settlement_id = Column(String, unique=True, index=True)
    settlement_period = Column(String)
    total_amount = Column(Float)
    stage_status = Column(String)

class StageN2Asins(BaseModel):
    """Stage N2 ASINs"""
    __tablename__ = "stage_n2_asins"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, unique=True, index=True)
    product_name = Column(String)
    brand = Column(String)
    category = Column(String)
    stage_status = Column(String)

class StageN2CatalogAliasMap(BaseModel):
    """Stage N2 Catalog Alias Map"""
    __tablename__ = "stage_n2_catalog_alias_map"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    alias_id = Column(String, unique=True, index=True)
    primary_asin = Column(String, index=True)
    alias_asin = Column(String, index=True)
    alias_type = Column(String)
    stage_status = Column(String)

class StageN2CatalogKits(BaseModel):
    """Stage N2 Catalog Kits"""
    __tablename__ = "stage_n2_catalog_kits"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    kit_id = Column(String, unique=True, index=True)
    kit_name = Column(String)
    kit_asin = Column(String, index=True)
    component_asin = Column(String, index=True)
    quantity = Column(Integer)
    stage_status = Column(String)

class StageN2CatalogPrimary(BaseModel):
    """Stage N2 Catalog Primary"""
    __tablename__ = "stage_n2_catalog_primary"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    asin = Column(String, unique=True, index=True)
    product_name = Column(String)
    brand = Column(String)
    category = Column(String)
    stage_status = Column(String)

class StageN2PnlAdvertising(BaseModel):
    """Stage N2 PnL Advertising"""
    __tablename__ = "stage_n2_pnl_advertising"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    ad_spend = Column(Float)
    ad_revenue = Column(Float)
    ad_profit = Column(Float)
    stage_status = Column(String)

class StageN2PnlCollect(BaseModel):
    """Stage N2 PnL Collect"""
    __tablename__ = "stage_n2_pnl_collect"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    collection_type = Column(String)
    amount = Column(Float)
    collection_date = Column(DateTime)
    stage_status = Column(String)

class StageN2PnlFbaReimbursements(BaseModel):
    """Stage N2 PnL FBA Reimbursements"""
    __tablename__ = "stage_n2_pnl_fba_reimbursements"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    reimbursement_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    reimbursement_amount = Column(Float)
    reimbursement_reason = Column(String)
    stage_status = Column(String)

class StageN2PnlFbaReplacements(BaseModel):
    """Stage N2 PnL FBA Replacements"""
    __tablename__ = "stage_n2_pnl_fba_replacements"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    replacement_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    replacement_cost = Column(Float)
    replacement_reason = Column(String)
    stage_status = Column(String)

class StageN2PnlFbaReturns(BaseModel):
    """Stage N2 PnL FBA Returns"""
    __tablename__ = "stage_n2_pnl_fba_returns"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    return_id = Column(String, unique=True, index=True)
    asin = Column(String, index=True)
    return_cost = Column(Float)
    return_reason = Column(String)
    stage_status = Column(String)

class StageN2PnlFbmShippingNonAmzn(BaseModel):
    """Stage N2 PnL FBM Shipping Non-Amazon"""
    __tablename__ = "stage_n2_pnl_fbm_shipping_non_amzn"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    order_id = Column(String, index=True)
    shipping_cost = Column(Float)
    shipping_carrier = Column(String)
    shipping_method = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlement(BaseModel):
    """Stage N2 PnL Settlement"""
    __tablename__ = "stage_n2_pnl_settlement"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    settlement_id = Column(String, unique=True, index=True)
    settlement_amount = Column(Float)
    settlement_date = Column(DateTime)
    stage_status = Column(String)

class StageN2PnlSettlementCogs(BaseModel):
    """Stage N2 PnL Settlement COGS"""
    __tablename__ = "stage_n2_pnl_settlement_cogs"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    cogs_amount = Column(Float)
    cogs_type = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementCustomerReturn(BaseModel):
    """Stage N2 PnL Settlement Customer Return"""
    __tablename__ = "stage_n2_pnl_settlement_customer_return"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    return_id = Column(String, unique=True, index=True)
    return_amount = Column(Float)
    return_reason = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementFbaInbound(BaseModel):
    """Stage N2 PnL Settlement FBA Inbound"""
    __tablename__ = "stage_n2_pnl_settlement_fba_inbound"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    shipment_id = Column(String, index=True)
    inbound_cost = Column(Float)
    inbound_type = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementPickPack(BaseModel):
    """Stage N2 PnL Settlement Pick & Pack"""
    __tablename__ = "stage_n2_pnl_settlement_pick_pack"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    order_id = Column(String, index=True)
    pick_pack_fee = Column(Float)
    weight_handling = Column(Float)
    stage_status = Column(String)

class StageN2PnlSettlementPlacement(BaseModel):
    """Stage N2 PnL Settlement Placement"""
    __tablename__ = "stage_n2_pnl_settlement_placement"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    placement_fee = Column(Float)
    placement_type = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementRemovalOrders(BaseModel):
    """Stage N2 PnL Settlement Removal Orders"""
    __tablename__ = "stage_n2_pnl_settlement_removal_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    removal_order_id = Column(String, unique=True, index=True)
    removal_cost = Column(Float)
    removal_type = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementSkuNoSku(BaseModel):
    """Stage N2 PnL Settlement SKU No SKU"""
    __tablename__ = "stage_n2_pnl_settlement_sku_no_sku"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    sku_status = Column(String)
    adjustment_amount = Column(Float)
    stage_status = Column(String)

class StageN2PnlSettlementStorageLongTerm(BaseModel):
    """Stage N2 PnL Settlement Storage Long Term"""
    __tablename__ = "stage_n2_pnl_settlement_storage_long_term"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    long_term_storage_fee = Column(Float)
    storage_period = Column(String)
    stage_status = Column(String)

class StageN2PnlSettlementStorageMonthly(BaseModel):
    """Stage N2 PnL Settlement Storage Monthly"""
    __tablename__ = "stage_n2_pnl_settlement_storage_monthly"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    asin = Column(String, index=True)
    monthly_storage_fee = Column(Float)
    storage_month = Column(Date)
    stage_status = Column(String)

class StageN2PnlSponsoredBrand(BaseModel):
    """Stage N2 PnL Sponsored Brand"""
    __tablename__ = "stage_n2_pnl_sponsored_brand"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    sponsored_brand_spend = Column(Float)
    sponsored_brand_revenue = Column(Float)
    stage_status = Column(String)

class StageN2PnlSponsoredDisplay(BaseModel):
    """Stage N2 PnL Sponsored Display"""
    __tablename__ = "stage_n2_pnl_sponsored_display"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    period_id = Column(String, index=True)
    campaign_id = Column(String, index=True)
    sponsored_display_spend = Column(Float)
    sponsored_display_revenue = Column(Float)
    stage_status = Column(String) 