#!/usr/bin/env python3
"""Generate detailed product pages for the Kisra Tech site.

Content lives in `_products_base.py` (DATA) + EXTRA below. Marketing PDFs are
auto-detected from `assets/pdf/marketing/` (ku / ar / en variants).

    python3 tools/build_products.py
"""
import glob
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "products")
sys.path.insert(0, HERE)
from _products_base import DATA  # noqa: E402

WA = "https://wa.me/9647706947874"
PHONE = "+964 770 694 7874"
MAIL = "arkan.leki@gmail.com"

MKT_DIR = os.path.join(ROOT, "assets", "pdf", "marketing")
MKT_PREFIX = {"kapitan": "kapitanpos", "exam": "puplis"}

# extra per-product downloads that are not the detected marketing catalogue
EXTRA_DOWNLOADS = {
    "gihan": [("marketing/gihan-guide-ku.pdf",
               "ڕێبەری بەکارهێنەر، کوردی (١٥ لاپەڕە)",
               "User guide — Kurdish (15 pages)")],
}

EXTRA = {
    "gihan": dict(
        why=[
            ("دەرفەتی فرۆشتن لەدەست ناچێت", "No sale gets lost",
             "هەر داواکارییەک لە هەر کەناڵێکەوە بێت لە یەک شوێن تۆمار دەکرێت.",
             "Every order from any channel lands in one place."),
            ("قازانجی ڕاستەقینە دەبینیت", "You see real profit",
             "نرخی فرۆشتن کەم کراوە لە تێچووی کاڵا، کۆمیشن و داشکاندن.",
             "Sale price minus cost, commission and discount per order."),
            ("کۆگا هەرگیز لەدەست ناچێت", "Stock never drifts",
             "لیستری جووڵەی کاڵا بۆ هەموو فرۆشتن و کڕین و گەڕاندنەوە.",
             "A movement ledger covering every sale, purchase and return."),
        ],
        how=[
            ("کاڵا و کۆگا دابنێ", "Add products and stock",
             "کاڵا، بارکۆد، نرخ و کۆگا هاوردە دەکرێت، یان لە Excel.",
             "Import from Excel, or type them in."),
            ("کاشێر و کارمەندان ڕێک بخە", "Set up cashier and staff",
             "ڕۆڵ و دەسەڵات بۆ هەر کارمەندێک، سندوق و شیفت.",
             "Roles, permissions, cash drawer and shifts."),
            ("بفرۆشە و ببینە", "Sell and see",
             "فرۆشتن لە چەند ئامێر و لقێک، ڕاپۆرتی ڕۆژانە و قازانج.",
             "Sell from several devices and branches; daily reports and profit."),
        ],
        stats=[("٤", "کەناڵی فرۆشتن", "sales channels"),
               ("٤", "زمان لەگەڵ RTL", "languages with RTL"),
               ("∞", "بەکارهێنەر بەپێی پاکێج", "users by package")],
        packages=[
            ("سەرەتا", "Starter", "٧٥٠,٠٠٠ دینار", "750,000 IQD", "١ فرۆشگا، ٣ بەکارهێنەر", "1 shop, 3 users"),
            ("پیشەگەر", "Pro", "١,٥٠٠,٠٠٠ دینار", "1,500,000 IQD", "چەند فرۆشگا،لق، ١٠ بەکارهێنەر", "multi-shop, 10 users"),
            ("کۆمپانیا", "Company", "پەیوەندی بکە", "contact us", "بێ سنوور، دابەشکردن", "unlimited, distribution"),
        ],
    ),
    "zuba": dict(
        why=[
            ("قەرز و پارە لە یەک شوێن", "Debt and money in one place",
             "دەفتەری قەرزی کڕیار و دابینکەر بە حیسابی خۆکار.",
             "Customer and supplier ledgers calculated automatically."),
            ("کۆگای فرە شوێن", "Multi-location stock",
             "کاڵا لە چەند کۆگا و لقێک، بە مێژووی جووڵە.",
             "Stock across warehouses and locations with movement history."),
            ("ڕاپۆرتی بەشداران", "Partner reports",
             "قازانجی گشتی و بەشی هەر بەشدارێک بە ڕوونی.",
             "Overall profit and each partner's share, clearly."),
        ],
        how=[
            ("داتای کۆن بگوازەرەوە", "Migrate your data",
             "کاڵا، کڕیار، قەرز و دابینکەران دەگوازرێنەوە.",
             "Products, customers, debt and suppliers are imported."),
            ("کۆگا و لقەکان ڕێک بخە", "Set up stock and locations",
             "کۆگا، لیستری کاڵا و ئاگادارکردنەوەی کەمبوون.",
             "Warehouses, ledgers and low-stock alerts."),
            ("فرۆشتن و کڕین دەست پێبکە", "Start selling and buying",
             "پسوولە، پێشکەشکردن، گەڕاندنەوە و پارەدان.",
             "Invoices, quotations, returns and payments."),
        ],
        stats=[("١٥", "تایبەتمەندی سەرەکی", "core features"),
               ("٣", "زمان لەگەڵ RTL", "languages with RTL"),
               ("∞", "لق و کۆگا", "branches and warehouses")],
        packages=[
            ("سەرەتا", "Starter", "٩٠٠ دۆلار+", "$900+", "١ کۆگا، ٣ بەکارهێنەر", "1 warehouse, 3 users"),
            ("پیشەگەر", "Pro", "١,٨٠٠ دۆلار+", "$1,800+", "چەند کۆگا و لق، ١٠ بەکارهێنەر", "multi-warehouse, 10 users"),
            ("پۆرتاڵی کڕیار", "Customer portal", "زیادە +٣٠٠ دۆلار", "+$300", "وێب بۆ کڕیار: باڵانس، قەرز و پسوولە", "customer web: balance, debt, invoices"),
            ("فرۆشگای گشتی", "Public storefront", "زیادە +٤٠٠ دۆلار", "+$400", "فرۆشگای گشتی بۆ کڕیارانی نوێ", "public storefront for new customers"),
            ("کۆمپانیا", "Company", "پەیوەندی بکە", "contact us", "چەند کۆگا + بەڕێوەبردنی ٤ دوکان", "multi-warehouse + up to 4 shops"),
        ],
    ),
    "kapitan": dict(
        why=[
            ("کافێ بەبێ ئینتەرنێت ناوەستێت", "The cafe keeps running",
             "هەموو شتێک لەسەر ئامێرەکانی خۆت ڕوودەدات؛ ئینتەرنێت تەنها پاڵپشتییە.",
             "Everything happens on your devices; the internet is only a backup."),
            ("چێشتخانە و کاش دەنگ دەدەن بە یەک", "Kitchen and till talk",
             "گارسۆن لە مێزەوە دەنێرێت؛ چێشتخانە دەستبەجێ دەبینێت.",
             "The waiter sends from the table; the kitchen sees it at once."),
            ("هیچ کۆمپیوتەرێکی نوێ پێویست نییە", "No new computer needed",
             "تابلێت و پرینتەرێکی بلوتووث بەسە.", "A tablet and a Bluetooth printer are enough."),
        ],
        how=[
            ("تابلێتەکان ڕێک بخە", "Set up the tablets",
             "چێشتخانە میوانداری دەکات؛ گارسۆن بە QR پەیوەست دەبێت.",
             "The kitchen hosts; the waiter joins with a QR code."),
            ("مێنیو و مێز دابنێ", "Add menu and tables",
             "مێنیو بە دوو ناو (کوردی،ئینگلیزی) و مێزەکان.",
             "Menu with two names (Kurdish/English) and your tables."),
            ("بفرۆشە و چاپ بکە", "Sell and print",
             "پسوولە بە بلوتووث چاپ دەبێت؛ تیکتی چێشتخانە بێ نرخ.",
             "Receipts print over Bluetooth; kitchen tickets carry no prices."),
        ],
        stats=[("٣", "ئامێر بەیەکەوە", "devices linked"),
               ("٠", "ئینتەرنێت پێویست", "internet required"),
               ("<١s", "هاوکاتکردن", "sync time")],
        packages=[
            ("کافێ", "Cafe", "٥٠٠,٠٠٠ دینار", "500,000 IQD", "تا ٣ ئامێر + پرینتەر، ساڵانە ١٥٠,٠٠٠", "up to 3 devices + printer, 150,000/yr"),
            ("ئامێری زیادە", "Extra device", "١٠٠,٠٠٠ دینار", "100,000 IQD", "هەر ئامێرێکی تر", "each additional device"),
            ("چەند لق و تایبەت", "Multi-branch / custom", "پەیوەندی بکە", "contact us", "بەپێی پێویست", "tailored"),
        ],
    ),
    "custom": dict(
        why=[
            ("بۆ کاری تۆ دروست کراوە", "Built for your workflow",
             "هیچ تایبەتمەندییەکی زیادە و هیچ کەموکوڕییەک لە کارەکەتدا.",
             "No extra features, no gaps in your process."),
            ("مەودای کارێکی نووسراو", "A written scope",
             "پێش دەستپێکردن هەموو شتێک بە نووسراو دیاری دەکرێت.",
             "Everything is fixed in writing before we start."),
            ("کۆدەکە هی تۆیە", "The code is yours",
             "دوای پارەدانی کۆتایی، کۆدی تایبەت بۆ پرۆژەکەت هی تۆیە.",
             "After final payment, the code we wrote is yours."),
        ],
        how=[
            ("چاوپێکەوتن و شیکردنەوە", "Discovery",
             "کارەکەت دەبینین و پێویستییەکان دەنووسین.",
             "We study your workflow and write the requirements."),
            ("پێشنیار و پێشەکی", "Proposal and deposit",
             "نرخ، بەروار و مەودای کار؛ پێشەکی ٥٠ لە سەد.",
             "Price, timeline and scope; 50% deposit."),
            ("گەشەپێدان و ڕادەستکردن", "Build and deliver",
             "دیزاین، کۆد، تاقیکردنەوە، ڕاهێنان و پاڵپشتی.",
             "Design, code, testing, training and support."),
        ],
        stats=[("٥٠٪", "پێشەکی", "deposit"),
               ("١٠٠٪", "کۆدی تایبەت", "custom code"),
               ("٣٠", "ڕۆژ گەرەنتی", "day warranty")],
        packages=[("پرۆژەی بچووک", "Small build", "١,٢٠٠ دۆلار+", "$1,200+", "١–٣ هەفتە", "1–3 weeks"),
                  ("پرۆژەی مامناوەند", "Medium build", "٣,٠٠٠ دۆلار+", "$3,000+", "٤–٨ هەفتە", "4–8 weeks"),
                  ("پلاتفۆرم", "Platform", "٥,٠٠٠ دۆلار+", "$5,000+", "٢–٤ مانگ", "2–4 months")],
    ),
    "website": dict(
        why=[
            ("لە گووگڵ دەبینرێت", "Found on Google", "ناونیشان، سەردێڕ و خێرایی دروست.", "Titles, descriptions and speed done properly."),
            ("بە زمانی کڕیارەکەت", "In your customer's language", "کوردی، عەرەبی و ئینگلیزی.", "Kurdish, Arabic and English."),
            ("لە مۆبایلدا جوانە", "Looks right on mobile", "زیاتر لە ٨٠٪ کڕیار بە مۆبایل دێت.", "Most visitors arrive on a phone."),
        ],
        how=[
            ("زانیاری و وێنە", "Content", "ناو، وێنە و زانیاری بازرگانییەکەت.", "Logo, photos and business details."),
            ("دیزاین و دروستکردن", "Design and build", "دیزاین بەپێی براندەکەت و RTL دروست.", "Design around your brand, RTL done right."),
            ("بڵاوکردنەوە", "Launch", "دۆمەین، هۆستینگ و گووگڵ.", "Domain, hosting and search setup."),
        ],
        stats=[("٣", "زمان", "languages"), ("$300", "سەرەتا", "starting price"), ("SEO", "ئامادە", "ready")],
        packages=[("یەک لاپەڕە", "One-page", "٣٠٠ دۆلار", "$300", "یەک لاپەڕە + فۆرم", "one page + form"),
                  ("چەند لاپەڕە", "Multi-page", "٦٠٠ دۆلار", "$600", "تا ٦ لاپەڕە", "up to 6 pages"),
                  ("فرە زمان", "Multilingual", "١,٠٠٠ دۆلار", "$1,000", "٣ زمان + SEO", "3 languages + SEO")],
    ),
    "ecommerce": dict(
        why=[
            ("فرۆشتن بەبێ دوکان", "Sell without a shop", "کاڵاکانت ٢٤ کاتژمێر بەردەستن.", "Your products are available 24/7."),
            ("داواکاری بە ڕێک", "Orders in order", "هەر داواکارییەک دۆخ و بەدواداچوونی هەیە.", "Every order has a status and tracking."),
            ("ڕاپۆرتی فرۆشتن", "Sales reports", "دەزانیت چ کاڵایەک دەفرۆشرێت.", "Know which products actually sell."),
        ],
        how=[
            ("کاڵا و وێنە", "Products and photos", "کاڵا، نرخ و وێنە لە پانێڵ.", "Products, prices and photos in the panel."),
            ("پارەدان و گەیاندن", "Payments and delivery", "زەین کاش، پارە لە کاتی گەیاندن.", "ZainCash or cash on delivery."),
            ("بڵاوکردنەوە", "Launch", "دۆمەین، هۆستینگ و ئامادەکردن.", "Domain, hosting and go-live."),
        ],
        stats=[("∞", "کاڵا", "products"), ("٣", "زمان", "languages"), ("$4000", "تەواو", "full build")],
        packages=[("بازاڕگە", "Marketplace", "٤,٠٠٠ دۆلار", "$4,000", "کاڵا بێ سنوور", "unlimited products"),
                  ("بازاڕگە + ئەپ", "Marketplace + app", "٧,٠٠٠ دۆلار", "$7,000", "ئەپ بۆ کڕیار", "customer app"),
                  ("تایبەت", "Custom", "پەیوەندی بکە", "contact us", "بەپێی پێویست", "tailored")],
    ),
    "exam": dict(
        why=[
            ("لیژنە بە دەست", "Papers by hand", "لیژنە بە CSV یان Excel دروست دەکرێت و هاوردە دەکرێت، نەک بە دەست نووسرێتەوە.", "Papers are authored or imported from CSV/Excel instead of being retyped."),
            ("بێ ئینتەرنێت لە کاتی تاقیکردنەوە", "No internet during the exam", "لەسەر سێرڤەرێکی ناوخۆیی کار دەکات؛ هیچ وەڵامێک لەدەست ناچێت.", "Runs on a local server; no answer is lost."),
            ("نمرەدان بە یەکجا", "One-pass grading", "هەموو وەڵامەکان یەکجا هەڵدەسەنگێنرێن و ڕاپۆرت دروست دەبێت.", "Every answer is graded together and reports are generated."),
        ],
        how=[
            ("تاقیکردنەوە دروست بکە", "Build the exam", "پرسیارەکان بە CSV،JSON هاوردە دەکرێن یان دەنووسرێن.", "Import questions from CSV or author them with six question types."),
            ("بڵاوی بکەوە", "Publish", "کۆدێک بۆ خوێندکاران؛ شاشەی تاقیکردنەوە و کاتژمێر.", "An access code for students; exam screen and timer."),
            ("ئەنجام ببینە", "See results", "نمرە، فلتەر، CSV و چاپ.", "Marks, filters, CSV and printing."),
        ],
        stats=[("٦١", "تاقیکردنەوە لە بانکی سیستەم", "exams in the system bank"),
               ("٢,١٣٤", "ئەنجامی تۆمارکراو", "results recorded"),
               ("٥٠", "خوێندکار بەیەکەوە", "students at once")],
        packages=[("پەیمانگا", "Institute", "١,٥٠٠ دۆلار", "$1,500", "تا ٣٠٠ خوێندکار، ساڵانە +٣٠٠ دۆلار", "up to 300 students, +$300/yr"),
                  ("زانکۆ", "University", "٢,٠٠٠ دۆلار", "$2,000", "تا ١,٥٠٠ خوێندکار، ساڵانە +٣٠٠ دۆلار", "up to 1,500 students, +$300/yr"),
                  ("تایبەت", "Custom", "پەیوەندی بکە", "contact us", "بێ سنوور و چەند کەمپەس", "unlimited / multi-campus")],
    ),
    "app": dict(
        why=[
            ("ئەپ و پانێڵ بەیەکەوە", "App and panel together", "کڕیار، کارمەند و بەڕێوەبەر لە یەک سیستەم.", "Customer, staff and admin in one system."),
            ("داواکاری بە کاتی ڕاستەقینە", "Real-time orders", "شوێن، دۆخ و ئاگادارکردنەوە.", "Location, status and notifications."),
            ("بۆ بازاڕی کوردستان", "Made for this market", "کوردی، عەرەبی، ئینگلیزی و RTL.", "Kurdish, Arabic, English and RTL."),
        ],
        how=[
            ("بیرۆکە و پلان", "Idea and plan", "مەودای کار، شاشەکان و مۆدێل.", "Scope, screens and data model."),
            ("ئەپ و پانێڵ", "App and panel", "ئەپی کڕیار،کارمەند + پانێڵی وێب.", "Customer/staff apps + web panel."),
            ("بڵاوکردنەوە", "Launch", "ئەپ ستۆر، گووگڵ پلەی و راهێنان.", "App Store, Google Play and training."),
        ],
        stats=[("٢", "ئەپ", "apps"), ("$5000+", "سەرەتا", "from"), ("٢–٤", "مانگ", "months")],
        packages=[("MVP", "MVP", "٥,٠٠٠ دۆلار+", "$5,000+", "ئەپ + پانێڵ", "app + panel"),
                  ("پلاتفۆرم", "Platform", "١٠,٠٠٠ دۆلار+", "$10,000+", "فرە ڕۆڵ و پارەدان", "multi-role + payments"),
                  ("تایبەت", "Custom", "پەیوەندی بکە", "contact us", "بەپێی پێویست", "tailored")],
    ),
}


