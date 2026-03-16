#!/usr/bin/env python3
"""Generate 10 port pages + 7 tip pages for CruiseLink v2"""
import os

BASE = '/Users/kim/.openclaw/workspace/cruiselink-v2'
PORTS_DIR = os.path.join(BASE, 'guide/ports')
TIPS_DIR = os.path.join(BASE, 'guide/tips')

GTM = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-K4PPLZNG');</script>
<!-- End Google Tag Manager -->"""

GTM_NS = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K4PPLZNG"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager -->"""

PORT_STYLE = """  <style>
    .g-hero{position:relative;height:420px;overflow:hidden;display:flex;align-items:flex-end}
    .g-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
    .g-hero-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.75) 0%,rgba(0,0,0,.1) 60%)}
    .g-hero-content{position:relative;z-index:1;width:100%;padding:36px 0;color:#fff}
    .breadcrumb{font-size:.82rem;color:rgba(255,255,255,.75);margin-bottom:10px}
    .breadcrumb a{color:rgba(255,255,255,.75);text-decoration:none}
    .g-hero h1{font-size:2rem;font-weight:900;margin:0 0 10px;line-height:1.2}
    .g-hero-meta{display:flex;gap:10px;flex-wrap:wrap;font-size:.85rem;opacity:.9}
    .g-hero-meta span{background:rgba(255,255,255,.15);padding:3px 10px;border-radius:20px;backdrop-filter:blur(4px)}
    .g-layout{display:grid;grid-template-columns:1fr 300px;gap:36px;max-width:1200px;margin:44px auto;padding:0 20px;align-items:start}
    @media(max-width:900px){.g-layout{grid-template-columns:1fr}.g-hero h1{font-size:1.5rem}}
    .g-body h2{font-size:1.3rem;font-weight:900;color:#1a237e;margin:36px 0 14px;padding-bottom:8px;border-bottom:3px solid #ff6f00;display:inline-block}
    .g-body h3{font-size:1.05rem;font-weight:700;color:#1a237e;margin:20px 0 8px}
    .g-body p{color:#616161;line-height:1.9;margin-bottom:14px}
    .g-body ul{padding-left:20px;color:#616161;line-height:2;margin-bottom:14px}
    .hl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}
    @media(max-width:600px){.hl-grid{grid-template-columns:repeat(2,1fr)}}
    .hl-card{background:#fafafa;border-radius:8px;padding:14px;border-left:3px solid #ff6f00}
    .hl-card .icon{font-size:1.5rem;margin-bottom:6px}
    .hl-card .name{font-size:.88rem;font-weight:700;color:#1a237e}
    .hl-card .desc{font-size:.78rem;color:#9e9e9e;margin-top:3px;line-height:1.5}
    .tip-list{background:#fff8e1;border-radius:8px;padding:16px 20px;margin:16px 0}
    .tip-list li{font-size:.88rem;color:#616161;line-height:1.9}
    .sidebar-card{background:#fff;border:1px solid #eeeeee;border-radius:8px;padding:20px;margin-bottom:18px;box-shadow:0 2px 8px rgba(0,0,0,.1)}
    .sidebar-card h3{font-size:.95rem;font-weight:700;color:#1a237e;margin:0 0 14px;padding-bottom:8px;border-bottom:2px solid #eeeeee}
    .cta-btn{display:block;background:#ff6f00;color:#fff;text-align:center;padding:13px;border-radius:8px;font-weight:700;font-size:.92rem;text-decoration:none;margin-top:8px;transition:background .2s}
    .cta-btn:hover{background:#e65100}
    .cta-btn.navy{background:#1a237e}
    .cta-btn.navy:hover{background:#0d1642}
    h2[id],h3[id]{scroll-margin-top:80px}
    .g-sidebar{position:sticky;top:80px}
    .nearby-port{display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid #eeeeee;font-size:.85rem;text-decoration:none;color:#616161}
    .nearby-port:last-child{border-bottom:none}
    .nearby-port:hover{color:#1a237e}
  </style>"""

TIP_STYLE = """  <style>
    .g-hero{position:relative;height:400px;overflow:hidden;display:flex;align-items:flex-end}
    .g-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
    .g-hero-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.78) 0%,rgba(0,0,0,.1) 60%)}
    .g-hero-content{position:relative;z-index:1;width:100%;padding:36px 0;color:#fff}
    .breadcrumb{font-size:.82rem;color:rgba(255,255,255,.75);margin-bottom:10px}
    .breadcrumb a{color:rgba(255,255,255,.75);text-decoration:none}
    .g-hero h1{font-size:2rem;font-weight:900;margin:0 0 10px;line-height:1.2}
    .g-layout{display:grid;grid-template-columns:1fr 300px;gap:36px;max-width:1200px;margin:44px auto;padding:0 20px;align-items:start}
    @media(max-width:900px){.g-layout{grid-template-columns:1fr}.g-hero h1{font-size:1.5rem}}
    .g-body h2{font-size:1.2rem;font-weight:900;color:#1a237e;margin:36px 0 14px;padding-bottom:8px;border-bottom:3px solid #ff6f00;display:inline-block}
    .g-body p{color:#616161;line-height:1.9;margin-bottom:12px}
    .g-body ul,.g-body ol{padding-left:22px;color:#616161;line-height:2.1;margin-bottom:14px}
    .tip-box{background:#fff8e1;border-left:4px solid #ff6f00;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0}
    .tip-box li{font-size:.88rem;color:#555;line-height:2}
    .sidebar-card{background:#fff;border:1px solid #eeeeee;border-radius:8px;padding:20px;margin-bottom:18px;box-shadow:0 2px 8px rgba(0,0,0,.08)}
    .sidebar-card h3{font-size:.9rem;font-weight:700;color:#1a237e;margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid #eeeeee}
    .toc-list{list-style:none;padding:0;margin:0}
    .toc-list li a{display:block;font-size:.83rem;color:#555;text-decoration:none;padding:5px 8px;border-radius:4px;transition:all .15s}
    .toc-list li a:hover{background:#f5f5f5;color:#1a237e}
    .cta-btn{display:block;background:#ff6f00;color:#fff;text-align:center;padding:13px;border-radius:8px;font-weight:700;font-size:.9rem;text-decoration:none;margin-top:8px;transition:background .2s}
    .cta-btn:hover{background:#e65100}
    .cta-btn.navy{background:#1a237e}
    .g-sidebar{position:sticky;top:80px}
    h2[id]{scroll-margin-top:80px}
  </style>"""

def port_html(filename, title_ko, title_en, country_flag, country_ko, region_ko, region_en,
              img_url, meta_desc, highlights, tips, nearby_ports, intro_p):
    slug = filename.replace('.html', '')
    highlights_html = '\n'.join([
        f'''        <div class="hl-card">
          <div class="icon">{h['icon']}</div>
          <div class="name">{h['name']}</div>
          <div class="desc">{h['desc']}</div>
        </div>''' for h in highlights
    ])
    tips_html = '\n'.join([f'<li>{t}</li>' for t in tips])
    nearby_html = '\n'.join([f'        <a class="nearby-port" href="{np["url"]}">{np["label"]}</a>' for np in nearby_ports])
    
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
{GTM}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_ko} 크루즈 기항지 가이드 2026 | 볼거리·투어·팁 총정리 - 크루즈링크</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{title_ko}, {title_en}, 크루즈 기항지, {region_ko} 크루즈, 크루즈 투어">
  <link rel="canonical" href="https://www.cruiselink.co.kr/guide/ports/{filename}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="크루즈링크">
  <meta property="og:title" content="{title_ko} 크루즈 기항지 가이드 2026 | 볼거리·투어·팁 총정리 - 크루즈링크">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="{img_url}">
  <meta property="og:url" content="https://www.cruiselink.co.kr/guide/ports/{filename}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
  <link rel="stylesheet" href="../../assets/css/style.css">
  <link rel="icon" type="image/png" href="../../assets/images/favicon.png">
  <link rel="shortcut icon" href="../../favicon.ico">
{PORT_STYLE}
</head>
<body>
{GTM_NS}

<div id="header"></div>

<section class="g-hero">
  <img src="{img_url}" alt="{title_ko}" loading="eager">
  <div class="g-hero-overlay"></div>
  <div class="g-hero-content">
    <div class="container">
      <div class="breadcrumb"><a href="../../">홈</a> › <a href="../">가이드</a> › <a href="./">기항지 정보</a> › {title_ko}</div>
      <h1>{country_flag} {title_ko} 기항지 가이드</h1>
      <div class="g-hero-meta">
        <span>🌍 {country_ko}</span>
        <span>🚢 {region_ko} 크루즈 기항지</span>
        <span>✈️ 크루즈 기항 시 볼거리 총정리</span>
      </div>
    </div>
  </div>
</section>

