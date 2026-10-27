"""Site-wide settings for PanamaExpatLife.com."""

SITE_NAME = "Panama Expat Life"
SITE_URL = "https://panamaexpatlife.com"
SITE_TAGLINE = "Practical, local guidance for moving to and living in Panama"
LANG = "en-CA"
LAST_CHECKED = "2026-10-27"          # ISO date shown as "Last checked" on pages
LAST_CHECKED_HUMAN = "October 2026"

# Kit (kit.com) form ID for the free checklist sign-up.
# Leave empty until the Kit form exists; the page then shows a "sign-up opens soon" note
# instead of a form that goes nowhere. The checklist itself is always visible as text.
KIT_FORM_ID = ""

PANAMA_PROPERTIES_URL = "https://www.panama-properties.com"
PANAMA_PROPERTIES_BUY_URL = "https://www.panama-properties.com/client-contact-form"

# Main navigation, in reading order. (slug, label)
NAV = [
    ("start-here", "Start here"),
    ("residency", "Residency"),
    ("cost-of-living", "Cost of living"),
    ("healthcare", "Healthcare"),
    ("money", "Money"),
    ("moving", "Moving"),
    ("where-to-live", "Where to live"),
    ("housing", "Housing"),
]
