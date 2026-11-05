#!/usr/bin/env python3
"""Generate static product pages for the Kisra Tech site.

Reads DATA, writes ../products/<key>.html using the shared site CSS/nav/footer.
Run from anywhere:  python3 tools/build_products.py
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "products")

WA = "https://wa.me/9647706947874"
PHONE = "+964 770 694 7874"
MAIL = "arkan.leki@gmail.com"

# ---------------------------------------------------------------- content
DATA = [
    dict(
        key="gihan",
        ku="گیهان", en="Gihan",
        kind_ku="سیستەمی بەڕێوەبردنی دوکان", kind_en="Retail ERP",
        tag_ku="فرۆشتن ، کۆگا و ڕاپۆرت لە یەک شاشەدا . بۆ دوکانەکانی تاکە لق و فرە لق.",
        tag_en="Sales, stock and reports in one screen — for single and multi-branch shops.",
        price="$500+", price_ku="دۆلار و زیاتر", price_en="from",
        overview_ku="گیهان سیستەمێکی تەواوی فرۆشتن و کۆگایە. هەر داواکارییەک لە هەر کەناڵێکەوە بێت — دوکان، کۆمەڵ، سۆشیاڵ میدیا یان ئەپی گەیاندن — لە یەک شوێن تۆمار دەکرێت و قازانجی ڕاستەقینە دەردەخات: نرخی فرۆشتن کەم کراوە لە تێچووی کاڵا، کۆمیشن و داشکاندن.",
        overview_en="Gihan is a complete sales and stock system. Every order from every channel — storefront, wholesale, social media or delivery apps — is recorded in one place and shows real profit: sale price minus product cost, channel commission and discount.",
        features=[
            ("فرۆشتن لە چەند ئامێر و چەند لقێک بەیەکەوە", "Sell from several devices and branches at once"),
            ("کۆگا و مێژووی جووڵەی هەموو کاڵایەک", "Stock and full movement history for every item"),
            ("ڕاپۆرتی ڕۆژانە ، قازانج و قەرزی کڕیار", "Daily reports, profit and customer debt"),
            ("بەکارهێنەر و دەسەڵات بۆ هەر کارمەندێک", "Users and permissions for every employee"),
            ("کار دەکات لەسەر مۆبایل ، تابلێت و کۆمپیوتەر", "Works on phone, tablet and computer"),
            ("کوردی و عەرەبی و ئینگلیزی لەگەڵ ڕاست بۆ چەپ", "Kurdish, Arabic and English with full RTL"),
        ],
        tech=["FASTAPI", "QUASAR PWA", "POSTGRESQL"],
        shots=["gihan.webp", "gihan-1.webp", "gihan-2.webp"],
        pdfs=[("kisra-gihan-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)"),
              ("kisra-gihan-catalogue.pdf", "کاتالۆگی بەرهەم (٢ لاپەڕە)", "Product catalogue (2 pages)")],
        faq=[("دامەزراندن چەند دەخایەنێت؟", "How long does setup take?",
              "بەپێی قەبارەی دوکان ، بە زۆری چەند ڕۆژێک. داتای کۆنیش دەگوازرێتەوە.",
              "A few days depending on shop size. Existing data is migrated as part of setup."),
             ("پاڵپشتی هەیە؟", "Is support included?",
              "٣٠ ڕۆژ گەرەنتی لەخۆدەگرێت. پاڵپشتی ساڵانە بە ٢٠٠ دۆلار بەردەستە.",
              "30 days warranty included. Yearly support is available for $200.")],
    ),
    dict(
        key="zuba",
        ku="زوبا", en="Zuba",
        kind_ku="سیستەمی بەڕێوەبردنی دابەشکردن", kind_en="Distribution ERP",
        tag_ku="کۆگا ، کڕیار و قەرز بۆ کۆمپانیاکانی دابەشکردن و بەتاڵفرۆشی.",
        tag_en="Stock, customers and debt for distribution and wholesale companies.",
        price="$800+", price_ku="دۆلار و زیاتر", price_en="from",
        overview_ku="زوبا بۆ کۆمپانیاکانی دابەشکردن دروست کراوە: کۆگای فرە شوێن، کڕین و گەڕاندنەوە، قەرزی کڕیار و دابینکەر، پارەدان و حیسابات، و ڕاپۆرتی بەشداران — هەمووی لە یەک سیستەمدا.",
        overview_en="Zuba is built for distribution companies: multi-location stock, purchasing and returns, customer and supplier debt, payments and accounting, partner reports — all in one system.",
        features=[
            ("کۆگای فرە شوێن و مێژووی جووڵەی کاڵا", "Multi-location stock with movement history"),
            ("کڕین ، گەڕاندنەوە و دابینکەران", "Purchasing, returns and suppliers"),
            ("قەرزی کڕیار و دابینکەر بە حیسابی خۆکار", "Customer and supplier debt calculated automatically"),
            ("پارەدان و حیسابات لە یەک شاشەدا", "Payments and accounting in one screen"),
            ("ڕاپۆرتی بەشداران و قازانجی گشتی", "Partner reports and overall profit"),
            ("کردارەکان بە کوردی و عەرەبی و ئینگلیزی", "Works in Kurdish, Arabic and English"),
        ],
        tech=["DJANGO", "DRF", "QUASAR", "POSTGRESQL"],
        shots=["zuba.webp", "zuba-1.webp", "zuba-2.webp", "zuba-3.webp"],
        pdfs=[("kisra-zuba-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)")],
        faq=[("نرخ بەپێی چییە؟", "What sets the price?",
              "قەبارەی کۆگا و ژمارەی لقەکان. سەرەتا لە ٨٠٠ دۆلارەوە.",
              "Stock size and number of locations. Starting from $800."),
             ("دەتوانێت لەگەڵ سیستەمی کۆن کار بکات؟", "Can it work with our old system?",
              "بەڵێ ، داتا دەگوازرێتەوە و لە کاتی دامەزراندن ڕێکدەخرێت.",
              "Yes — data is migrated and reconciled during setup.")],
    ),
    dict(
        key="kapitan",
        ku="کاپیتان پۆس", en="Kapitan POS",
        kind_ku="سیستەمی فرۆشتنی خواردنگا", kind_en="Café POS",
        tag_ku="پۆسێکی خێرا بۆ کافێ ، خواردنگا و چێشتخانە . بێ ئینتەرنێت کار دەکات.",
        tag_en="A fast POS for cafés and restaurants — works fully offline.",
        price="$600+", price_ku="دۆلار و زیاتر", price_en="from",
        overview_ku="کاپیتان پۆس لەسەر ئامێرەکانی خۆت کار دەکات: تابلێتی گارسۆن، تابلێتی چێشتخانە و تابلێتی کاش — تەنها وەک پاڵپشتی، داتا دەکاتە کلۆد. ئەگەر وایفای بپچڕێت، فرۆشتن ناوەستێت.",
        overview_en="Kapitan POS runs on your own devices: waiter tablet, kitchen display and till — the cloud is only a backup. If the Wi-Fi drops, selling does not stop.",
        features=[
            ("فرۆشتن لەسەر تابلێت بە یەک دەست لێدان", "Sell from a tablet in one tap"),
            ("چاپەری بلوتووث ٨٠ ملم بۆ پسوولە", "80 mm Bluetooth receipt printing"),
            ("مێز و شاشەی چێشتخانە بەیەکەوە", "Tables and kitchen display linked"),
            ("کارکردنی ئۆفلاین و هاوکاتکردنی خۆکار", "Offline-first with automatic sync"),
            ("پانێڵی بەڕێوەبردن لە وێب", "Web management panel"),
            ("سێ زمان و مێنیوی فرە زمان", "Three languages, multilingual menu"),
        ],
        tech=["FLUTTER", "BLUETOOTH PRINT", "OFFLINE-FIRST"],
        shots=["kapitan.webp", "kapitan-1.webp", "kapitan-2.webp", "kapitan-3.webp"],
        pdfs=[("kisra-kapitan-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)"),
              ("marketing/kapitanpos-marketing.pdf", "کاتالۆگی تەواو (١٦ لاپەڕە)", "Full marketing PDF (16 pages)")],
        faq=[("پێویستی بە کۆمپیوتەر هەیە؟", "Do I need a computer?",
              "نەخێر — تەنها تابلێت و چاپەرێکی بلوتووث.",
              "No — just a tablet and a Bluetooth printer."),
             ("ئینتەرنێت پێویستە؟", "Is internet required?",
              "نەخێر. سیستەم ئۆفلاین کار دەکات و کاتێک ئینتەرنێت هەبوو خۆی هاوکات دەکات.",
              "No. It works offline and syncs automatically when internet returns.")],
    ),
    dict(
        key="custom",
        ku="پرۆژەی تایبەت", en="Custom ERP",
        kind_ku="سیستەمی تایبەت بۆ کارەکەت", kind_en="Bespoke business system",
        tag_ku="سیستەمێک کە بە تەواوی بۆ کاری خۆت دروست کراوە.",
        tag_en="A system built around your workflow, end to end.",
        price="$1200+", price_ku="دۆلار و زیاتر", price_en="from",
        overview_ku="ئەگەر سیستەمی ئامادە بۆ کارەکەت گونجاو نەبوو، پرۆژەی تایبەت دروست دەکەین: پلان، دیزاین، گەشەپێدان، بڵاوکردنەوە و راهێنان — هەمووی بەپێی مەودای کارێکی نووسراو.",
        overview_en="When a ready-made system does not fit, we build the custom one: planning, design, development, deployment and training — all against a written scope.",
        features=[
            ("پلان و دیزاین بەپێی کاری ڕاستەقینەی تۆ", "Planning and design around your real workflow"),
            ("وێب ، مۆبایل یان هەردووکیان", "Web, mobile, or both"),
            ("کوردی و عەرەبی و ئینگلیزی لەگەڵ ڕاست بۆ چەپ", "Kurdish, Arabic and English with RTL"),
            ("پەیوەندی بە سیستەم و خزمەتگوزارییەکانی تر", "Integrations with your other systems"),
            ("بڵاوکردنەوە و راهێنانی کارمەندان", "Deployment and staff training"),
            ("پاڵپشتی و گەشەپێدانی دواتر", "Support and further development"),
        ],
        tech=["YOUR STACK", "API", "RTL"],
        shots=["custom.webp", "gihan.webp", "zuba.webp"],
        pdfs=[("kisra-custom-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)")],
        faq=[("نرخ چۆن دیاری دەکرێت؟", "How is the price set?",
              "بەپێی مەودای کار. پێشەکی ٥٠ لە سەد لە کاتی ڕێککەوتن.",
              "By scope. 50% deposit at signing, 40% at delivery, 10% at acceptance."),
             ("چەند دەخایەنێت؟", "How long does it take?",
              "لە چەند هەفتەیەکەوە بۆ چەند مانگێک، بەپێی قەبارە. بەروار لە پێشنیارەکەدا دیاری دەکرێت.",
              "Weeks to months depending on size — the timeline is fixed in the proposal.")],
    ),
    dict(
        key="website",
        ku="ماڵپەڕی بازرگانی", en="Business website",
        kind_ku="ماڵپەڕی کۆمپانیا و بەرهەم", kind_en="Company website",
        tag_ku="ماڵپەڕی خێرا و جوان بە کوردی و عەرەبی و ئینگلیزی ، ئامادە بۆ گەڕان لە گووگڵ.",
        tag_en="A fast, multilingual company site that is ready for Google.",
        price="$300", price_ku="دۆلار", price_en="one-time",
        overview_ku="ماڵپەڕی فەرمی بۆ بازرگانییەکەت: دیزاین بەپێی ناوی بازرگانی، فرە زمان، خێرا و ئامادە بۆ مۆبایل — لەگەڵ فۆرمی پەیوەندی و واتساپ.",
        overview_en="An official site for your business: designed around your brand, multilingual, fast and mobile-ready — with a contact form and WhatsApp.",
        features=[
            ("دیزاین بەپێی ناوی بازرگانییەکەت", "Design built around your brand"),
            ("کوردی و عەرەبی و ئینگلیزی لەگەڵ ڕاست بۆ چەپ", "Kurdish, Arabic and English with RTL"),
            ("خێرا و ئامادە بۆ مۆبایل", "Fast and mobile-ready"),
            ("فۆرمی پەیوەندی و واتساپ", "Contact form and WhatsApp"),
            ("ئامادە بۆ گووگڵ (SEO)", "Search-engine ready (SEO)"),
            ("دۆمەین و هۆستینگ بەردەستە", "Domain and hosting available"),
        ],
        tech=["HTML", "RTL", "SEO"],
        shots=["website-shaz.webp"],
        pdfs=[("kisra-website-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)")],
        faq=[("دۆمەین و هۆستینگ لەخۆ دەگرێت؟", "Is domain and hosting included?",
              "نەخێر، بەڵام ڕێکدەخەین و ساڵانە بە نرخی کڕینەکەی دەبێت.",
              "Not included, but we set it up and it stays at cost."),
             ("دەتوانم خۆم نوێی بکەمەوە؟", "Can I update it myself?",
              "بەڵێ — لاپەڕەکان ساکارن و راهێنان دەدرێت.",
              "Yes — pages are simple and we train you on updates.")],
    ),
    dict(
        key="ecommerce",
        ku="بازاڕگەی ئەلیکترۆنی", en="Online marketplace",
        kind_ku="فرۆشتنی ئۆنلاین", kind_en="E-commerce platform",
        tag_ku="بازاڕگەیەکی تەواو بۆ فرۆشتنی ئۆنلاین ، لەگەڵ بەڕێوەبردنی کاڵا و داواکاری و پارەدان.",
        tag_en="A complete online store with products, orders and payments.",
        price="$4000", price_ku="دۆلار", price_en="one-time",
        overview_ku="بازاڕگەی ئەلیکترۆنی بە تەواوی: کاڵا و وێنە و نرخ، داواکاری و بەدواداچوونی ناردن، هەژماری کڕیار و ڕاپۆرتی فرۆشتن — بە کوردی و عەرەبی و ئینگلیزی.",
        overview_en="A full online store: products, photos and prices, orders and delivery tracking, customer accounts and sales reports — in Kurdish, Arabic and English.",
        features=[
            ("کاڵا ، وێنە و نرخ لە پانێڵێکدا", "Products, photos and prices in one panel"),
            ("داواکاری و بەدواداچوونی ناردن", "Orders and delivery tracking"),
            ("هەژماری کڕیار و مێژووی کڕین", "Customer accounts and purchase history"),
            ("ڕاپۆرتی فرۆشتن و قازانج", "Sales and profit reports"),
            ("فرە زمان و ڕاست بۆ چەپ", "Multilingual and RTL"),
            ("ئامادە بۆ پارەدان و گەیاندن", "Ready for payments and delivery"),
        ],
        tech=["NEXT.JS", "SUPABASE", "RTL"],
        shots=["ecommerce-jumla.webp"],
        pdfs=[("kisra-ecommerce-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)")],
        faq=[("چەند کاڵا دەتوانم دابنێم؟", "How many products can I add?",
              "بێ سنوور. پانێڵ بۆ چەند هەزار کاڵا ئامادەیە.",
              "Unlimited — the panel handles thousands of products."),
             ("پارەدان چۆنە؟", "How do payments work?",
              "بەپێی پێویست: پارەدان لە کاتی گەیاندن، زەین کاش، یان دەروازەی پارەدانی ئۆنلاین.",
              "Whatever fits: cash on delivery, ZainCash, or an online payment gateway.")],
    ),
    dict(
        key="exam",
        ku="سیستەمی تاقیکردنەوە", en="Exam system",
        kind_ku="تاقیکردنەوەی خوێندکاران", kind_en="Exams for institutes",
        tag_ku="سیستەمێکی تاقیکردنەوەی ئۆنلاین کە پێویستی بە ئینتەرنێت نییە لە کاتی تاقیکردنەوەدا.",
        tag_en="Online exams that need no internet during the test.",
        price="$1500–2000", price_ku="دۆلار · ساڵانە ٣٠٠ دۆلار", price_en="+ $300/yr",
        overview_ku="سیستەمی تاقیکردنەوەی پەیمانگا و زانکۆ: لیژنەی کاغەزەکە خۆکار ئامادە دەکات، خوێندکاران لە وێبگەڕ تاقیکردنەوە دەکەن، و هەموو وەڵامەکان یەکجا هەڵدەسەنگێنرێن. لە ماوەی تاقیکردنەوەدا پێویستی بە ئینتەرنێت نییە.",
        overview_en="An exam system for institutes and universities: papers are generated automatically, students take the test in a browser, and every answer is graded in one pass. No internet is needed during the exam.",
        features=[
            ("لیژنەی کاغەزەکە خۆکار ئامادە دەکات", "Papers generated automatically"),
            ("خوێندکاران لە وێبگەڕ تاقیکردنەوە دەکەن", "Students take exams in the browser"),
            ("هەموو وەڵامەکان یەکجا هەڵدەسەنگێنرێن", "All answers graded in one pass"),
            ("ئەنجام و ڕاپۆرت بۆ مامۆستا", "Results and reports for teachers"),
            ("چاودێری و کۆنترۆڵی کاتی", "Live monitoring and timing"),
            ("لەسەر سێرڤەرێکی خۆماڵی کار دەکات", "Runs on a local server"),
        ],
        tech=["FLASK", "SQLITE", "FLUTTER"],
        shots=["exam-puplis.webp"],
        pdfs=[("kisra-exam-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)"),
              ("marketing/puplis-marketing-ku.pdf", "کاتالۆگی تەواو — کوردی (٩ لاپەڕە)", "Full marketing PDF — Kurdish (9 pages)"),
              ("marketing/puplis-marketing-ar.pdf", "کاتالۆگی تەواو — عەرەبی", "Full marketing PDF — Arabic"),
              ("marketing/puplis-marketing-en.pdf", "کاتالۆگی تەواو — ئینگلیزی", "Full marketing PDF — English")],
        faq=[("بۆ چەند خوێندکار گونجاوە؟", "How many students does it handle?",
              "٥٠ خوێندکار لە یەک کاتدا دەست پێدەکەن؛ بۆ زانکۆکان بەپێی قەبارە ڕێکدەخرێت.",
              "50 students start at once; large universities are sized to fit."),
             ("ئینتەرنێت پێویستە؟", "Is internet required?",
              "لە کاتی تاقیکردنەوەدا نەخێر — لەسەر سێرڤەری خۆماڵی کار دەکات.",
              "Not during the exam — it runs on a local server.")],
    ),
    dict(
        key="app",
        ku="ئەپی تایبەت", en="Custom app",
        kind_ku="پلاتفۆرمی تایبەت", kind_en="Custom platform",
        tag_ku="ئەپی تایبەت بۆ دەلیڤەری ، تاکسی یان هەر بیرۆکەیەکی نوێ — لە پلانەوە بۆ بڵاوکردنەوە.",
        tag_en="Your own platform for delivery, taxi or a new idea — from plan to launch.",
        price="$5000+", price_ku="دۆلار و زیاتر", price_en="from",
        overview_ku="پلاتفۆرمی تەواو: ئەپی کڕیار، ئەپی کارمەند و پانێڵی بەڕێوەبردن — لەگەڵ شوێن، داواکاری بە کاتی ڕاستەقینە، پارەدان و هەژمار. وەک پۆشیا.",
        overview_en="A complete platform: customer app, staff app and admin panel — with location, real-time orders, payments and accounts. Like Poshya.",
        features=[
            ("ئەپی کڕیار و ئەپی کارمەند", "Customer app and staff app"),
            ("شوێن و داواکاری بە کاتی ڕاستەقینە", "Location and real-time orders"),
            ("پارەدان و هەژمار", "Payments and accounts"),
            ("پانێڵی بەڕێوەبردن لە وێب", "Web admin panel"),
            ("فرە زمان و ڕاست بۆ چەپ", "Multilingual and RTL"),
            ("بڵاوکردنەوە لە ئەپ ستۆر و گووگڵ پلەی", "App Store and Google Play publishing"),
        ],
        tech=["EXPO", "NEXT.JS", "SUPABASE"],
        shots=["app-poshya.webp"],
        pdfs=[("kisra-app-sheet.pdf", "پەڕەی بەرهەم (١ لاپەڕە)", "Product sheet (1 page)")],
        faq=[("چەند دەخایەنێت؟", "How long does it take?",
              "دوو بۆ چوار مانگ بەپێی قەبارە. پێشەکی ٥٠ لە سەد.",
              "Two to four months depending on scope. 50% deposit."),
             ("خاوەندارێتی کام لایەنە؟", "Who owns the code?",
              "دوای پارەدانی کۆتایی، کۆدی تایبەت بۆ پرۆژەکە هی تۆیە.",
              "After the final payment, the code written for your project is yours.")],
    ),
]

# ---------------------------------------------------------------- template
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
      <img class="ku" src="../assets/logo/lockup-ku.png" alt="Kisra Tech — کیسرا تێک">
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
        <div class="pp-tech">
          {tech}
        </div>
      </div>
      <div class="pp-features">
        <div class="mono kicker">FEATURES</div>
        <h2><span class="ku">چی لەخۆ دەگرێت</span><span class="en">What it includes</span></h2>
        <ul class="check-list">
          {features}
        </ul>
      </div>
    </div>
  </section>

  <section class="section pp-gallery">
    <div class="wrap">
      <div class="mono kicker">SCREENS</div>
      <h2><span class="ku">شاشەکان</span><span class="en">Screens</span></h2>
      <div class="shots-grid">{shots}</div>
    </div>
  </section>

  <section class="section pp-downloads">
    <div class="wrap">
      <div class="mono kicker">DOWNLOADS</div>
      <h2><span class="ku">داگرتن و کاتالۆگ</span><span class="en">Downloads</span></h2>
      <p class="pp-note"><span class="ku">هەمان زانیاری بە PDF — بۆ ناردن بۆ کڕیار یان چاپکردن.</span><span class="en">The same material as PDF — to send to a client or print.</span></p>
      <div class="dl-grid">{pdfs}</div>
      <div class="pdf-preview">
        <div class="pdf-preview-head">
          <span class="mono">PDF PREVIEW</span>
          <a class="product-link" href="../assets/pdf/{hero_pdf}" download><span class="ku">داگرتن</span><span class="en">Download</span> ↗</a>
        </div>
        <a class="pdf-thumb" href="../assets/pdf/{hero_pdf}" target="_blank" rel="noopener">
          <img src="../assets/pdf/preview/{key}.webp" alt="{en} — PDF preview" loading="lazy">
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

  <section class="cta">
    <div class="wrap">
      <div class="cta-card reveal">
        <div>
          <h2><span class="ku">با {ku} دابنێین</span><span class="en">Let’s set up {en}</span></h2>
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
    <div class="foot-bottom" style="margin-top:0;border-top:0;padding-top:0">
      <span class="mono">© <span id="year">2026</span> KISRA TECH — KURDISTAN REGION, IRAQ</span>
      <a class="mono" href="../index.html"><span class="ku">گەڕانەوە بۆ سەرەتا</span><span class="en">Back to home</span></a>
    </div>
  </div>
</footer>

<script src="../js/app.js"></script>
</body>
</html>
"""