<div class="g-layout">
  <article class="g-body">

    <h2 id="intro">{title_ko} 소개</h2>
    {intro_p}

    <h2 id="highlights">주요 볼거리 & 명소</h2>
    <div class="hl-grid">
{highlights_html}
    </div>

    <h2 id="tips">크루즈 기항지 실전 팁</h2>
    <ul class="tip-list">{tips_html}</ul>

    <h2 id="cruise">이 기항지를 포함한 크루즈 찾기</h2>
    <p>{title_ko}을(를) 기항하는 크루즈 상품은 크루즈링크에서 검색하실 수 있습니다. 전문 상담원이 최적의 노선과 일정을 안내해 드립니다.</p>

  </article>

  <aside class="g-sidebar">
    <div class="sidebar-card">
      <h3>📋 목차</h3>
      <ul style="list-style:none;padding:0;margin:0">
        <li style="margin-bottom:2px"><a href="#intro" style="font-size:.85rem;color:#616161;text-decoration:none;padding:4px 8px;display:block;border-radius:4px" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background=''">지역 소개</a></li>
        <li style="margin-bottom:2px"><a href="#highlights" style="font-size:.85rem;color:#616161;text-decoration:none;padding:4px 8px;display:block;border-radius:4px" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background=''">주요 볼거리</a></li>
        <li style="margin-bottom:2px"><a href="#tips" style="font-size:.85rem;color:#616161;text-decoration:none;padding:4px 8px;display:block;border-radius:4px" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background=''">실전 팁</a></li>
        <li style="margin-bottom:2px"><a href="#cruise" style="font-size:.85rem;color:#616161;text-decoration:none;padding:4px 8px;display:block;border-radius:4px" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background=''">크루즈 찾기</a></li>
      </ul>
    </div>
    <div class="sidebar-card">
      <h3>🚢 이 기항지 크루즈 예약</h3>
      <p style="font-size:.83rem;color:#616161;margin-bottom:4px">{title_ko} 기항 크루즈를 찾아보세요.</p>
      <a class="cta-btn" href="../../search.html">크루즈 검색</a>
      <a class="cta-btn navy" href="../../#inquiry">무료 상담 신청</a>
    </div>
    <div class="sidebar-card">
      <h3>🌍 {region_ko} 다른 기항지</h3>
{nearby_html}
    </div>
  </aside>
</div>

<div id="footer"></div>
<script src="../../assets/data/translations.js"></script>
<script src="../../assets/js/api.js"></script>
<script src="../../assets/js/components.js"></script>
<script>
  document.getElementById('header').innerHTML = Components.header('guide', '../../');;
  document.getElementById('footer').innerHTML = Components.footer('../../');
</script>

<div id="guideShareBarMount"></div>
<script>document.getElementById('guideShareBarMount').outerHTML = Components.shareBar();</script>
</body></html>"""


def tip_html(filename, title_ko, img_url, meta_desc, sections, toc_items):
    toc_html = '\n'.join([f'      <li><a href="#{item["id"]}">{item["label"]}</a></li>' for item in toc_items])
    sections_html = '\n'.join([s for s in sections])
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
{GTM}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_ko} 2026 | 크루즈링크 가이드</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://www.cruiselink.co.kr/guide/tips/{filename}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="크루즈링크">
  <meta property="og:title" content="{title_ko} 2026 - 크루즈링크">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="{img_url}">
  <meta property="og:url" content="https://www.cruiselink.co.kr/guide/tips/{filename}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
  <link rel="stylesheet" href="../../assets/css/style.css">
  <link rel="icon" type="image/png" href="../../assets/images/favicon.png">
  <link rel="shortcut icon" href="../../favicon.ico">
{TIP_STYLE}
</head>
<body>
{GTM_NS}

<div id="header"></div>
<section class="g-hero">
  <img src="{img_url}" alt="{title_ko}" loading="eager">
  <div class="g-hero-overlay"></div>
  <div class="g-hero-content">
    <div class="container">
      <div class="breadcrumb">
        <a href="../../">홈</a> › <a href="../">가이드</a> › <a href="./">크루즈 팁</a> › {title_ko}
      </div>
      <h1>{title_ko}</h1>
    </div>
  </div>
</section>
<div class="g-layout">
  <article class="g-body">
{sections_html}
    <h2 id="inquiry">✉️ 크루즈 상담 문의</h2>
    <p>더 궁금한 점이 있으시면 크루즈링크에 문의해 주세요.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:12px">
      <a href="https://pf.kakao.com/_xgYbJG" target="_blank" class="cta-btn" style="flex:1;min-width:160px">💬 카카오톡 상담</a>
      <a href="../../" class="cta-btn navy" style="flex:1;min-width:160px">🚢 크루즈 상품 보기</a>
    </div>
  </article>
  <aside class="g-sidebar">
    <div class="sidebar-card">
      <h3>📌 목차</h3>
      <ul class="toc-list">
{toc_html}
        <li><a href="#inquiry">✉️ 상담 문의</a></li>
      </ul>
    </div>
    <div class="sidebar-card">
      <h3>🚢 크루즈 상담</h3>
      <a href="https://pf.kakao.com/_xgYbJG" target="_blank" class="cta-btn">카카오톡 문의</a>
      <a href="../../" class="cta-btn navy" style="margin-top:8px">상품 검색하기</a>
    </div>
  </aside>
</div>
<div id="guideShareBarMount"></div>
<script>document.getElementById('guideShareBarMount').outerHTML = Components.shareBar();</script>
<div id="footer"></div>
<script src="../../assets/js/components.js"></script>
<script>
  document.getElementById('header').innerHTML = Components.header('guide', '../../');
  document.getElementById('footer').innerHTML = Components.footer('../../');
</script>
</body>
</html>"""


