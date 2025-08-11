# Import base models
from .base import Base, BaseModel

# Import Amazon models
from .amazon.ads import (
    AmznAdsSbCampaigns,
    AmznAdsSdAdvertisedProduct,
    AmznAdsSponsoredProducts,
    AmznAdsSbPurchasedProduct
)

from .amazon.fba import (
    AmznFbaEstimatedFbaFeesTxtData,
    AmznSettlementReportDataV2,
    AmznFbaFulfillmentCustomerReturnsData,
    AmznFbaFulfillmentCustomerShipmentReplacementData,
    AmznFbaFulfillmentRemovalOrderDetailData,
    AmznFbaInboundShipmentItems,
    AmznFbaInboundShipmentTransportDetails,
    AmznFbaInboundShipments,
    AmznFbaInventoryPlanningData,
    AmznFbaLongtermStorageFeeChargesData,
    AmznFbaMyiAllInventoryData,
    AmznFbaReimbursementsData,
    AmznFbaStorageFeeChargesData
)

from .amazon.orders.orders import (
    AmznFlatFileAllOrdersDataByLastUpdateGeneral,
    AmznFlatFileReturnsDataByReturnDate,
    AmznFlatFileReturnsDataByReturnDateCollect,
    AmznFlatFileReturnsDataByReturnDateDelete
)

from .amazon.reports.reports import (
    AmznLedgerDetailViewData,
    AmznLedgerDetailViewDataCollect,
    AmznLedgerDetailViewDataProcess,
    AmznMerchantListingsAllData,
    AmznMerchantListingsAllDataCollect,
    AmznMerchantListingsAllDataProcess,
    ManualAmzFbaPlacementFee
)

from .amazon.catalog.catalog import (
    N2Asins,
    N2CatalogAliasMap,
    N2CatalogKits,
    N2CatalogPrimary
)

from .amazon.pnl.pnl import (
    N2Pnl,
    N2PnlAdvertising,
    N2PnlCollect,
    N2PnlFbaReimbursements,
    N2PnlFbaReplacements,
    N2PnlFbaReturns,
    N2PnlFbmShippingNonAmzn,
    N2PnlSettlement,
    N2PnlSettlementCogs,
    N2PnlSettlementCustomerReturn,
    N2PnlSettlementFbaInbound,
    N2PnlSettlementPickPack,
    N2PnlSettlementPlacement,
    N2PnlSettlementRemovalOrders,
    N2PnlSettlementSkuNoSku,
    N2PnlSettlementStorageLongTerm,
    N2PnlSettlementStorageMonthly,
    N2PnlSponsoredBrand,
    N2PnlSponsoredDisplay,
    N2PnlUnsettledOrders
)

from .amazon.stage.stage import (
    StageAmznFlatFileReturnsDataByReturnDateCollect,
    StageAmznFlatFileReturnsDataByReturnDateDelete,
    StageAmznLedgerDetailViewDataCollect,
    StageAmznLedgerDetailViewDataProcess,
    StageAmznMerchantListingsAllDataCollect,
    StageAmznMerchantListingsAllDataProcess,
    StageAmznSettlementReportDataV2,
    StageN2AmznSettlementSummary,
    StageN2Asins,
    StageN2CatalogAliasMap,
    StageN2CatalogKits,
    StageN2CatalogPrimary,
    StageN2PnlAdvertising,
    StageN2PnlCollect,
    StageN2PnlFbaReimbursements,
    StageN2PnlFbaReplacements,
    StageN2PnlFbaReturns,
    StageN2PnlFbmShippingNonAmzn,
    StageN2PnlSettlement,
    StageN2PnlSettlementCogs,
    StageN2PnlSettlementCustomerReturn,
    StageN2PnlSettlementFbaInbound,
    StageN2PnlSettlementPickPack,
    StageN2PnlSettlementPlacement,
    StageN2PnlSettlementRemovalOrders,
    StageN2PnlSettlementSkuNoSku,
    StageN2PnlSettlementStorageLongTerm,
    StageN2PnlSettlementStorageMonthly,
    StageN2PnlSponsoredBrand,
    StageN2PnlSponsoredDisplay
)

from .supply_chain.supply_chain import (
    ScCatalog,
    ScCatalogChild,
    ScOrders,
    ScOrderItems,
    ScProductGroup,
    N2ScCogs,
    TableSettings
)

# Import legacy models (your original models)
from .legacy import Customer, Product, Order, OrderItem