ENRICH = {
    "gihan": dict(
        features=[
            ("کاشێری خێرا + چاپ،واتسئاپی پسووڵە", "Fast cashier + print/WhatsApp receipt"),
            ("کۆدی کڕیار و گروپی داشکاندن", "Customer codes and discount groups"),
            ("چوار کەناڵی فرۆشتن لە یەک شوێن", "Four sales channels in one place"),
            ("قازانجی هەر داواکارییەک", "Profit on every order"),
            ("کۆگا بە لیستری جووڵە", "Stock with a movement ledger"),
            ("چەند فرۆشگا،لق لە یەک سیستەم", "Multi-store / multi-branch in one system"),
            ("ڕۆڵ و دەسەڵات بۆ کاشێر و بەڕێوەبەر", "Roles and permissions for cashier and manager"),
            ("کۆنتەرۆلی سندوق و ڕاپۆرتی ڕۆژانە", "Cash drawer control and daily reports"),
            ("کۆمیشنی ئەپی گەیاندن وەک خەرجی", "Delivery commission recorded as an expense"),
            ("PWA، کارکردن لە وێبگەڕ بێ دامەزراندن", "PWA — runs in the browser, no install"),
        ],
        faq=[
            ("بە چ زمانێکە؟", "Which languages?", "کوردی، عەرەبی، فارسی و ئینگلیزی، RTL تەواو.", "Kurdish, Arabic, Persian and English, full RTL."),
            ("داتای کۆنم دەگوازرێتەوە؟", "Can my old data move?", "بەڵێ، کاڵا،کڕیار،قەرز لە Excel.", "Yes — products, customers and debt from Excel."),
            ("لە کوێ کار دەکات؟", "Where does it run?", "سێرڤەری خۆت یان هەور؛ لە وێبگەڕ لەسەر PC، تابلێت و مۆبایل.", "Your server or the cloud; in a browser on PC, tablet and phone."),
            ("ئەپ هەیە؟", "Is there a mobile app?", "نا، بەڵام PWA وەک ئەپ لەسەر مۆبایل دادەبەزێت.", "No, but the PWA installs like an app."),
            ("پشتگیری؟", "Support?", "٣ مانگ لەخۆدەگرێت.", "3 months included."),
            ("نرخ؟", "Price?", "بەپێی پاکێج؛ بۆ نرخی تایبەت پەیوەندی بکە.", "By package; ask for a custom quote."),
        ],
    ),
    "zuba": dict(
        features=[
            ("فرۆشتن و چاپکردنی پسووڵە", "Sales and printable invoices"),
            ("پێشکەشکردن و پێشنووس", "Quotations and offers"),
            ("گەڕاندنەوەی کاڵا و داشکاندن", "Returns and discounts"),
            ("بەڕێوەبردنی کۆگا و بارکۆد", "Inventory and barcode management"),
            ("ئاگادارکردنەوەی کەمبوونی کۆگا", "Low-stock alerts"),
            ("دەفتەری قەرزی کڕیاران", "Customer debt ledger"),
            ("کڕین لە دابینکەران و داواکاری کڕین", "Supplier purchasing and purchase orders"),
            ("پارە، خەرجی و سەندوق", "Cash, expenses and cashbox"),
            ("ڕاپۆرت و قازانجی خاوێن", "Reports and net profit"),
            ("بەکارهێنەر، ڕۆڵ و دەسەڵات", "Users, roles and permissions"),
            ("سێ زمان + ڕاستبۆچەپ (RTL)", "Three languages with full RTL"),
            ("گەڕانی خێرا بە بارکۆد و مۆبایل", "Fast search by barcode and phone"),
            ("پۆرتاڵی وێب بۆ کڕیار: باڵانس، قەرز و پسوولە", "Customer web portal: balance, debt and invoices"),
            ("فرۆشگای گشتی بۆ کڕیارانی نوێ", "Public storefront for new customers"),
            ("چەند کۆگا و بەڕێوەبردنی چەند دوکان (وەک ئۆنلاین کۆمپانی)", "Several warehouses and several shops (like Online Company)"),
        ],
        faq=[
            ("لە کوێ کار دەکات؟", "Where does it run?", "لەسەر سێرڤەری خۆت یان هەور؛ بە وێبگەڕ.", "On your server or the cloud, through a browser."),
            ("داتای کۆن دەگوازرێتەوە؟", "Is migration possible?", "بەڵێ، کاڵا، کڕیار، قەرز و دابینکەران.", "Yes — products, customers, debt and suppliers."),
            ("چەند بەکارهێنەر؟", "How many users?", "بەپێی پاکێج، لە ٣ بۆ بێ سنوور.", "By package, from 3 to unlimited."),
            ("پشتگیری و راهێنان؟", "Support and training?", "راهێنانی کارمەندان لە کاتی دامەزراندن و ٣ مانگ پشتگیری.", "Staff training at setup and 3 months of support."),
        ],
    ),
    "kapitan": dict(
        features=[
            ("وەیتەر: مێز، دانیشتن و داواکاری بە خول", "Waiter: tables, seating and order rounds"),
            ("شاشەی چێشتخانە (نوێ ← ئامادەکردن ← ئامادە)", "Kitchen display (new → preparing → ready)"),
            ("کاشێر، پارەدان و لیستی پاککردنەوە", "Cashier, payment and cleaning list"),
            ("تێل بۆ دوکانی بچووک", "Till mode for small shops"),
            ("کارکردن بەبێ ئینتەرنێت و بێ سێرڤەر", "Works with no internet and no server"),
            ("هاوتاکردنی خۆکاری ئامێرەکان لەسەر WiFi", "Automatic device sync over WiFi"),
            ("چاپکردنی خۆکاری پسووڵە بە Bluetooth", "Automatic Bluetooth receipt printing"),
            ("تیکتی چێشتخانە بێ نرخ", "Kitchen ticket without prices"),
            ("مێنیو بە دوو ناو (کوردی،ئینگلیزی)", "Menu with two names (Kurdish/English)"),
            ("داتا لەسەر ئامێر، بێ کرێی مانگانە", "On-device data — no monthly bill"),
        ],
        faq=[
            ("ئینتەرنێت پێویستە؟", "Is internet required?", "نا؛ تەنها WiFi ی دوکان یان هۆتسپۆتی مۆبایل.", "No — only local WiFi or a phone hotspot."),
            ("چەند ئامێر؟", "How many devices?", "٢–٣ (وەیتەر، چێشتخانە، کاشێر)، هەر ئامێرێک ڕۆڵێکی هەیە.", "2–3 (waiter, kitchen, cashier), each with its own role."),
            ("چ پرینتەرێک؟", "Which printer?", "٨٠ ملم گەرمی بە Bluetooth (ESC،POS).", "80 mm thermal over Bluetooth (ESC/POS)."),
            ("پسووڵە بە کوردی؟", "Kurdish receipts?", "نا؛ پرینتەرەکانی گەرمی کوردی پشتگیری ناکەن. ناوی کاڵا لە ئەپدا کوردی دەردەکەوێت.", "No — thermal printers don't render Kurdish; product names show in Kurdish in the app."),
            ("ئایفۆن؟", "iPhone?", "نا، تەنها ئەندرۆید.", "No — Android only."),
            ("نرخ؟", "Price?", "بەپێی پاکێج.", "By package."),
        ],
    ),
    "exam": dict(
        features=[
            ("دروستکردن و بڵاوکردنەوەی تاقیکردنەوە بە کۆد", "Build and publish exams with an access code"),
            ("شەش جۆری پرسیار", "Six question types"),
            ("هاوردەکردنی CSV،JSON بە ڕاپۆرتی پێشوەخت", "CSV/JSON import with a dry-run report"),
            ("شاشەی خوێندکار: یەک پرسیار، پالێت، کاتژمێر", "Student screen: one question, palette, timer"),
            ("دانیشتنی ئۆفلاین بە ناردنی خۆکار", "Offline sitting with queued submit"),
            ("ئەنجام، فلتەر، CSV و چاپ", "Results, filters, CSV and printing"),
            ("چاودێری زیندووی دانیشتن", "Live sitting monitor"),
            ("ئاسایش: وەڵامی ڕاست هەرگیز بۆ خوێندکار نانێردرێت", "Security: correct answers never reach the student"),
            ("گواستنەوە لە وەشانی کۆن", "Migration from the old version"),
        ],
        faq=[
            ("بێ ئینتەرنێت کار دەکات؟", "Does it work offline?", "بەڵێ، تەنها سەرەتا و ناردن تۆڕ دەوێت؛ دانیشتن ئۆفلاین بەردەوام دەبێت.", "Yes — only start and submit need network; the sitting continues offline."),
            ("چ ئامێرێک پێویستە؟", "What hardware is needed?", "وێبگەڕ لەسەر PC یان تابلێت؛ سێرڤەرێکی ناوخۆیی.", "A browser on PC or tablet; a local server."),
            ("وەڵامەکان پارێزراون؟", "Are answers protected?", "وەڵامی ڕاست هەرگیز بۆ خوێندکار نانێردرێت؛ نمرەدان لە سێرڤەر.", "Correct answers never go to the student; grading happens on the server."),
            ("لە سیستەمی کۆن دەگوازرێتەوە؟", "Can you migrate our old system?", "بەڵێ، ٥٤ بنکەدراوە و ٥,٧٤٦ وەڵام تاقیکراونەتەوە (٩٨.٢٪ وەک یەک).", "Yes — 54 databases and 5,746 answers were tested (98.2% identical)."),
            ("چەند خوێندکار بە یەکەوە؟", "How many students at once?", "لەسەر سێرڤەرێکی ئاسایی بە ئاسانی ٥٠+؛ بەپێی پاکێج.", "50+ on a normal server; by package."),
            ("نرخ؟", "Price?", "پەیمانگا ١,٥٠٠ دۆلار، زانکۆ ٢,٠٠٠ دۆلار، ساڵانە ٣٠٠ دۆلار.", "Institute $1,500, university $2,000, $300 per year."),
        ],
    ),
}

