from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date, BIGINT, DECIMAL
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class AmznAdsSbCampaigns(BaseModel):
    """Amazon Sponsored Brands advertising campaign data
    
    Tracks brand awareness and new customer acquisition campaigns on Amazon.
    Appears at the top of Amazon search results with brand logo and multiple products,
    focusing on brand discovery rather than individual product sales.
    """
    __tablename__ = "amzn_ads_sb_campaigns"
    
    amzn_ads_sb_campaigns_id = Column(Integer, primary_key=True, index=True)
    
    # Campaign Identification
    campaign_id = Column(BIGINT, index=True)
    campaign_name = Column(Text)
    profile_id = Column(Text)
    date = Column(Date, index=True)
    
    # Financial Metrics
    cost = Column(DECIMAL(10, 2))
    campaign_budget_amount = Column(DECIMAL(10, 2))
    campaign_budget_currency_code = Column(Text)
    campaign_budget_type = Column(Text)
    cost_type = Column(Text)
    
    # Performance Metrics
    impressions = Column(Integer)
    clicks = Column(Integer)
    view_click_through_rate = Column(DECIMAL(5, 4))
    viewability_rate = Column(DECIMAL(5, 4))
    top_of_search_impression_share = Column(DECIMAL(5, 4))
    viewable_impressions = Column(Integer)
    
    # Sales Attribution
    sales = Column(DECIMAL(10, 2))
    sales_clicks = Column(DECIMAL(10, 2))
    sales_promoted = Column(DECIMAL(10, 2))
    units_sold = Column(Integer)
    units_sold_clicks = Column(Integer)
    purchases = Column(Integer)
    purchases_clicks = Column(Integer)
    purchases_promoted = Column(Integer)
    
    # New Customer Acquisition (Most Important for Sponsored Brands)
    new_to_brand_sales = Column(DECIMAL(10, 2))
    new_to_brand_sales_clicks = Column(DECIMAL(10, 2))
    new_to_brand_sales_percentage = Column(DECIMAL(5, 4))
    new_to_brand_purchases = Column(Integer)
    new_to_brand_purchases_clicks = Column(Integer)
    new_to_brand_purchases_percentage = Column(DECIMAL(5, 4))
    new_to_brand_purchases_rate = Column(DECIMAL(5, 4))
    new_to_brand_units_sold = Column(Integer)
    new_to_brand_units_sold_clicks = Column(Integer)
    new_to_brand_units_sold_percentage = Column(DECIMAL(5, 4))
    
    # Engagement Metrics
    detail_page_views = Column(Integer)
    detail_page_views_clicks = Column(Integer)
    new_to_brand_detail_page_views = Column(Integer)
    new_to_brand_detail_page_views_clicks = Column(Integer)
    new_to_brand_detail_page_view_rate = Column(DECIMAL(5, 4))
    add_to_cart = Column(Integer)
    add_to_cart_clicks = Column(Integer)
    add_to_cart_rate = Column(DECIMAL(5, 4))
    add_to_list = Column(Integer)
    add_to_list_from_clicks = Column(Integer)
    ecp_add_to_cart = Column(DECIMAL(10, 2))
    
    # Brand Awareness
    branded_searches = Column(Integer)
    branded_searches_clicks = Column(Integer)
    
    # Video Metrics
    video_complete_views = Column(Integer)
    video_first_quartile_views = Column(Integer)
    video_midpoint_views = Column(Integer)
    video_third_quartile_views = Column(Integer)
    video_5_second_views = Column(Integer)
    video_5_second_view_rate = Column(DECIMAL(5, 4))
    video_unmutes = Column(Integer)
    
    # Specialized Metrics
    qualified_borrows = Column(Integer)
    qualified_borrows_from_clicks = Column(Integer)
    royalty_qualified_borrows = Column(Integer)
    royalty_qualified_borrows_from_clicks = Column(Integer)
    new_to_brand_ecp_detail_page_view = Column(DECIMAL(10, 2))
    
    # Campaign Status
    campaign_status = Column(Text)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznAdsSdAdvertisedProduct(BaseModel):
    """Amazon Sponsored Display advertising product-level data
    
    Tracks display advertising performance at the product level across Amazon's display network.
    Shows ads on Amazon's display network (product pages, shopping results, etc.) and targets
    customers based on shopping behavior and interests.
    """
    __tablename__ = "amzn_ads_sd_advertised_product"
    
    ads_sd_advertised_product_id = Column(Integer, primary_key=True, index=True)
    
    # Product Identification
    promoted_sku = Column(Text, index=True)
    promoted_asin = Column(Text, index=True)
    ad_id = Column(BIGINT, index=True)
    ad_group_id = Column(BIGINT, index=True)
    ad_group_name = Column(Text)
    campaign_id = Column(BIGINT, index=True)
    campaign_name = Column(Text)
    profile_id = Column(Text)
    date = Column(Date, index=True)
    
    # Financial Metrics
    cost = Column(DECIMAL(10, 2))
    campaign_budget_currency_code = Column(Text)
    bid_optimization = Column(Text)
    
    # Performance Metrics
    impressions = Column(Integer)
    impressions_views = Column(Integer)
    clicks = Column(Integer)
    view_click_through_rate = Column(DECIMAL(5, 4))
    viewability_rate = Column(DECIMAL(5, 4))
    impressions_frequency_average = Column(DECIMAL(5, 2))
    
    # Sales Attribution
    sales = Column(DECIMAL(10, 2))
    sales_clicks = Column(DECIMAL(10, 2))
    sales_promoted_clicks = Column(DECIMAL(10, 2))
    units_sold = Column(Integer)
    units_sold_clicks = Column(Integer)
    purchases = Column(Integer)
    purchases_clicks = Column(Integer)
    purchases_promoted_clicks = Column(Integer)
    
    # New Customer Acquisition
    new_to_brand_sales = Column(DECIMAL(10, 2))
    new_to_brand_sales_clicks = Column(DECIMAL(10, 2))
    new_to_brand_purchases = Column(Integer)
    new_to_brand_purchases_clicks = Column(Integer)
    new_to_brand_units_sold = Column(Integer)
    new_to_brand_units_sold_clicks = Column(Integer)
    
    # Engagement Metrics
    detail_page_views = Column(Integer)
    detail_page_views_clicks = Column(Integer)
    new_to_brand_detail_page_views = Column(Integer)
    new_to_brand_detail_page_view_clicks = Column(Integer)
    new_to_brand_detail_page_view_views = Column(Integer)
    new_to_brand_detail_page_view_rate = Column(DECIMAL(5, 4))
    add_to_cart = Column(Integer)
    add_to_cart_clicks = Column(Integer)
    add_to_cart_views = Column(Integer)
    add_to_cart_rate = Column(DECIMAL(5, 4))
    add_to_list = Column(Integer)
    add_to_list_from_clicks = Column(Integer)
    add_to_list_from_views = Column(Integer)
    
    # Brand Awareness
    branded_searches = Column(Integer)
    branded_searches_clicks = Column(Integer)
    branded_searches_views = Column(Integer)
    branded_search_rate = Column(DECIMAL(5, 4))
    
    # Video Metrics
    video_complete_views = Column(Integer)
    video_first_quartile_views = Column(Integer)
    video_midpoint_views = Column(Integer)
    video_third_quartile_views = Column(Integer)
    video_unmutes = Column(Integer)
    
    # Specialized Metrics
    qualified_borrows = Column(Integer)
    qualified_borrows_from_clicks = Column(Integer)
    qualified_borrows_from_views = Column(Integer)
    royalty_qualified_borrows = Column(Integer)
    royalty_qualified_borrows_from_clicks = Column(Integer)
    royalty_qualified_borrows_from_views = Column(Integer)
    leads = Column(Integer)
    lead_form_opens = Column(Integer)
    link_outs = Column(Integer)
    cumulative_reach = Column(Integer)
    new_to_brand_ecp_detail_page_view = Column(DECIMAL(10, 2))
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznAdsSponsoredProducts(BaseModel):
    """Amazon Sponsored Products advertising data at the product level
    
    Tracks performance of individual product advertising campaigns in Amazon search results.
    Shows individual products in Amazon search results and product pages when customers
    search for relevant keywords, focusing on driving immediate sales for specific products.
    """
    __tablename__ = "amzn_ads_sponsored_products"
    
    sponsored_products_advertised_product_id = Column(Integer, primary_key=True, index=True)
    
    # Product Identification
    advertised_sku = Column(Text, index=True)
    advertised_asin = Column(Text, index=True)
    campaign_name = Column(Text)
    ad_group_name = Column(Text)
    portfolio_id = Column(BIGINT, index=True)
    profile_id = Column(Text)
    date = Column(Date, index=True)
    
    # Financial Metrics
    spend = Column(DECIMAL(10, 2))
    campaign_budget_currency_code = Column(Text)
    cost_per_click = Column(DECIMAL(10, 4))
    acos_clicks7d = Column(DECIMAL(5, 4))
    roas_clicks7d = Column(DECIMAL(5, 4))
    
    # Performance Metrics
    impressions = Column(Integer)
    clicks = Column(Integer)
    click_through_rate = Column(DECIMAL(5, 4))
    
    # Sales Attribution (7-day window)
    sales7d = Column(DECIMAL(10, 2))
    purchases7d = Column(DECIMAL(10, 2))
    units_sold_same_sku7d = Column(Integer)
    units_sold_other_sku7d = Column(Integer)
    attributed_sales_same_sku7d = Column(DECIMAL(10, 2))
    sales_other_sku7d = Column(DECIMAL(10, 2))
    units_sold_clicks7d = Column(DECIMAL(10, 2))
    
    # Sales Attribution (30-day window)
    sales30d = Column(DECIMAL(10, 2))
    purchases30d = Column(DECIMAL(10, 2))
    units_sold_same_sku30d = Column(Integer)
    
    # Technical Processing Fields
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    previous_row_ids = Column(ARRAY(Integer))
    extra = Column(JSONB)