# Export all models
__all__ = [
    # Base
    'Base',
    'BaseModel',
    
    # Amazon Ads
    'AmznAdsSbCampaigns',
    'AmznAdsSdAdvertisedProduct', 
    'AmznAdsSponsoredProducts',
    'AmznAdsSbPurchasedProduct',
    
    # Amazon FBA
    'AmznFbaEstimatedFbaFeesTxtData',
    'AmznSettlementReportDataV2',
    'AmznFbaFulfillmentCustomerReturnsData',
    'AmznFbaFulfillmentCustomerShipmentReplacementData',
    'AmznFbaFulfillmentRemovalOrderDetailData',
    'AmznFbaInboundShipmentItems',
    'AmznFbaInboundShipmentTransportDetails',
    'AmznFbaInboundShipments',
    'AmznFbaInventoryPlanningData',
    'AmznFbaLongtermStorageFeeChargesData',
    'AmznFbaMyiAllInventoryData',
    'AmznFbaReimbursementsData',
    'AmznFbaStorageFeeChargesData',
    
    # Amazon Orders
    'AmznFlatFileAllOrdersDataByLastUpdateGeneral',
    'AmznFlatFileReturnsDataByReturnDate',
    'AmznFlatFileReturnsDataByReturnDateCollect',
    'AmznFlatFileReturnsDataByReturnDateDelete',
    
    # Amazon Reports
    'AmznLedgerDetailViewData',
    'AmznLedgerDetailViewDataCollect',
    'AmznLedgerDetailViewDataProcess',
    'AmznMerchantListingsAllData',
    'AmznMerchantListingsAllDataCollect',
    'AmznMerchantListingsAllDataProcess',
    'ManualAmzFbaPlacementFee',
    
    # Amazon Catalog
    'N2Asins',
    'N2CatalogAliasMap',
    'N2CatalogKits',
    'N2CatalogPrimary',
    
    # Amazon PnL
    'N2Pnl',
    'N2PnlAdvertising',
    'N2PnlCollect',
    'N2PnlFbaReimbursements',
    'N2PnlFbaReplacements',
    'N2PnlFbaReturns',
    'N2PnlFbmShippingNonAmzn',
    'N2PnlSettlement',
    'N2PnlSettlementCogs',
    'N2PnlSettlementCustomerReturn',
    'N2PnlSettlementFbaInbound',
    'N2PnlSettlementPickPack',
    'N2PnlSettlementPlacement',
    'N2PnlSettlementRemovalOrders',
    'N2PnlSettlementSkuNoSku',
    'N2PnlSettlementStorageLongTerm',
    'N2PnlSettlementStorageMonthly',
    'N2PnlSponsoredBrand',
    'N2PnlSponsoredDisplay',
    'N2PnlUnsettledOrders',
    
    # Amazon Stage
    'StageAmznFlatFileReturnsDataByReturnDateCollect',
    'StageAmznFlatFileReturnsDataByReturnDateDelete',
    'StageAmznLedgerDetailViewDataCollect',
    'StageAmznLedgerDetailViewDataProcess',
    'StageAmznMerchantListingsAllDataCollect',
    'StageAmznMerchantListingsAllDataProcess',
    'StageAmznSettlementReportDataV2',
    'StageN2AmznSettlementSummary',
    'StageN2Asins',
    'StageN2CatalogAliasMap',
    'StageN2CatalogKits',
    'StageN2CatalogPrimary',
    'StageN2PnlAdvertising',
    'StageN2PnlCollect',
    'StageN2PnlFbaReimbursements',
    'StageN2PnlFbaReplacements',
    'StageN2PnlFbaReturns',
    'StageN2PnlFbmShippingNonAmzn',
    'StageN2PnlSettlement',
    'StageN2PnlSettlementCogs',
    'StageN2PnlSettlementCustomerReturn',
    'StageN2PnlSettlementFbaInbound',
    'StageN2PnlSettlementPickPack',
    'StageN2PnlSettlementPlacement',
    'StageN2PnlSettlementRemovalOrders',
    'StageN2PnlSettlementSkuNoSku',
    'StageN2PnlSettlementStorageLongTerm',
    'StageN2PnlSettlementStorageMonthly',
    'StageN2PnlSponsoredBrand',
    'StageN2PnlSponsoredDisplay',
    
    # Supply Chain
    'ScCatalog',
    'ScCatalogChild',
    'ScOrders',
    'ScOrderItems',
    'ScProductGroup',
    'N2ScCogs',
    'TableSettings',
    
    # Legacy
    'Customer',
    'Product', 
    'Order',
    'OrderItem'
] 