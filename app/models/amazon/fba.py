from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date, DECIMAL
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class AmznFbaEstimatedFbaFeesTxtData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) estimated fee data for products
    
    Tracks estimated FBA fees for products to understand fulfillment costs and pricing 
    strategy in advance. Based on product dimensions, weight, and pricing, used for 
    cost analysis and pricing decisions.
    """
    __tablename__ = "amzn_fba_estimated_fba_fees_txt_data"
    
    fba_estimated_fba_fees_txt_data_id = Column(Integer, primary_key=True, index=True)
    
    # Product Identification
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text, index=True)
    amazon_store = Column(Text)
    product_name = Column(Text)
    product_group = Column(Text)
    brand = Column(Text)
    fulfilled_by = Column(Text)
    
    # Pricing Information
    your_price = Column(DECIMAL(10, 2))
    sales_price = Column(DECIMAL(10, 2))
    currency = Column(Text)
    
    # Product Dimensions
    longest_side = Column(DECIMAL(8, 2))
    median_side = Column(DECIMAL(8, 2))
    shortest_side = Column(DECIMAL(8, 2))
    length_and_girth = Column(DECIMAL(8, 2))
    unit_of_dimension = Column(Text)
    item_package_weight = Column(DECIMAL(8, 2))
    unit_of_weight = Column(Text)
    product_size_tier = Column(Text)
    
    # Estimated Fee Breakdown
    estimated_fee_total = Column(DECIMAL(10, 2))
    estimated_referral_fee_per_unit = Column(DECIMAL(10, 2))
    estimated_variable_closing_fee = Column(DECIMAL(10, 2))
    estimated_order_handling_fee_per_order = Column(DECIMAL(10, 2))
    estimated_pick_pack_fee_per_unit = Column(DECIMAL(10, 2))
    estimated_weight_handling_fee_per_unit = Column(DECIMAL(10, 2))
    expected_fulfillment_fee_per_unit = Column(DECIMAL(10, 2))
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznSettlementReportDataV2(BaseModel):
    """Amazon settlement report data - the primary source for all financial transactions
    
    Tracks all financial transactions from Amazon including sales, fees, refunds, and adjustments.
    This is the definitive source of truth for all financial transactions on Amazon, essential for 
    accurate profit/loss calculations, financial reporting, and business analysis.
    """
    __tablename__ = "amzn_settlement_report_data_v2"
    
    settlement_report_data_id = Column(Integer, primary_key=True, index=True)
    
    # Settlement Identification
    settlement_id = Column(Text, unique=True, index=True)
    settlement_start_date = Column(DateTime, index=True)
    settlement_end_date = Column(DateTime, index=True)
    deposit_date = Column(DateTime, index=True)
    total_amount = Column(DECIMAL(10, 2))
    currency = Column(Text)
    
    # Transaction Details
    transaction_type = Column(Text)
    amount = Column(DECIMAL(10, 2))
    amount_type = Column(Text)
    amount_description = Column(Text)
    posted_date = Column(Date, index=True)
    posted_date_time = Column(DateTime, index=True)
    
    # Order Information
    order_id = Column(Text, index=True)
    merchant_order_id = Column(Text)
    order_item_code = Column(Text)
    merchant_order_item_id = Column(Text)
    sku = Column(Text, index=True)
    quantity_purchased = Column(Integer)
    
    # Fulfillment Information
    fulfillment_id = Column(Text)
    shipment_id = Column(Text)
    marketplace_name = Column(Text)
    
    # Adjustment Information
    adjustment_id = Column(Text)
    merchant_adjustment_item_id = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaFulfillmentCustomerReturnsData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Customer Returns data
    
    Tracks products that customers have returned to Amazon. Crucial for inventory management,
    product quality analysis, financial impact assessment, customer service, and supply
    chain optimization.
    """
    __tablename__ = "amzn_fba_fulfillment_customer_returns_data"
    
    fba_fulfillment_customer_returns_data_id = Column(Integer, primary_key=True, index=True)
    
    # Return Identification
    order_id = Column(Text, index=True)
    return_date = Column(DateTime, index=True)
    license_plate_number = Column(Text)
    
    # Product Information
    sku = Column(Text, index=True)
    asin = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    product_name = Column(Text)
    quantity = Column(Integer)
    
    # Fulfillment Details
    fulfillment_center_id = Column(Text)
    detailed_disposition = Column(Text)
    status = Column(Text)
    reason = Column(Text)
    
    # Customer Feedback
    customer_comments = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznFbaFulfillmentCustomerShipmentReplacementData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Customer Shipment Replacement data
    
    Tracks when Amazon sends replacement items to customers due to issues with original 
    shipments. Crucial for inventory management, customer service analysis, financial 
    impact assessment, quality control, and supply chain optimization.
    """
    __tablename__ = "amzn_fba_fulfillment_customer_shipment_replacement_data"
    
    fba_fulfillment_customer_shipment_replacement_data_id = Column(Integer, primary_key=True, index=True)
    
    # Replacement Identification
    replacement_amazon_order_id = Column(Text, index=True)
    original_amazon_order_id = Column(Text, index=True)
    shipment_date = Column(DateTime, index=True)
    
    # Product Information
    sku = Column(Text, index=True)
    asin = Column(Text, index=True)
    quantity = Column(Integer)
    
    # Fulfillment Details
    fulfillment_center_id = Column(Text)
    original_fulfillment_center_id = Column(Text)
    replacement_reason_code = Column(Integer)
    
    # Processing Information
    grouped_rows_count = Column(Integer)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznFbaFulfillmentRemovalOrderDetailData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Removal Order Detail data
    
    Tracks when sellers request removal of inventory from Amazon's fulfillment centers.
    Crucial for inventory management, cost analysis, supply chain optimization,
    financial impact assessment, and operational efficiency monitoring.
    """
    __tablename__ = "amzn_fba_fulfillment_removal_order_detail_data"
    
    fba_fulfillment_removal_order_detail_id = Column(Integer, primary_key=True, index=True)
    
    # Order Identification
    order_id = Column(Text, index=True)
    request_date = Column(DateTime, index=True)
    last_updated_date = Column(DateTime)
    
    # Order Details
    order_source = Column(Text)
    order_type = Column(Text)
    order_status = Column(Text)
    
    # Product Information
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    disposition = Column(Text)
    
    # Quantity Tracking
    requested_quantity = Column(Integer)
    cancelled_quantity = Column(Integer)
    disposed_quantity = Column(Integer)
    shipped_quantity = Column(Integer)
    in_process_quantity = Column(Integer)
    
    # Financial Information
    removal_fee = Column(DECIMAL(10, 2))
    currency = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznFbaInboundShipmentItems(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Inbound Shipment Items data
    
    Tracks individual products within inbound shipments to Amazon's fulfillment centers.
    Crucial for inventory management, supply chain optimization, cost allocation,
    quality control, and financial impact assessment.
    """
    __tablename__ = "amzn_fba_inbound_shipment_items"
    
    fba_inbound_shipment_items_id = Column(Integer, primary_key=True, index=True)
    
    # Shipment Identification
    shipment_id = Column(Text, index=True)
    seller_sku = Column(Text, index=True)
    fulfillment_network_sku = Column(Text, index=True)
    
    # Quantity Tracking
    quantity_shipped = Column(Integer)
    quantity_received = Column(Integer)
    quantity_in_case = Column(Integer)
    
    # Timing and Release
    release_date = Column(DateTime)
    
    # Preparation Details
    prep_instruction = Column(Text)
    prep_owner = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaInboundShipmentTransportDetails(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Inbound Shipment Transport Details data
    
    Tracks transportation costs and details for inbound shipments to Amazon's fulfillment centers.
    Crucial for cost allocation, financial impact assessment, supply chain optimization,
    settlement reconciliation, and budget planning.
    """
    __tablename__ = "amzn_fba_inbound_shipment_transport_details"
    
    fba_inbound_shipment_transport_detail_id = Column(Integer, primary_key=True, index=True)
    
    # Transport Identification
    shipment_id = Column(Text, index=True)
    
    # Financial Information
    partnered_value = Column(DECIMAL(10, 2))
    void_deadline = Column(DateTime)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaInventoryPlanningData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Inventory Planning data
    
    Provides comprehensive inventory analysis and recommendations for optimizing FBA operations.
    Crucial for inventory optimization, cost management, sales performance analysis,
    planning recommendations, storage fee optimization, and supply chain planning.
    """
    __tablename__ = "amzn_fba_inventory_planning_data"
    
    fba_inventory_planning_data_id = Column(Integer, primary_key=True, index=True)
    
    # Basic Product Information
    snapshot_date = Column(Date, index=True)
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text, index=True)
    product_name = Column(Text)
    condition = Column(Text)
    
    # Inventory Levels
    available = Column(Integer)
    pending_removal_quantity = Column(Integer)
    reserved_quantity = Column(Integer)
    unfulfillable_quantity = Column(Integer)
    inbound_quantity = Column(Integer)
    inbound_working = Column(Integer)
    inbound_shipped = Column(Integer)
    inbound_received = Column(Integer)
    
    # Inventory Aging (Long-term Storage)
    inv_age_0_to_90_days = Column(Integer)
    inv_age_91_to_180_days = Column(Integer)
    inv_age_181_to_270_days = Column(Integer)
    inv_age_271_to_365_days = Column(Integer)
    inv_age_365_plus_days = Column(Integer)
    inv_age_0_to_30_days = Column(Integer)
    inv_age_31_to_60_days = Column(Integer)
    inv_age_61_to_90_days = Column(Integer)
    inv_age_181_to_330_days = Column(Integer)
    inv_age_331_to_365_days = Column(Integer)
    
    # Long-term Storage Fee Quantities
    quantity_to_be_charged_ais_181_to_210_days = Column(Integer)
    quantity_to_be_charged_ais_211_to_240_days = Column(Integer)
    quantity_to_be_charged_ais_241_to_270_days = Column(Integer)
    quantity_to_be_charged_ais_271_to_300_days = Column(Integer)
    quantity_to_be_charged_ais_301_to_330_days = Column(Integer)
    quantity_to_be_charged_ais_331_to_365_days = Column(Integer)
    quantity_to_be_charged_ais_365_plus_days = Column(Integer)
    
    # Long-term Storage Fee Estimates
    estimated_ais_181_to_210_days = Column(DECIMAL(10, 2))
    estimated_ais_211_to_240_days = Column(DECIMAL(10, 2))
    estimated_ais_241_to_270_days = Column(DECIMAL(10, 2))
    estimated_ais_271_to_300_days = Column(DECIMAL(10, 2))
    estimated_ais_301_to_330_days = Column(DECIMAL(10, 2))
    estimated_ais_331_to_365_days = Column(DECIMAL(10, 2))
    estimated_ais_365_plus_days = Column(DECIMAL(10, 2))
    
    # Sales Performance
    units_shipped_t7 = Column(Integer)
    units_shipped_t30 = Column(Integer)
    units_shipped_t60 = Column(Integer)
    units_shipped_t90 = Column(Integer)
    sales_shipped_last_7_days = Column(DECIMAL(10, 2))
    sales_shipped_last_30_days = Column(DECIMAL(10, 2))
    sales_shipped_last_60_days = Column(DECIMAL(10, 2))
    sales_shipped_last_90_days = Column(DECIMAL(10, 2))
    sell_through = Column(DECIMAL(5, 4))
    
    # Pricing Information
    currency = Column(Text)
    your_price = Column(DECIMAL(10, 2))
    sales_price = Column(DECIMAL(10, 2))
    lowest_price_new_plus_shipping = Column(DECIMAL(10, 2))
    lowest_price_used = Column(DECIMAL(10, 2))
    featuredoffer_price = Column(DECIMAL(10, 2))
    
    # Amazon Recommendations
    alert = Column(Text)
    recommended_action = Column(Text)
    recommended_sales_price = Column(DECIMAL(10, 2))
    recommended_sale_duration_days = Column(Integer)
    recommended_removal_quantity = Column(Integer)
    estimated_cost_savings_of_recommended_actions = Column(DECIMAL(10, 2))
    recommended_ship_in_quantity = Column(Integer)
    recommended_ship_in_date = Column(DateTime)
    
    # Supply Chain Metrics
    days_of_supply = Column(Integer)
    weeks_of_cover_t30 = Column(DECIMAL(5, 2))
    weeks_of_cover_t90 = Column(DECIMAL(5, 2))
    estimated_excess_quantity = Column(Integer)
    total_days_of_supply_including_units_from_open_shipments = Column(Integer)
    historical_days_of_supply = Column(DECIMAL(5, 2))
    short_term_historical_days_of_supply = Column(DECIMAL(5, 2))
    long_term_historical_days_of_supply = Column(DECIMAL(5, 2))
    
    # Storage and Volume
    item_volume = Column(DECIMAL(10, 4))
    volume_unit_measurement = Column(Text)
    storage_type = Column(Text)
    storage_volume = Column(DECIMAL(10, 4))
    estimated_storage_cost_next_month = Column(DECIMAL(10, 2))
    
    # Marketplace Information
    marketplace = Column(Text)
    product_group = Column(Text)
    sales_rank = Column(Integer)
    
    # Inventory Health
    fba_minimum_inventory_level = Column(Integer)
    fba_inventory_level_health_status = Column(Text)
    exempted_from_low_inventory_level_fee = Column(Text)
    low_inventory_level_fee_applied_in_current_week = Column(Text)
    
    # Additional Metrics
    no_sale_last_6_months = Column(Integer)
    inventory_supply_at_fba = Column(Integer)
    reserved_fc_transfer = Column(Integer)
    reserved_fc_processing = Column(Integer)
    reserved_customer_order = Column(Integer)
    
    # Timing and Status
    listed_date = Column(DateTime)
    unlisted_date = Column(DateTime)
    inventory_age_snapshot_date = Column(DateTime)
    last_updated_date_for_historical_days_of_supply = Column(DateTime)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaLongtermStorageFeeChargesData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) Long-term Storage Fee Charges data
    
    Tracks fees charged for inventory that has been stored in Amazon's fulfillment centers 
    for extended periods. Crucial for cost management, inventory optimization, financial 
    planning, compliance tracking, and performance analysis.
    """
    __tablename__ = "amzn_fba_longterm_storage_fee_charges_data"
    
    fba_longterm_storage_fee_charges_id = Column(Integer, primary_key=True, index=True)
    
    # Basic Product Information
    snapshot_date = Column(DateTime, index=True)
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text, index=True)
    product_name = Column(Text)
    condition = Column(Text)
    
    # Volume and Storage Information
    per_unit_volume = Column(DECIMAL(10, 4))
    volume_unit = Column(Text)
    country = Column(Text)
    
    # Financial Information
    currency = Column(Text)
    qty_charged = Column(Integer)
    amount_charged = Column(DECIMAL(10, 2))
    rate_surcharge = Column(DECIMAL(10, 4))
    
    # Age-based Surcharge Details
    surcharge_age_tier = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaMyiAllInventoryData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) inventory data showing current stock levels and status across all fulfillment centers
    
    Tracks real-time inventory levels, availability, and status across Amazon's fulfillment network.
    Crucial for inventory planning, stockout prevention, inbound tracking, and supply chain optimization.
    """
    __tablename__ = "amzn_fba_myi_all_inventory_data"
    
    fba_myi_all_inventory_id = Column(Integer, primary_key=True, index=True)
    
    # Product Identification
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text, index=True)
    product_name = Column(Text)
    condition = Column(Text)
    marketplace = Column(Text)
    
    # Pricing Information
    your_price = Column(DECIMAL(10, 2))
    
    # Fulfillment Channel Status
    mfn_listing_exists = Column(Text)
    mfn_fulfillable_quantity = Column(Integer)
    afn_listing_exists = Column(Text)
    
    # Current Inventory Levels (AFN - Amazon Fulfilled Network)
    afn_warehouse_quantity = Column(Integer)
    afn_fulfillable_quantity = Column(Integer)
    afn_unsellable_quantity = Column(Integer)
    afn_reserved_quantity = Column(Integer)
    afn_total_quantity = Column(Integer)
    
    # Inventory Metrics
    per_unit_volume = Column(DECIMAL(10, 4))
    
    # Inbound Inventory
    afn_inbound_working_quantity = Column(Integer)
    afn_inbound_shipped_quantity = Column(Integer)
    afn_inbound_receiving_quantity = Column(Integer)
    afn_researching_quantity = Column(Integer)
    
    # Future Supply
    afn_reserved_future_supply = Column(Integer)
    afn_future_supply_buyable = Column(Integer)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaReimbursementsData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) reimbursement data for lost, damaged, or incorrectly processed inventory
    
    Tracks reimbursements from Amazon for inventory issues and ensures proper financial accounting.
    Crucial for accurate financial reporting, inventory valuation, and recovering costs from 
    Amazon's operational issues.
    """
    __tablename__ = "amzn_fba_reimbursements_data"
    
    fba_reimbursements_data_id = Column(Integer, primary_key=True, index=True)
    
    # Reimbursement Identification
    approval_date = Column(DateTime, index=True)
    reimbursement_id = Column(Text, unique=True, index=True)
    case_id = Column(Text)
    amazon_order_id = Column(Text, index=True)
    original_reimbursement_id = Column(Text)
    original_reimbursement_type = Column(Text)
    
    # Product Information
    sku = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    asin = Column(Text, index=True)
    product_name = Column(Text)
    condition = Column(Text)
    
    # Reimbursement Details
    reason = Column(Text)
    currency_unit = Column(Text)
    amount_per_unit = Column(DECIMAL(10, 2))
    amount_total = Column(DECIMAL(10, 2))
    
    # Quantity Information
    quantity_reimbursed_cash = Column(Integer)
    quantity_reimbursed_inventory = Column(Integer)
    quantity_reimbursed_total = Column(Integer)
    
    # Processing Information
    grouped_rows_count = Column(Integer)
    previous_row_ids = Column(ARRAY(Integer))
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaStorageFeeChargesData(BaseModel):
    """Amazon FBA (Fulfillment by Amazon) monthly storage fee charges data for inventory stored in Amazon's fulfillment centers
    
    Tracks and analyzes monthly storage fees charged by Amazon for storing inventory in their fulfillment centers,
    enabling cost optimization and inventory management. Critical for understanding the true cost of FBA inventory storage.
    """
    __tablename__ = "amzn_fba_storage_fee_charges_data"
    
    fba_storage_fee_charges_id = Column(Integer, primary_key=True, index=True)
    
    # Product Identification
    asin = Column(Text, index=True)
    fnsku = Column(Text, index=True)
    product_name = Column(Text)
    fulfillment_center = Column(Text)
    country_code = Column(Text)
    
    # Product Dimensions and Weight
    longest_side = Column(DECIMAL(10, 4))
    median_side = Column(DECIMAL(10, 4))
    shortest_side = Column(DECIMAL(10, 4))
    measurement_units = Column(Text)
    weight = Column(DECIMAL(10, 4))
    weight_units = Column(Text)
    item_volume = Column(DECIMAL(10, 4))
    volume_units = Column(Text)
    product_size_tier = Column(Text)
    
    # Inventory Levels
    average_quantity_on_hand = Column(DECIMAL(10, 4))
    average_quantity_pending_removal = Column(DECIMAL(10, 4))
    estimated_total_item_volume = Column(DECIMAL(10, 4))
    average_quantity_customer_orders = Column(DECIMAL(10, 4))
    
    # Storage Fee Calculation
    month_of_charge = Column(Date, index=True)
    storage_utilization_ratio = Column(DECIMAL(10, 4))
    storage_utilization_ratio_units = Column(Text)
    base_rate = Column(DECIMAL(10, 4))
    utilization_surcharge_rate = Column(DECIMAL(10, 4))
    avg_qty_for_sus = Column(DECIMAL(10, 4))
    est_vol_for_sus = Column(DECIMAL(10, 4))
    est_base_msf = Column(DECIMAL(10, 2))
    est_sus = Column(DECIMAL(10, 2))
    estimated_monthly_storage_fee = Column(DECIMAL(10, 2))
    
    # Fee Details and Discounts
    currency = Column(Text)
    dangerous_goods_storage_type = Column(Text)
    eligible_for_inventory_discount = Column(Text)
    qualifies_for_inventory_discount = Column(Text)
    total_incentive_fee_amount = Column(DECIMAL(10, 2))
    breakdown_incentive_fee_amount = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)

class AmznFbaInboundShipments(BaseModel):
    """Amazon FBA Inbound Shipments"""
    __tablename__ = "amzn_fba_inbound_shipments"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your specific fields here based on your schema
    # Example fields (adjust according to your actual schema):
    shipment_id = Column(String, unique=True, index=True)
    shipment_name = Column(String)
    shipment_status = Column(String)
    shipment_date = Column(DateTime)
    destination_center = Column(String) 