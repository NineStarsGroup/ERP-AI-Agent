# Models Organization

This directory contains all database models organized by category for better maintainability.

## Structure

```
app/models/
├── __init__.py          # Main models package - imports all models
├── base.py              # Base model with common fields (created_at)
├── models.py            # Backward compatibility file
├── legacy.py            # Original models (Customer, Product, Order, OrderItem)
├── README.md            # This file
├── amazon/              # Amazon-related models
│   ├── __init__.py      # Amazon models package
│   ├── ads.py           # Amazon Advertising models (4 tables)
│   ├── fba.py           # Amazon FBA models (13 tables) - COMPREHENSIVE
│   ├── orders/          # Amazon Orders models
│   │   ├── __init__.py
│   │   └── orders.py    # Order and returns data (4 tables)
│   ├── reports/         # Amazon Reports models
│   │   ├── __init__.py
│   │   └── reports.py   # Ledger and merchant data (7 tables)
│   ├── catalog/         # Amazon Catalog models
│   │   ├── __init__.py
│   │   └── catalog.py   # Product catalog data (4 tables)
│   ├── pnl/             # Amazon PnL models
│   │   ├── __init__.py
│   │   └── pnl.py       # Profit & Loss data (20 tables)
│   └── stage/           # Amazon Stage models
│       ├── __init__.py
│       └── stage.py     # Staging data for processing (30 tables)
└── supply_chain/        # Supply Chain models
    ├── __init__.py
    └── supply_chain.py  # Supply chain data (7 tables)
```

## Base Model

All models inherit from `BaseModel` which provides:
- `created_at`: DateTime field automatically set to UTC timestamp when record is created

## Model Categories

### Amazon Models

#### Advertising (`amazon/ads.py`)
- `AmznAdsSbCampaigns` - Sponsored Brands Campaigns
- `AmznAdsSdAdvertisedProduct` - Sponsored Display Advertised Products (COMPREHENSIVE)
- `AmznAdsSponsoredProducts` - Sponsored Products (COMPREHENSIVE)

#### FBA (`amazon/fba.py`) - **COMPREHENSIVE IMPLEMENTATION**
**All models include complete field mappings, proper data types, and detailed business context:**

- `AmznFbaEstimatedFbaFeesTxtData` - Estimated FBA fees for products based on dimensions, weight, and pricing
- `AmznSettlementReportDataV2` - **PRIMARY SOURCE** for all financial transactions (sales, fees, refunds, adjustments)
- `AmznFbaFulfillmentCustomerReturnsData` - Customer returns tracking for inventory management and quality analysis
- `AmznFbaFulfillmentCustomerShipmentReplacementData` - Shipment replacements due to issues with original shipments
- `AmznFbaFulfillmentRemovalOrderDetailData` - Removal orders from Amazon fulfillment centers
- `AmznFbaInboundShipmentItems` - Individual products within inbound shipments
- `AmznFbaInboundShipmentTransportDetails` - Transportation costs for inbound shipments
- `AmznFbaInventoryPlanningData` - **COMPREHENSIVE** inventory analysis with 80+ fields including aging, recommendations, and supply chain metrics
- `AmznFbaLongtermStorageFeeChargesData` - Long-term storage fees for extended inventory periods
- `AmznFbaMyiAllInventoryData` - Real-time inventory levels across all fulfillment centers
- `AmznFbaReimbursementsData` - Reimbursements for lost, damaged, or incorrectly processed inventory
- `AmznFbaStorageFeeChargesData` - Monthly storage fees with utilization surcharges and discounts
- `AmznFbaInboundShipments` - Basic inbound shipments (needs completion)

**Key Features of FBA Models:**
- Complete field mappings from SQL schemas
- Proper PostgreSQL data types (DECIMAL, TIMESTAMPTZ, JSONB, ARRAY)
- Logical field grouping with detailed comments
- Technical processing fields (job_execution_id, job_chunk_name, etc.)
- Business context documentation for each model
- Support for data deduplication and incremental processing

#### Orders (`amazon/orders/orders.py`)
- `AmznFlatFileAllOrdersDataByLastUpdateGeneral` - All Orders Data
- `AmznFlatFileReturnsDataByReturnDate` - Returns Data
- `AmznFlatFileReturnsDataByReturnDateCollect` - Returns Data Collect
- `AmznFlatFileReturnsDataByReturnDateDelete` - Returns Data Delete

#### Reports (`amazon/reports/reports.py`)
- `AmznLedgerDetailViewData` - Ledger Detail View
- `AmznLedgerDetailViewDataCollect` - Ledger Data Collect
- `AmznLedgerDetailViewDataProcess` - Ledger Data Process
- `AmznMerchantListingsAllData` - Merchant Listings
- `AmznMerchantListingsAllDataCollect` - Merchant Listings Collect
- `AmznMerchantListingsAllDataProcess` - Merchant Listings Process
- `ManualAmzFbaPlacementFee` - Manual FBA Placement Fee

#### Catalog (`amazon/catalog/catalog.py`)
- `N2Asins` - N2 ASINs
- `N2CatalogAliasMap` - Catalog Alias Map
- `N2CatalogKits` - Catalog Kits
- `N2CatalogPrimary` - Catalog Primary

