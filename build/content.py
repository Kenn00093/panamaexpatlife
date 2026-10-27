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

<h2 id="scouting-trip">Planning your scouting trip</h2>
<p>A scouting trip is research, not a holiday. Panama's dry season runs roughly from mid-December to April and the rainy season from May to November, so if you can, go in the one you expect to like less. A few habits make the trip far more useful:</p>
<ul>
  <li><strong>Split your time between regions.</strong> Two weeks is a sensible minimum. Spend several days in each of your shortlisted areas rather than day-tripping from one base. See <a href="/where-to-stay/">where to stay on your scouting trip</a> for the best base in each region.</li>
  <li><strong>Rent a car once you leave Panama City.</strong> Buses link the main towns, but beach communities, highland villages and the Azuero Peninsula are much easier to compare with your own wheels. Visitors can drive on a valid foreign licence for up to 90 days; carry it with your passport, because police checkpoints are common. See <a href="/renting-a-car/">renting a car in Panama</a> for insurance, tolls and road tips.</li>
  <li><strong>Get travel medical insurance.</strong> Your home health plan covers little or nothing in Panama. See <a href="/travel-insurance/">travel insurance for your scouting trip</a>.</li>
  <li><strong>Have data from the moment you land.</strong> Setting up a travel eSIM such as <a href="https://airalo.tpx.lu/A0bmF3qo" rel="sponsored nofollow noopener" target="_blank">Airalo</a> (affiliate link) before you fly means maps and messaging work as soon as you leave the airport. Buy a local SIM later if you stay. See <a href="/phones-and-internet/">phones and internet in Panama</a>.</li>
  <li><strong>Live an ordinary week.</strong> Do the grocery shop, find the nearest clinic and pharmacy, drive at rush hour and walk around after dark. A normal Tuesday tells you more than a viewpoint.</li>
  <li><strong>Talk to people who live there.</strong> Long-term renters, local business owners and expat groups will tell you what brochures leave out, from water and power cuts to the best time of year.</li>
  <li><strong>Don't sign anything yet.</strong> Use the trip to shortlist towns, meet a lawyer or two and line up a rental for your move. Buying can wait.</li>
