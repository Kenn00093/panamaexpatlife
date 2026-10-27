"""Page content for PanamaExpatLife.com.

Every page is plain HTML written into static files at build time, so search engines and
AI answer engines read the full text without running any JavaScript.

Each page: slug, title (the <title>), h1, description (meta description), lead (a short
direct answer shown first; this is what answer engines tend to quote), body (HTML),
faq (list of (question, answer) pairs, also emitted as FAQPage structured data), related.
Use Canadian/British spelling: neighbourhood, colour, centre, licence (noun).
"""

from config import PANAMA_PROPERTIES_BUY_URL, PANAMA_PROPERTIES_URL

# ---------------------------------------------------------------------------
# Section pages
# ---------------------------------------------------------------------------

PAGES = [
# ---------------------------------------------------------------- START HERE
{
"slug": "start-here",
"title": "Moving to Panama: Where to Begin | Panama Expat Life",
"h1": "Moving to Panama: where to begin",
"kicker": "Start here",
"description": "A plain-English roadmap for moving to Panama: visit first, choose a region, pick a residency route, sort healthcare and banking, then rent before you buy.",
"lead": "Most successful moves to Panama follow the same order: visit first, choose a region, pick a residency route, sort out healthcare and banking, then rent for six to twelve months before you buy anything. Doing it in that order saves people the most money and the most regret.",
"body": """
<h2 id="roadmap">The move, step by step</h2>
<ol class="steps">
  <li><strong>Visit with a purpose.</strong> Spend at least two weeks, ideally in the season you like least. Rainy-season afternoons, highland chill and coastal heat feel very different from a dry-season holiday.</li>
  <li><strong>Narrow it to one or two regions.</strong> Panama City, the Pacific beaches, the Chiriqu&iacute; highlands, the Azuero Peninsula and the Caribbean side each suit different people. See <a href="/where-to-live/">Where to live</a>.</li>
  <li><strong>Choose a residency route.</strong> Retirees usually look at the Pensionado visa; working-age movers often look at Friendly Nations. See <a href="/residency/">Residency</a>.</li>
  <li><strong>Hire your own immigration lawyer.</strong> Residency in Panama is filed through a Panamanian attorney. Pick one before you start gathering documents, because each route needs different paperwork, apostilles and translations.</li>
  <li><strong>Plan healthcare.</strong> Decide between local private insurance and an international plan before you arrive. See <a href="/healthcare/">Healthcare</a>.</li>
  <li><strong>Start on banking early.</strong> Opening a Panamanian bank account can take weeks and usually needs reference letters from your home bank. See <a href="/money/">Money</a>.</li>
  <li><strong>Decide what to bring.</strong> Pets, household goods and cars each have their own process. See <a href="/moving/">Moving</a>.</li>
  <li><strong>Rent before you buy.</strong> Six to twelve months in a rental tells you more about a town than any number of visits. See <a href="/housing/">Housing</a>.</li>
</ol>

<h2 id="right-for-you">Is Panama right for you?</h2>
<p>Panama suits people who want a US-dollar economy, a relatively easy residency process for retirees, good private hospitals in the larger centres and a wide choice of climates within a few hours' drive. It is a less natural fit for anyone who wants things to work the way they do at home.</p>
<div class="two-col">
  <div>
    <h3>What people tend to love</h3>
    <ul>
      <li>The US dollar is legal tender, so there's no exchange-rate risk for dollar earners.</li>
      <li>Retiree residency (Pensionado) is among the more accessible in the region, with lifetime discounts.</li>
      <li>Climate choice: cool mountain towns, dry Pacific beaches and the Caribbean, all in one small country.</li>
      <li>Panama City has modern private hospitals and direct flights to much of the Americas and Europe.</li>
    </ul>
  </div>
  <div>
    <h3>What takes adjusting to</h3>
    <ul>
      <li>Bureaucracy is paper-heavy and slow, and rules change.</li>
      <li>Outside Panama City, specialist care can mean a drive of several hours.</li>
      <li>Imported goods and air-conditioned electricity cost more than many people expect.</li>
      <li>Spanish matters more than you think once you leave the expat bubble.</li>
    </ul>
  </div>
</div>

<h2 id="lessons">What expats wish they'd known</h2>
<p>We're interviewing people who have made the move to every region of Panama, and adding their lessons here as we go. The themes that come up most often so far:</p>
<ul>
  <li>Rent first. Almost everyone who bought in their first month would do it differently.</li>
  <li>Start Spanish lessons before you arrive, even an hour a week.</li>
  <li>Keep a home-country bank account and card open; local banking takes time.</li>
  <li>Build in buffer time for every government process.</li>
</ul>

<h2 id="checklist">Get the free move checklist</h2>
<p>Our <a href="/free-checklist/">free Panama move checklist</a> turns everything on this page into a month-by-month timeline, from twelve months out to your first week in the country.</p>
""",
"faq": [
("What is the first step in moving to Panama?",
 "Visit first, for at least two weeks and ideally in the season you like least, then narrow your search to one or two regions before choosing a residency route."),
("Should I rent or buy when I first move to Panama?",
 "Rent for six to twelve months first. Living in a town through both seasons tells you far more than short visits, and it avoids the most common and most expensive mistake new arrivals make."),
("Do I need a lawyer to get residency in Panama?",
 "Yes. Residency applications in Panama are filed through a Panamanian attorney, so choose one before you start gathering documents."),
],
"related": ["residency", "where-to-live", "housing"],
},

# ---------------------------------------------------------------- RESIDENCY
{
"slug": "residency",
"title": "Panama Residency Visas Explained: Pensionado, Friendly Nations, Investor | Panama Expat Life",
"h1": "Panama residency visas explained",
"kicker": "Residency",
"description": "How Panama's main residency routes work in 2026: the Pensionado retiree visa, the Friendly Nations visa and the Qualified Investor programme, with who each one suits.",
"lead": "Most people moving to Panama use one of three routes. Retirees with a lifetime pension of at least US$1,000 a month usually choose the Pensionado visa. Citizens of eligible countries with a qualifying job offer or a US$200,000 property or bank deposit often use Friendly Nations. Larger investors can use the Qualified Investor programme, whose rules were overhauled in September 2026.",
"body": """
<p class="notice"><strong>Rules change often.</strong> Everything below was checked in <time datetime="2026-10-27">October 2026</time> against current published guidance. Always confirm the details with your own Panamanian immigration lawyer before you apply, transfer money or buy property for residency.</p>

<h2 id="compare">The three main routes compared</h2>
<div class="table-wrap">
<table>
  <caption>Main Panama residency routes, October 2026</caption>
  <thead><tr><th scope="col">Route</th><th scope="col">Main requirement</th><th scope="col">Status</th><th scope="col">Best for</th></tr></thead>
  <tbody>
    <tr><th scope="row">Pensionado</th><td>Lifetime pension of US$1,000/month, or US$750/month plus Panamanian property worth over US$100,000</td><td>Permanent from the start</td><td>Retirees</td></tr>
    <tr><th scope="row">Friendly Nations</th><td>Citizenship of an eligible country, plus a qualifying job offer, or US$200,000 in property or a 3-year bank deposit</td><td>Two-year provisional, then permanent</td><td>Working-age movers, remote workers with savings</td></tr>
    <tr><th scope="row">Qualified Investor</th><td>Large investment in property, securities or a bank deposit; amounts depend on the route (see below)</td><td>Permanent</td><td>Investors who want a fast, permanent outcome</td></tr>
  </tbody>
</table>
</div>

<h2 id="pensionado">How does the Pensionado visa work?</h2>
<p>The Pensionado (retiree) visa is for anyone receiving a lifetime pension from a government, an international organisation or a legally operating private company. The usual threshold is <strong>US$1,000 a month</strong>. If you own Panamanian property worth more than US$100,000, the pension threshold drops to <strong>US$750 a month</strong>. Couples can generally combine pensions, and there is no minimum age beyond being an adult.</p>
<p>Pensionado holders receive permanent residency and, under a separate law, a set of well-known discounts on things like entertainment, hotels, public transport, flights, restaurants, medicines and doctors' visits.</p>

<h2 id="friendly-nations">How does the Friendly Nations visa work?</h2>
<p>Friendly Nations is open to citizens of a list of countries Panama considers friendly, which includes Canada, the United States, the United Kingdom and most of Europe. The list was most recently set out in an executive decree in August 2026, so check your country is still on it.</p>
<p>You then qualify in one of three ways:</p>
<ul>
  <li><strong>Employment:</strong> a job with a registered Panamanian company, which has to obtain a work permit for you.</li>
  <li><strong>Property:</strong> real estate in your name with a registered value of at least US$200,000.</li>
  <li><strong>Bank deposit:</strong> US$200,000 in a three-year fixed deposit at a Panamanian bank.</li>
</ul>
<p>You first receive a two-year provisional residency, then apply for permanent residency. Permanent residents can usually apply for citizenship after five years.</p>

<h2 id="qualified-investor">How does the Qualified Investor programme work?</h2>
<p>The Qualified Investor programme gives permanent residency in return for a larger investment, and it is usually the fastest route. Its rules were rewritten by a new executive decree that took effect in <strong>September 2026</strong>, and published summaries still disagree on some details. Current guidance describes minimums of around:</p>
<ul>
  <li>US$300,000 for a brand-new property bought directly from the developer</li>
  <li>US$500,000 for resale property, securities, or a deposit at a state bank</li>
  <li>US$750,000 for a fixed deposit at a private bank</li>
</ul>
<p>A five-year holding period applies. Because this programme changed so recently, treat these figures as a starting point for a conversation with your lawyer, not a basis for a purchase.</p>

<h2 id="before-you-apply">Before you apply</h2>
<ul>
  <li>Most routes need a police record check, apostilled documents and Spanish translations.</li>
  <li>Applications are filed through a Panamanian attorney, not by you directly.</li>
  <li>Citizens of Canada, the US and many European countries can usually visit as tourists for up to 180 days while preparing, but check your own nationality's current entry rules.</li>
</ul>
""",
"faq": [
("How much pension do I need for Panama's Pensionado visa?",
 "Generally a lifetime pension of US$1,000 a month, or US$750 a month if you also own Panamanian property worth more than US$100,000. Confirm current figures with a Panamanian immigration lawyer."),
("How much do I need to invest for the Panama Friendly Nations visa?",
 "If you don't qualify through a job offer, the usual options are property with a registered value of at least US$200,000 or a US$200,000 three-year deposit at a Panamanian bank."),
("Is Canada a Friendly Nations country for Panama?",
 "Yes. Canada, the United States, the United Kingdom and most European countries are on Panama's Friendly Nations list, which was last set out in an executive decree in August 2026."),
("What changed with Panama's Qualified Investor visa in 2026?",
 "A new executive decree took effect in September 2026. It created different minimums for new property from a developer and for resale property, and added a five-year holding period. Check current amounts with a lawyer before investing."),
],
"related": ["start-here", "money", "housing"],
},

# ---------------------------------------------------------------- COST OF LIVING
{
"slug": "cost-of-living",
"title": "Cost of Living in Panama: What Expats Really Spend | Panama Expat Life",
"h1": "The real cost of living in Panama",
"kicker": "Cost of living",
"description": "What drives the cost of living in Panama for expats: housing, electricity and air conditioning, food, healthcare and how costs differ between Panama City, the beaches, the highlands and Azuero.",
"lead": "Panama is cheaper than most of North America and Western Europe, but not as cheap as its reputation. Your biggest variables are where you live, how much you use air conditioning, and whether you shop like a local or buy imported brands. A household that rents outside Panama City, eats local produce and uses little air conditioning spends far less than one living in a city tower on imported groceries.",
"body": """
<h2 id="what-drives-costs">What drives your monthly costs</h2>
<div class="table-wrap">
<table>
  <caption>Main cost drivers for expats in Panama</caption>
  <thead><tr><th scope="col">Cost</th><th scope="col">Tends to be cheaper when&hellip;</th><th scope="col">Tends to be pricier when&hellip;</th></tr></thead>
  <tbody>
    <tr><th scope="row">Housing</th><td>You live outside Panama City and rent long-term from a local owner</td><td>You want a furnished ocean-view apartment in the city or a gated beach community</td></tr>
    <tr><th scope="row">Electricity</th><td>You live in the cooler highlands, where few homes need air conditioning</td><td>You run air conditioning day and night on the coast or in the city</td></tr>
    <tr><th scope="row">Groceries</th><td>You buy local fruit, vegetables, rice, chicken and fish</td><td>You buy imported brands, wine and cheese</td></tr>
    <tr><th scope="row">Healthcare</th><td>You use local private clinics and local insurance</td><td>You need an international plan or travel for specialist care</td></tr>
    <tr><th scope="row">Transport</th><td>You live in a walkable town or the city and use taxis and buses</td><td>You need a car for a rural or beach property</td></tr>
  </tbody>
</table>
</div>

<h2 id="by-region">How costs differ by region</h2>
<ul>
  <li><strong>Panama City:</strong> the highest housing costs and the widest choice of everything else. You may not need a car.</li>
  <li><strong>Pacific beaches (Coronado and nearby):</strong> moderate housing costs, but most people need a car and air conditioning.</li>
  <li><strong>Chiriqu&iacute; highlands (Boquete, Volc&aacute;n):</strong> mild temperatures keep electricity bills low; Boquete housing costs more than Volc&aacute;n.</li>
  <li><strong>Azuero Peninsula (Pedas&iacute;, Las Tablas, Chitr&eacute;):</strong> often among the more affordable regions, with a strong local culture and fewer imported goods on the shelves.</li>
  <li><strong>Bocas del Toro:</strong> island logistics make many goods more expensive, and boat transport adds up.</li>
</ul>

<h2 id="budget-tips">Ways expats keep costs down</h2>
<ul>
  <li>Shop at local markets and fruit stands rather than only at large supermarkets.</li>
  <li>Choose a home with good cross-ventilation, shade and ceiling fans.</li>
  <li>Use Pensionado discounts if you qualify.</li>
  <li>Rent before buying, so you learn the real costs of a town before committing.</li>
</ul>

<p>We're building town-by-town monthly budgets from real expat households. Join our <a href="/free-checklist/">free checklist list</a> to get them when they're published.</p>
""",
"faq": [
("Is Panama cheap to live in?",
 "Panama is cheaper than most of North America and Western Europe, but not as cheap as some neighbouring countries. Where you live, your air-conditioning use and how much imported food you buy make the biggest difference."),
("What is the most expensive part of living in Panama?",
 "For most expats it is housing, especially in Panama City. On the coast and in the city, electricity for air conditioning is often the second surprise."),
("Where is the cheapest place to live in Panama for expats?",
 "Smaller towns on the Azuero Peninsula and in the Chiriqu&iacute; highlands outside Boquete tend to be among the more affordable, though choice of housing and services is more limited."),
],
"related": ["where-to-live", "housing", "healthcare"],
},

# ---------------------------------------------------------------- HEALTHCARE
{
"slug": "healthcare",
"title": "Healthcare in Panama for Expats: Insurance, Hospitals and Costs | Panama Expat Life",
"h1": "Healthcare in Panama for expats",
"kicker": "Healthcare",
"description": "How healthcare works for expats in Panama: private vs public care, local vs international health insurance, and where the main hospitals are by region.",
"lead": "Most expats in Panama use private hospitals and clinics, paid for with either a local Panamanian insurance plan or an international plan. Panama City has the country's largest and best-equipped private hospitals; regional cities such as David and Chitr&eacute; cover most everyday needs, and complex or specialist care usually means a trip to the capital.",
"body": """
<h2 id="public-private">Public or private care?</h2>
<p>Panama has a public system run through the Ministry of Health and the Social Security Fund (CSS), mainly used by Panamanian workers and their families. Most foreign residents use the private system instead, where appointments are faster and English is more widely spoken, especially in Panama City.</p>

<h2 id="insurance">Local vs international health insurance</h2>
<div class="table-wrap">
<table>
  <caption>Choosing health insurance in Panama</caption>
  <thead><tr><th scope="col"></th><th scope="col">Local Panamanian plan</th><th scope="col">International plan</th></tr></thead>
  <tbody>
    <tr><th scope="row">Cost</th><td>Usually lower</td><td>Usually higher</td></tr>
    <tr><th scope="row">Coverage area</th><td>Mainly Panama</td><td>Several countries, sometimes including the US or Canada</td></tr>
    <tr><th scope="row">Age limits</th><td>Many plans limit new applicants by age</td><td>Often more flexible for older applicants</td></tr>
    <tr><th scope="row">Best for</th><td>People who will receive almost all care in Panama</td><td>People who travel a lot or want the option of treatment abroad</td></tr>
  </tbody>
</table>
</div>
<p>Pre-existing conditions and age limits vary a lot between insurers. An independent broker who works with several companies can compare plans for you at no extra cost.</p>

<h2 id="hospitals">Where the hospitals are</h2>
<ul>
  <li><strong>Panama City:</strong> the largest private hospitals in the country and most specialists.</li>
  <li><strong>Chiriqu&iacute; (Boquete, Volc&aacute;n, David):</strong> private hospitals in David, about 45 minutes from Boquete.</li>
  <li><strong>Azuero (Pedas&iacute;, Las Tablas):</strong> hospitals and private clinics in Chitr&eacute; and Las Tablas.</li>
  <li><strong>Pacific beaches (Coronado):</strong> local clinics, with Panama City roughly an hour or more away depending on traffic.</li>
  <li><strong>Bocas del Toro:</strong> basic care on the islands; serious cases are usually flown to Panama City or David.</li>
</ul>
<p>We're adding a detailed hospital and clinic guide for each region, with what each one handles.</p>

<h2 id="medicines">Pharmacies and medicines</h2>
<p>Pharmacies are common in towns of any size, and many medicines that need a prescription at home can be bought with less paperwork, though controlled drugs still need one. Bring a supply of your regular medications and their generic names when you move.</p>
""",
"faq": [
("Do expats need health insurance in Panama?",
 "It isn't required for every residency route, but almost all expats should have it. Private care is affordable compared with North America, but serious treatment can still be very expensive without insurance."),
("Is healthcare in Panama good?",
 "Private hospitals in Panama City are modern and well equipped, and many doctors trained abroad. Care outside the capital is more limited, so complex treatment usually means travelling to Panama City."),
("What is the best health insurance for expats in Panama?",
 "It depends on your age, health and travel plans. Local plans are cheaper but mainly cover Panama; international plans cost more but cover treatment abroad. An independent broker can compare both."),
],
"related": ["money", "where-to-live", "cost-of-living"],
},

# ---------------------------------------------------------------- MONEY
{
"slug": "money",
"title": "Banking and Money in Panama for Expats | Panama Expat Life",
"h1": "Banking and money in Panama",
"kicker": "Money",
"description": "Panama uses the US dollar. How expats open a Panamanian bank account, move money to Panama, and what Panama's territorial tax system means.",
"lead": "Panama uses the US dollar as its everyday currency, alongside its own balboa coins, so there's no exchange rate to worry about if you earn in US dollars. Opening a local bank account is slower than most people expect: banks usually want reference letters, proof of income and an in-person visit, so start early and keep your home-country accounts open.",
"body": """
<h2 id="currency">Currency</h2>
<p>The US dollar is legal tender in Panama. The Panamanian balboa is pegged one-to-one to the dollar and exists mainly as coins, which you'll get in change alongside US coins. Cards are widely accepted in Panama City; cash is still king in small towns and at markets.</p>

<h2 id="bank-account">Opening a bank account as a foreigner</h2>
<p>Panamanian banks follow strict know-your-customer rules. Expect to provide:</p>
<ul>
  <li>Your passport and a second form of ID</li>
  <li>A reference letter from your current bank, and sometimes a professional reference</li>
  <li>Proof of income or the source of your funds</li>
  <li>Proof of address</li>
</ul>
<p>Requirements vary by bank and change over time. US citizens may find some banks more cautious because of US reporting rules. Many people find the process easier once they have residency, or with an introduction from their lawyer.</p>

<h2 id="moving-money">Moving money to Panama</h2>
<p>A traditional international wire works, but bank fees and exchange margins (if you're converting from Canadian dollars, pounds or euros) add up. Specialist currency transfer services often offer better rates for larger amounts, such as a property purchase or a residency deposit. Compare the total cost, not just the fee.</p>

<h2 id="tax">Tax basics</h2>
<p>Panama uses a territorial tax system: in general, it taxes income earned in Panama, not income from abroad. That doesn't remove obligations at home. US citizens, for example, are taxed on worldwide income wherever they live, and other countries have their own residency rules. Speak to a tax adviser who understands both countries before you move.</p>
""",
"faq": [
("What currency does Panama use?",
 "The US dollar. Panama's own currency, the balboa, is pegged one-to-one to the dollar and is used mainly as coins."),
("Can a foreigner open a bank account in Panama?",
 "Yes, but expect to provide reference letters, proof of income or source of funds and proof of address, and usually to visit in person. It often takes several weeks."),
("Does Panama tax foreign income?",
 "Panama generally taxes only income earned in Panama. Your home country may still tax you, so get advice from a tax professional who knows both systems."),
],
"related": ["residency", "moving", "housing"],
},

# ---------------------------------------------------------------- MOVING
{
"slug": "moving",
"title": "Moving to Panama: Pets, Household Goods and Cars | Panama Expat Life",
"h1": "Moving your life to Panama",
"kicker": "Moving",
"description": "How to bring your dog or cat to Panama, whether to ship household goods or buy new, and what to know about bringing a car.",
"lead": "The three big logistics questions are your pets, your belongings and your car. Pets can come with an endorsed health certificate, up-to-date rabies vaccination and advance notice to Panama's health ministry. Most people ship far less than they expect, because shipping, import paperwork and Panama's climate make many household items a poor fit.",
"body": """
<h2 id="pets">Bringing a dog or cat to Panama</h2>
<p>For dogs and cats travelling from the United States, the current process is:</p>
<ol class="steps">
  <li><strong>Rabies vaccination</strong> from three months of age, with at least 30 days between the first rabies shot and travel. Pets under four months old aren't admitted.</li>
  <li><strong>Health certificate</strong> from an accredited veterinarian, endorsed by the national veterinary authority (APHIS in the US).</li>
  <li><strong>Panamanian consular stamp</strong> on the endorsed certificate before travel.</li>
  <li><strong>Home quarantine notice</strong> sent to Panama's Ministry of Health at least three days before arrival, with your flight details.</li>
</ol>
<p>Pets normally complete a short home quarantine rather than staying in a facility. Requirements from Canada, the UK and Europe follow a similar pattern but differ in the details, and airlines have their own rules, so check with your vet and airline early. A pet relocation service can handle the paperwork if you'd rather not.</p>

<h2 id="household-goods">Ship your belongings or buy new?</h2>
<ul>
  <li><strong>Worth bringing:</strong> things that are expensive or hard to find in Panama, such as good kitchen knives, quality bedding, specialist tools, sports gear and anything sentimental.</li>
  <li><strong>Usually not worth shipping:</strong> large furniture, especially upholstered pieces and particleboard that suffer in humidity, and appliances that may not suit local power or parts supply.</li>
  <li><strong>Pensionado holders</strong> can usually import household goods with a one-time duty exemption up to a set value. Confirm the current limit with your lawyer before you book a container.</li>
</ul>

<h2 id="cars">Bringing a car</h2>
<p>You can import a vehicle, but duties, shipping and paperwork often make it cheaper to buy in Panama, where most popular models are sold and serviced. Pensionado holders have historically had vehicle import benefits; check the current terms before deciding.</p>
<p>Visitors can usually drive on a valid foreign licence for a limited period (commonly 90 days); residents need to switch to a Panamanian licence.</p>
""",
"faq": [
("Can I bring my dog to Panama?",
 "Yes. You'll need a current rabies vaccination, an endorsed health certificate stamped by a Panamanian consulate, and to notify Panama's Ministry of Health at least three days before arrival. Most pets then complete a short home quarantine."),
("Do pets have to go into quarantine in Panama?",
 "Usually only home quarantine, provided the paperwork is in order and the Ministry of Health has been notified before arrival."),
("Should I ship my furniture to Panama?",
 "Usually not. Humidity is hard on upholstered and particleboard furniture, and shipping plus import paperwork often costs more than buying locally. Bring smaller, high-value and sentimental items instead."),
],
"related": ["start-here", "money", "residency"],
},

# ---------------------------------------------------------------- WHERE TO LIVE
{
"slug": "where-to-live",
"title": "Where to Live in Panama: Expat Regions Compared | Panama Expat Life",
"h1": "Where to live in Panama",
"kicker": "Where to live",
"description": "Panama's main expat regions compared: Panama City, the Pacific beaches, El Valle, the Chiriqu&iacute; highlands and coast, the Azuero Peninsula, the Veraguas coast, the Caribbean and the islands.",
"lead": "Expats in Panama mostly settle in nine regions. Panama City offers convenience and healthcare; the Pacific beaches around Coronado offer easy access to the city; Boquete and Volc&aacute;n offer a cool mountain climate; the Azuero Peninsula offers authentic small-town life and surf; and Bocas del Toro offers Caribbean island living. The right choice depends mostly on climate, how close you want to be to a major hospital, and how much you want an established expat community.",
"body": """
<h2 id="regions">The nine expat regions at a glance</h2>
<div class="table-wrap">
<table>
  <caption>Panama's expat regions compared</caption>
  <thead><tr><th scope="col">Region</th><th scope="col">Towns and areas</th><th scope="col">Climate</th><th scope="col">Suits people who want&hellip;</th></tr></thead>
  <tbody>
    <tr><th scope="row">Panama City</th><td>Casco Viejo, El Cangrejo, Costa del Este, Punta Pacifica, Clayton, Panama Pacifico</td><td>Hot and humid</td><td>Convenience, top hospitals, restaurants, an international airport</td></tr>
    <tr><th scope="row">Pacific beaches</th><td>Coronado, Gorgona, San Carlos, Playa Blanca, Santa Clara, Farallon</td><td>Hot, one of the drier parts of the country</td><td>Beach life within reach of the city</td></tr>
    <tr><th scope="row">Mountain towns near the city</th><td>El Valle de Ant&oacute;n, Altos del Mar&iacute;a</td><td>Cooler, green</td><td>Fresh air and quiet, a couple of hours from the city</td></tr>
    <tr><th scope="row">Chiriqu&iacute; highlands</th><td>Boquete, Volc&aacute;n, Cerro Punta, Potrerillos</td><td>Spring-like, cool nights</td><td>Mild weather, gardens, a large established expat community</td></tr>
    <tr><th scope="row">Chiriqu&iacute; lowlands and coast</th><td>David, Boca Chica, Las Lajas, Puerto Armuelles</td><td>Hot</td><td>City services in David or a quiet Pacific coast</td></tr>
    <tr><th scope="row">Azuero Peninsula</th><td>Pedas&iacute;, Los Destiladeros, Playa Ven&aacute;o, Las Tablas, Chitr&eacute;, Cambutal</td><td>Hot and relatively dry</td><td>Authentic Panamanian culture, surf, a slower pace</td></tr>
    <tr><th scope="row">Veraguas coast</th><td>Santa Catalina, Torio, Mariato</td><td>Hot and humid</td><td>Remote, nature-first living, surfing and diving</td></tr>
    <tr><th scope="row">Caribbean</th><td>Bocas del Toro, Portobelo</td><td>Hot, wetter</td><td>Island life and the water</td></tr>
    <tr><th scope="row">Islands near the city</th><td>Taboga, Contadora</td><td>Hot</td><td>Island quiet with Panama City close by</td></tr>
  </tbody>
</table>
</div>

<h2 id="choosing">How to choose</h2>
<ul>
  <li><strong>Climate first.</strong> If you dislike heat, start with Boquete, Volc&aacute;n or El Valle.</li>
  <li><strong>Healthcare distance.</strong> Map the drive to the nearest hospital you'd actually use.</li>
  <li><strong>Community.</strong> Boquete, Coronado and Panama City have large expat communities; much of Azuero and Veraguas does not, and Spanish matters more there.</li>
  <li><strong>Season.</strong> Visit in the rainy season (roughly May to November in most of the country) as well as the dry season.</li>
</ul>

<p>Detailed guides to each region, written by people who live there, are on the way. Join the <a href="/free-checklist/">free checklist list</a> to hear when they're published.</p>
""",
"faq": [
("Where do most expats live in Panama?",
 "The largest expat communities are in Panama City, the Pacific beach towns around Coronado and the Chiriqu&iacute; highlands around Boquete. Smaller communities live on the Azuero Peninsula, in Bocas del Toro and in El Valle de Ant&oacute;n."),
("Where is the coolest climate in Panama?",
 "The Chiriqu&iacute; highlands, including Boquete, Volc&aacute;n and Cerro Punta, have spring-like days and cool nights. El Valle de Ant&oacute;n is also noticeably cooler than the coast."),
("What is the best beach town in Panama for expats?",
 "Coronado is the most established, with easy access to Panama City. Pedas&iacute; and the Azuero coast suit people who want a quieter, more traditional town, and Bocas del Toro suits those who want Caribbean island life."),
],
"related": ["cost-of-living", "housing", "healthcare"],
},

# ---------------------------------------------------------------- HOUSING
{
"slug": "housing",
"title": "Renting and Buying Property in Panama as a Foreigner | Panama Expat Life",
"h1": "Renting and buying a home in Panama",
"kicker": "Housing",
"description": "How to find a long-term rental in Panama, why to rent before you buy, and how buying property in Panama works for foreigners: titles, lawyers and costs.",
"lead": "Rent for six to twelve months before you buy. When you do buy, foreigners can generally own property in Panama with the same rights as Panamanians, with some restrictions near borders and on certain coastal and island land. Always use your own independent lawyer to check the title, and know whether a property is titled land or rights-of-possession land.",
"body": """
<h2 id="renting">Finding a long-term rental</h2>
<p>Many of the best long-term rentals are never advertised online. Expat community groups, local property managers and word of mouth find more than websites do, especially outside Panama City. When you rent:</p>
<ul>
  <li>Expect a security deposit, often one or two months' rent.</li>
  <li>Get a written lease that states who pays for electricity, water, internet and maintenance.</li>
  <li>Visit in the rainy season to check for leaks, mould and road access.</li>
  <li>Check mobile signal and internet options at the actual address.</li>
</ul>

<h2 id="buying">Buying property as a foreigner</h2>
<p>The basics every buyer should know:</p>
<ul>
  <li><strong>Titled vs rights-of-possession.</strong> Titled property is registered in Panama's Public Registry. Rights-of-possession (ROP) land isn't, which carries more risk and limits financing and resale. Know which one you're buying.</li>
  <li><strong>Your own lawyer.</strong> Hire an independent lawyer who works only for you to search the title, check for liens and debts, and review the contract.</li>
  <li><strong>Closing costs.</strong> Buyers typically pay their lawyer plus notary and Public Registry fees. In Panama the seller normally pays any real estate commission.</li>
  <li><strong>Restricted areas.</strong> Foreign ownership is limited within a set distance of the borders and on some islands and beachfront land. Your lawyer will check.</li>
  <li><strong>Residency link.</strong> Some residency routes count property towards the requirement, so plan your purchase and your visa together.</li>
</ul>

<h2 id="buyer-agent">Want help buying?</h2>
<p>If you're ready to look at property in Pedas&iacute; and the Azuero coast, Boquete, Panama City and Casco Viejo, Coronado or Bocas del Toro, our affiliated brokerage <a href="__PP_URL__" rel="noopener">Panama Properties</a> represents buyers. As is usual in Panama, buyers pay no agent fee; the seller pays the commission. <a href="__PP_BUY_URL__" rel="noopener">Start the buying process with Panama Properties</a>.</p>
<p class="small">Panama Properties is affiliated with Panama Expat Life. See our <a href="/about/#disclosure">disclosure</a>.</p>
""".replace("__PP_URL__", PANAMA_PROPERTIES_URL).replace("__PP_BUY_URL__", PANAMA_PROPERTIES_BUY_URL),
"faq": [
("Can foreigners buy property in Panama?",
 "Yes. Foreigners generally have the same property rights as Panamanians, with restrictions close to the borders and on some islands and coastal land."),
("What is rights-of-possession land in Panama?",
 "Land that isn't registered in Panama's Public Registry. It can be bought and sold, but it carries more risk than titled property and is harder to finance and resell."),
("Who pays the real estate commission in Panama?",
 "The seller normally pays the agent's commission. Buyers typically pay their own lawyer plus notary and Public Registry fees."),
("Should I rent before buying in Panama?",
 "Yes. Renting for six to twelve months lets you experience both seasons, the roads, the neighbours and the services before you commit."),
],
"related": ["where-to-live", "residency", "money"],
},
]