# ============================================================
# PORT DATA
# ============================================================
ports = [
  {
    "filename": "dubai.html",
    "title_ko": "두바이",
    "title_en": "Dubai",
    "country_flag": "🇦🇪",
    "country_ko": "아랍에미리트",
    "region_ko": "중동",
    "region_en": "Middle East",
    "img_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1200&q=80",
    "meta_desc": "두바이(Dubai) 크루즈 기항지 완벽 가이드. 버즈 칼리파, 두바이 몰, 사막 사파리 등 주요 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>두바이(Dubai)는 아랍에미리트(UAE)의 대표적인 국제 크루즈 기항지로, 세계 최고층 빌딩 버즈 칼리파와 인공섬 팜 아일랜드로 유명합니다. 두바이 크루즈 터미널(Dubai Cruise Terminal)은 크루즈 선박의 모항이자 기항지로 모두 이용됩니다.</p><p>크루즈 터미널은 Port Rashid에 위치하며 시내 주요 명소까지 택시로 15~30분 거리입니다. MSC, 코스타, 실버씨 등 다수의 선사가 두바이를 아라비아반도 크루즈 노선의 핵심 기항지로 운영하고 있습니다.</p><p>두바이는 현대 건축물과 사막 문화가 공존하는 독특한 기항지로, 쇼핑·미식·액티비티 모두를 하루 안에 경험할 수 있습니다.</p>",
    "highlights": [
      {"icon": "🏙️", "name": "버즈 칼리파", "desc": "세계 최고층 828m. 124층 전망대 사전 예매 필수"},
      {"icon": "🛍️", "name": "두바이 몰", "desc": "세계 최대 쇼핑몰. 아쿠아리움·아이스링크 내부"},
      {"icon": "🌴", "name": "팜 아일랜드", "desc": "인공 야자나무 섬. 아틀란티스 호텔 어트랙션"},
      {"icon": "🕌", "name": "골드 수크", "desc": "재래시장. 황금 장신구·향신료·직물 쇼핑"},
      {"icon": "🏜️", "name": "사막 사파리", "desc": "낙타 탑승·모래 썰매·BBQ 디너 체험"},
      {"icon": "⛵", "name": "두바이 크릭", "desc": "전통 목선 다우(Dhow)를 타고 역사 지구 유람"},
    ],
    "tips": [
      "크루즈 터미널에서 시내까지 택시 약 15분, 요금 약 AED 30~50",
      "사막 사파리 투어는 하루짜리 크루즈 기항으로는 당일치기 가능 (오전 출발 조건)",
      "두바이 쇼핑몰은 냉방이 매우 강하므로 긴 소매 하나 준비 권장",
      "금요일 정오~오후에는 골드 수크 등 일부 시장 휴무 가능",
      "라마단 기간 중 기항 시 공공장소 음식·음료 섭취 자제 (일몰 후 정상화)",
      "화폐는 UAE 디르함(AED), 환전보다 현지 ATM이 유리",
    ],
    "nearby_ports": [
      {"url": "abu-dhabi.html", "label": "🇦🇪 아부다비"},
      {"url": "muscat.html", "label": "🇴🇲 무스카트 (오만)"},
    ],
  },
  {
    "filename": "danang.html",
    "title_ko": "다낭",
    "title_en": "Da Nang",
    "country_flag": "🇻🇳",
    "country_ko": "베트남",
    "region_ko": "동남아",
    "region_en": "Southeast Asia",
    "img_url": "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?w=1200&q=80",
    "meta_desc": "다낭(Da Nang) 크루즈 기항지 완벽 가이드. 미케 해변, 호이안 구시가지, 바나힐 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>다낭(Da Nang)은 베트남 중부의 대표 크루즈 기항지로, 맑은 바다와 세계문화유산 호이안(Hội An)이 인근에 있어 크루즈 여행자들에게 인기가 높습니다. 다낭 항구(Tiên Sa Port)는 도심에서 약 10km 거리에 위치합니다.</p><p>미케 비치(Mỹ Khê Beach)는 포브스가 선정한 세계 6대 해변 중 하나로, 크루즈 기항 시 당일 해변 라운지를 이용할 수 있습니다. 골든 브릿지(Golden Bridge)가 위치한 바나힐(Bà Nà Hills)도 하루 코스로 방문 가능합니다.</p><p>MSC, 코스타, 노르웨이안 크루즈 등 다수 선사가 동남아 노선에 다낭을 포함하고 있습니다.</p>",
    "highlights": [
      {"icon": "🏖️", "name": "미케 비치", "desc": "포브스 선정 세계 6대 해변. 크루즈 터미널 인접"},
      {"icon": "🌉", "name": "골든 브릿지 (바나힐)", "desc": "거대한 손 위에 놓인 황금빛 보행교. 산악 테마파크"},
      {"icon": "🏮", "name": "호이안 구시가지", "desc": "유네스코 세계문화유산. 등불 축제·전통 시장"},
      {"icon": "🛕", "name": "마블 마운틴", "desc": "대리석 산 속 불교 사원과 동굴. 시내에서 30분"},
      {"icon": "🐉", "name": "드래건 브릿지", "desc": "주말 밤 불·물 뿜는 야경 명소. 다낭 시내 중심"},
      {"icon": "🍜", "name": "다낭 야시장", "desc": "한강변 야시장. 현지 음식·기념품 쇼핑"},
    ],
    "tips": [
      "다낭 항구에서 시내까지 택시 약 15분, 호이안까지 약 30분 (요금 협상 필수)",
      "그랩(Grab) 앱 설치 필수 — 택시보다 저렴하고 요금 투명",
      "호이안 투어 시 반드시 사전에 왕복 교통 예약 필요 (기항 시간 엄수)",
      "바나힐 케이블카는 날씨에 따라 운행 중단될 수 있음",
      "5~9월 우기, 10~12월이 건기로 크루즈 기항 최적 시즌",
      "현지 통화 동(VND) 준비 권장. 소액 쇼핑은 현금 필수",
    ],
    "nearby_ports": [
      {"url": "ho-chi-minh.html", "label": "🇻🇳 호치민"},
      {"url": "hong-kong.html", "label": "🇭🇰 홍콩"},
      {"url": "singapore.html", "label": "🇸🇬 싱가포르"},
    ],
  },
  {
    "filename": "ho-chi-minh.html",
    "title_ko": "호치민",
    "title_en": "Ho Chi Minh City",
    "country_flag": "🇻🇳",
    "country_ko": "베트남",
    "region_ko": "동남아",
    "region_en": "Southeast Asia",
    "img_url": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=1200&q=80",
    "meta_desc": "호치민(사이공) 크루즈 기항지 완벽 가이드. 전쟁박물관, 벤탄시장, 메콩강 투어 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>호치민(Ho Chi Minh City, 구 사이공)은 베트남 남부 최대 도시로, 크루즈 선박은 주로 풀미(Phú Mỹ) 항구에 기항합니다. 풀미 항에서 호치민 시내까지는 약 70km로 버스 또는 택시로 1시간 30분~2시간 소요됩니다.</p><p>호치민은 프랑스 식민지 시대의 유산과 현대 베트남이 공존하는 역동적인 도시입니다. 전쟁박물관(War Remnants Museum), 통일궁(Reunification Palace), 노트르담 대성당 등 역사 유적과 벤탄(Bến Thành) 시장이 인기 명소입니다.</p><p>메콩강 델타(Mekong Delta) 당일 투어도 크루즈 기항 일정에 맞춰 운영되고 있습니다.</p>",
    "highlights": [
      {"icon": "🏛️", "name": "전쟁박물관", "desc": "베트남 전쟁 유물 전시. 역사를 이해하는 핵심 명소"},
      {"icon": "🏰", "name": "통일궁", "desc": "1975년 베트남 통일의 상징. 냉전 시대 지휘 벙커"},
      {"icon": "⛪", "name": "노트르담 대성당", "desc": "프랑스 식민지 시대 건축물. 분홍색 외관"},
      {"icon": "🛒", "name": "벤탄 시장", "desc": "호치민 최대 재래시장. 식재료·기념품·노점 음식"},
      {"icon": "🚤", "name": "메콩강 투어", "desc": "쾌속정으로 수상 마을 탐방. 현지 밀림 음식 체험"},
      {"icon": "🍜", "name": "부이비엔 거리", "desc": "호치민 배낭여행자 거리. 야시장·바·노점 밀집"},
    ],
    "tips": [
      "풀미 항에서 시내까지 편도 약 2시간 — 크루즈 기항 시간 넉넉하게 계획 (최소 8시간 기항)",
      "선사 공식 투어보다 현지 투어 에이전시 예약 시 비용 절감",
      "쌀국수(퍼/Phở) 현지 가격 약 3만~5만 동(약 1,500~2,500원)",
      "그랩(Grab) 앱 필수. 오토바이 택시(Grab Bike)는 빠르지만 짐 있을 때 불편",
      "기온 30도 이상 연중 무더움 — 가벼운 옷과 선크림·모자 필수",
      "달러(USD) 또는 동(VND) 모두 통용. 환율은 현지 환전소가 유리",
    ],
    "nearby_ports": [
      {"url": "danang.html", "label": "🇻🇳 다낭"},
      {"url": "singapore.html", "label": "🇸🇬 싱가포르"},
      {"url": "bangkok.html", "label": "🇹🇭 방콕/람차방"},
    ],
  },
  {
    "filename": "bangkok.html",
    "title_ko": "방콕/람차방",
    "title_en": "Bangkok / Laem Chabang",
    "country_flag": "🇹🇭",
    "country_ko": "태국",
    "region_ko": "동남아",
    "region_en": "Southeast Asia",
    "img_url": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=1200&q=80",
    "meta_desc": "방콕/람차방 크루즈 기항지 완벽 가이드. 왓 프라깨우, 차오프라야 강, 파타야 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>태국의 크루즈 기항지는 방콕 인근의 람차방(Laem Chabang) 항구입니다. 람차방 항에서 방콕 시내까지는 약 130km로 버스·택시로 약 2시간 소요됩니다. 방콕 도심보다 가까운 파타야(Pattaya)는 약 30분 거리입니다.</p><p>방콕은 화려한 왕궁과 사원, 활기찬 재래시장, 수상 시장으로 유명합니다. 왓 프라깨우(에메랄드 불상 사원), 왓 포(와불 사원), 차오프라야 강 유람이 핵심 코스입니다.</p><p>람차방 기항 시 선사 공식 방콕 투어를 이용하거나, 현지 당일 투어를 예약하는 것이 일반적입니다.</p>",
    "highlights": [
      {"icon": "🏯", "name": "왓 프라깨우 (왕궁)", "desc": "에메랄드 불상 봉안 사원. 태국 최고 성지"},
      {"icon": "🛕", "name": "왓 포", "desc": "46m 와불상. 태국 전통 마사지 학교 발상지"},
      {"icon": "⛵", "name": "차오프라야 강 유람", "desc": "왕궁·사원·수상가옥 탐방. 롱테일 보트 투어"},
      {"icon": "🛒", "name": "아시아티크", "desc": "차오프라야 강변 야시장. 2,000개 이상 점포"},
      {"icon": "🌊", "name": "파타야 비치", "desc": "람차방 30분 거리. 해변·수상스포츠·나이트라이프"},
      {"icon": "🏨", "name": "짜뚜짝 시장", "desc": "세계 최대 주말 시장. 8,000개 이상 노점"},
    ],
    "tips": [
      "람차방→방콕 왕복 이동만 약 4시간 소요 — 최소 10시간 기항 조건에서 방콕 방문 가능",
      "선사 공식 방콕 투어 이용 시 하선 마감 시간 보장 (개별 투어는 교통 지연 위험)",
      "왕궁·사원 입장 시 반바지·민소매 금지 — 긴 바지·어깨 가리는 옷 필수",
      "태국 바트(THB) 환전. 공항·터미널 환전소보다 시내 환전상 환율 유리",
      "그랩(Grab) 앱 태국에서도 사용 가능. 미터 택시 탑승 시 미터 on 요청 필수",
      "열대 기후로 연중 무더움. 우기(5~10월) 기간 스콜 대비 우산 지참",
    ],
    "nearby_ports": [
      {"url": "singapore.html", "label": "🇸🇬 싱가포르"},
      {"url": "kota-kinabalu.html", "label": "🇲🇾 코타키나발루"},
      {"url": "phuket.html", "label": "🇹🇭 푸켓"},
    ],
  },
  {
    "filename": "kota-kinabalu.html",
    "title_ko": "코타키나발루",
    "title_en": "Kota Kinabalu",
    "country_flag": "🇲🇾",
    "country_ko": "말레이시아",
    "region_ko": "동남아",
    "region_en": "Southeast Asia",
    "img_url": "https://images.unsplash.com/photo-1596422846543-75c6fc197f11?w=1200&q=80",
    "meta_desc": "코타키나발루(Kota Kinabalu) 크루즈 기항지 완벽 가이드. 키나발루산, 수리아 사바 쇼핑몰, 섬 호핑 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>코타키나발루(Kota Kinabalu, 약칭 KK)는 말레이시아 사바 주의 주도로, 동남아 크루즈의 인기 기항지입니다. 아름다운 일몰과 섬 호핑(island hopping), 열대우림 어드벤처로 유명합니다.</p><p>크루즈 선박은 제셀턴 포인트(Jesselton Point Ferry Terminal) 또는 수리아 사바 인근 항구에 기항합니다. 시내 주요 명소는 터미널에서 도보 또는 택시로 10~20분 거리입니다.</p><p>키나발루 국립공원(유네스코 세계자연유산)은 당일 투어로 방문 가능하며, 맑은 바다에서 스노클링·다이빙을 즐기기에도 최적의 기항지입니다.</p>",
    "highlights": [
      {"icon": "🏔️", "name": "키나발루 국립공원", "desc": "유네스코 세계자연유산. 동남아 최고봉 4,095m"},
      {"icon": "🏝️", "name": "툰쿠 압둘 라만 공원", "desc": "5개 섬으로 구성된 해양공원. 스노클링·다이빙"},
      {"icon": "🌅", "name": "KK 워터프론트", "desc": "일몰 명소. 레스토랑·바·나이트 마켓 밀집"},
      {"icon": "🛒", "name": "수리아 사바 쇼핑몰", "desc": "항구 바로 옆. 면세점·로컬 브랜드 쇼핑"},
      {"icon": "🌿", "name": "라야 라야 섬", "desc": "크리스탈 워터. 당일 섬 호핑 투어 인기"},
      {"icon": "🦧", "name": "로칸 우탄 센터", "desc": "오랑우탄 보호 구역. 열대우림 야생 동물 탐방"},
    ],
    "tips": [
      "제셀턴 포인트에서 섬 호핑 보트 당일 예약 가능 (코타키나발루 해양공원 입장권 별도)",
      "말레이시아 링깃(MYR) 환전. USD·카드도 대부분 쇼핑몰에서 사용 가능",
      "키나발루 국립공원은 KK에서 차로 1시간 30분 — 기항 시간 최소 8시간 필요",
      "열대성 스콜 잦음 — 방수 카메라 케이스·우산 필수",
      "신선한 열대과일 저렴. 워터프론트 야시장에서 꼭 맛볼 것",
      "종교적 보수 성향 지역 포함 — 사원 방문 시 어깨·무릎 가리는 복장",
    ],
    "nearby_ports": [
      {"url": "singapore.html", "label": "🇸🇬 싱가포르"},
      {"url": "penang.html", "label": "🇲🇾 페낭"},
      {"url": "bali.html", "label": "🇮🇩 발리"},
    ],
  },
  {
    "filename": "corfu.html",
    "title_ko": "코르푸",
    "title_en": "Corfu",
    "country_flag": "🇬🇷",
    "country_ko": "그리스",
    "region_ko": "지중해",
    "region_en": "Mediterranean",
    "img_url": "https://images.unsplash.com/photo-1533104816931-20fa691ff6ca?w=1200&q=80",
    "meta_desc": "코르푸(Corfu) 크루즈 기항지 완벽 가이드. 코르푸 구시가지, 아킬레이온 궁전, 팔레오카스트리차 해변 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>코르푸(Corfu, 그리스어: Κέρκυρα/Kerkyra)는 그리스 이오니아 제도에 위치한 아름다운 섬으로, 지중해 크루즈의 인기 기항지입니다. 올리브 나무와 에메랄드빛 바다, 베네치아 식민지 시대의 역사가 어우러진 곳입니다.</p><p>코르푸 항구(Kerkyra Port)는 구시가지 바로 옆에 위치하여 도보로 구시가지를 탐방하기 매우 편리합니다. 코르푸 구시가지는 유네스코 세계문화유산으로 지정되어 있습니다.</p><p>MSC, 코스타, 로열 캐리비안 등 지중해 크루즈 노선 다수가 코르푸를 기항지로 포함합니다.</p>",
    "highlights": [
      {"icon": "🏛️", "name": "코르푸 구시가지", "desc": "유네스코 세계문화유산. 베네치아 건축·좁은 골목"},
      {"icon": "🏰", "name": "구 요새 (Old Fortress)", "desc": "16세기 베네치아 요새. 이오니아해 파노라마 뷰"},
      {"icon": "🏛️", "name": "아킬레이온 궁전", "desc": "오스트리아 황후 시씨가 건립. 그리스 신화 조각상"},
      {"icon": "🏖️", "name": "팔레오카스트리차 해변", "desc": "코르푸 최고 절경. 수정같이 맑은 에메랄드 바다"},
      {"icon": "🫒", "name": "올리브 농장 투어", "desc": "천 년 수령 올리브나무. 현지 올리브오일 시음"},
      {"icon": "🛒", "name": "스피아나다 광장", "desc": "유럽 최대 광장 중 하나. 카페·기념품 쇼핑"},
    ],
    "tips": [
      "항구에서 구시가지까지 도보 5분 — 기항 시 독립 관광 가능",
      "팔레오카스트리차 해변은 택시·투어버스로 약 30분 (편도)",
      "7~8월 성수기 피크. 크루즈 동시 기항 시 구시가지 혼잡",
      "그리스 현지 통화 유로(EUR). 카드 대부분 사용 가능",
      "현지 특산품: 쿠마쿠아트(금귤) 리큐어, 누가, 올리브오일 — 기념품으로 인기",
      "아킬레이온 궁전 방문 시 언덕 위 위치 — 편한 신발 필수",
    ],
    "nearby_ports": [
      {"url": "santorini.html", "label": "🇬🇷 산토리니"},
      {"url": "athens.html", "label": "🇬🇷 아테네 (피레우스)"},
      {"url": "dubrovnik.html", "label": "🇭🇷 두브로브니크"},
      {"url": "kotor.html", "label": "🇲🇪 코토르"},
    ],
  },
  {
    "filename": "tromso.html",
    "title_ko": "트롬소",
    "title_en": "Tromsø",
    "country_flag": "🇳🇴",
    "country_ko": "노르웨이",
    "region_ko": "북유럽",
    "region_en": "Northern Europe",
    "img_url": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=1200&q=80",
    "meta_desc": "트롬소(Tromsø) 크루즈 기항지 완벽 가이드. 오로라 관측, 북극 대성당, 개썰매 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>트롬소(Tromsø)는 노르웨이 북부 북위 69°의 북극권 도시로, '오로라의 수도(Aurora Capital)'로 불립니다. 북유럽 크루즈, 특히 오로라 크루즈의 핵심 기항지입니다.</p><p>트롬소 항구는 도심과 매우 인접해 있어 하선 후 도보로 시내 대부분을 탐방할 수 있습니다. 허트겐루텐(Hurtigruten) 등 노르웨이 연안 크루즈와 MSC, 실버씨 등의 북극권 특별 크루즈가 기항합니다.</p><p>9월~3월 방문 시 오로라(북극광) 관측 확률이 높으며, 한여름(6~7월)에는 '한밤의 태양(Midnight Sun)'을 볼 수 있는 신비한 기항지입니다.</p>",
    "highlights": [
      {"icon": "🌌", "name": "오로라 관측", "desc": "9~3월 북극광 최적 시즌. 외곽 어두운 곳에서 관측"},
      {"icon": "⛪", "name": "북극 대성당", "desc": "독특한 삼각형 건축물. 트롬소의 랜드마크"},
      {"icon": "🚡", "name": "플로야 케이블카", "desc": "트롬소 전경 파노라마. 겨울·여름 모두 운행"},
      {"icon": "🐕", "name": "개썰매 투어", "desc": "허스키 개썰매 체험. 11~3월 시즌 운영"},
      {"icon": "🐳", "name": "고래 관찰 크루즈", "desc": "11~1월 범고래·혹등고래 피오르드 투어"},
      {"icon": "🏔️", "name": "피오르드 하이킹", "desc": "여름 시즌 다양한 트레킹 코스. 설산 조망"},
    ],
    "tips": [
      "오로라 관측은 날씨 의존 — 구름 없고 맑은 날 야외 최소 1~2시간 대기 필요",
      "기온 영하 10~20도 가능 — 레이어링 방한복·방수 장갑·털모자 필수",
      "트롬소 시내 면세점에서 노르웨이 특산품(연어 통조림·치즈) 구매 추천",
      "노르웨이 크로네(NOK) 사용. 물가 비쌈 — 선내 식사 위주 권장",
      "플로야 케이블카는 사전 온라인 예약 시 할인 혜택",
      "한밤의 태양 시즌(6~7월): 24시간 밝음 — 안대 지참 권장",
    ],
    "nearby_ports": [
      {"url": "bergen.html", "label": "🇳🇴 베르겐"},
      {"url": "oslo.html", "label": "🇳🇴 오슬로"},
      {"url": "reykjavik.html", "label": "🇮🇸 레이캬비크"},
    ],
  },
  {
    "filename": "roatan.html",
    "title_ko": "로아탄",
    "title_en": "Roatán",
    "country_flag": "🇭🇳",
    "country_ko": "온두라스",
    "region_ko": "카리브해",
    "region_en": "Caribbean",
    "img_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1200&q=80",
    "meta_desc": "로아탄(Roatán) 크루즈 기항지 완벽 가이드. 메소아메리카 산호초, 스노클링, 집라인 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>로아탄(Roatán)은 온두라스 카리브해에 위치한 섬으로, 세계 2위 규모의 메소아메리카 산호초(Mesoamerican Barrier Reef) 바로 인접해 있어 스노클링과 스쿠버다이빙의 천국입니다.</p><p>로열 캐리비안, 카니발, NCL 등 카리브해 크루즈 선사 대부분이 로아탄을 핵심 기항지로 운영합니다. 선사 전용 비치클럽(Royal Caribbean의 Harvest Cove 등)도 로아탄에 위치합니다.</p><p>가성비 높은 카리브해 기항지로 투명한 바다, 백사장 해변, 열대우림 집라인을 하루에 모두 경험할 수 있습니다.</p>",
    "highlights": [
      {"icon": "🤿", "name": "스노클링 & 다이빙", "desc": "메소아메리카 산호초. 세계 최고 수준의 시야"},
      {"icon": "🦤", "name": "카리브해 정원", "desc": "이구아나·열대조류 서식지. 국립 자연보호구"},
      {"icon": "🌊", "name": "웨스트 베이 비치", "desc": "로아탄 최고 백사장. 크리스탈 워터·야자수"},
      {"icon": "🪂", "name": "집라인 어드벤처", "desc": "열대우림 상공 짚라인. 카리브해 조망"},
      {"icon": "🐬", "name": "돌핀 인카운터", "desc": "돌고래와 수영 체험. 선사 투어 포함 상품 다수"},
      {"icon": "🏖️", "name": "하비스트 코브", "desc": "로열 캐리비안 전용 비치클럽. 수상 놀이기구"},
    ],
    "tips": [
      "로아탄 항구(Mahogany Bay 또는 Coxen Hole)에서 웨스트 베이까지 택시 약 20분",
      "스노클링 장비는 선내 대여보다 항구 근처 현지 대여가 저렴",
      "달러(USD) 사용 가능. 현지 렘피라(HNL)보다 달러 사용이 더 편리",
      "선사 전용 투어(집라인·돌핀 스윔) 사전 온라인 예약 권장",
      "자외선 차단 선크림 SPF50+ 필수. 산호초 보호를 위해 리프 세이프 제품 사용",
      "항구 상점가 바가지 주의 — 흥정 기본",
    ],
    "nearby_ports": [
      {"url": "cozumel.html", "label": "🇲🇽 코수멜"},
      {"url": "grand-cayman.html", "label": "🇰🇾 그랜드 케이맨"},
      {"url": "nassau.html", "label": "🇧🇸 나소"},
    ],
  },
  {
    "filename": "st-lucia.html",
    "title_ko": "세인트루시아",
    "title_en": "Saint Lucia",
    "country_flag": "🌴",
    "country_ko": "세인트루시아",
    "region_ko": "카리브해",
    "region_en": "Caribbean",
    "img_url": "https://images.unsplash.com/photo-1580237541049-2d715a09486e?w=1200&q=80",
    "meta_desc": "세인트루시아(Saint Lucia) 크루즈 기항지 완벽 가이드. 피통 산, 유황 온천, 열대우림 투어 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>세인트루시아(Saint Lucia)는 동카리브해에 위치한 아름다운 섬나라로, 유네스코 세계자연유산인 피통 산(Piton Mountains)과 세계 유일의 드라이브인 화산으로 유명합니다. 카리브해에서 가장 낭만적인 기항지 중 하나로 꼽힙니다.</p><p>크루즈 선박은 주로 카스트리(Castries) 항구에 기항합니다. 항구에서 피통 산까지는 약 1~2시간 소요됩니다. 세인트루시아는 허니문 크루즈와 자연 탐방 크루즈에 특히 인기가 높습니다.</p><p>MSC, 로열 캐리비안, 카니발 등 카리브해 크루즈 노선에 세인트루시아가 포함되어 있습니다.</p>",
    "highlights": [
      {"icon": "⛰️", "name": "피통 산", "desc": "유네스코 세계자연유산. 카리브해 최고의 절경"},
      {"icon": "🌋", "name": "드라이브인 화산", "desc": "세계 유일 드라이브인 화산. 유황 온천 인접"},
      {"icon": "🌿", "name": "열대우림 투어", "desc": "집라인·캐노피 워크·폭포 하이킹 결합 투어"},
      {"icon": "🏖️", "name": "앙스 샤스타네 해변", "desc": "세인트루시아 최고 스노클링 포인트"},
      {"icon": "🍫", "name": "카카오 농장 투어", "desc": "초콜릿 원료 카카오 재배 농장 방문 체험"},
      {"icon": "🛥️", "name": "세일보트 크루즈", "desc": "카리브해 세일링. 피통 산 배경 선셋 뷰"},
    ],
    "tips": [
      "카스트리 항구에서 피통 산까지 약 1시간 30분 — 왕복 최소 5시간 필요",
      "동카리브 달러(XCD) 또는 USD 사용. 카드 대부분 가능",
      "유황 온천은 수영복 필수. 피부 자극 가능성 있으니 장시간 입욕 자제",
      "열대우림 집라인 예약은 선사 투어 또는 현지 에이전시 사전 예약 권장",
      "4~6월 카리브해 허리케인 시즌 외 11~3월이 건기로 최적",
      "피통 산 하이킹은 가이드 필수 — 개인 단독 등산 금지",
    ],
    "nearby_ports": [
      {"url": "barbados.html", "label": "🌴 바베이도스"},
      {"url": "san-juan.html", "label": "🇵🇷 산후안"},
      {"url": "st-maarten.html", "label": "🇸🇽 신트마르턴"},
    ],
  },
  {
    "filename": "barbados.html",
    "title_ko": "바베이도스",
    "title_en": "Barbados",
    "country_flag": "🌴",
    "country_ko": "바베이도스",
    "region_ko": "카리브해",
    "region_en": "Caribbean",
    "img_url": "https://images.unsplash.com/photo-1543731068-7e0f5beff43a?w=1200&q=80",
    "meta_desc": "바베이도스(Barbados) 크루즈 기항지 완벽 가이드. 해리슨 동굴, 럼 증류소, 카리브해 해변 등 볼거리와 크루즈 실전 팁을 크루즈링크가 정리합니다.",
    "intro_p": "<p>바베이도스(Barbados)는 동카리브해의 섬나라로, '럼의 고향'이자 카리브해 크루즈의 주요 모항(homeport) 및 기항지입니다. 브리지타운(Bridgetown)은 크루즈 선사들이 카리브해 일정을 시작하는 거점 도시입니다.</p><p>브리지타운 및 갈라운드 항구(Bridgetown & Garrison)는 유네스코 세계문화유산으로 지정된 역사 지구입니다. 영국 식민지 시대의 건축물과 카리브해 문화가 조화를 이루는 독특한 분위기를 자랑합니다.</p><p>카니발, 로열 캐리비안, 실버씨 등 다수 선사가 바베이도스를 모항 또는 기항지로 운영합니다.</p>",
    "highlights": [
      {"icon": "🪨", "name": "해리슨 동굴", "desc": "석회암 종유동굴. 전기차 투어로 탐방"},
      {"icon": "🥃", "name": "마운트 게이 럼 증류소", "desc": "세계 최고(最古) 럼 증류소 1703년 창립"},
      {"icon": "🏖️", "name": "크레인 비치", "desc": "바베이도스 최고 해변. 분홍빛 모래사장"},
      {"icon": "🐢", "name": "호크스빌 바다거북", "desc": "바닷속 거북 스노클링 투어. 야생 개체 보호"},
      {"icon": "🏛️", "name": "브리지타운 역사 지구", "desc": "유네스코 세계문화유산. 영국식 건축물"},
      {"icon": "🌊", "name": "웨스트 코스트 카타마란", "desc": "카타마란 범선 스노클링+선셋 크루즈"},
    ],
    "tips": [
      "바베이도스 달러(BBD) 사용. 1 USD = 2 BBD로 환율 고정 — 미달러 직접 사용 가능",
      "해리슨 동굴은 사전 예약 권장. 성수기 당일 예약은 매진 가능",
      "마운트 게이 럼 투어 후 면세 구매 가능 — 선내 반입 용량 확인 필수",
      "해변 수상스포츠는 포트 터미널 인근보다 웨스트 코스트(West Coast)가 더 조용하고 저렴",
      "영어 공용어 사용 — 언어 장벽 없음",
      "우버 사용 불가. ZR 버스(노란색 미니버스) 또는 택시 이용",
    ],
    "nearby_ports": [
      {"url": "st-lucia.html", "label": "🌴 세인트루시아"},
      {"url": "san-juan.html", "label": "🇵🇷 산후안"},
      {"url": "st-thomas.html", "label": "🇺🇸 세인트토마스"},
    ],
  },
]