def build():
    os.makedirs(OUT, exist_ok=True)
    for p in DATA:
        features = "\n".join(
            f'<li><span class="ku">{ku}</span><span class="en">{en}</span></li>'
            for ku, en in p["features"])
        shots = "\n".join(
            f'<figure><img src="../assets/shots/{s}" alt="{p["en"]} screenshot" loading="lazy"></figure>'
            for s in p["shots"])
        pdfs = "\n".join(
            f'''<a class="dl-card" href="../assets/pdf/{f}" download>
                  <span class="dl-ext">PDF</span>
                  <b><span class="ku">{ku}</span><span class="en">{en}</span></b>
                  <span class="dl-arrow">↓</span>
                </a>''' for f, ku, en in p["pdfs"])
        faq = "\n".join(
            f'''<details class="faq-item"><summary><span class="ku">{q_ku}</span><span class="en">{q_en}</span></summary>
                  <p class="ku">{a_ku}</p><p class="en">{a_en}</p></details>'''
            for q_ku, q_en, a_ku, a_en in p["faq"])
        tech = "\n".join(f'<span class="chip">{t}</span>' for t in p["tech"])

        html_out = (HEAD + BODY).format(
            key=p["key"], ku=p["ku"], en=p["en"],
            tag_ku=html.escape(p["tag_ku"]), tag_en=html.escape(p["tag_en"]),
            price=p["price"], price_ku=p["price_ku"], price_en=p["price_en"],
            kicker=f'KISRA PRODUCT · {p["en"].upper()}',
            overview_ku=p["overview_ku"], overview_en=p["overview_en"],
            tech=tech, features=features, shots=shots, pdfs=pdfs, faq=faq,
            hero=p["shots"][0], hero_pdf=p["pdfs"][0][0],
            wa=WA, phone=PHONE, phone_raw=PHONE.replace(" ", ""), mail=MAIL,
        )
        with open(os.path.join(OUT, f'{p["key"]}.html'), "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote", f'products/{p["key"]}.html')


if __name__ == "__main__":
    build()