# ---------------------------------------------------------------------------
# Checklist (shown in full as HTML on /free-checklist/)
# ---------------------------------------------------------------------------

CHECKLIST = [
("12 months before", [
  "Make a scouting trip of at least two weeks, ideally in the rainy season.",
  "Shortlist one or two regions.",
  "Start Spanish lessons, even an hour a week.",
  "Read up on the residency routes and decide which you might qualify for.",
]),
("9 months before", [
  "Choose an independent Panamanian immigration lawyer.",
  "Get your lawyer's document list for your residency route.",
  "Order police record checks, birth and marriage certificates as needed.",
  "Ask your home bank for a reference letter (and keep your home accounts open).",
]),
("6 months before", [
  "Have documents apostilled and, if required, translated into Spanish.",
  "Compare local and international health insurance.",
  "Start your pets' vaccination and health-certificate timeline with your vet.",
  "Decide what to ship, store, sell or give away.",
]),
("3 months before", [
  "Line up a furnished long-term rental for your first six to twelve months.",
  "Get moving and shipping quotes if you're sending belongings.",
  "Compare currency transfer services for moving larger sums.",
  "Book flights, including pet travel if needed.",
]),
("1 month before", [
  "Collect originals of every document your lawyer needs.",
  "Get your pets' health certificate endorsed and stamped by a Panamanian consulate.",
  "Notify Panama's Ministry of Health of your pets' arrival at least three days ahead.",
  "Set up mail forwarding and a plan for paying bills at home.",
]),
("First week in Panama", [
  "Meet your lawyer and start your residency filing.",
  "Get a local SIM card.",
  "Find your nearest pharmacy, clinic and hospital.",
  "Begin the bank account application.",
]),
]