class AmznAdsSbPurchasedProduct(BaseModel):
    """Amazon Sponsored Brands Purchased Product data with 14-day attribution metrics"""
    __tablename__ = "amzn_ads_sb_purchased_product"

    amzn_ads_sb_purchased_product_id = Column(Integer, primary_key=True, index=True)

    # Date/profile
    date = Column(Date, index=True)
    profile_id = Column(Text)

    # Campaign / Ad group context
    campaign_id = Column(BIGINT, index=True)
    campaign_name = Column(Text)
    campaign_price_type_code = Column(Text)
    campaign_budget_currency_code = Column(Text)
    ad_group_id = Column(BIGINT, index=True)
    ad_group_name = Column(Text)
    attribution_type = Column(Text)

    # Product
    purchased_asin = Column(Text, index=True)
    product_name = Column(Text)
    product_category = Column(Text)

    # 14-day performance metrics
    sales_14d = Column(DECIMAL(10, 2))
    orders_14d = Column(Integer)
    units_sold_14d = Column(Integer)
    sales_clicks_14d = Column(DECIMAL(10, 2))
    orders_clicks_14d = Column(Integer)
    units_sold_clicks_14d = Column(Integer)

    # New-to-brand metrics (14d)
    new_to_brand_sales_14d = Column(DECIMAL(10, 2))
    new_to_brand_purchases_14d = Column(Integer)
    new_to_brand_units_sold_14d = Column(Integer)
    new_to_brand_sales_percentage_14d = Column(DECIMAL(5, 4))
    new_to_brand_purchases_percentage_14d = Column(DECIMAL(5, 4))
    new_to_brand_units_sold_percentage_14d = Column(DECIMAL(5, 4))

    # Processing metadata
    previous_row_ids = Column(ARRAY(Integer))
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)