for p in DATA:
    p.update(EXTRA.get(p["key"], {}))
    p.update(ENRICH.get(p["key"], {}))



def marketing_pdfs(key):
    prefix = MKT_PREFIX.get(key, key)
    files = sorted(glob.glob(os.path.join(MKT_DIR, f"{prefix}*.pdf")))
    out = []
    for f in files:
        name = os.path.basename(f)
        if "guide" in name:
            continue
        lang = "ku"
        for l in ("ku", "ar", "en"):
            if f"-{l}.pdf" in name or f"_{l}." in name:
                lang = l
        label = {"ku": ("کوردی", "Kurdish"), "ar": ("عەرەبی", "Arabic"), "en": ("ئینگلیزی", "English")}[lang]
        out.append((f"marketing/{name}", label[0], label[1]))
    return out


HEAD = """<!DOCTYPE html>
<html lang="ckb" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ku} — کیسرا تێک</title>
<meta name="description" content="{tag_ku}">
<meta name="theme-color" content="#FBF8F1">
<link rel="icon" href="../assets/logo/favicon.png">
<link rel="canonical" href="https://arkan-leki.github.io/kisra/products/{key}.html">
<meta property="og:type" content="product">
<meta property="og:title" content="{ku} — Kisra Tech">
<meta property="og:description" content="{tag_ku}">
<meta property="og:image" content="https://arkan-leki.github.io/kisra/assets/og-image.jpg">
<link rel="stylesheet" href="../css/styles.css">
</head>
<body>

<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="../index.html" aria-label="Kisra Tech">
      <img class="ku" src="../assets/logo/lockup-ku.png" alt="Kisra Tech، کیسرا تێک">
      <img class="en" src="../assets/logo/lockup-en.png" alt="Kisra Tech">
    </a>
    <nav class="nav-links" id="navLinks">
      <a href="../index.html#products"><span class="ku">بەرهەمەکان</span><span class="en">Products</span></a>
      <a href="../index.html#clients"><span class="ku">کڕیارەکان</span><span class="en">Clients</span></a>
      <a href="../index.html#services"><span class="ku">خزمەتگوزاری</span><span class="en">Services</span></a>
      <a href="../index.html#contact"><span class="ku">پەیوەندی</span><span class="en">Contact</span></a>
    </nav>
    <div class="nav-actions">
      <button class="lang-btn" id="langBtn" aria-label="Switch language">EN</button>
      <a class="btn btn-ink btn-sm" href="{wa}" target="_blank" rel="noopener"><span class="ku">واتساپ</span><span class="en">WhatsApp</span></a>
      <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

BODY = """<main class="product-page">
  <section class="pp-hero">
    <div class="wrap">
      <nav class="crumbs"><a href="../index.html"><span class="ku">سەرەتا</span><span class="en">Home</span></a> <span>/</span> <a href="../index.html#products"><span class="ku">بەرهەمەکان</span><span class="en">Products</span></a> <span>/</span> <b><span class="ku">{ku}</span><span class="en">{en}</span></b></nav>
      <div class="pp-hero-grid">
        <div>
          <div class="mono kicker">{kicker}</div>
          <h1><span class="ku">{ku}</span><span class="en">{en}</span></h1>
          <p class="pp-tag"><span class="ku">{tag_ku}</span><span class="en">{tag_en}</span></p>
          <div class="pp-meta">
            <div class="pp-price"><span class="mono"><span class="ku">نرخ</span><span class="en">price</span></span><b>{price}</b><small><span class="ku">{price_ku}</span><span class="en">{price_en}</span></small></div>
            <a class="btn btn-gold" href="{wa}" target="_blank" rel="noopener"><span class="ku">پەیوەندی بکە</span><span class="en">Get in touch</span></a>
            <a class="btn btn-ghost" href="../assets/pdf/{catalog}" download><span class="ku">داگرتنی کاتالۆگی PDF</span><span class="en">Download PDF catalogue</span></a>
          </div>
        </div>
        <div class="pp-shot"><img src="../assets/shots/{hero}" alt="{en} screenshot"></div>
      </div>
    </div>
  </section>

  <section class="section pp-about">
    <div class="wrap pp-2col">
      <div>
        <div class="mono kicker">OVERVIEW</div>
        <h2><span class="ku">دەربارەی {ku}</span><span class="en">About {en}</span></h2>
        <p class="pp-overview"><span class="ku">{overview_ku}</span><span class="en">{overview_en}</span></p>
        <div class="pp-tech">{tech}</div>
      </div>
      <div>
        <div class="mono kicker">WHY</div>
        <h2><span class="ku">بۆچی {ku}؟</span><span class="en">Why {en}?</span></h2>
        <div class="why-list">{why}</div>
      </div>
    </div>
  </section>

  <section class="section pp-how">
    <div class="wrap">
      <div class="mono kicker">HOW IT WORKS</div>
      <h2><span class="ku">چۆن کار دەکات</span><span class="en">How it works</span></h2>
      <div class="how-grid">{how}</div>
      <div class="stat-band">{stats}</div>
    </div>
  </section>

  <section class="section pp-features-sec">
    <div class="wrap">
      <div class="mono kicker">FEATURES</div>
      <h2><span class="ku">تایبەتمەندییەکان</span><span class="en">Features</span></h2>
      <ul class="feature-grid">{features}</ul>
    </div>
  </section>

  <section class="section pp-gallery">
    <div class="wrap">
      <div class="mono kicker">SCREENS</div>
      <h2><span class="ku">شاشەکان</span><span class="en">Screens</span></h2>
      <div class="shots-grid{shots_class}">{shots}</div>
    </div>
  </section>

  <section class="section pp-packages">
    <div class="wrap">
      <div class="mono kicker">PACKAGES</div>
      <h2><span class="ku">پاکێج و نرخ</span><span class="en">Packages and pricing</span></h2>
      <div class="pkg-grid">{packages}</div>
    </div>
  </section>

  <section class="section pp-downloads">
    <div class="wrap">
      <div class="mono kicker">DOWNLOADS</div>
      <h2><span class="ku">داگرتنەکان</span><span class="en">Downloads</span></h2>
      <p class="pp-note"><span class="ku">پەڕەی بەرهەم و کاتالۆگەکانی PDF.</span><span class="en">Product sheet and the PDF catalogues.</span></p>
      <div class="dl-grid">{pdfs}</div>
      <div class="pdf-preview">
        <div class="pdf-preview-head">
          <span class="mono">PDF PREVIEW</span>
          <a class="product-link" href="../assets/pdf/{preview_pdf}" target="_blank" rel="noopener"><span class="ku">کردنەوە</span><span class="en">Open</span> ↗</a>
        </div>
        <a class="pdf-thumb" href="../assets/pdf/{preview_pdf}" target="_blank" rel="noopener">
          <img src="../assets/pdf/preview/{preview_key}.webp" alt="{en} PDF preview" loading="lazy">
        </a>
      </div>
    </div>
  </section>

  <section class="section pp-faq">
    <div class="wrap">
      <div class="mono kicker">FAQ</div>
      <h2><span class="ku">پرسیارە باوەکان</span><span class="en">Common questions</span></h2>
      <div class="faq-list">{faq}</div>
    </div>
  </section>

  {works}

  <section class="cta">
    <div class="wrap">
      <div class="cta-card reveal">
        <div>
          <h2><span class="ku">با {ku} دابنێین</span><span class="en">Let's set up {en}</span></h2>
          <p><span class="ku">پەیوەندی بکە، کارەکەت دەبینین و پێشنیارێکی ڕوون دەدەینەوە.</span><span class="en">Tell us what you run today. You get a clear plan and a price.</span></p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-ink" href="{wa}" target="_blank" rel="noopener"><span class="ku">لە واتساپ پەیوەندی بکە</span><span class="en">Message on WhatsApp</span></a>
          <div class="cta-contact"><a href="tel:{phone_raw}" dir="ltr">{phone}</a><br><a href="mailto:{mail}" dir="ltr">{mail}</a></div>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <img class="foot-logo ku" src="../assets/logo/lockup-ku.png" alt="Kisra Tech — کیسرا تێک">
        <img class="foot-logo en" src="../assets/logo/lockup-en.png" alt="Kisra Tech">
        <p><span class="ku">سیستەم بۆ بازرگانی. دروستکراوە لە کوردستان، بۆ کوردستان.</span><span class="en">Business software. Built in Kurdistan, for Kurdistan.</span></p>
        <div class="foot-social">
          <a href="https://wa.me/9647706947874" target="_blank" rel="noopener" aria-label="WhatsApp" title="WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.7 2z"/></svg></a>
          <a href="mailto:arkan.leki@gmail.com" aria-label="Email" title="Email"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></a>
          <a href="../assets/pdf/kisra-catalogue-long-a4.pdf" download aria-label="Catalogue PDF" title="Catalogue PDF"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg></a>
        </div>
      </div>
      <div class="foot-col">
        <h4><span class="ku">بەرهەمەکان</span><span class="en">Products</span></h4>
        <a href="gihan.html"><span class="ku">گیهان</span><span class="en">Gihan</span></a>
        <a href="zuba.html"><span class="ku">زوبا</span><span class="en">Zuba</span></a>
        <a href="kapitan.html"><span class="ku">کاپیتان پۆس</span><span class="en">Kapitan POS</span></a>
        <a href="exam.html"><span class="ku">سیستەمی تاقیکردنەوە</span><span class="en">Exam system</span></a>
        <a href="custom.html"><span class="ku">پرۆژەی تایبەت</span><span class="en">Custom build</span></a>
      </div>
      <div class="foot-col">
        <h4><span class="ku">کۆمپانیا</span><span class="en">Company</span></h4>
        <a href="../index.html#work"><span class="ku">کارەکانمان</span><span class="en">Work</span></a>
        <a href="../index.html#clients"><span class="ku">کڕیارەکان</span><span class="en">Clients</span></a>
        <a href="../index.html#services"><span class="ku">خزمەتگوزارییەکان</span><span class="en">Services</span></a>
        <a href="../assets/pdf/kisra-catalogue-long-a4.pdf" download><span class="ku">کاتالۆگ (PDF)</span><span class="en">Catalogue (PDF)</span></a>
      </div>
      <div class="foot-col">
        <h4><span class="ku">پەیوەندی</span><span class="en">Contact</span></h4>
        <a href="mailto:arkan.leki@gmail.com" dir="ltr">arkan.leki@gmail.com</a>
        <a href="tel:+9647706947874" dir="ltr">+964 770 694 7874</a>
        <a href="https://wa.me/9647706947874" target="_blank" rel="noopener">WhatsApp</a>
        <a href="../index.html#contact"><span class="ku">فۆرمی پەیوەندی</span><span class="en">Get in touch</span></a>
      </div>
    </div>
    <div class="foot-wordmark">Kisra<span class="dot">.</span>Tech</div>
    <div class="foot-bottom">
      <span dir="ltr">© <span id="year">2026</span> KISRA TECH — KURDISTAN REGION, IRAQ</span>
      <a href="../index.html"><span class="ku">گەڕانەوە بۆ سەرەتا</span><span class="en">Back to home</span></a>
    </div>
  </div>