</ul>

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
("How long should a scouting trip to Panama be?",
 "At least two weeks, split between the one or two regions you are considering. Visitors can drive on a valid foreign licence for up to 90 days, and a rental car makes it much easier to compare towns outside Panama City."),
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
<p>A traditional international wire works, but bank fees and exchange margins (if you're converting from Canadian dollars, pounds or euros) add up. Specialist currency transfer services often offer better rates for larger amounts, such as a property purchase or a residency deposit. Compare the total cost, not just the fee. See <a href="/moving-money/">Moving money to Panama</a> for options, paperwork and how to avoid wire fraud.</p>

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

# ---------------------------------------------------------------- WHERE TO STAY (draft, no hotel links yet)
{
"slug": "where-to-stay",
"title": "Where to Stay on a Panama Scouting Trip, Region by Region | Panama Expat Life",
"h1": "Where to stay on your Panama scouting trip",
"kicker": "Scouting trip",
"description": "Where to base yourself in each part of Panama when you're scouting for a move: Panama City, the Pacific beaches, El Valle, Boquete, the Azuero Peninsula and Bocas del Toro.",
"lead": "On a scouting trip, stay where you might actually live, not in a resort. Base yourself in the town centre or neighbourhood you're considering, book a few nights in each region on your shortlist, and choose places with a kitchen so you can shop, cook and live an ordinary day.",
"body": """
<h2 id="how-to-choose">How to choose a base</h2>
<ul>
  <li><strong>Stay in the place, not near it.</strong> A beach resort or a highway-side hotel tells you little about daily life. Pick somewhere you can walk to a grocery store, a pharmacy and a caf&eacute;.</li>
  <li><strong>Book three or four nights per region.</strong> One night is a stopover; three or four lets you see a weekday and a weekend.</li>
  <li><strong>Choose a kitchen when you can.</strong> An apartment or a guesthouse with a kitchen means shopping at local supermarkets and markets, which is the quickest way to test prices.</li>
  <li><strong>Mix in a short-term rental.</strong> If a town makes your shortlist, a week in a rental there tells you more than another hotel night: water pressure, power cuts, noise and neighbours.</li>
</ul>

<h2 id="panama-city">Panama City</h2>
<p>Most trips start and end here, and it is worth two or three nights even if you plan to live elsewhere, because it is where you'll fly, see specialists and handle paperwork.</p>
<ul>
  <li><strong>Casco Viejo</strong> is historic, walkable and lively, with restaurants and plazas. It is charming for a first visit but noisier and more tourist-focused than where most residents live.</li>
  <li><strong>El Cangrejo</strong> is central, practical and walkable, close to hospitals, supermarkets and the metro. It is the best base for seeing everyday city life.</li>
  <li><strong>Costa del Este</strong> and <strong>Punta Pacifica</strong> show modern high-rise living near the main private hospitals. They are quieter at street level and you'll mostly drive or take taxis.</li>
</ul>
<p><strong>Test while you're there:</strong> rush-hour traffic, the drive to the hospital you'd use, and an evening walk around the neighbourhood.</p>

<h2 id="pacific-beaches">Pacific beaches</h2>
<p>The beach towns about an hour or so west of the city along the Pan-American Highway are among the driest parts of the country and have the largest beach expat community.</p>
<ul>
  <li><strong>Coronado</strong> is the services hub, with supermarkets, clinics and banks. Stay inside the town rather than on the highway strip so you can judge it as a place to live.</li>
  <li><strong>Gorgona</strong> and <strong>San Carlos</strong> are smaller and quieter, a short drive from Coronado's shops.</li>
</ul>
<p><strong>Test while you're there:</strong> the drive to Panama City at a busy time, weekday versus weekend crowds, and how far the nearest hospital is.</p>

<h2 id="el-valle">El Valle de Ant&oacute;n</h2>
<p>A mountain valley about two hours from the city, with cooler air and a small-town feel. Stay close to the centre and the market so you can walk, and check how you'd reach the beaches and the city for errands.</p>

<h2 id="chiriqui-highlands">Boquete and the Chiriqu&iacute; highlands</h2>
<p>Spring-like weather and Panama's best-known mountain expat community. Fly or drive to David, the provincial city, then head up into the hills.</p>
<ul>
  <li><strong>Boquete town centre</strong> is the easiest base: walkable, with restaurants, a supermarket and community events.</li>
  <li><strong>Volc&aacute;n</strong> and <strong>Cerro Punta</strong> are quieter, cooler and more agricultural. Spend a night or two if Boquete feels too busy.</li>
</ul>
<p><strong>Test while you're there:</strong> the wind and rain in the season you visit, the drive down to David for hospitals and big shops, and how your clothes and home would cope with the damp.</p>

<h2 id="azuero">Pedas&iacute; and the Azuero Peninsula</h2>
<p>Traditional Panamanian small towns, surf beaches and a slower pace, about five hours' drive from the city. Fewer expats live here than in Boquete or Coronado, so Spanish matters more.</p>
<ul>
  <li><strong>Pedas&iacute;</strong> is the most popular base, with a walkable centre and beaches a short drive away.</li>
  <li><strong>Las Tablas</strong> and <strong>Chitr&eacute;</strong> are the larger service towns, with hospitals, banks and bigger supermarkets. Spend a day in each to see what's within reach.</li>
</ul>
<p><strong>Test while you're there:</strong> the drive to Chitr&eacute; or Las Tablas for services, internet speed where you'd live, and how quiet the low season feels.</p>

<h2 id="caribbean">Bocas del Toro</h2>
<p>Caribbean island living, with water taxis instead of roads for many trips. Stay on <strong>Isla Col&oacute;n</strong>, the main island, to judge services and daily life, then spend a night or two on a quieter island if that's the lifestyle you're after.</p>
<p><strong>Test while you're there:</strong> how you'd get groceries, healthcare and flights to the city, and the wetter weather, which can come in any month.</p>

<h2 id="longer-stays">After the scouting trip</h2>
<p>Once you've chosen a region, rent for six to twelve months before you buy. See <a href="/housing/">Housing</a> for how long-term rentals work, and our <a href="/free-checklist/">free move checklist</a> for what to do when.</p>
""",
"faq": [
("Where should I stay on a scouting trip to Panama?",
 "Stay in the town or neighbourhood you're considering living in rather than a resort, ideally somewhere with a kitchen, and spend three or four nights in each region on your shortlist."),
("Which Panama City neighbourhood is best for a first visit?",
 "El Cangrejo is the most practical base for seeing everyday city life, being central and walkable with hospitals and the metro nearby. Casco Viejo is more charming but noisier and more tourist-focused."),
("How long should I stay in each region?",
 "Three or four nights per region lets you see both a weekday and a weekend. If a town makes your shortlist, follow up with a week in a short-term rental."),
],
"related": ["start-here", "where-to-live", "housing"],
},

# ---------------------------------------------------------------- RENTING A CAR
# AFFILIATE: add the DiscoverCars link (Travelpayouts) where marked once approved.
{
"slug": "renting-a-car",
"title": "Renting a Car in Panama: Insurance, Tolls and Driving Tips | Panama Expat Life",
"h1": "Renting a car in Panama",
"kicker": "Getting around",
"description": "What to know before renting a car in Panama: the mandatory liability insurance that isn't in most online quotes, licences, tolls, police checkpoints and road conditions.",
"lead": "Renting a car is the easiest way to compare towns outside Panama City. Visitors can drive on a valid foreign licence for up to 90 days, but budget for the mandatory third-party liability insurance, which is often left out of the cheap daily rates you see online, and for a security hold on a credit card.",
"body": """
<h2 id="insurance">The insurance surprise</h2>
<p>Third-party liability insurance is mandatory in Panama and is usually sold at the rental counter. Many online quotes don't include it, so the price you pay at pickup can be several times the daily rate you booked. When you compare companies, compare the total with liability insurance included.</p>
<ul>
  <li><strong>Liability insurance</strong> covers damage or injury you cause to others. It's required by law, and most companies won't let you replace it with credit card coverage.</li>
  <li><strong>Collision damage cover</strong> for the rental car itself is where your credit card may help. Ask your card issuer for a letter confirming the cover applies in Panama and bring it with you. Expect a larger hold on your card if you decline the company's own cover.</li>
  <li><strong>Read what's excluded.</strong> Tires, glass and the underside of the car are often excluded unless you buy extra cover.</li>
</ul>
<!-- AFFILIATE: DiscoverCars, "compare total prices including insurance" -->

<h2 id="what-you-need">What you need to rent</h2>
<ul>
  <li><strong>A valid driver's licence</strong> from home. Visitors can drive on it for up to 90 days; residents need a Panamanian licence.</li>
  <li><strong>Your passport</strong>, with the entry stamp you received on arrival.</li>
  <li><strong>A credit card in the driver's name.</strong> Most companies won't accept debit or prepaid cards for the security deposit, and holds can run from a few hundred dollars to several thousand.</li>
  <li><strong>Age.</strong> The minimum is usually 21, with a young-driver surcharge under 25 and some car classes limited to drivers over 25.</li>
</ul>
<p>You can't take a Panamanian rental car across the border into Costa Rica.</p>

<h2 id="pickup">Where to pick up</h2>
<p>Panama City traffic is heavy and the road layout is confusing for newcomers, so if you're spending your first days in the city, use taxis or ride-hailing there and collect the car when you leave. If you're heading straight west to the beaches or the highlands, picking up at Tocumen airport avoids crossing the city twice. One-way rentals, such as collecting in Panama City and returning in David, are often possible but may carry a fee.</p>
<p>At pickup, photograph or film every side of the car, the interior, the fuel gauge and the odometer, and make sure existing damage is marked on the form.</p>

<h2 id="tolls">Tolls and the Panapass</h2>
<p>The main toll expressways in and around Panama City, the Corredor Sur and Corredor Norte, take payment only by Panapass, an electronic windshield sticker. Most rental cars already have one, and the company will offer a daily toll package or charge you per use. Outside the city, the main highways to the Pacific beaches, Chiriqu&iacute; and the Azuero Peninsula are toll-free.</p>

<h2 id="on-the-road">On the road</h2>
<ul>
  <li><strong>Police checkpoints</strong> are common, especially on the Pan-American Highway. Slow down, be polite and have your passport, licence and the rental papers ready.</li>
  <li><strong>Drive in daylight.</strong> It gets dark around 6:30 pm all year, and rural roads are often unlit, with potholes, pedestrians, animals and slow trucks.</li>
  <li><strong>Speed limits change often</strong>, sometimes with little warning, and speed checks are common. Fines are paid at a transit authority office, not to the officer.</li>
  <li><strong>Use Waze or Google Maps.</strong> Waze is widely used in Panama and flags police and hazards reported by other drivers.</li>
  <li><strong>Don't drink and drive at all</strong>, keep your phone out of your hand, and wear your seat belt.</li>
  <li><strong>Fuel up</strong> before long stretches in the interior, where stations can be far apart.</li>
  <li><strong>Leave nothing visible</strong> in a parked car.</li>
</ul>

<h2 id="four-by-four">Do you need a 4x4?</h2>
<p>Not for the main towns. The roads to Coronado, El Valle, Boquete and Pedas&iacute; are paved. A car with higher clearance helps if you plan to look at land, beaches or farms down dirt roads, especially in the rainy season. For Bocas del Toro you don't need a car on the islands at all: you can leave it on the mainland or, more simply, fly.</p>

<h2 id="accidents">If something goes wrong</h2>
<p>In an accident, don't move the car unless it's dangerous to leave it. Call the police and the rental company's emergency number, wait for the police report (it can take a while), and take your own photos. The insurance claim usually depends on that report.</p>
""",
"faq": [
("Can I drive in Panama with a Canadian or US licence?",
 "Yes. Visitors can drive on a valid foreign licence for up to 90 days. Carry your passport with your entry stamp as well, because police checkpoints are common. Residents need a Panamanian licence."),
("Why is renting a car in Panama more expensive than the online quote?",
 "Third-party liability insurance is mandatory in Panama and is often sold at the rental counter rather than included in online quotes. Compare total prices with liability insurance included."),
("Does my credit card's rental insurance work in Panama?",
 "It may cover damage to the rental car, but it usually can't replace Panama's mandatory liability insurance. Get a letter from your card issuer confirming cover in Panama and expect a larger security hold if you decline the rental company's damage cover."),
],
"related": ["start-here", "where-to-stay", "flying-to-panama"],
},

# ---------------------------------------------------------------- TRAVEL INSURANCE
# AFFILIATE: add VisitorsCoverage / Insubuy (Travelpayouts) where marked once approved.
{
"slug": "travel-insurance",
"title": "Travel Insurance for a Panama Scouting Trip | Panama Expat Life",
"h1": "Travel insurance for your scouting trip",
"kicker": "Scouting trip",
"description": "Why you need travel medical insurance for a Panama scouting trip, what your home health plan won't cover, and what to check in a policy before you buy.",
"lead": "Buy travel medical insurance before a scouting trip to Panama. Canadian provincial health plans pay only a small share of emergency costs abroad, Medicare generally doesn't cover care outside the US, and private hospitals in Panama may expect payment or an insurance guarantee before treating you.",
"body": """
<h2 id="why">Why your home coverage isn't enough</h2>
<ul>
  <li><strong>Canadians:</strong> provincial health plans cover emergency care abroad only up to their own low rates, typically a small fraction of the real bill. Ambulances, medical evacuation and prescriptions are often not covered at all.</li>
  <li><strong>Americans:</strong> Original Medicare usually doesn't cover care outside the US. Some Medicare supplement (Medigap) plans include limited foreign emergency cover; check yours. Private US health plans vary, so ask your insurer what they pay in Panama.</li>
  <li><strong>UK travellers:</strong> the Global Health Insurance Card doesn't apply in Panama.</li>
</ul>
<p>Private hospitals in Panama City are good and cheaper than in North America, but a serious illness or injury can still cost tens of thousands of dollars, and you may be asked to pay or show proof of insurance up front.</p>

<h2 id="what-to-check">What to check in a policy</h2>
<ul>
  <li><strong>Emergency medical limit.</strong> Look for a high limit, and check whether the insurer pays the hospital directly or reimburses you later.</li>
  <li><strong>Medical evacuation and repatriation.</strong> If you're in Bocas del Toro, the Azuero or the highlands, getting to a major hospital, or home, can be the most expensive part.</li>
  <li><strong>Pre-existing conditions.</strong> Many policies exclude them unless they've been stable for a set period before you travel. Answer the medical questions honestly; a wrong answer can void the policy.</li>
  <li><strong>Activities.</strong> Surfing, diving, zip-lining and hiking volcanoes may need to be added.</li>
  <li><strong>Trip length and age limits.</strong> Make sure the policy covers your whole trip, including any extension, and check age limits on credit card travel insurance, which are often lower than people expect.</li>
  <li><strong>Trip cancellation and interruption</strong> are optional. They're worth considering if you've prepaid flights and rentals you can't get back.</li>
</ul>
<!-- AFFILIATE: VisitorsCoverage / Insubuy comparison link -->

<h2 id="when-to-buy">When to buy</h2>
<p>Buy before you leave home. Many policies, especially Canadian ones, can't be bought once you've already left, and cancellation cover usually only applies if you buy it soon after booking.</p>

<h2 id="after-you-move">After you move</h2>
<p>Travel insurance is meant for trips, not for living in Panama. Once you move, you'll need local or international health insurance instead. See <a href="/healthcare/">Healthcare</a> for how those compare. Canadians should also check how long they can be away before losing provincial coverage, which affects when to switch.</p>
""",
"faq": [
("Do I need travel insurance to visit Panama?",
 "It isn't a general entry requirement for Canadian, US or UK visitors, but you should have it. Home health plans cover little or nothing in Panama, and private hospitals may want payment or an insurance guarantee before treatment."),
("Does Medicare cover me in Panama?",
 "Generally no. Original Medicare covers care outside the US only in rare cases. Some Medigap plans include limited foreign emergency cover, so check your plan and buy travel medical insurance for the gap."),
("Can I use travel insurance after I move to Panama?",
 "No. Travel insurance covers trips, not living abroad. Once you move, switch to local Panamanian or international health insurance."),
],
"related": ["start-here", "healthcare", "where-to-stay"],
},

# ---------------------------------------------------------------- MOVING MONEY
# AFFILIATE: add Wise (Partnerize) and Xe (Impact) where marked once approved.
{
"slug": "moving-money",
"title": "Moving Money to Panama: Wires, Transfer Services and Fees | Panama Expat Life",
"h1": "Moving money to Panama",
"kicker": "Money",
"description": "How to move money to Panama for a rental deposit, residency or a property purchase: bank wires vs transfer services, source-of-funds paperwork, fees and avoiding wire fraud.",
"lead": "Panama uses the US dollar, so the cost of moving money is mostly in currency conversion and wire fees. For larger sums, compare a bank wire with a specialist transfer service on the total cost, keep records of where the money came from, and confirm payment details by phone before you send anything.",
"body": """
<h2 id="what-it-costs">Where the cost is</h2>
<p>If your money is already in US dollars, sending it to Panama is a straightforward international wire, with fees at both ends and sometimes from an intermediary bank in between. If it's in Canadian dollars, pounds or euros, the exchange rate matters far more than the fee: a margin of a few percent on a large transfer can cost more than everything else combined.</p>

<h2 id="options">Your options</h2>
<table>
  <caption>Ways to move money to Panama</caption>
  <thead><tr><th scope="col">Option</th><th scope="col">Good for</th><th scope="col">Watch for</th></tr></thead>
  <tbody>
    <tr><th scope="row">Bank wire from home</th><td>Simple, familiar, high limits</td><td>Exchange margins, outgoing and incoming fees, intermediary bank deductions</td></tr>
    <tr><th scope="row">Specialist transfer service</th><td>Converting currency at a better rate, especially for larger amounts</td><td>Transfer limits, how long the money takes to arrive, whether the receiving bank asks questions</td></tr>
    <tr><th scope="row">ATM withdrawals</th><td>Day-to-day cash while you settle in</td><td>Fees from both banks and daily limits</td></tr>
    <tr><th scope="row">Credit card</th><td>Everyday spending in cities</td><td>Foreign transaction fees on many cards</td></tr>
  </tbody>
</table>
<!-- AFFILIATE: Wise and Xe links, "compare a specialist transfer service" -->

<h2 id="paperwork">Source-of-funds paperwork</h2>
<p>Panamanian banks and lawyers follow strict anti-money-laundering rules. For any large amount, such as a residency deposit or a property purchase, expect to show where the money came from. Keep these ready:</p>
<ul>
  <li>Bank statements showing the funds in your account</li>
  <li>Documents for where they came from, such as a home sale, a pension or investment statements, or an inheritance</li>
  <li>Recent tax returns, which some banks ask for</li>
</ul>
<p>Your lawyer will tell you exactly what's needed. Sorting it out before you send means the money isn't held up when it arrives.</p>

<h2 id="before-a-local-account">Before you have a Panamanian bank account</h2>
<p>Opening a local account can take weeks, so the first large payments usually go elsewhere. Rental deposits are often paid by wire to the landlord or agent, and property deposits are commonly held by a lawyer or escrow agent. Ask who holds the money, and on what conditions it's released, before you pay. See <a href="/money/">Banking and money</a> for how to open an account.</p>

<h2 id="fraud">Avoid wire fraud</h2>
<ul>
  <li><strong>Confirm payment details by phone</strong> with someone you know, using a number you already have, never one from the email.</li>
  <li><strong>Be suspicious of any change</strong> to bank details sent by email, especially at the last minute.</li>
  <li><strong>Send a small test payment first</strong> and confirm it arrived before sending the rest.</li>
</ul>

<h2 id="everyday">Everyday money once you're here</h2>
<ul>
  <li><strong>Keep your home bank accounts open.</strong> You'll need them for pensions, taxes and paying bills at home.</li>
  <li><strong>Carry a card with no foreign transaction fees</strong> and tell your bank you're in Panama.</li>
  <li><strong>Carry small bills.</strong> Many small shops can't change a $50 or $100 note, and cash is still common outside Panama City.</li>
</ul>
""",
"faq": [
("What is the cheapest way to send money to Panama?",
 "It depends on the amount and currency. If you're converting from Canadian dollars, pounds or euros, a specialist transfer service often beats a bank's exchange rate. Compare the total amount that arrives, not just the fee."),
("Do I need to prove where my money came from?",
 "For large amounts, usually yes. Panamanian banks and lawyers ask for bank statements and documents showing the source of the funds, such as a home sale or pension statements."),
("Can I send money to Panama before I have a local bank account?",
 "Yes. Early payments such as rental or property deposits are often wired to a landlord, lawyer or escrow agent. Confirm who holds the money and the release conditions before you pay."),
],
"related": ["money", "residency", "housing"],
},

# ---------------------------------------------------------------- PHONES AND INTERNET
{
"slug": "phones-and-internet",
"title": "Phones and Internet in Panama: SIM Cards, eSIMs and Home Internet | Panama Expat Life",
"h1": "Phones and internet in Panama",
"kicker": "Getting connected",
"description": "How to get a phone plan and internet in Panama: travel eSIMs, local SIM cards from Tigo and +M&oacute;vil, home internet, Starlink in rural areas, and WhatsApp.",
"lead": "For a scouting trip, a travel eSIM gives you data the moment you land. Once you're living here, a local prepaid or postpaid plan from Panama's two mobile carriers, Tigo and +M&oacute;vil, is cheaper. In cities you can get fibre or cable internet at home; in rural areas, Starlink is an option.",
"body": """
<h2 id="esim">Scouting trip: a travel eSIM</h2>
<p>An eSIM is set up on your phone before you leave, so you have maps, ride-hailing and WhatsApp as soon as you land, without hunting for a SIM shop. Check that your phone is unlocked and supports eSIM, buy a Panama plan from a provider such as <a href="https://airalo.tpx.lu/A0bmF3qo" rel="sponsored nofollow noopener" target="_blank">Airalo</a> or <a href="https://saily.tpx.lu/zDFW3eir" rel="sponsored nofollow noopener" target="_blank">Saily</a> (affiliate links) before you fly, and switch it on when you arrive. Keep your home SIM active for bank security codes sent by text.</p>

<h2 id="local-sim">Living here: a local SIM</h2>
<p>Panama has two mobile carriers, Tigo and +M&oacute;vil (Cable &amp; Wireless). Both sell cheap prepaid plans and monthly contracts. Coverage is good in cities and towns but patchy in the mountains, on remote beaches and on some islands, so ask neighbours which network works best where you plan to live. Bring your passport when you buy a SIM.</p>
<p>+M&oacute;vil has begun offering satellite messaging on some phones in areas with no signal. It's limited to messaging and a few apps for now, but useful in remote places.</p>

<h2 id="whatsapp">WhatsApp runs everything</h2>
<p>Almost everyone in Panama, from landlords and lawyers to doctors and the local hardware store, uses WhatsApp. Set it up before you arrive and keep the same number if you can, so your contacts don't change when you switch SIMs.</p>

<h2 id="home-internet">Home internet</h2>
<ul>
  <li><strong>Cities and larger towns</strong> generally have fibre or cable internet from the same two companies, fast enough for video calls and streaming.</li>
  <li><strong>Rural areas</strong> may have only slow wireless service or none at all. Starlink satellite internet is available in Panama and is a common fix where nothing else reaches.</li>
  <li><strong>Test before you sign a lease.</strong> If you work online, run a speed test at the property at a busy time of day, and ask what happens during power cuts.</li>
</ul>
""",
"faq": [
("Which mobile carrier is best in Panama?",
 "Panama has two carriers, Tigo and +M&oacute;vil. Both cover cities and towns well; in rural areas coverage varies, so ask locals which network works best where you'll be."),
("Should I get an eSIM or a local SIM for a trip to Panama?",
 "For a short trip, a travel eSIM is the easiest option because it works the moment you land. For longer stays, a local prepaid plan is usually cheaper."),
("Can I get good internet in rural Panama?",
 "Sometimes. Towns often have fibre or cable; more remote homes may rely on Starlink satellite internet. Test the connection before signing a lease if you work online."),
],
"related": ["start-here", "where-to-live", "housing"],
},

# ---------------------------------------------------------------- FLYING TO PANAMA
# AFFILIATE: add a flight search link (Travelpayouts) where marked once approved.
{
"slug": "flying-to-panama",
"title": "Flying to Panama: Airports, Direct Flights and Getting Around | Panama Expat Life",
"h1": "Flying to Panama",
"kicker": "Getting around",
"description": "Flying to Panama from Canada, the US and the UK: Tocumen airport, direct routes, domestic flights to David and Bocas del Toro, entry rules and getting from the airport.",
"lead": "Most international flights land at Tocumen International Airport outside Panama City, the hub of Copa Airlines, with direct flights from many US cities and from Toronto, Montr&eacute;al and, seasonally, Calgary. From the city, domestic flights reach David (for Boquete) and Bocas del Toro, and the Pacific beaches and the Azuero are an easy drive.",
"body": """
<h2 id="airports">Panama's main airports</h2>
<ul>
  <li><strong>Tocumen International (PTY)</strong>, east of Panama City, handles almost all international flights.</li>
  <li><strong>Albrook (PAC)</strong>, in the city, is the main domestic airport, with flights to David, Bocas del Toro, Changuinola and Chitr&eacute;.</li>
  <li><strong>R&iacute;o Hato (RIH)</strong>, near the Pacific beaches, gets seasonal winter flights from Toronto and Montr&eacute;al, mostly for beach resorts. It's handy for Coronado and the beaches if the dates work.</li>
  <li><strong>David (DAV)</strong> serves Boquete and the rest of Chiriqu&iacute;.</li>
</ul>

<h2 id="direct-flights">Direct flights</h2>
<p>Copa flies nonstop to Panama City from a long list of US cities, and US airlines add more. From Canada there are direct flights from Toronto and Montr&eacute;al, with seasonal winter service from Calgary. From the UK and Europe you'll usually connect, either through a US hub or on a direct flight from cities such as Madrid or Amsterdam. Because Tocumen is a hub, Panama is also easy to reach from most of Latin America.</p>
<!-- AFFILIATE: flight search link -->

<h2 id="entry">Entry rules</h2>
<p>Canadian, US and UK citizens don't need a visa for a tourist visit. Bring a passport valid for at least six months beyond your stay and a return or onward ticket, and be ready to show you can support yourself during your visit. The length of stay you're allowed is set by immigration on arrival, so check your entry stamp. If you're bringing a pet, see <a href="/moving/">Moving</a>.</p>

<h2 id="from-the-airport">Getting from Tocumen into the city</h2>
<ul>
  <li><strong>Official airport taxis</strong> charge a fixed fare agreed before you set off, usually around $30 to $40 to the centre.</li>
  <li><strong>Uber</strong> is usually cheaper. Pickups are from a designated area, not the arrivals door, and you'll need data, so set up your <a href="/phones-and-internet/">eSIM</a> before you fly.</li>
  <li><strong>A pre-booked transfer</strong> costs more than Uber but a driver meets you in arrivals at a fixed price, which helps after a late flight or with lots of luggage. <a href="https://kiwitaxi.tpx.lu/ImrsLPQm" rel="sponsored nofollow noopener" target="_blank">Kiwitaxi</a> (affiliate link) takes bookings from Tocumen to Panama City and beyond.</li>
  <li><strong>The metro</strong> has an airport branch on Line 2. It's by far the cheapest option but slow, with a transfer, and awkward with big bags.</li>
  <li><strong>Rental cars</strong> can be collected at the airport. See <a href="/renting-a-car/">Renting a car</a>.</li>
</ul>

<h2 id="delays">If your flight is delayed or cancelled</h2>
<p>Depending on the airline and route, passenger rules in Canada, the EU and the UK can entitle you to compensation for long delays, cancellations or being bumped from an overbooked flight, sometimes years after the trip. You can claim from the airline yourself for free. A claims service such as <a href="https://airhelp.tpx.lu/cc7eRN6U" rel="sponsored nofollow noopener" target="_blank">AirHelp</a> (affiliate link) checks whether you qualify and handles the claim for a share of any payout.</p>

<h2 id="getting-around">Reaching the regions</h2>
<table>
  <caption>Getting from Panama City to the main regions</caption>
  <thead><tr><th scope="col">Region</th><th scope="col">Best way</th></tr></thead>
  <tbody>
    <tr><th scope="row">Pacific beaches (Coronado)</th><td>Drive or bus along the Pan-American Highway, roughly an hour or so depending on traffic</td></tr>
    <tr><th scope="row">El Valle de Ant&oacute;n</th><td>Drive or bus, about two hours</td></tr>
    <tr><th scope="row">Boquete</th><td>Fly to David, then drive or bus up to Boquete; or drive the whole way in about seven hours</td></tr>
    <tr><th scope="row">Pedas&iacute; and the Azuero</th><td>Drive, about five hours; Chitr&eacute; has domestic flights</td></tr>
    <tr><th scope="row">Bocas del Toro</th><td>Fly from Albrook to Isla Col&oacute;n</td></tr>
  </tbody>
</table>
""",
"faq": [
("Which airport do I fly into for Panama?",
 "Most international flights land at Tocumen International Airport (PTY) outside Panama City. Domestic flights to David and Bocas del Toro leave from Albrook, the city's domestic airport."),
("Are there direct flights from Canada to Panama?",
 "Yes. There are direct flights from Toronto and Montr&eacute;al to Panama City, seasonal winter flights from Calgary, and seasonal flights from Toronto and Montr&eacute;al to R&iacute;o Hato near the Pacific beaches."),
("Do I need a visa to visit Panama?",
 "Canadian, US and UK citizens don't need a visa for a tourist visit. Bring a passport valid for at least six months and a return or onward ticket, and check the length of stay on your entry stamp."),
],
"related": ["start-here", "renting-a-car", "where-to-stay"],
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
  "Get a local SIM card, or set up a travel eSIM such as <a href=\"https://airalo.tpx.lu/A0bmF3qo\" rel=\"sponsored nofollow noopener\" target=\"_blank\">Airalo</a> (affiliate link) before you fly, so you have data the moment you land.",
  "Find your nearest pharmacy, clinic and hospital.",
  "Begin the bank account application.",
]),
]