class AmznAdsSpSearchTerm(BaseModel):
    """Amazon Sponsored Products Search Terms performance data"""
    __tablename__ = "amzn_ads_sp_search_term"

    sp_search_term_id = Column(Integer, primary_key=True, index=True)

    # Core performance metrics
    impressions = Column(Integer)
    add_to_list = Column(Integer)
    qualified_borrows = Column(Integer)
    royalty_qualified_borrows = Column(Integer)
    clicks = Column(Integer)
    cost_per_click = Column(DECIMAL(10, 4))
    click_through_rate = Column(DECIMAL(5, 4))
    cost = Column(DECIMAL(10, 2))

    # Attribution windows (purchases)
    purchases1d = Column(DECIMAL(10, 2))
    purchases7d = Column(DECIMAL(10, 2))
    purchases14d = Column(DECIMAL(10, 2))
    purchases30d = Column(DECIMAL(10, 2))
    purchases_same_sku1d = Column(DECIMAL(10, 2))
    purchases_same_sku7d = Column(DECIMAL(10, 2))
    purchases_same_sku14d = Column(DECIMAL(10, 2))
    purchases_same_sku30d = Column(DECIMAL(10, 2))

    # Attribution windows (units)
    units_sold_clicks1d = Column(Integer)
    units_sold_clicks7d = Column(Integer)
    units_sold_clicks14d = Column(Integer)
    units_sold_clicks30d = Column(Integer)

    # Attribution windows (sales)
    sales1d = Column(DECIMAL(10, 2))
    sales7d = Column(DECIMAL(10, 2))
    sales14d = Column(DECIMAL(10, 2))
    sales30d = Column(DECIMAL(10, 2))
    attributed_sales_same_sku1d = Column(DECIMAL(10, 2))
    attributed_sales_same_sku7d = Column(DECIMAL(10, 2))
    attributed_sales_same_sku14d = Column(DECIMAL(10, 2))
    attributed_sales_same_sku30d = Column(DECIMAL(10, 2))
    units_sold_same_sku1d = Column(Integer)
    units_sold_same_sku7d = Column(Integer)
    units_sold_same_sku14d = Column(Integer)
    units_sold_same_sku30d = Column(Integer)

    # Kindle-specific
    kindle_edition_normalized_pages_read14d = Column(Integer)
    kindle_edition_normalized_pages_royalties14d = Column(DECIMAL(10, 2))

    # Other SKU performance
    sales_other_sku7d = Column(DECIMAL(10, 2))
    units_sold_other_sku7d = Column(Integer)

    # Efficiency metrics
    acos_clicks7d = Column(DECIMAL(10, 4))
    acos_clicks14d = Column(DECIMAL(10, 4))
    roas_clicks7d = Column(DECIMAL(10, 4))
    roas_clicks14d = Column(DECIMAL(10, 4))

    # Keyword and search term context
    keyword_id = Column(BIGINT, index=True)
    keyword = Column(Text)
    search_term = Column(Text, index=True)
    keyword_type = Column(Text)
    match_type = Column(Text)
    targeting = Column(Text)
    ad_keyword_status = Column(Text)
    keyword_bid = Column(DECIMAL(10, 4))

    # Campaign and ad group
    campaign_id = Column(BIGINT, index=True)
    campaign_name = Column(Text)
    ad_group_id = Column(BIGINT, index=True)
    ad_group_name = Column(Text)
    portfolio_id = Column(BIGINT, index=True)
    campaign_budget_currency_code = Column(Text)
    campaign_budget_type = Column(Text)
    campaign_budget_amount = Column(DECIMAL(10, 2))
    campaign_status = Column(Text)

    # Date/profile
    date = Column(Date, index=True)
    profile_id = Column(Text)

    # Processing metadata
    previous_row_ids = Column(ARRAY(Integer))
    job_execution_id = Column(Integer)
    job_chunk_name = Column(Text)
    job_chunk_fetched_at = Column(DateTime(timezone=True))
    extra = Column(JSONB)