#### PnL (`amazon/pnl/pnl.py`)
- `N2Pnl` - Main PnL
- `N2PnlAdvertising` - Advertising PnL
- `N2PnlCollect` - Collection PnL
- `N2PnlFbaReimbursements` - FBA Reimbursements
- `N2PnlFbaReplacements` - FBA Replacements
- `N2PnlFbaReturns` - FBA Returns
- `N2PnlFbmShippingNonAmzn` - FBM Shipping Non-Amazon
- `N2PnlSettlement` - Settlement PnL
- `N2PnlSettlementCogs` - Settlement COGS
- `N2PnlSettlementCustomerReturn` - Settlement Customer Return
- `N2PnlSettlementFbaInbound` - Settlement FBA Inbound
- `N2PnlSettlementPickPack` - Settlement Pick & Pack
- `N2PnlSettlementPlacement` - Settlement Placement
- `N2PnlSettlementRemovalOrders` - Settlement Removal Orders
- `N2PnlSettlementSkuNoSku` - Settlement SKU No SKU
- `N2PnlSettlementStorageLongTerm` - Settlement Storage Long Term
- `N2PnlSettlementStorageMonthly` - Settlement Storage Monthly
- `N2PnlSponsoredBrand` - Sponsored Brand PnL
- `N2PnlSponsoredDisplay` - Sponsored Display PnL
- `N2PnlUnsettledOrders` - Unsettled Orders

#### Stage (`amazon/stage/stage.py`)
- 30 stage models for data collection and processing

### Supply Chain Models (`supply_chain/supply_chain.py`)
- `ScCatalog` - Supply Chain Catalog
- `ScCatalogChild` - Supply Chain Catalog Child
- `ScOrders` - Supply Chain Orders
- `ScOrderItems` - Supply Chain Order Items
- `ScProductGroup` - Supply Chain Product Group
- `N2ScCogs` - Supply Chain COGS
- `TableSettings` - Table Settings

### Legacy Models (`legacy.py`)
- `Customer` - Customer information
- `Product` - Product catalog
- `Order` - Order records
- `OrderItem` - Order line items

## Usage

### Import all models
```python
from app.models import *
```

### Import specific categories
```python
from app.models.amazon.ads import AmznAdsSbCampaigns
from app.models.amazon.fba import AmznFbaMyiAllInventoryData, AmznSettlementReportDataV2
from app.models.legacy import Customer, Product
```

### Import base classes
```python
from app.models.base import Base, BaseModel
```

## Adding New Models

1. **Create new model file** in appropriate category directory
2. **Inherit from BaseModel** to get `created_at` field
3. **Add to `__init__.py`** in the category directory
4. **Update main `__init__.py`** to import and export the new model

Example:
```python
# app/models/amazon/new_category.py
from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMPTZ, JSONB
from sqlalchemy.dialects.postgresql import ARRAY

class NewModel(BaseModel):
    __tablename__ = "new_table"
    
    new_model_id = Column(Integer, primary_key=True, index=True)
    
    # Business fields
    name = Column(String)
    amount = Column(DECIMAL(10, 2))
    
    # Technical processing fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(String)
    job_chunk_fetched_at = Column(TIMESTAMPTZ)
    extra = Column(JSONB)
```

## Data Processing Flow

The models support a comprehensive data processing pipeline:

1. **Source Data**: Amazon APIs and reports
2. **Staging**: Raw data collection in stage models
3. **Processing**: Data transformation and enrichment
4. **Storage**: Final data in business models
5. **Analysis**: PnL calculations and business intelligence

## Technical Features

- **PostgreSQL Optimization**: Uses native PostgreSQL types (DECIMAL, TIMESTAMPTZ, JSONB, ARRAY)
- **Data Deduplication**: Support for `previous_row_ids` arrays
- **Incremental Processing**: Job execution tracking for efficient updates
- **Error Handling**: Comprehensive error tracking and recovery
- **Performance**: Proper indexing on key business fields
- **Scalability**: Modular design supports large-scale data processing

## Data Processing Flow

The models support a comprehensive data processing pipeline:

1. **Source Data**: Amazon APIs and reports
2. **Staging**: Raw data collection in stage models
3. **Processing**: Data transformation and enrichment
4. **Storage**: Final data in business models
5. **Analysis**: PnL calculations and business intelligence

## Technical Features

- **PostgreSQL Optimization**: Uses native PostgreSQL types (DECIMAL, TIMESTAMPTZ, JSONB, ARRAY)
- **Data Deduplication**: Support for `previous_row_ids` arrays
- **Incremental Processing**: Job execution tracking for efficient updates
- **Error Handling**: Comprehensive error tracking and recovery
- **Performance**: Proper indexing on key business fields
- **Scalability**: Modular design supports large-scale data processing

## Notes

- All models automatically get a `created_at` timestamp field
- Models are organized by business domain (Amazon, Legacy, etc.)
- Each category can be further subdivided as needed
- The structure supports easy addition of new model categories
- FBA models include comprehensive business documentation
- Support for 97+ total tables across all categories 