# ============================================================
# TIP DATA
# ============================================================
tips = [
  {
    "filename": "cruise-gratuities.html",
    "title_ko": "크루즈 봉사료(팁) 완벽 가이드",
    "img_url": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1200&q=80",
    "meta_desc": "크루즈 봉사료(팁) 완벽 가이드. 선사별 그라튜어티 금액, 자동 부과 vs 수동 팁, 팁 절약 팁까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "what", "label": "🪙 크루즈 봉사료란?"},
      {"id": "amount", "label": "💰 선사별 봉사료 금액"},
      {"id": "auto", "label": "⚙️ 자동 vs 수동 팁"},
      {"id": "who", "label": "👥 누가 팁을 받나?"},
      {"id": "tips", "label": "💡 절약 팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈 여행에서 봉사료(Gratuity/Service Charge)는 많은 분들이 헷갈리는 항목입니다. 선사별로 금액과 정책이 다르며, 미리 알고 가야 예산을 정확히 계획할 수 있습니다.</p>
    <h2 id="what">🪙 크루즈 봉사료란?</h2>
    <p>크루즈 봉사료는 객실 청소 스탭, 식당 웨이터, 바 직원 등 선상 서비스 직원들에 대한 팁을 통합하여 자동 부과하는 시스템입니다. 육지 레스토랑의 팁과 유사하지만, 크루즈에서는 통상 1인당 하루 단위로 부과됩니다.</p>
    <p>대부분의 선사는 자동 봉사료(Auto Gratuity)를 시스템으로 청구합니다. 일부 선사는 크루즈 요금에 포함(All-Inclusive)되기도 합니다.</p>
    <h2 id="amount">💰 선사별 봉사료 금액 (1인 1박 기준, 2026년)</h2>
    <ul>
      <li>🛳️ <strong>로열 캐리비안</strong> — 약 $18~20 (일반 객실 기준), 스위트 약 $23</li>
      <li>🛳️ <strong>카니발 크루즈</strong> — 약 $16~18</li>
      <li>🛳️ <strong>노르웨이안(NCL)</strong> — 약 $20~25 (프리스타일 다이닝 포함)</li>
      <li>🛳️ <strong>MSC 크루즈</strong> — 약 €14~16 (유럽 노선 기준)</li>
      <li>🛳️ <strong>코스타 크루즈</strong> — 약 €13~15</li>
      <li>🛳️ <strong>실버씨/리젠트</strong> — 요금에 완전 포함(All-In), 추가 팁 불필요</li>
      <li>🛳️ <strong>허틀그루텐</strong> — 서비스 요금 포함 상품 다수</li>
    </ul>
    <p>⚠️ 바(Bar) 이용 시 음료 가격에 약 18~20% 자동 추가 부과. 음료 패키지 구매 시 포함 여부 확인 필수.</p>
    <h2 id="auto">⚙️ 자동 봉사료 vs 수동 팁</h2>
    <p>대부분의 선사는 자동 봉사료를 크루즈 카드(선내 계정)에 매일 자동 청구합니다. 원할 경우 프런트 데스크에서 조정(감액 또는 취소)이 가능하지만, 직원 급여에 직접적 영향을 미치므로 신중해야 합니다.</p>
    <ul class="tip-box">
      <li>✅ 자동 봉사료 그대로 유지 → 가장 일반적이고 간편한 방법</li>
      <li>✅ 특별히 친절한 직원에게 추가 현금 팁 → 개인 선택</li>
      <li>✅ 럭셔리 선사(실버씨·리젠트) → 팁 불필요, 요금에 포함</li>
    </ul>
    <h2 id="who">👥 봉사료는 누가 받나?</h2>
    <p>자동 봉사료는 통합 풀(Pool)로 모아져 다음 직원들에게 배분됩니다:</p>
    <ul>
      <li>🛏️ 객실 청소 스탭 (Stateroom Attendant)</li>
      <li>🍽️ 메인 다이닝룸 웨이터·보조 웨이터</li>
      <li>🍷 소믈리에·음료 서버</li>
      <li>🎭 일부 엔터테인먼트·어린이 클럽 직원</li>
    </ul>
    <h2 id="tips">💡 봉사료 관련 절약 팁</h2>
    <ul>
      <li>💳 크루즈 예약 시 봉사료 포함(All-Inclusive) 상품 선택 시 별도 비용 없음</li>
      <li>📅 일부 선사는 예약 시 봉사료 선결제(Pre-pay Gratuities) 시 할인 또는 고정 금액 혜택</li>
      <li>🍸 음료 패키지 구매 시 봉사료 포함 여부 꼭 확인 (포함 패키지 vs 별도 청구)</li>
      <li>🧾 하선 전 선내 계정 명세서 확인 — 이중 청구 또는 오류 체크</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-casino.html",
    "title_ko": "크루즈 카지노 이용 완벽 가이드",
    "img_url": "https://images.unsplash.com/photo-1596838132731-d0a2c9e37226?w=1200&q=80",
    "meta_desc": "크루즈 카지노 이용 완벽 가이드. 운영 시간, 드레스코드, 게임 종류, 크레딧 시스템, 초보자 팁까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "intro", "label": "🎰 크루즈 카지노 기본 정보"},
      {"id": "games", "label": "🃏 주요 게임 종류"},
      {"id": "credit", "label": "💳 크레딧 & 결제 시스템"},
      {"id": "rules", "label": "📋 주의사항 & 규정"},
      {"id": "tips", "label": "💡 초보자 실전 팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈 선내 카지노는 항구에 정박 중에는 운영하지 않고 공해 상에서만 운영됩니다. 카지노 이용은 만 18세(일부 선사 21세) 이상만 가능합니다.</p>
    <h2 id="intro">🎰 크루즈 카지노 기본 정보</h2>
    <p>대부분의 크루즈 선사는 선내에 전용 카지노를 운영합니다. 슬롯머신, 블랙잭, 룰렛, 포커 등 다양한 게임을 즐길 수 있으며, 카지노 전용 음료 서비스도 제공됩니다.</p>
    <ul>
      <li>⏰ <strong>운영 시간</strong>: 공해 상 항해 시에만 운영 (기항지 입·출항 시 폐쇄)</li>
      <li>🎂 <strong>이용 연령</strong>: 선사마다 18세 또는 21세 이상</li>
      <li>👔 <strong>드레스코드</strong>: 수영복·맨발 입장 금지. 일반 캐주얼 복장 허용</li>
      <li>📵 <strong>사진 촬영</strong>: 대부분 카지노 내 사진 촬영 금지</li>
    </ul>
    <h2 id="games">🃏 주요 게임 종류</h2>
    <ul>
      <li>🎰 <strong>슬롯머신</strong> — 가장 쉬운 입문 게임. $0.01~$5 동전 단위 다양</li>
      <li>🃏 <strong>블랙잭</strong> — 딜러와 1대1 카드 게임. 최소 베팅 $5~$25</li>
      <li>🎡 <strong>룰렛</strong> — 번호·색상 베팅. 유럽식(37칸) 권장</li>
      <li>♠️ <strong>텍사스 홀덤 포커</strong> — 대형 선사 전용 포커 룸 운영</li>
      <li>🎲 <strong>크랩스</strong> — 주사위 게임. 룰 숙지 필요</li>
    </ul>
    <h2 id="credit">💳 크레딧 & 결제 시스템</h2>
    <p>크루즈 카지노에서 현금 대신 카지노 크레딧 또는 선내 계정을 연결해 이용합니다.</p>
    <ul>
      <li>💰 선내 계정(Cruise Card)으로 카지노 크레딧 구매 가능</li>
      <li>💵 일부 카지노는 현금 ATM 운영 (수수료 $5~10 발생)</li>
      <li>🎟️ 카지노 크레딧 구매 시 선내 계정 청구 → 하선 시 정산</li>
      <li>🏆 카지노 포인트(플레이어스 카드) 적립 가능 → 음료·크레딧 교환</li>
    </ul>
    <h2 id="rules">📋 주의사항 & 규정</h2>
    <ul class="tip-box">
      <li>⚠️ 카지노 내 음주 운전(카지노 크레딧 과소비) 주의 — 예산 한도 설정 권장</li>
      <li>⚠️ 포커 테이블에서의 매너 숙지 필수 (초보자는 딜러에게 규칙 질문 가능)</li>
      <li>⚠️ 미성년자 동반 카지노 구역 진입 불가</li>
      <li>⚠️ 이기거나 질 경우 감정 조절 — 과도한 베팅 자제</li>
    </ul>
    <h2 id="tips">💡 초보자 실전 팁</h2>
    <ul>
      <li>🎓 대부분의 크루즈 카지노는 첫날 또는 항해 중 무료 게임 강습(Casino Tutorial) 제공</li>
      <li>💳 플레이어스 카드(Players Club) 즉시 발급 — 베팅할수록 포인트 적립</li>
      <li>🍹 카지노 이용 시 음료 무료 서비스 제공 선사 多 (미국 선사 기준)</li>
      <li>🎰 슬롯머신은 최저 베팅($0.01)부터 시작 — 예산 소진 방지</li>
      <li>🛑 예산 한도를 미리 정하고 한도 도달 시 즉시 퇴장</li>
      <li>📱 일부 선사 앱에서 카지노 프로모션·토너먼트 일정 확인 가능</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-spa.html",
    "title_ko": "크루즈 스파·웰니스 완벽 가이드",
    "img_url": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=1200&q=80",
    "meta_desc": "크루즈 스파·웰니스 완벽 가이드. 선내 스파 종류, 예약 방법, 가격, 할인 팁까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "intro", "label": "🧖 크루즈 스파 기본 정보"},
      {"id": "services", "label": "💆 주요 서비스 종류"},
      {"id": "price", "label": "💰 가격 & 패키지"},
      {"id": "book", "label": "📅 예약 방법"},
      {"id": "tips", "label": "💡 절약 & 실전 팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈 선내 스파는 육지 고급 리조트 스파 못지않은 서비스를 제공합니다. 항해 중 파도 소리를 들으며 받는 마사지는 크루즈만의 특별한 경험입니다.</p>
    <h2 id="intro">🧖 크루즈 스파 기본 정보</h2>
    <p>대형 크루즈 선사의 스파는 대부분 전문 운영사(Steiner Leisure, Mandara Spa 등)가 위탁 운영합니다. 마사지·페이셜·바디 트리트먼트·헤어살롱·네일숍이 통합 운영됩니다.</p>
    <ul>
      <li>🕐 <strong>운영 시간</strong>: 보통 오전 8시~오후 10시 (선사별 상이)</li>
      <li>👙 <strong>테르말 스위트</strong>: 사우나·스팀룸·자쿠지·온열 의자 별도 유료</li>
      <li>🧴 <strong>판매 압박</strong>: 트리트먼트 후 제품 구매 권유 — 거절 자유</li>
      <li>🎁 <strong>기프트 카드</strong>: 파트너에게 스파 선물 가능 (프런트 또는 앱에서 구매)</li>
    </ul>
    <h2 id="services">💆 주요 서비스 종류</h2>
    <ul>
      <li>💆 <strong>스웨디시 마사지</strong> — 전신 릴랙스. 50분 $120~180</li>
      <li>🪨 <strong>핫 스톤 마사지</strong> — 온열 스톤 근육 이완. 75분 $150~220</li>
      <li>🌿 <strong>아로마테라피</strong> — 에센셜 오일 전신 트리트먼트. 50분 $130~190</li>
      <li>💅 <strong>페이셜 트리트먼트</strong> — 딥 클렌징·안티에이징. 50분 $100~160</li>
      <li>💇 <strong>헤어 & 네일</strong> — 헤어컬러·드라이·매니큐어 등 다양</li>
      <li>🧘 <strong>요가·명상 클래스</strong> — 일부 선사 갑판 야외 요가 무료 제공</li>
    </ul>
    <h2 id="price">💰 가격 & 패키지</h2>
    <p>스파 서비스는 일반적으로 비싸지만 패키지 이용 시 할인됩니다:</p>
    <ul>
      <li>🎟️ <strong>스파 패키지</strong> — 복수 트리트먼트 묶음 구매 시 10~20% 할인</li>
      <li>🌅 <strong>테르말 스위트 패스</strong> — 크루즈 전 기간 이용권. 1인 $150~300 수준</li>
      <li>💑 <strong>커플 트리트먼트</strong> — 2인 동시 마사지. 단품보다 15% 내외 저렴</li>
    </ul>
    <h2 id="book">📅 예약 방법</h2>
    <ul>
      <li>📱 선사 앱으로 승선 전 온라인 사전 예약 가능 (인기 시간대 매진 방지)</li>
      <li>🛎️ 승선 첫날 스파 데스크 직접 방문 예약 가능</li>
      <li>⏰ 기항지 당일 스파 예약 시 할인 제공하는 선사 多 (직원 유휴시간 활용)</li>
    </ul>
    <h2 id="tips">💡 절약 & 실전 팁</h2>
    <ul>
      <li>📅 기항지 당일 예약 시 최대 25% 할인 — 선박이 항구에 있는 날 스파 이용</li>
      <li>🌅 초기 탑승 당일 또는 마지막 날 오전 예약 시 할인 이벤트 多</li>
      <li>🧴 스파 제품 구매 압박 정중히 거절 가능 — No, thank you면 충분</li>
      <li>🧘 무료 요가·스트레칭 클래스 일정 선사 앱에서 확인</li>
      <li>♨️ 테르말 스위트 패스는 7박 이상 크루즈에서 가성비 우수</li>
      <li>💧 스파 이용 후 충분한 수분 섭취 권장 (선내 레스토랑 무료 물 이용)</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-upgrade.html",
    "title_ko": "크루즈 선실 업그레이드 전략 가이드",
    "img_url": "https://images.unsplash.com/photo-1548543604-578d0b5f61f9?w=1200&q=80",
    "meta_desc": "크루즈 선실 업그레이드 전략 완벽 가이드. 무료 업그레이드 받는 법, 비드 업그레이드, 선사별 팁까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "types", "label": "🛏️ 선실 등급 종류"},
      {"id": "free", "label": "🎁 무료 업그레이드 받는 법"},
      {"id": "bid", "label": "💰 비드 업그레이드(입찰)"},
      {"id": "tips", "label": "💡 실전 업그레이드 전략"},
      {"id": "when", "label": "⏰ 최적 타이밍"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈 선실 업그레이드는 운이 필요하지만, 전략적으로 접근하면 확률을 높일 수 있습니다. 무료 업그레이드부터 비드 시스템까지 핵심 전략을 정리합니다.</p>
    <h2 id="types">🛏️ 크루즈 선실 등급 종류</h2>
    <ul>
      <li>🪟 <strong>인사이드 (Inside)</strong> — 창문 없음. 가장 저렴</li>
      <li>🌊 <strong>오션뷰 (Ocean View)</strong> — 창문 있음. 바다 전망</li>
      <li>🚪 <strong>발코니 (Balcony)</strong> — 개인 발코니. 크루즈 여행의 꽃</li>
      <li>🛋️ <strong>미니 스위트</strong> — 넓은 거실 공간. 프리미엄 어메니티</li>
      <li>👑 <strong>스위트 (Suite)</strong> — 버틀러 서비스·전용 라운지 포함</li>
    </ul>
    <h2 id="free">🎁 무료 업그레이드 받는 법</h2>
    <p>무료 업그레이드는 선사 재량이지만, 가능성을 높이는 방법들이 있습니다:</p>
    <ul>
      <li>🎯 <strong>보장(Guarantee) 객실 예약</strong> — 특정 등급 최저가 예약 시 선사가 자체 배정. 높은 등급으로 배정될 가능성</li>
      <li>💎 <strong>로열티 프로그램</strong> — 골드·플래티넘 등 상위 멤버십 보유 시 업그레이드 우선순위</li>
      <li>🎂 <strong>특별 행사 언급</strong> — 허니문·기념일 예약 시 선사에 미리 알리기</li>
      <li>📞 <strong>승선 직전 문의</strong> — 출항 48~72시간 전 빈 상위 객실 발생 시 업그레이드 제안</li>
    </ul>
    <h2 id="bid">💰 비드 업그레이드 (Bid Upgrade)</h2>
    <p>로열 캐리비안·MSC·NCL 등 주요 선사는 출항 수주 전 업그레이드 입찰(Bid) 시스템을 운영합니다:</p>
    <ul>
      <li>📧 출항 30~90일 전 이메일로 입찰 초대 발송</li>
      <li>💵 원하는 업그레이드 가격 입력 (최저 입찰가부터 설정 가능)</li>
      <li>✅ 선사 수락 시 자동 청구 + 확정 이메일 수신</li>
      <li>❌ 미선정 시 원래 객실 유지, 비용 미청구</li>
    </ul>
    <p>💡 비드 최저가의 110~130% 수준 제시 시 당첨 확률 증가. 성수기보다 비수기 입찰 성공률 높음.</p>
    <h2 id="tips">💡 실전 업그레이드 전략</h2>
    <ul class="tip-box">
      <li>✅ 비수기 크루즈 예약 — 공실률이 높아 무료 업그레이드 빈도 증가</li>
      <li>✅ 체크인 시 직원에게 정중하게 업그레이드 문의 (당당하게, 구걸 아님)</li>
      <li>✅ 선사 공식 앱 또는 온라인 체크인 시 업그레이드 상품 확인</li>
      <li>✅ 같은 등급 내 더 좋은 위치 객실 요청 (중간층, 선수 근처 등)</li>
    </ul>
    <h2 id="when">⏰ 업그레이드 최적 타이밍</h2>
    <ul>
      <li>📅 <strong>예약 시</strong> — Guarantee 객실 선택으로 자동 배정 유도</li>
      <li>📅 <strong>출항 30~90일 전</strong> — 비드 업그레이드 시스템 이메일 확인</li>
      <li>📅 <strong>출항 48~72시간 전</strong> — 온라인 체크인 또는 전화 문의</li>
      <li>📅 <strong>터미널 체크인 시</strong> — 카운터 직원에게 직접 문의</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-photo-package.html",
    "title_ko": "크루즈 사진 패키지 가이드",
    "img_url": "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=1200&q=80",
    "meta_desc": "크루즈 사진 패키지 완벽 가이드. 선사별 포토 패키지 가격, 구매 시점, 셀프 촬영 팁까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "intro", "label": "📷 크루즈 포토 서비스 기본"},
      {"id": "package", "label": "🎟️ 포토 패키지 종류"},
      {"id": "price", "label": "💰 선사별 가격"},
      {"id": "tips", "label": "💡 구매 & 절약 팁"},
      {"id": "self", "label": "📸 셀프 촬영 꿀팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈에서는 전문 포토그래퍼가 탑승하여 승선 시, 포멀 나잇, 기항지 입·출항 등 다양한 순간을 촬영합니다. 사진 패키지 구매 여부와 시점이 비용에 큰 차이를 만듭니다.</p>
    <h2 id="intro">📷 크루즈 포토 서비스 기본</h2>
    <p>크루즈 선내 전문 포토그래퍼는 다음 상황에 촬영 서비스를 제공합니다:</p>
    <ul>
      <li>🚢 <strong>승선 환영 사진</strong> — 갱웨이 앞 기념사진</li>
      <li>👔 <strong>포멀 나잇</strong> — 계단·배경판 앞 공식 드레스 사진</li>
      <li>🌊 <strong>갑판 및 풀사이드</strong> — 일몰·선상 활동 중 촬영</li>
      <li>🏖️ <strong>기항지 투어</strong> — 일부 선사는 기항지 투어에 포토그래퍼 동행</li>
      <li>🎄 <strong>테마 이벤트</strong> — 크루즈 선사 행사 시 전문 촬영</li>
    </ul>
    <h2 id="package">🎟️ 포토 패키지 종류</h2>
    <ul>
      <li>🖼️ <strong>단품 구매</strong> — 사진 갤러리에서 마음에 드는 사진만 개별 구매 (장당 $20~35)</li>
      <li>📦 <strong>패키지 A</strong> — 디지털 다운로드 무제한. 인화 없음 (약 $150~250)</li>
      <li>📦 <strong>패키지 B</strong> — 인화 사진 + 디지털 혼합 패키지 (약 $200~350)</li>
      <li>📦 <strong>올인클루시브</strong> — 무제한 디지털 + 포토북 + 인화 (약 $300~500)</li>
    </ul>
    <h2 id="price">💰 선사별 가격 비교</h2>
    <ul>
      <li>🛳️ <strong>로열 캐리비안</strong> — 무제한 디지털 패키지 약 $199~349</li>
      <li>🛳️ <strong>카니발</strong> — 포토 패키지 $99~199 (기간 한정 프로모션 多)</li>
      <li>🛳️ <strong>MSC</strong> — 디지털 패키지 €89~199</li>
      <li>🛳️ <strong>노르웨이안(NCL)</strong> — 패키지 $149~299</li>
    </ul>
    <h2 id="tips">💡 구매 & 절약 팁</h2>
    <ul class="tip-box">
      <li>✅ 승선 첫날 또는 둘째 날 패키지 구매 시 얼리버드 할인 (15~25%) 제공</li>
      <li>✅ 마지막 날(하선 전날) 구매 시 재고 소진 할인 가능 — 단, 원하는 사진 먼저 확인</li>
      <li>✅ 포토그래퍼에게 촬영 요청 적극 활용 — 패키지 구매 여부와 무관하게 요청 가능</li>
      <li>✅ 사진 갤러리 방문 시 구매 압박 느껴지면 다음에 다시 방문한다고 말하면 OK</li>
    </ul>
    <h2 id="self">📸 셀프 촬영 꿀팁</h2>
    <ul>
      <li>🌅 <strong>골든 아워</strong> — 일출·일몰 시각 갑판 상단에서 최고의 자연광</li>
      <li>📱 <strong>클립형 광각 렌즈</strong> — 스마트폰 장착 시 선내 공간 넓게 촬영</li>
      <li>🌊 <strong>선수 갑판</strong> — 바람이 거세지만 영화 같은 구도 가능</li>
      <li>🏊 <strong>수영장 선셋 샷</strong> — 수영장 반영을 이용한 드라마틱 구도</li>
      <li>🌙 <strong>야간 갑판</strong> — 별 사진·해상 야경. 삼각대 소형 휴대 권장</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-kids-club.html",
    "title_ko": "크루즈 어린이 클럽 & 키즈 프로그램 가이드",
    "img_url": "https://images.unsplash.com/photo-1484820540004-14229fe36ca4?w=1200&q=80",
    "meta_desc": "크루즈 어린이 클럽 & 키즈 프로그램 완벽 가이드. 선사별 연령대 프로그램, 비용, 주의사항까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "intro", "label": "👨‍👩‍👧 크루즈 키즈 클럽 기본"},
      {"id": "lines", "label": "🛳️ 선사별 키즈 프로그램"},
      {"id": "age", "label": "🎂 연령대별 프로그램"},
      {"id": "cost", "label": "💰 비용 & 야간 보육"},
      {"id": "tips", "label": "💡 가족 크루즈 실전 팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈는 가족 여행의 최고 선택지 중 하나입니다. 선내 어린이 클럽이 아이들을 돌봐주는 동안 어른들만의 시간도 가질 수 있기 때문입니다.</p>
    <h2 id="intro">👨‍👩‍👧 크루즈 키즈 클럽 기본</h2>
    <p>대형 크루즈 선사는 거의 모두 전문 어린이 프로그램(Kids Club)을 무료로 운영합니다. 연령별로 구분된 공간에서 교육·놀이·창작 활동이 진행됩니다.</p>
    <ul>
      <li>🆓 <strong>기본 이용 무료</strong> — 대부분 선사 키즈 클럽 운영시간 내 무료</li>
      <li>💰 <strong>야간 보육 유료</strong> — 저녁 10시 이후 야간 베이비시팅 별도 요금</li>
      <li>📋 <strong>사전 등록 필수</strong> — 승선 후 또는 선사 앱으로 등록 필요</li>
      <li>🔒 <strong>보안 시스템</strong> — 등록된 보호자만 픽업 가능 (팔찌/카드 확인)</li>
    </ul>
    <h2 id="lines">🛳️ 선사별 키즈 프로그램</h2>
    <ul>
      <li>🌊 <strong>로열 캐리비안 — Adventure Ocean</strong>: 3~17세. 드림웍스 캐릭터 만남 이벤트</li>
      <li>🎠 <strong>카니발 — Camp Ocean</strong>: 2~17세. 세 가지 연령 그룹 분리 운영</li>
      <li>🎨 <strong>디즈니 크루즈 — Disney's Youth Activities</strong>: 3~17세. 디즈니 캐릭터·영화 테마</li>
      <li>🏄 <strong>NCL — Splash Academy</strong>: 3~17세. 스포츠·창작·요리 다양 프로그램</li>
      <li>🌍 <strong>MSC — MSC for Me Kids</strong>: 3~17세. 언어별 그룹 운영</li>
    </ul>
    <h2 id="age">🎂 연령대별 프로그램</h2>
    <ul>
      <li>👶 <strong>영아(0~2세)</strong> — 전용 키즈 클럽 미운영. 베이비시팅 유료 예약</li>
      <li>🧒 <strong>유아(3~5세)</strong> — 간단한 공예·읽기·색칠·체조 활동</li>
      <li>🧑 <strong>아동(6~11세)</strong> — 요리 교실·과학 실험·수영·보물찾기</li>
      <li>👦 <strong>청소년(12~17세)</strong> — 10대 전용 라운지·비디오게임·파티·스포츠</li>
    </ul>
    <h2 id="cost">💰 비용 & 야간 보육</h2>
    <ul>
      <li>🆓 정규 운영시간 키즈 클럽 이용: <strong>무료</strong></li>
      <li>💵 야간 그룹 보육(저녁 10시~자정): $6~8/시간</li>
      <li>💵 개인 베이비시터: $15~20/시간 (사전 예약 필수)</li>
    </ul>
    <h2 id="tips">💡 가족 크루즈 실전 팁</h2>
    <ul class="tip-box">
      <li>✅ 키즈 클럽 사전 등록은 승선 당일 바로 — 인기 시간대는 조기 마감</li>
      <li>✅ 아이 알레르기·특이사항 사전 고지 (영어로 메모 준비 권장)</li>
      <li>✅ 디즈니 크루즈는 가족 크루즈 최고 선택지지만 가격 프리미엄 있음</li>
      <li>✅ 로열 캐리비안 오아시스급 선박에는 워터 파크·암벽등반·서핑 시뮬레이터 탑재</li>
      <li>✅ 기항지 투어 시 가족 친화 투어 선택 — 어린이 체력 고려 2~3시간 내 코스</li>
      <li>✅ 자외선 차단제·모자·수영 기저귀 충분히 준비</li>
    </ul>""",
    ],
  },
  {
    "filename": "cruise-medical.html",
    "title_ko": "크루즈 의료·응급 서비스 가이드",
    "img_url": "https://images.unsplash.com/photo-1584982751601-97dcc096659c?w=1200&q=80",
    "meta_desc": "크루즈 의료·응급 서비스 완벽 가이드. 선내 의료 시설, 비용, 여행자 보험, 응급 상황 대처법까지 크루즈링크가 정리합니다.",
    "toc_items": [
      {"id": "facility", "label": "🏥 선내 의료 시설"},
      {"id": "cost", "label": "💰 의료 비용"},
      {"id": "insurance", "label": "🛡️ 여행자 보험"},
      {"id": "emergency", "label": "🚨 응급 상황 대처"},
      {"id": "tips", "label": "💡 건강 준비 실전 팁"},
    ],
    "sections": [
      """    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">크루즈 여행 중 건강 문제가 발생할 수 있습니다. 선내 의료 시설과 비용, 여행자 보험 가입의 중요성을 미리 파악해 두세요.</p>
    <h2 id="facility">🏥 선내 의료 시설</h2>
    <p>대형 크루즈 선사는 모두 선내 의료 센터(Medical Center)를 운영합니다. 의사(선의)와 간호사가 24시간 대기하며 응급 처치, 투약, 검사가 가능합니다.</p>
    <ul>
      <li>🩺 <strong>선내 의사</strong>: 선의(Ship's Doctor) 24시간 대기. 해상 의학 전문의</li>
      <li>💊 <strong>기본 의약품</strong>: 상비약·응급 약품 구비. 처방 약품 구매 가능</li>
      <li>🔬 <strong>검사 장비</strong>: X-ray·혈액검사 등 기본 진단 장비 보유</li>
      <li>🚁 <strong>중증 응급</strong>: 선박 이탈 헬기 이송 또는 기항지 하선 후 육상 이송</li>
    </ul>
    <h2 id="cost">💰 선내 의료 비용</h2>
    <p>⚠️ 선내 의료 서비스는 유료이며 상당히 비쌉니다:</p>
    <ul>
      <li>👨‍⚕️ <strong>기본 진료(외래)</strong>: $150~300</li>
      <li>💉 <strong>주사·처치</strong>: 추가 $50~200</li>
      <li>🛏️ <strong>입원(선내 병실)</strong>: 1일 $500~1,000+</li>
      <li>🚁 <strong>의료 헬기 이송</strong>: $10,000~50,000+ (보험 없을 경우 전액 본인 부담)</li>
    </ul>
    <h2 id="insurance">🛡️ 여행자 보험 — 크루즈 필수</h2>
    <p>크루즈 여행에서 여행자 보험은 선택이 아닌 필수입니다:</p>
    <ul>
      <li>🩺 <strong>의료비 보장</strong> — 선내 진료비 + 기항지 현지 병원비 커버</li>
      <li>✈️ <strong>여행 취소/지연 보장</strong> — 항공 결항, 크루즈 일정 변경 보상</li>
      <li>🧳 <strong>수하물 분실·지연</strong> — 짐 분실 시 보상</li>
      <li>🚁 <strong>의료 이송</strong> — 헬기 이송 비용 보장 (가장 중요)</li>
    </ul>
    <p>한국 여행자 보험 중 크루즈 전용 또는 해외 여행자 보험 가입 권장. 보장 한도 의료비 $100,000 이상 제품 선택.</p>
    <h2 id="emergency">🚨 응급 상황 대처법</h2>
    <ul>
      <li>📞 <strong>선내 응급 전화</strong>: 각 선박별 응급 번호 확인 (객실 안내서 참조)</li>
      <li>🏥 <strong>의료 센터 위치</strong>: 승선 후 반드시 확인 (통상 하갑판)</li>
      <li>💊 <strong>상비약 직접 준비</strong>: 처방약·두통약·지사제·멀미약 반드시 지참</li>
      <li>🌡️ <strong>기항지에서 증상 악화 시</strong>: 선사 투어 중이면 투어 가이드에게 즉시 신고</li>
    </ul>
    <h2 id="tips">💡 건강 준비 실전 팁</h2>
    <ul class="tip-box">
      <li>✅ 처방약은 원본 처방전 + 여분 약 지참 (통관 시 필요 가능)</li>
      <li>✅ 멀미약(스코폴라민 패치·본빈)은 한국 출발 전 구매 (선내 판매 비쌈)</li>
      <li>✅ 크루즈 여행자 보험 가입 시 '의료 이송' 특약 포함 여부 확인</li>
      <li>✅ 기저질환자(심장·당뇨 등)는 출발 전 주치의 소견서 지참 권장</li>
      <li>✅ 노로바이러스 예방: 손 세정제 자주 사용, 뷔페 집게 사용 준수</li>
      <li>✅ 여행자 보험 서류(보험증서·연락처)는 디지털+인쇄본 모두 지참</li>
    </ul>""",
    ],
  },
]


def write_port(port_data):
    html = port_html(**port_data)
    path = os.path.join(PORTS_DIR, port_data['filename'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ PORT: {port_data['filename']}")


def write_tip(tip_data):
    html = tip_html(**tip_data)
    path = os.path.join(TIPS_DIR, tip_data['filename'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ TIP:  {tip_data['filename']}")


if __name__ == '__main__':
    for p in ports:
        write_port(p)
    for t in tips:
        write_tip(t)
    print("\n🎉 모든 파일 생성 완료!")
