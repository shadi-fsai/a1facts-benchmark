"""
Domain Authority Mapping for Source Reliability Assessment

This provides objective ground truth for website reliability ratings (A-F scale)
based on established authority metrics, regulatory recognition, and reputation.
"""

DOMAIN_AUTHORITY = {
    # ===== MEDICAL & HEALTH =====
    # A-tier: Government agencies, regulatory bodies, official medical organizations
    "nih.gov": "A",
    "cdc.gov": "A",
    "who.int": "A",
    "fda.gov": "A",
    "nejm.org": "A",  # New England Journal of Medicine
    "thelancet.com": "A",
    "bmj.com": "A",  # British Medical Journal
    
    # B-tier: Major academic medical centers, established institutions
    "mayoclinic.org": "B",
    "hopkinsmedicine.org": "B",
    "clevelandclinic.org": "B",
    "health.harvard.edu": "B",
    "stanfordhealthcare.org": "B",
    
    # C-tier: Commercial but established health information sites
    "webmd.com": "C",
    "healthline.com": "C",
    "medicalnewstoday.com": "C",
    "drugs.com": "C",
    
    # ===== FINANCIAL =====
    # A-tier: Government regulatory agencies, official sources
    "sec.gov": "A",
    "federalreserve.gov": "A",
    "treasury.gov": "A",
    "imf.org": "A",
    "worldbank.org": "A",
    
    # B-tier: Major financial news outlets, established institutions
    "reuters.com": "B",
    "bloomberg.com": "B",
    "wsj.com": "B",  # Wall Street Journal
    "ft.com": "B",  # Financial Times
    "economist.com": "B",
    
    # C-tier: Financial news with commercial interests
    "marketwatch.com": "C",
    "cnbc.com": "C",
    "yahoo.com/finance": "C",
    "fool.com": "C",  # Motley Fool
    
    # ===== NEWS & GENERAL =====
    # A-tier: Wire services, public broadcasters
    "apnews.com": "A",
    "reuters.com": "A",
    "bbc.com": "A",
    "pbs.org": "A",
    "npr.org": "A",
    
    # B-tier: Major newspapers, established news organizations
    "nytimes.com": "B",
    "washingtonpost.com": "B",
    "theguardian.com": "B",
    "usatoday.com": "B",
    
    # C-tier: News aggregators, mixed reliability
    "cnn.com": "C",
    "foxnews.com": "C",
    "msnbc.com": "C",
    "huffpost.com": "C",
    
    # ===== SCIENTIFIC & ACADEMIC =====
    # A-tier: Peer-reviewed journals, scientific organizations
    "nature.com": "A",
    "science.org": "A",
    "pnas.org": "A",
    "ieee.org": "A",
    
    # B-tier: University research sites, academic institutions
    "mit.edu": "B",
    "stanford.edu": "B",
    "harvard.edu": "B",
    "ox.ac.uk": "B",  # Oxford
    
    # ===== UNRELIABLE (E-tier) =====
    # Known misinformation, conspiracy, or unreliable sources
    "naturalnews.com": "E",
    "infowars.com": "E",
    "beforeitsnews.com": "E",
    "worldtruth.tv": "E",
}


def get_reliability_rating(url: str) -> str:
    """
    Get reliability rating for a URL based on domain authority.
    
    Args:
        url: Website URL (can be full URL or just domain)
        
    Returns:
        Reliability rating (A, B, C, D, E, or F)
    """
    # Extract domain from URL
    domain = url.lower()
    for prefix in ["https://", "http://", "www."]:
        domain = domain.replace(prefix, "")
    domain = domain.split("/")[0]
    
    # Check against known domains
    if domain in DOMAIN_AUTHORITY:
        return DOMAIN_AUTHORITY[domain]
    
    # Default to F (cannot be judged) for unknown domains
    return "F"


def get_domains_by_rating(rating: str) -> list:
    """Get all domains with a specific reliability rating."""
    return [domain for domain, r in DOMAIN_AUTHORITY.items() if r == rating]