</footer>

<script src="../js/app.js"></script>
</body>
</html>
"""

WORKS_HTML = '<div class="pp-work"><img src="../assets/shots/app-poshya.webp" alt="Poshya" loading="lazy"><div><b><span class="ku">پۆشیا</span><span class="en">Poshya</span></b><p><span class="ku">بازاڕگەیەکی مۆدەی سێ زمانەیە بۆ کڕیار و فرۆشگاکان لە کوردستان و عێراق.</span><span class="en">A trilingual fashion marketplace for shoppers and stores across Kurdistan and Iraq.</span></p></div></div>\n<div class="pp-work"><div><b><span class="ku">فێرگە</span><span class="en">Ferga</span></b><p><span class="ku">مارکێتپلەیسێکی خوێندنە کە خوێندکاران بە مامۆستا و سەنتەر و قوتابخانەکان دەگەینێت.</span><span class="en">An ed-tech marketplace connecting students with tutors, centres and schools.</span></p></div></div>\n<div class="pp-work"><img src="../assets/shots/ecommerce-jumla.webp" alt="Jumla Iraq" loading="lazy"><div><b><span class="ku">جوملە عێراق</span><span class="en">Jumla Iraq</span></b><p><span class="ku">بازاڕگەیەکی B2B بۆ کۆمپانیا و فرۆشیارەکانی عێراق کە داواکاری نرخ و کاتالۆگی کۆ لە یەک شوێن کۆ دەکاتەوە.</span><span class="en">A B2B wholesale marketplace connecting Iraqi businesses with verified suppliers.</span></p></div></div>\n<div class="pp-work"><img src="../assets/shots/website-shaz.webp" alt="Shaz Print" loading="lazy"><div><b><span class="ku">شاز</span><span class="en">Shaz Print</span></b><p><span class="ku">ماڵپەڕێکی کوردی و ڕاست بۆ چەپ بۆ کۆمپانیایەکی چاپ و ڕیکلام لە گەرمیان.</span><span class="en">A Kurdish RTL marketing site for a print and advertising company in Garmian.</span></p></div></div>\n<div class="pp-work"><img src="../assets/shots/exam-puplis.webp" alt="Puplis" loading="lazy"><div><b><span class="ku">پوپلیس</span><span class="en">Puplis</span></b><p><span class="ku">سیستەمێکی تاقیکردنەوەی ئۆفلاینە بۆ پەیمانگا و زانکۆکان کە لە کاتی تاقیکردنەوەدا پێویستی بە ئینتەرنێت نییە.</span><span class="en">An offline exam platform for institutes and universities that needs no internet during the test.</span></p></div></div>'

LONG_CATALOGUE = ("kisra-catalogue-long-a4.pdf", "کاتالۆگی تەواوی کۆمپانیا (٨ بەرهەم)", "Full company catalogue (8 products)")


def build():
    os.makedirs(OUT, exist_ok=True)
    for p in DATA:
        why = "\n".join(
            f'<div class="why-item-light"><b><span class="ku">{t_ku}</span><span class="en">{t_en}</span></b>'
            f'<p><span class="ku">{d_ku}</span><span class="en">{d_en}</span></p></div>'
            for t_ku, t_en, d_ku, d_en in p.get("why", []))
        how = "\n".join(
            f'<div class="how-step"><span class="how-num">{i+1:02d}</span>'
            f'<h3><span class="ku">{t_ku}</span><span class="en">{t_en}</span></h3>'
            f'<p><span class="ku">{d_ku}</span><span class="en">{d_en}</span></p></div>'
            for i, (t_ku, t_en, d_ku, d_en) in enumerate(p.get("how", [])))
        stats = "\n".join(
            f'<div class="stat-band-item"><b>{v}</b><span><span class="ku">{l_ku}</span><span class="en">{l_en}</span></span></div>'
            for v, l_ku, l_en in p.get("stats", []))
        features = "\n".join(
            f'<li><span class="ku">{ku}</span><span class="en">{en}</span></li>'
            for ku, en in p["features"])
        shots = "\n".join(
            f'<figure><img src="../assets/shots/{s}" alt="{p["en"]} screenshot" loading="lazy"></figure>'
            for s in p["shots"])
        packages = "\n".join(
            f'<div class="pkg"><b><span class="ku">{n_ku}</span><span class="en">{n_en}</span></b>'
            f'<div class="pkg-price">{pr_ku}<span class="pkg-price-en">{pr_en}</span></div>'
            f'<p><span class="ku">{note_ku}</span><span class="en">{note_en}</span></p></div>'
            for n_ku, n_en, pr_ku, pr_en, note_ku, note_en in p.get("packages", []))

        mkt = marketing_pdfs(p["key"])
        dl = []
        for f, l_ku, l_en in mkt:
            dl.append((f, f"کاتالۆگی فەرمی، {l_ku}", f"Marketing catalogue — {l_en}"))
        dl.append((p["pdfs"][0][0], "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)"))
        for f, ku, en in p["pdfs"][1:]:
            if not f.startswith("marketing/"):
                dl.append((f, ku, en))
        for f, ku, en in EXTRA_DOWNLOADS.get(p["key"], []):
            if f not in [d[0] for d in dl]:
                dl.append((f, ku, en))
        dl.append(LONG_CATALOGUE)
        pdfs = "\n".join(
            f'<a class="dl-card" href="../assets/pdf/{f}" download>'
            f'<span class="dl-ext">PDF</span>'
            f'<b><span class="ku">{ku}</span><span class="en">{en}</span></b>'
            f'<span class="dl-arrow">↓</span></a>' for f, ku, en in dl)

        catalog = mkt[0][0] if mkt else p["pdfs"][0][0]
        preview_pdf = mkt[0][0] if mkt else p["pdfs"][0][0]
        preview_key = ("mkt-" + p["key"]) if mkt else p["key"]

        faq = "\n".join(
            f'<details class="faq-item"><summary><span class="ku">{q_ku}</span><span class="en">{q_en}</span></summary>'
            f'<p class="ku">{a_ku}</p><p class="en">{a_en}</p></details>'
            for q_ku, q_en, a_ku, a_en in p["faq"])
        tech = "\n".join(f'<span class="chip">{t}</span>' for t in p["tech"])

        if p["key"] in ("custom", "app", "ecommerce", "website"):
            works_block = ("""  <section class="section pp-works">
    <div class="wrap">
      <div class="mono kicker">PROOF</div>
      <h2><span class="ku">کارەکانی پێشوو</span><span class="en">Previous work</span></h2>
      <p class="pp-note"><span class="ku">ئەم سیستەمانە دروستکراون و بەکاردێن، نەک نموونەی خەیاڵی.</span><span class="en">These are real systems we built and shipped, not mockups.</span></p>
      <div class="pp-works-grid">""" + WORKS_HTML + """</div>
    </div>
  </section>""")
        else:
            works_block = ""
        shots_class = " single" if len(p["shots"]) == 1 else (" triple" if len(p["shots"]) == 3 else "")
        html_out = (HEAD + BODY).format(
            key=p["key"], ku=p["ku"], en=p["en"],
            tag_ku=html.escape(p["tag_ku"]), tag_en=html.escape(p["tag_en"]),
            price=p["price"], price_ku=p["price_ku"], price_en=p["price_en"],
            kicker="KISRA PRODUCT · " + p["en"].upper(),
            overview_ku=p["overview_ku"], overview_en=p["overview_en"],
            tech=tech, why=why, how=how, stats=stats,
            features=features, shots=shots, packages=packages, pdfs=pdfs,
            faq=faq, hero=p["shots"][0],
            catalog=catalog, preview_pdf=preview_pdf, preview_key=preview_key,
            wa=WA, phone=PHONE, phone_raw=PHONE.replace(" ", ""), mail=MAIL,
            works=works_block, shots_class=shots_class,
        )
        with open(os.path.join(OUT, p["key"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote products/" + p["key"] + ".html", len(mkt), "marketing pdfs")


if __name__ == "__main__":
    build()
