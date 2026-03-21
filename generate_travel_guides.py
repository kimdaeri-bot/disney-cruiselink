#!/usr/bin/env python3
"""Generate 32 travel guide pages for cruiselink-v2"""
import os

BASE = "/Users/kim/.openclaw/workspace/cruiselink-v2/guide/travel"

TEMPLATE = '''<!DOCTYPE html>
<html lang="ko">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-K4PPLZNG');</script>
<!-- End Google Tag Manager -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} 2026 | 크루즈링크 해외여행 가이드</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.cruiselink.co.kr/guide/travel/{slug}/">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="크루즈링크">
  <meta property="og:title" content="{title} - 크루즈링크">
  <meta property="og:image" content="{og_image}">
  <meta property="og:url" content="https://www.cruiselink.co.kr/guide/travel/{slug}/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
  <link rel="stylesheet" href="../../../assets/css/style.css">
  <link rel="icon" type="image/png" href="../../../assets/images/favicon.png">
  <link rel="shortcut icon" href="../../../favicon.ico">
  <style>
    .g-hero{{position:relative;height:400px;overflow:hidden;display:flex;align-items:flex-end}}
    .g-hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
    .g-hero-overlay{{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.78) 0%,rgba(0,0,0,.1) 60%)}}
    .g-hero-content{{position:relative;z-index:1;width:100%;padding:36px 0;color:#fff}}
    .breadcrumb{{font-size:.82rem;color:rgba(255,255,255,.75);margin-bottom:10px}}
    .breadcrumb a{{color:rgba(255,255,255,.75);text-decoration:none}}
    .g-layout{{display:grid;grid-template-columns:1fr 300px;gap:36px;max-width:1200px;margin:44px auto;padding:0 20px;align-items:start}}
    @media(max-width:900px){{.g-layout{{grid-template-columns:1fr}}.g-hero h1{{font-size:1.5rem}}}}
    .g-body h2{{font-size:1.2rem;font-weight:900;color:#1a237e;margin:36px 0 14px;padding-bottom:8px;border-bottom:3px solid #ff6f00;display:inline-block}}
    .g-body p{{color:#616161;line-height:1.9;margin-bottom:12px}}
    .g-body ul,.g-body ol{{padding-left:22px;color:#616161;line-height:2.1;margin-bottom:14px}}
    .tip-box{{background:#fff8e1;border-left:4px solid #ff6f00;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0}}
    .tip-box li{{font-size:.88rem;color:#555;line-height:2}}
    .info-box{{background:#e8f5e9;border-left:4px solid #43a047;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0}}
    .warn-box{{background:#fce4ec;border-left:4px solid #e91e63;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0}}
    .sidebar-card{{background:#fff;border:1px solid #eeeeee;border-radius:8px;padding:20px;margin-bottom:18px;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
    .sidebar-card h3{{font-size:.9rem;font-weight:700;color:#1a237e;margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid #eeeeee}}
    .toc-list{{list-style:none;padding:0;margin:0}}
    .toc-list li a{{display:block;font-size:.83rem;color:#555;text-decoration:none;padding:5px 8px;border-radius:4px;transition:all .15s}}
    .toc-list li a:hover{{background:#f5f5f5;color:#1a237e}}
    .cta-btn{{display:block;background:#ff6f00;color:#fff;text-align:center;padding:13px;border-radius:8px;font-weight:700;font-size:.9rem;text-decoration:none;margin-top:8px;transition:background .2s}}
    .cta-btn:hover{{background:#e65100}}
    .cta-btn.navy{{background:#1a237e}}
    .g-sidebar{{position:sticky;top:80px}}
    h2[id]{{scroll-margin-top:80px}}
    .compare-table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:.88rem}}
    .compare-table th{{background:#1a237e;color:#fff;padding:10px 12px;text-align:left}}
    .compare-table td{{padding:9px 12px;border-bottom:1px solid #eee;color:#555}}
    .compare-table tr:nth-child(even){{background:#f9f9f9}}
    .two-col{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0}}
    @media(max-width:600px){{.two-col{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K4PPLZNG"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager -->

<div id="header"></div>
<section class="g-hero">
  <img src="{og_image}" alt="{title}" loading="eager">
  <div class="g-hero-overlay"></div>
  <div class="g-hero-content">
    <div class="container">
      <div class="breadcrumb">
        <a href="../../../">홈</a> › <a href="../../">가이드</a> › <a href="../">해외여행 가이드</a> › {title}
      </div>
      <h1>{title}</h1>
    </div>
  </div>
</section>
<div class="g-layout">
  <article class="g-body">
    <p style="font-size:1rem;color:#444;line-height:1.9;margin-bottom:28px">{intro}</p>
{body}
    <h2 id="inquiry">✉️ 크루즈링크 여행 상담</h2>
    <p>해외여행과 크루즈를 함께 즐기고 싶으시다면 크루즈링크에 문의해 주세요. 맞춤형 패키지를 제안해 드립니다.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:12px">
      <a href="https://pf.kakao.com/_xgYbJG" target="_blank" class="cta-btn" style="flex:1;min-width:160px">💬 카카오톡 상담</a>
      <a href="../../../" class="cta-btn navy" style="flex:1;min-width:160px">🚢 크루즈 상품 보기</a>
    </div>
  </article>
  <aside class="g-sidebar">
    <div class="sidebar-card">
      <h3>📌 목차</h3>
      <ul class="toc-list">
{toc}
        <li><a href="#inquiry">✉️ 크루즈링크 상담</a></li>
      </ul>
    </div>
    <div class="sidebar-card">
      <h3>✈️ 관련 가이드</h3>
      <ul class="toc-list">
{related}
      </ul>
    </div>
    <div class="sidebar-card">
      <h3>🚢 크루즈 상담</h3>
      <a href="https://pf.kakao.com/_xgYbJG" target="_blank" class="cta-btn">카카오톡 문의</a>
      <a href="../../../" class="cta-btn navy" style="margin-top:8px">상품 검색하기</a>
    </div>
  </aside>
</div>
<div id="footer"></div>
<script src="../../../assets/js/components.js"></script>
<script>
  document.getElementById('header').innerHTML = Components.header('guide', '../../../');
  document.getElementById('footer').innerHTML = Components.footer('../../../');
</script>
</body>
</html>'''

PAGES = [
  {
    "slug": "flight-cheap",
    "title": "항공권 싸게 사는 법 완전 가이드",
    "description": "항공권 최저가 구매 전략 총정리. 최적 예약 타이밍, 가격 추적 도구, 환승 활용법, 얼리버드 vs 막판 특가까지.",
    "og_image": "https://images.pexels.com/photos/358319/pexels-photo-358319.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "항공권 가격은 같은 노선이라도 언제 사느냐에 따라 2~3배 이상 차이가 납니다. 올바른 전략만 알면 누구나 더 저렴하게 항공권을 살 수 있습니다.",
    "body": """    <h2 id="timing">⏰ 최적 예약 타이밍</h2>
    <p>항공권은 출발 약 <strong>6~8주 전</strong>이 평균적으로 가장 저렴합니다. 단, 성수기(여름·연휴)는 3~4개월 전부터 미리 예약하는 것이 유리합니다.</p>
    <table class="compare-table">
      <tr><th>구분</th><th>비수기 노선</th><th>성수기 노선</th><th>특가 노선</th></tr>
      <tr><td>최적 예약 시기</td><td>4~6주 전</td><td>3~4개월 전</td><td>공지 즉시</td></tr>
      <tr><td>가장 비싼 시기</td><td>출발 1~2주 전</td><td>출발 2~4주 전</td><td>성수기 주말</td></tr>
      <tr><td>추천 요일</td><td>화·수요일</td><td>화·수요일</td><td>요일 무관</td></tr>
    </table>
    <h2 id="tools">🔧 가격 추적 도구 활용법</h2>
    <p>항공권 가격은 매일 수십 번 바뀝니다. 가격 알림 도구를 활용하면 최저가 타이밍을 놓치지 않을 수 있습니다.</p>
    <ul>
      <li>✈️ <strong>구글 플라이트</strong> — 가격 추적 알림 설정, 달력 뷰로 저렴한 날짜 한눈에 파악</li>
      <li>🔍 <strong>스카이스캐너</strong> — '가장 저렴한 월' 검색, 전체 월 달력 비교</li>
      <li>🎯 <strong>카약(Kayak)</strong> — 가격 예측 기능(오를지/내릴지), 환율 비교</li>
      <li>📱 <strong>네이버 항공권</strong> — 한국 출발 최저가 비교, 환불 정책 필터</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 검색 후 항공사 공식 홈에서 직접 구매하면 추가 할인 또는 마일리지 적립 혜택</li>
        <li>✅ 시크릿/프라이빗 브라우저 사용 — 쿠키 기반 가격 상승 방지</li>
        <li>✅ VPN으로 출발국 변경 시 현지 요금 적용되는 경우 있음 (단, 결제 카드 주의)</li>
      </ul>
    </div>
    <h2 id="strategy">💡 저렴한 항공권 구매 전략</h2>
    <div class="two-col">
      <div style="background:#e8f5e9;padding:14px;border-radius:8px">
        <strong style="color:#2e7d32">✅ 추천 전략</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>인근 공항 출발 비교 (인천↔김포↔청주)</li>
          <li>환승 항공편 가격 비교</li>
          <li>편도 2장 조합 (OW×2)</li>
          <li>얼리버드 + 유연한 날짜</li>
          <li>연간 할인 카드·마일리지 카드 활용</li>
        </ul>
      </div>
      <div style="background:#fce4ec;padding:14px;border-radius:8px">
        <strong style="color:#c62828">⚠️ 주의 사항</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>최저가 LCC: 수하물 추가비 계산 필수</li>
          <li>환불 불가 요금제 신중히 선택</li>
          <li>연결편 시간 여유 최소 2시간</li>
          <li>야간 도착 교통편 사전 확인</li>
          <li>여행자보험 별도 가입 권장</li>
        </ul>
      </div>
    </div>
    <h2 id="lcc">🎯 저가항공(LCC) 완전 활용법</h2>
    <p>LCC는 기본 운임은 저렴하지만 부가 서비스 비용을 합산하면 대형항공사와 비슷해지는 경우가 많습니다. 옵션 선택 전략이 핵심입니다.</p>
    <ul>
      <li>🧳 <strong>수하물 정책 확인</strong> — 일부 LCC는 기내 반입 가방도 유료 (Ryanair 등)</li>
      <li>🍽️ <strong>기내식 사전 예약</strong> — 탑승 후보다 30~50% 저렴</li>
      <li>💺 <strong>좌석 사전 배정</strong> — 무료 좌석 vs 유료 선호 좌석 확인</li>
      <li>💳 <strong>결제 수수료</strong> — 신용카드 수수료 없는 결제 수단 활용</li>
    </ul>""",
    "toc": [
      ("timing", "⏰ 최적 예약 타이밍"),
      ("tools", "🔧 가격 추적 도구"),
      ("strategy", "💡 저렴한 구매 전략"),
      ("lcc", "🎯 LCC 완전 활용법"),
    ],
    "related": [
      ("../flight-baggage/", "항공사별 수하물 규정"),
      ("../flight-mileage/", "항공 마일리지 가이드"),
      ("../flight-upgrade/", "비즈니스 업그레이드 팁"),
      ("../travel-exchange/", "해외 환전 가이드"),
    ]
  },
  {
    "slug": "flight-baggage",
    "title": "항공사별 수하물 규정 완전 비교",
    "description": "2026년 항공사별 수하물 무게·크기 규정 총정리. 위탁 수하물, 기내 반입, 추가 수하물 요금 비교.",
    "og_image": "https://images.pexels.com/photos/1008155/pexels-photo-1008155.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "항공사마다 수하물 규정이 천차만별입니다. 출발 전 반드시 확인하지 않으면 공항에서 추가 요금 폭탄을 맞을 수 있습니다. 2026년 주요 항공사 수하물 규정을 한 번에 비교해 드립니다.",
    "body": """    <h2 id="fsc">✈️ 대형항공사(FSC) 수하물 규정</h2>
    <table class="compare-table">
      <tr><th>항공사</th><th>위탁 수하물</th><th>기내 반입</th><th>추가 요금</th></tr>
      <tr><td>대한항공</td><td>이코노미 23kg×1개</td><td>10kg (3면합 115cm)</td><td>$60~100/개</td></tr>
      <tr><td>아시아나</td><td>이코노미 23kg×1개</td><td>10kg (3면합 115cm)</td><td>$50~80/개</td></tr>
      <tr><td>에어프랑스</td><td>이코노미 23kg×1개</td><td>12kg</td><td>€40~80/개</td></tr>
      <tr><td>루프트한자</td><td>이코노미 23kg×1개</td><td>8kg</td><td>€50~100/개</td></tr>
      <tr><td>싱가포르항공</td><td>이코노미 30kg(총량)</td><td>7kg</td><td>$50~100/개</td></tr>
      <tr><td>JAL/ANA</td><td>이코노미 23kg×2개</td><td>10kg</td><td>$50~100/개</td></tr>
    </table>
    <h2 id="lcc">💸 저가항공(LCC) 수하물 규정</h2>
    <table class="compare-table">
      <tr><th>항공사</th><th>위탁 포함 여부</th><th>기내 반입</th><th>위탁 추가 요금</th></tr>
      <tr><td>제주항공</td><td>15kg 포함</td><td>10kg</td><td>₩35,000~60,000</td></tr>
      <tr><td>진에어</td><td>15kg 포함</td><td>10kg</td><td>₩35,000~60,000</td></tr>
      <tr><td>에어서울</td><td>15kg 포함</td><td>10kg</td><td>₩30,000~50,000</td></tr>
      <tr><td>에어아시아</td><td>미포함 (추가 구매)</td><td>7kg</td><td>$12~40/개</td></tr>
      <tr><td>라이언에어</td><td>미포함</td><td>10kg (유료)</td><td>€10~40/개</td></tr>
      <tr><td>이지젯</td><td>미포함</td><td>1개 무료</td><td>£16~50/개</td></tr>
    </table>
    <div class="warn-box">
      <strong>⚠️ 주의!</strong><br>
      <ul style="margin:8px 0 0;padding-left:18px;font-size:.88rem;line-height:2">
        <li>LCC는 사전 구매 시 공항 현장의 3~5배 저렴 — 반드시 온라인 예약 시 추가</li>
        <li>수하물 무게 초과: 일반적으로 kg당 $5~15 추가 요금</li>
        <li>크기 초과 (대형 짐): 별도 oversized 요금 적용</li>
      </ul>
    </div>
    <h2 id="tips">💡 수하물 절약 팁</h2>
    <ul>
      <li>🎒 <strong>기내 반입 최대 활용</strong> — 23kg 위탁 대신 10kg 기내 반입으로 비용 절감</li>
      <li>📦 <strong>압축 팩 사용</strong> — 부피 30~50% 절감 (무게는 동일)</li>
      <li>👗 <strong>무거운 옷 착용</strong> — 부츠·두꺼운 재킷은 탑승 시 착용</li>
      <li>⚖️ <strong>공항 저울 활용</strong> — 짐 맡기기 전 무게 확인 후 재배분</li>
      <li>🛍️ <strong>면세 쇼핑 계획</strong> — 귀국 시 짐 공간 여유 계산</li>
    </ul>
    <h2 id="prohibited">🚫 기내 반입 금지 물품</h2>
    <div class="two-col">
      <div style="background:#fce4ec;padding:14px;border-radius:8px">
        <strong style="color:#c62828">기내 반입 금지</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>액체류 100ml 초과 (각각)</li>
          <li>날카로운 물건 (가위·칼)</li>
          <li>라이터 1개 초과</li>
          <li>보조배터리 100Wh 초과</li>
          <li>스프레이류 일부</li>
        </ul>
      </div>
      <div style="background:#fff3e0;padding:14px;border-radius:8px">
        <strong style="color:#e65100">위탁도 금지</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>리튬배터리 (기내 반입 필수)</li>
          <li>폭발물·인화성 물질</li>
          <li>드라이아이스 2.5kg 초과</li>
          <li>자기폭풍 물질</li>
          <li>독극물</li>
        </ul>
      </div>
    </div>""",
    "toc": [
      ("fsc", "✈️ 대형항공사 규정 비교"),
      ("lcc", "💸 저가항공 규정 비교"),
      ("tips", "💡 수하물 절약 팁"),
      ("prohibited", "🚫 반입 금지 물품"),
    ],
    "related": [
      ("../flight-cheap/", "항공권 싸게 사는 법"),
      ("../flight-delay/", "항공편 지연·결항 대처법"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
      ("../travel-customs/", "세관 신고 가이드"),
    ]
  },
  {
    "slug": "flight-mileage",
    "title": "항공 마일리지 적립·사용 완전 가이드",
    "description": "항공 마일리지 최대한 모으고 스마트하게 사용하는 법. 신용카드 적립, 제휴 파트너, 마일리지 항공권 예약 전략.",
    "og_image": "https://images.pexels.com/photos/2063786/pexels-photo-2063786.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "마일리지를 제대로 활용하면 비즈니스클래스를 이코노미 가격에 즐길 수 있습니다. 적립부터 사용까지, 마일리지 여행의 모든 것을 정리했습니다.",
    "body": """    <h2 id="earn">💳 마일리지 적립 방법</h2>
    <p>마일리지는 비행뿐 아니라 일상에서도 적립할 수 있습니다. 적립처를 다양화하면 더 빠르게 마일리지를 쌓을 수 있습니다.</p>
    <table class="compare-table">
      <tr><th>적립 방법</th><th>대한항공 SKYPASS</th><th>아시아나 ASIANA Club</th></tr>
      <tr><td>항공편 탑승</td><td>운임 클래스별 50~200%</td><td>운임 클래스별 50~200%</td></tr>
      <tr><td>마일리지 신용카드</td><td>1,000원당 1~3마일</td><td>1,000원당 1~3마일</td></tr>
      <tr><td>호텔 숙박</td><td>제휴 호텔 1박 500~3,000마일</td><td>제휴 호텔 1박 500~2,000마일</td></tr>
      <tr><td>렌터카</td><td>1일 500~1,000마일</td><td>1일 500~1,000마일</td></tr>
      <tr><td>쇼핑몰</td><td>10,000원당 100마일 내외</td><td>10,000원당 100마일 내외</td></tr>
    </table>
    <h2 id="cards">💳 마일리지 신용카드 비교</h2>
    <ul>
      <li>🌟 <strong>대한항공 카드</strong> — 1,000원당 1마일 기본, 해외 사용 시 1.5마일</li>
      <li>🌟 <strong>아시아나 카드</strong> — 1,000원당 1마일, 가맹점 추가 적립</li>
      <li>🌟 <strong>아멕스 골드</strong> — 국제선 이용 시 보너스 마일, 포인트→마일 전환</li>
      <li>🌟 <strong>현대카드 M</strong> — M포인트→마일 전환, 공항 라운지 무료</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 카드 실적 조건 충족 시 연 20,000~50,000 보너스 마일 제공 카드 활용</li>
        <li>✅ 가족 합산 적립 프로그램 (패밀리 마일리지) 활용으로 빠른 목표 달성</li>
        <li>✅ 마일리지 유효기간 10년 — 소멸 전 사용 계획 수립</li>
      </ul>
    </div>
    <h2 id="redeem">🎫 마일리지 사용 전략</h2>
    <p>마일리지는 사용 방법에 따라 가치가 크게 달라집니다. 항공권 발권에 사용할 때 가장 높은 가치를 발휘합니다.</p>
    <table class="compare-table">
      <tr><th>사용 방법</th><th>마일당 가치</th><th>추천도</th></tr>
      <tr><td>국제선 이코노미 발권</td><td>10~15원</td><td>★★★☆</td></tr>
      <tr><td>국제선 비즈니스 발권</td><td>20~40원</td><td>★★★★★</td></tr>
      <tr><td>국제선 퍼스트 발권</td><td>30~60원</td><td>★★★★★</td></tr>
      <tr><td>좌석 업그레이드</td><td>10~20원</td><td>★★★★</td></tr>
      <tr><td>쇼핑·호텔</td><td>5~8원</td><td>★★</td></tr>
      <tr><td>현금 전환</td><td>5원</td><td>★</td></tr>
    </table>
    <h2 id="alliance">🌐 항공 동맹 마일리지 활용</h2>
    <p>대한항공은 스카이팀(SkyTeam), 아시아나는 스타얼라이언스(Star Alliance) 소속입니다. 동맹 파트너 항공사 이용 시에도 마일리지가 적립됩니다.</p>
    <ul>
      <li>🌍 <strong>스카이팀</strong> — 에어프랑스, 델타, KLM, 중국남방항공 등 19개 항공사</li>
      <li>⭐ <strong>스타얼라이언스</strong> — 루프트한자, 싱가포르항공, ANA, 유나이티드 등 26개 항공사</li>
      <li>💎 동맹 파트너 비즈니스클래스 탑승 시 마일리지 가치 극대화</li>
    </ul>""",
    "toc": [
      ("earn", "💳 마일리지 적립 방법"),
      ("cards", "💳 마일리지 카드 비교"),
      ("redeem", "🎫 마일리지 사용 전략"),
      ("alliance", "🌐 항공 동맹 활용"),
    ],
    "related": [
      ("../flight-cheap/", "항공권 싸게 사는 법"),
      ("../flight-upgrade/", "비즈니스 업그레이드 팁"),
      ("../travel-card/", "해외여행 카드 비교"),
      ("../flight-longhaul/", "장거리 비행 꿀팁"),
    ]
  },
  {
    "slug": "flight-upgrade",
    "title": "비즈니스클래스 업그레이드 받는 법",
    "description": "비즈니스클래스를 저렴하게 또는 무료로 업그레이드 받는 모든 방법. 마일리지 업그레이드, 입찰, 당일 업그레이드 전략.",
    "og_image": "https://images.pexels.com/photos/1169754/pexels-photo-1169754.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "비즈니스클래스 요금을 그대로 내지 않아도 됩니다. 마일리지 활용, 입찰 시스템, 당일 업그레이드까지 — 현명한 여행자가 비즈니스클래스를 즐기는 방법을 공개합니다.",
    "body": """    <h2 id="methods">🎯 업그레이드 받는 5가지 방법</h2>
    <ul>
      <li>✈️ <strong>마일리지 업그레이드</strong> — 적립된 마일리지로 이코노미→비즈니스 업그레이드 (가장 확실)</li>
      <li>💰 <strong>유료 업그레이드</strong> — 체크인 시 차액 지불. 정가보다 30~60% 저렴한 경우 많음</li>
      <li>🎰 <strong>입찰 업그레이드</strong> — 최저 입찰가에서 시작, 항공사가 수락하면 업그레이드</li>
      <li>🎁 <strong>당일 공항 업그레이드</strong> — 빈 좌석 발생 시 우선 대상자에게 제공</li>
      <li>👑 <strong>상태 업그레이드</strong> — 항공사 엘리트 등급 보유 시 자동 우선순위</li>
    </ul>
    <h2 id="bidding">🎯 입찰 업그레이드 전략</h2>
    <p>많은 항공사가 출발 전 이메일로 업그레이드 입찰을 제안합니다. 적절한 입찰 금액 전략이 중요합니다.</p>
    <table class="compare-table">
      <tr><th>노선</th><th>최저 입찰가</th><th>낙찰 예상 금액</th><th>정가 대비</th></tr>
      <tr><td>한국↔유럽 (10시간)</td><td>$200</td><td>$400~600</td><td>40~60% 절감</td></tr>
      <tr><td>한국↔미국 (12시간)</td><td>$250</td><td>$500~800</td><td>50~70% 절감</td></tr>
      <tr><td>한국↔동남아 (5시간)</td><td>$80</td><td>$150~250</td><td>30~50% 절감</td></tr>
      <tr><td>한국↔일본 (2시간)</td><td>$30</td><td>$50~100</td><td>20~40% 절감</td></tr>
    </table>
    <div class="tip-box">
      <ul>
        <li>✅ 입찰 시 최저가보다 30~40% 높게 제시하면 낙찰 확률 상승</li>
        <li>✅ 만석 가능성이 낮은 비수기·평일 노선에서 유리</li>
        <li>✅ 탑승 72~24시간 전 이메일 확인 — 업그레이드 제안 놓치지 말기</li>
      </ul>
    </div>
    <h2 id="airport">🏢 공항 당일 업그레이드 전략</h2>
    <ul>
      <li>⏰ <strong>일찍 체크인</strong> — 업그레이드 대기자 리스트 앞순위 확보</li>
      <li>👔 <strong>단정한 복장</strong> — 공식 통계는 없지만 정장 차림이 유리하다는 의견 다수</li>
      <li>🎂 <strong>특별한 날 언급</strong> — 허니문·생일·기념일을 카운터에서 정중히 언급</li>
      <li>💎 <strong>엘리트 등급 가입</strong> — 항공사 멤버십 상위 등급이 업그레이드 우선순위</li>
      <li>✈️ <strong>단독 여행자 유리</strong> — 남은 1~2석에 단독 여행자가 업그레이드되기 쉬움</li>
    </ul>
    <h2 id="mileage-upgrade">✈️ 마일리지 업그레이드 필요 마일수</h2>
    <table class="compare-table">
      <tr><th>항공사</th><th>한국↔유럽 (편도)</th><th>한국↔미국 (편도)</th><th>한국↔일본 (편도)</th></tr>
      <tr><td>대한항공</td><td>30,000마일</td><td>35,000마일</td><td>8,000마일</td></tr>
      <tr><td>아시아나</td><td>28,000마일</td><td>32,000마일</td><td>8,000마일</td></tr>
      <tr><td>싱가포르항공</td><td>35,000마일</td><td>43,000마일</td><td>10,000마일</td></tr>
    </table>""",
    "toc": [
      ("methods", "🎯 업그레이드 5가지 방법"),
      ("bidding", "🎯 입찰 업그레이드 전략"),
      ("airport", "🏢 공항 당일 전략"),
      ("mileage-upgrade", "✈️ 마일리지 업그레이드"),
    ],
    "related": [
      ("../flight-cheap/", "항공권 싸게 사는 법"),
      ("../flight-mileage/", "마일리지 가이드"),
      ("../flight-longhaul/", "장거리 비행 꿀팁"),
      ("../travel-card/", "해외여행 카드 비교"),
    ]
  },
  {
    "slug": "flight-delay",
    "title": "항공편 지연·결항 대처법 & 보상 청구",
    "description": "항공편 지연·결항 시 즉각 대처법과 보상 청구 방법. EU 261/2004, 미국 DOT 규정, 한국 소비자 보호 기준.",
    "og_image": "https://images.pexels.com/photos/2026324/pexels-photo-2026324.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "항공편 지연이나 결항은 여행의 최악의 상황 중 하나입니다. 하지만 법적으로 보장된 보상 권리를 알고 있으면 적절한 보상을 받을 수 있습니다.",
    "body": """    <h2 id="immediate">🚨 지연·결항 즉각 대처법</h2>
    <p>지연·결항 공지를 받는 순간 빠른 행동이 중요합니다. 가장 먼저 해야 할 일들입니다.</p>
    <ol>
      <li>📸 <strong>증거 수집</strong> — 전광판·문자·이메일 스크린샷 즉시 저장</li>
      <li>📞 <strong>항공사 연락</strong> — 카운터 줄보다 앱·전화로 빠르게 재예약</li>
      <li>🏨 <strong>호텔 필요 시</strong> — 항공사에 숙박 제공 요청 (결항 시 의무)</li>
      <li>🍽️ <strong>식사 바우처</strong> — 2시간 이상 지연 시 요청 가능</li>
      <li>💳 <strong>여행자보험 신고</strong> — 지연 보험 청구를 위해 확인서 수령</li>
    </ol>
    <h2 id="eu261">🇪🇺 EU 261/2004 — 유럽 출발 보상 규정</h2>
    <p>유럽 출발 또는 EU 항공사를 이용하는 경우 강력한 보상 규정이 적용됩니다.</p>
    <table class="compare-table">
      <tr><th>비행 거리</th><th>지연 기준</th><th>보상금액</th></tr>
      <tr><td>1,500km 이하</td><td>3시간 이상</td><td>€250</td></tr>
      <tr><td>1,500~3,500km</td><td>3시간 이상</td><td>€400</td></tr>
      <tr><td>3,500km 초과</td><td>4시간 이상</td><td>€600</td></tr>
      <tr><td>결항 (사전 미통보)</td><td>-</td><td>€250~600</td></tr>
    </table>
    <div class="info-box">
      <strong>ℹ️ EU 보상 청구 방법</strong><br>
      <ul style="margin:8px 0 0;padding-left:18px;font-size:.88rem;line-height:2">
        <li>항공사 직접 청구 → 거부 시 → 각국 국가항공당국(NEB) 신고</li>
        <li>AirHelp, ClaimCompass 등 전문 대행업체 활용 (수수료 25~35%)</li>
        <li>소멸시효: 각국 다름 (프랑스 5년, 독일 3년, 영국 6년)</li>
      </ul>
    </div>
    <h2 id="korea">🇰🇷 한국 출발 보상 기준</h2>
    <table class="compare-table">
      <tr><th>상황</th><th>항공사 책임</th><th>보상 내용</th></tr>
      <tr><td>2시간 이상 지연</td><td>항공사 귀책</td><td>식사 제공 또는 교통비</td></tr>
      <tr><td>4시간 이상 지연</td><td>항공사 귀책</td><td>숙박 + 식사 제공</td></tr>
      <tr><td>결항 (24시간 전 통보)</td><td>-</td><td>환불 또는 재예약</td></tr>
      <tr><td>불가항력 (기상·파업)</td><td>면책</td><td>환불만 의무</td></tr>
    </table>
    <h2 id="insurance">🛡️ 여행자보험 지연 보상 활용</html>
    <ul>
      <li>⏰ <strong>지연 보상</strong> — 통상 3~6시간 이상 지연 시 1일 3~5만원</li>
      <li>✈️ <strong>항공기 납치 보상</strong> — 24시간당 보상</li>
      <li>🧳 <strong>수하물 지연</strong> — 필수품 구매비용 실비 보상</li>
      <li>📋 <strong>청구 서류</strong> — 지연확인서, 영수증, 탑승권 사본 필수</li>
    </ul>""",
    "toc": [
      ("immediate", "🚨 즉각 대처법"),
      ("eu261", "🇪🇺 EU 261 보상 규정"),
      ("korea", "🇰🇷 한국 출발 기준"),
      ("insurance", "🛡️ 여행보험 보상"),
    ],
    "related": [
      ("../flight-cheap/", "항공권 싸게 사는 법"),
      ("../flight-baggage/", "수하물 규정 비교"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
      ("../travel-visa/", "비자 완전 가이드"),
    ]
  },
  {
    "slug": "flight-transit",
    "title": "트랜짓·레이오버 완전 가이드",
    "description": "경유지에서 짧은 시간도 여행으로 — 트랜짓 비자, 공항 탈출 팁, 주요 허브공항 환승 시간 가이드.",
    "og_image": "https://images.pexels.com/photos/2026324/pexels-photo-2026324.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "환승 시간이 길 때 공항에만 있는 것은 낭패입니다. 트랜짓 비자 규정을 알고 공항을 탈출해 경유지를 여행지로 즐기는 방법을 알려드립니다.",
    "body": """    <h2 id="transit-types">🔄 트랜짓 vs 레이오버 차이</h2>
    <div class="two-col">
      <div style="background:#e8f5e9;padding:14px;border-radius:8px">
        <strong style="color:#2e7d32">🔄 트랜짓 (Transit)</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>일반적으로 24시간 미만</li>
          <li>입국심사 없이 환승 구역만 이동</li>
          <li>무비자 환승 가능한 경우 많음</li>
          <li>공항 내 상업시설 이용 가능</li>
        </ul>
      </div>
      <div style="background:#fff3e0;padding:14px;border-radius:8px">
        <strong style="color:#e65100">🌙 레이오버 (Layover)</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>일반적으로 24시간 이상</li>
          <li>입국 후 시내 관광 가능</li>
          <li>비자 필요 여부 확인 필수</li>
          <li>호텔 숙박 예약 필요</li>
        </ul>
      </div>
    </div>
    <h2 id="visa-free">🛂 무비자 환승 가능 주요 국가</h2>
    <table class="compare-table">
      <tr><th>국가/공항</th><th>한국 여권</th><th>환승 비자 조건</th><th>공항 탈출 가능</th></tr>
      <tr><td>🇸🇬 싱가포르 창이</td><td>무비자 96시간</td><td>불필요</td><td>✅ 가능</td></tr>
      <tr><td>🇦🇪 두바이 DXB</td><td>무비자 30일</td><td>불필요</td><td>✅ 가능</td></tr>
      <tr><td>🇯🇵 일본 각 공항</td><td>무비자 90일</td><td>불필요</td><td>✅ 가능</td></tr>
      <tr><td>🇹🇭 방콕 수완나품</td><td>무비자 30일</td><td>불필요</td><td>✅ 가능</td></tr>
      <tr><td>🇺🇸 미국 각 공항</td><td>ESTA 필요</td><td>ESTA 사전 취득</td><td>✅ ESTA 있으면</td></tr>
      <tr><td>🇨🇳 중국 주요공항</td><td>144시간 무비자</td><td>조건 충족 시</td><td>✅ 144h 이내</td></tr>
    </table>
    <h2 id="hubs">🏢 주요 허브공항 환승 시간 기준</h2>
    <ul>
      <li>🇸🇬 <strong>싱가포르 창이</strong> — 최소 1시간, 권장 2시간. 세계 최고 공항 편의시설</li>
      <li>🇦🇪 <strong>두바이 DXB</strong> — 최소 1.5시간, 권장 2.5시간. 대형 공항으로 이동 시간 길수 있음</li>
      <li>🇩🇪 <strong>프랑크푸르트 FRA</strong> — 최소 1.5시간, 다른 터미널 이동 시 45분 소요</li>
      <li>🇬🇧 <strong>런던 히스로 LHR</strong> — 최소 2시간, 터미널 간 이동 필수 확인</li>
      <li>🇯🇵 <strong>도쿄 나리타 NRT</strong> — 최소 1.5시간, 자국 출발자는 세관 거쳐야</li>
    </ul>
    <h2 id="tips">💡 환승 여행 꿀팁</h2>
    <ul>
      <li>📦 <strong>수하물 확인</strong> — 연결편까지 직통 수하물 서비스(Through Baggage) 여부 확인</li>
      <li>🎫 <strong>환승 투어</strong> — 싱가포르 창이·두바이 등 공항 무료 환승 투어 프로그램 활용</li>
      <li>🛏️ <strong>라운지 이용</strong> — Priority Pass·공항 라운지로 장시간 환승 피로 해소</li>
      <li>🌙 <strong>야간 환승</strong> — 공항 호텔 vs 환승 전용 캡슐 호텔 비교 예약</li>
    </ul>""",
    "toc": [
      ("transit-types", "🔄 트랜짓 vs 레이오버"),
      ("visa-free", "🛂 무비자 환승 국가"),
      ("hubs", "🏢 허브공항 환승 기준"),
      ("tips", "💡 환승 여행 꿀팁"),
    ],
    "related": [
      ("../flight-cheap/", "항공권 싸게 사는 법"),
      ("../travel-visa/", "비자 완전 가이드"),
      ("../travel-esta/", "ESTA·eTA 신청 가이드"),
      ("../travel-immigration/", "입국 심사 꿀팁"),
    ]
  },
  {
    "slug": "flight-longhaul",
    "title": "장거리 비행 꿀팁 완전 가이드",
    "description": "10시간 이상 장거리 비행을 편안하게 — 좌석 선택, 수면 전략, 건강 관리, 기내 필수템 총정리.",
    "og_image": "https://images.pexels.com/photos/1169754/pexels-photo-1169754.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "장거리 비행은 설레기도 하지만 체력 소모가 큽니다. 올바른 좌석 선택, 수면 전략, 건강 관리법을 알면 목적지에 도착할 때 훨씬 더 컨디션이 좋아집니다.",
    "body": """    <h2 id="seat">💺 좌석 선택 전략</h2>
    <p>장거리 비행에서 좌석 선택은 매우 중요합니다. 목적에 따라 최적 좌석이 다릅니다.</p>
    <table class="compare-table">
      <tr><th>좌석 위치</th><th>장점</th><th>단점</th><th>추천 대상</th></tr>
      <tr><td>비상구 좌석</td><td>다리 공간 넓음</td><td>좌석 틸팅 제한</td><td>키 큰 분</td></tr>
      <tr><td>앞쪽 (1~10열)</td><td>빠른 하기, 조용함</td><td>좌석 틸팅 안 됨(1열)</td><td>비즈니스 여행자</td></tr>
      <tr><td>창가 (A/K 열)</td><td>기댈 수 있음, 뷰</td><td>화장실 이동 불편</td><td>수면 중시</td></tr>
      <tr><td>통로 (C/H 열)</td><td>화장실 이동 쉬움</td><td>카트 통행, 접촉</td><td>자주 일어나는 분</td></tr>
      <tr><td>중앙 (B열)</td><td>없음</td><td>양쪽 불편</td><td>비추천</td></tr>
    </table>
    <h2 id="sleep">😴 기내 수면 전략</h2>
    <ul>
      <li>🌙 <strong>취침 시간 맞추기</strong> — 목적지 도착 시간에 맞춰 수면 조절로 시차 적응</li>
      <li>👁️ <strong>안대 필수</strong> — 기내 조명 차단, 수면의 질 향상</li>
      <li>🎧 <strong>노이즈 캔슬링 이어폰</strong> — 기내 소음(75~85dB) 차단</li>
      <li>🦺 <strong>목베개</strong> — U자형보다 앞쪽 지지형이 더 효과적</li>
      <li>💊 <strong>수면제·멜라토닌</strong> — 의사 처방 후 사용, 도착 전 중단</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 탑승 전 카페인 6시간 전부터 끊기</li>
        <li>✅ 알코올은 탈수와 수면의 질 저하 — 최소화</li>
        <li>✅ 기내식은 조명이 켜질 때만 먹고 나머지 시간은 수면에 집중</li>
      </ul>
    </div>
    <h2 id="health">🏥 건강 관리</h2>
    <ul>
      <li>💧 <strong>수분 보충</strong> — 1시간당 250ml 물 섭취 (기내 습도 20% 이하)</li>
      <li>🦵 <strong>혈전증 예방</strong> — 2시간마다 일어나 걷기, 압박 스타킹 착용</li>
      <li>👂 <strong>귀 압력 조절</strong> — 이착륙 시 하품·껌·코 막고 삼키기</li>
      <li>🧴 <strong>피부 보습</strong> — 보습 크림·로션 수시 도포 (액체류 규정 내)</li>
      <li>😷 <strong>마스크 착용</strong> — 순환 공기로 인한 감염 위험 감소</li>
    </ul>
    <h2 id="packing">🎒 기내 필수템 리스트</h2>
    <div class="two-col">
      <div style="background:#e8f5e9;padding:14px;border-radius:8px">
        <strong style="color:#2e7d32">✅ 필수 아이템</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>노이즈캔슬링 이어폰</li>
          <li>안대 + 목베개</li>
          <li>립밤 + 보습 크림</li>
          <li>개인 담요/숄</li>
          <li>슬리퍼 (기내용)</li>
          <li>충전 케이블</li>
        </ul>
      </div>
      <div style="background:#fff3e0;padding:14px;border-radius:8px">
        <strong style="color:#e65100">💡 추천 아이템</strong>
        <ul style="margin:8px 0 0;padding-left:18px;font-size:.85rem;line-height:2">
          <li>압박 스타킹</li>
          <li>세면도구 미니세트</li>
          <li>영양제 (비타민C)</li>
          <li>간식 (건과류)</li>
          <li>오프라인 콘텐츠 다운로드</li>
          <li>멀티 어댑터 (기내 충전구용)</li>
        </ul>
      </div>
    </div>""",
    "toc": [
      ("seat", "💺 좌석 선택 전략"),
      ("sleep", "😴 기내 수면 전략"),
      ("health", "🏥 건강 관리"),
      ("packing", "🎒 기내 필수템"),
    ],
    "related": [
      ("../flight-upgrade/", "비즈니스 업그레이드 팁"),
      ("../flight-transit/", "트랜짓 레이오버 가이드"),
      ("../travel-jetlag/", "시차 적응 완전 가이드"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
    ]
  },
  {
    "slug": "travel-exchange",
    "title": "해외 환전 완전 가이드",
    "description": "해외여행 환전 방법 총정리. 은행 환전, 공항 환전, 현지 ATM 비교 및 환율 우대 받는 법.",
    "og_image": "https://images.pexels.com/photos/164527/pexels-photo-164527.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "환전을 어디서 하느냐에 따라 여행 경비가 달라집니다. 가장 유리한 환전 방법과 절약 팁을 정리했습니다.",
    "body": """    <h2 id="compare">💱 환전 방법 비교</h2>
    <table class="compare-table">
      <tr><th>방법</th><th>환율 우대</th><th>편의성</th><th>추천도</th></tr>
      <tr><td>은행 앱 환전 (인터넷)</td><td>최대 90%</td><td>★★★★</td><td>★★★★★</td></tr>
      <tr><td>시중 은행 창구</td><td>50~70%</td><td>★★★</td><td>★★★</td></tr>
      <tr><td>공항 환전소</td><td>30~50%</td><td>★★★★★</td><td>★★</td></tr>
      <tr><td>현지 ATM 인출</td><td>공시환율 기준</td><td>★★★★</td><td>★★★★</td></tr>
      <tr><td>호텔/관광지 환전소</td><td>10~30%</td><td>★★★★★</td><td>★</td></tr>
    </table>
    <h2 id="tips">💡 환율 우대 받는 법</h2>
    <ul>
      <li>📱 <strong>은행 앱 사전 환전</strong> — 출발 2~3일 전 앱으로 환전 신청 후 공항 수령</li>
      <li>🏦 <strong>주거래 은행 활용</strong> — 급여·예금 실적 있으면 90% 우대 가능</li>
      <li>📊 <strong>환율 모니터링</strong> — 네이버·하나은행 환율 알림 설정</li>
      <li>💳 <strong>트래블카드</strong> — 트래블월렛·트래블로그 앱으로 환율 우대 충전</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 달러/유로는 한국에서 환전이 유리, 동남아 통화는 현지 ATM 인출이 저렴할 수 있음</li>
        <li>✅ 환전 금액: 여행 기간 × 1일 예산 × 1.2 (여유분 20% 추가)</li>
        <li>✅ 남은 외화는 귀국 후 즉시 재환전 — 장기 보유 시 환율 손실</li>
      </ul>
    </div>
    <h2 id="country">🌍 나라별 환전 전략</h2>
    <table class="compare-table">
      <tr><th>목적지</th><th>추천 방법</th><th>비고</th></tr>
      <tr><td>미국</td><td>달러 사전 환전 or 카드</td><td>팁 문화 — 현금 소량 필수</td></tr>
      <tr><td>유럽(유로존)</td><td>유로 사전 환전 or 카드</td><td>카드 사용률 높음</td></tr>
      <tr><td>일본</td><td>엔화 사전 환전</td><td>현금 위주 문화</td></tr>
      <tr><td>태국</td><td>달러 환전 후 현지 ATM</td><td>수퍼리치 환전소 유리</td></tr>
      <tr><td>베트남</td><td>달러 환전 후 현지 환전</td><td>동(VND) 현지 환전 유리</td></tr>
      <tr><td>UAE</td><td>달러 or 카드</td><td>디르함 한국 환전 불리</td></tr>
    </table>
    <h2 id="safety">🔒 환전·현금 보안</h2>
    <ul>
      <li>💼 <strong>현금 분산 보관</strong> — 지갑·가방·숙소 금고에 나눠 보관</li>
      <li>🔐 <strong>허리 지갑</strong> — 소매치기 많은 지역에서 여권·현금 분리 보관</li>
      <li>💳 <strong>카드 백업</strong> — 현금 분실 시 대비해 해외 결제 카드 2장 이상 소지</li>
      <li>📞 <strong>분실 신고 번호</strong> — 해외에서 카드 분실 시 연락할 번호 저장</li>
    </ul>""",
    "toc": [
      ("compare", "💱 환전 방법 비교"),
      ("tips", "💡 환율 우대 팁"),
      ("country", "🌍 나라별 환전 전략"),
      ("safety", "🔒 환전 보안"),
    ],
    "related": [
      ("../travel-card/", "해외여행 카드 비교"),
      ("../travel-atm/", "해외 ATM 이용법"),
      ("../travel-tipping/", "나라별 팁 문화"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
    ]
  },
  {
    "slug": "travel-card",
    "title": "해외여행 최적 카드 비교 가이드",
    "description": "해외에서 유리한 신용카드·체크카드·트래블카드 비교. 해외 수수료 0%, 환율 우대, 공항 라운지 혜택 총정리.",
    "og_image": "https://images.pexels.com/photos/164527/pexels-photo-164527.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "해외에서 잘못된 카드를 사용하면 결제금액의 2~3%가 수수료로 빠져나갑니다. 해외여행에 최적화된 카드 선택으로 불필요한 비용을 없애세요.",
    "body": """    <h2 id="fees">💸 해외 카드 수수료 구조</h2>
    <p>해외에서 카드를 사용하면 여러 수수료가 복합적으로 부과됩니다. 총 수수료율이 낮은 카드를 선택하는 것이 핵심입니다.</p>
    <table class="compare-table">
      <tr><th>수수료 종류</th><th>일반 카드</th><th>해외특화 카드</th></tr>
      <tr><td>국제 브랜드 수수료(VISA/MC)</td><td>1%</td><td>0~1%</td></tr>
      <tr><td>해외이용 수수료</td><td>0.25~1%</td><td>0%</td></tr>
      <tr><td>환전 스프레드</td><td>1~2%</td><td>0~0.5%</td></tr>
      <tr><td>ATM 인출 수수료</td><td>2,000~5,000원</td><td>0~2,000원</td></tr>
      <tr><td>총 수수료</td><td>약 2~4%</td><td>약 0~1%</td></tr>
    </table>
    <h2 id="recommended">💳 추천 해외여행 카드</h2>
    <ul>
      <li>🏆 <strong>트래블로그 체크카드</strong> — 해외 수수료 0%, 실시간 환율 충전, 30개국 통화</li>
      <li>🏆 <strong>트래블월렛</strong> — 앱으로 충전, 환율 우대, 40개국 이상 현지 ATM 무료 인출</li>
      <li>🏆 <strong>하나 트래블로그</strong> — 해외 수수료 면제, 제휴 ATM 무료</li>
      <li>🌟 <strong>현대카드 Zero Edition</strong> — 해외 수수료 0.3%, 연회비 저렴</li>
      <li>🌟 <strong>신한 SOL트래블체크</strong> — 해외 수수료 0%, 환전 우대</li>
    </ul>
    <div class="info-box">
      <strong>ℹ️ 트래블 카드 vs 일반 카드 차이</strong><br>
      <ul style="margin:8px 0 0;padding-left:18px;font-size:.88rem;line-height:2">
        <li>트래블 카드: 출발 전 앱에서 원하는 통화로 충전 → 현지에서 해당 통화로 결제</li>
        <li>일반 해외 카드: 결제 시점 환율 적용 — 환율 변동 리스크 있음</li>
        <li>마일리지 카드: 수수료 있지만 마일리지 적립 가능 — 장거리 여행자에 유리</li>
      </ul>
    </div>
    <h2 id="lounge">✈️ 공항 라운지 혜택 카드</h2>
    <table class="compare-table">
      <tr><th>카드</th><th>라운지 혜택</th><th>연회비</th></tr>
      <tr><td>삼성카드 iD Air</td><td>인천공항 라운지 무제한</td><td>150,000원</td></tr>
      <tr><td>현대카드 The Black</td><td>PP 무제한</td><td>매우 높음</td></tr>
      <tr><td>아멕스 골드</td><td>프라이오리티 패스</td><td>150,000원</td></tr>
      <tr><td>롯데카드 항공마일</td><td>인천 라운지 2회</td><td>100,000원</td></tr>
    </table>
    <h2 id="strategy">🎯 카드 사용 전략</h2>
    <ul>
      <li>💰 <strong>큰 금액 결제</strong> — 마일리지 카드로 적립 극대화</li>
      <li>💸 <strong>소액 결제</strong> — 트래블 카드로 수수료 절감</li>
      <li>💵 <strong>현금 인출</strong> — 트래블 카드 연계 ATM에서 무료 인출</li>
      <li>🔒 <strong>카드 2장 이상</strong> — 분실·도난 대비 다른 브랜드(VISA+Mastercard)</li>
    </ul>""",
    "toc": [
      ("fees", "💸 해외 수수료 구조"),
      ("recommended", "💳 추천 카드"),
      ("lounge", "✈️ 라운지 혜택"),
      ("strategy", "🎯 카드 사용 전략"),
    ],
    "related": [
      ("../travel-exchange/", "해외 환전 가이드"),
      ("../travel-atm/", "해외 ATM 이용법"),
      ("../travel-tipping/", "나라별 팁 문화"),
      ("../flight-mileage/", "마일리지 가이드"),
    ]
  },
  {
    "slug": "travel-atm",
    "title": "해외 ATM 이용법 & 주의사항",
    "description": "해외 ATM 안전하게 사용하는 법. 수수료 최소화, 카드 스키밍 예방, 나라별 ATM 이용 팁.",
    "og_image": "https://images.pexels.com/photos/164527/pexels-photo-164527.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "해외에서 ATM은 현금을 구하는 가장 편리한 방법이지만, 수수료와 보안 위험을 알지 못하면 낭패를 볼 수 있습니다.",
    "body": """    <h2 id="fees">💸 ATM 수수료 구조</h2>
    <table class="compare-table">
      <tr><th>수수료 종류</th><th>금액</th><th>절감 방법</th></tr>
      <tr><td>현지 ATM 수수료</td><td>$2~5</td><td>은행 ATM 이용</td></tr>
      <tr><td>한국 카드사 수수료</td><td>$2~3 또는 인출액 1~2%</td><td>트래블카드 이용</td></tr>
      <tr><td>국제 브랜드 수수료</td><td>인출액 0.5~1%</td><td>일부 카드는 면제</td></tr>
      <tr><td>환전 마진</td><td>0~3%</td><td>로컬 통화 선택</td></tr>
    </table>
    <h2 id="dcc">⚠️ DCC(동적 화폐 전환) 함정</h2>
    <p>해외 ATM에서 한국 원화로 인출 옵션이 나타나면 반드시 거부해야 합니다. DCC는 불리한 환율을 적용해 3~5% 추가 손해를 봅니다.</p>
    <div class="warn-box">
      <strong>⚠️ ATM에서 이런 화면이 나오면 주의!</strong><br>
      <ul style="margin:8px 0 0;padding-left:18px;font-size:.88rem;line-height:2">
        <li>"Do you want to pay in KRW (Korean Won)?" → <strong>NO 선택</strong></li>
        <li>"Proceed with conversion?" → <strong>DECLINE 선택</strong></li>
        <li>"Accept the exchange rate offered?" → <strong>REJECT 선택</strong></li>
        <li>항상 현지 통화(Local Currency)로 인출</li>
      </ul>
    </div>
    <h2 id="safety">🔒 ATM 보안 수칙</h2>
    <ul>
      <li>🏦 <strong>은행 공식 ATM 이용</strong> — 거리 ATM보다 은행 지점 내 ATM이 안전</li>
      <li>👁️ <strong>주변 확인</strong> — 뒤에 서 있는 사람 없는지 확인</li>
      <li>🖐️ <strong>키패드 가리기</strong> — PIN 입력 시 손으로 가리기</li>
      <li>🔍 <strong>카드 리더 점검</strong> — 카드 삽입구가 헐겁거나 이상하면 이용 금지</li>
      <li>📱 <strong>소액씩 인출</strong> — 한 번에 대액 인출보다 필요할 때마다 소액 인출</li>
    </ul>
    <h2 id="country">🌍 나라별 ATM 팁</h2>
    <table class="compare-table">
      <tr><th>국가</th><th>추천 ATM</th><th>주의사항</th></tr>
      <tr><td>🇺🇸 미국</td><td>Chase, Bank of America</td><td>수수료 $2~3 일반적</td></tr>
      <tr><td>🇪🇺 유럽</td><td>Euronet 피하기</td><td>DCC 제안 빈번</td></tr>
      <tr><td>🇯🇵 일본</td><td>7-Eleven, Japan Post</td><td>외국 카드 허용 제한적</td></tr>
      <tr><td>🇹🇭 태국</td><td>KASIKORN, SCB</td><td>인출당 220바트 수수료</td></tr>
      <tr><td>🇻🇳 베트남</td><td>Vietcombank, Techcombank</td><td>인출 한도 낮음(2백만동)</td></tr>
    </table>""",
    "toc": [
      ("fees", "💸 ATM 수수료 구조"),
      ("dcc", "⚠️ DCC 함정 주의"),
      ("safety", "🔒 ATM 보안 수칙"),
      ("country", "🌍 나라별 ATM 팁"),
    ],
    "related": [
      ("../travel-exchange/", "해외 환전 가이드"),
      ("../travel-card/", "해외여행 카드 비교"),
      ("../travel-theft/", "도난·분실 신고 가이드"),
      ("../travel-tipping/", "나라별 팁 문화"),
    ]
  },
  {
    "slug": "travel-tipping",
    "title": "나라별 팁 문화 완전 가이드",
    "description": "나라별 팁(tip) 문화 완전 비교. 미국·유럽·일본·동남아·중동 팁 에티켓과 적정 금액.",
    "og_image": "https://images.pexels.com/photos/164527/pexels-photo-164527.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "팁 문화는 나라마다 완전히 다릅니다. 팁을 줘야 하는 나라에서 안 주면 실례, 주지 않아도 되는 나라에서 억지로 주면 당황스럽습니다.",
    "body": """    <h2 id="tipping-map">🗺️ 나라별 팁 문화 지도</h2>
    <table class="compare-table">
      <tr><th>나라</th><th>팁 문화</th><th>레스토랑</th><th>택시</th><th>호텔</th></tr>
      <tr><td>🇺🇸 미국</td><td>필수</td><td>15~20%</td><td>15~20%</td><td>$2~5/박</td></tr>
      <tr><td>🇨🇦 캐나다</td><td>필수</td><td>15~20%</td><td>15%</td><td>$2~3/박</td></tr>
      <tr><td>🇲🇽 멕시코</td><td>권장</td><td>10~15%</td><td>10%</td><td>$1~2/박</td></tr>
      <tr><td>🇬🇧 영국</td><td>권장</td><td>10~12.5%</td><td>반올림</td><td>£1~2</td></tr>
      <tr><td>🇫🇷 프랑스</td><td>선택</td><td>5~10%</td><td>반올림</td><td>€1~2</td></tr>
      <tr><td>🇩🇪 독일</td><td>선택</td><td>5~10%</td><td>반올림</td><td>€1~2</td></tr>
      <tr><td>🇯🇵 일본</td><td>거의 없음</td><td>불필요</td><td>불필요</td><td>불필요</td></tr>
      <tr><td>🇰🇷 한국</td><td>없음</td><td>불필요</td><td>불필요</td><td>불필요</td></tr>
      <tr><td>🇹🇭 태국</td><td>선택</td><td>50~100바트</td><td>반올림</td><td>20~50바트</td></tr>
      <tr><td>🇦🇪 UAE</td><td>선택</td><td>10~15%</td><td>반올림</td><td>5~10디르함</td></tr>
    </table>
    <h2 id="usa">🇺🇸 미국 팁 에티켓</h2>
    <p>미국은 서비스업 종사자들이 팁으로 생계를 유지합니다. 팁은 사실상 의무입니다.</p>
    <ul>
      <li>🍽️ <strong>레스토랑</strong> — 세금 제외 금액의 15~20%. 그룹(6인+)은 자동 팁(Gratuity) 포함</li>
      <li>🚕 <strong>우버/리프트</strong> — 앱에서 15~20% 팁 선택</li>
      <li>☕ <strong>카페·바</strong> — $1~2 또는 음료값의 10~15%</li>
      <li>🏨 <strong>벨보이·하우스키핑</strong> — $2~5/건</li>
      <li>💇 <strong>헤어/네일</strong> — 15~20%</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 계산서에 Gratuity가 이미 포함되어 있으면 추가 팁 불필요</li>
        <li>✅ 팁은 항상 현금 또는 카드 결제 시 별도 팁란에 입력</li>
        <li>✅ 서비스가 나빴어도 10% 이하로 내리는 것이 관례 (안 주는 것은 실례)</li>
      </ul>
    </div>
    <h2 id="no-tip">🚫 팁을 주면 안 되는 상황</h2>
    <ul>
      <li>🇯🇵 <strong>일본</strong> — 팁 제도 자체가 없음. 줘도 거절하거나 당황함</li>
      <li>🇸🇬 <strong>싱가포르</strong> — 고급 레스토랑 외에는 불필요 (서비스 차지 10% 포함)</li>
      <li>🇦🇺 <strong>호주</strong> — 의무 아님, 감동적인 서비스에만 소액</li>
      <li>🛳️ <strong>크루즈 선상</strong> — 대부분 자동으로 DSC(일일 봉사료) 청구됨</li>
    </ul>""",
    "toc": [
      ("tipping-map", "🗺️ 나라별 팁 문화"),
      ("usa", "🇺🇸 미국 팁 에티켓"),
      ("no-tip", "🚫 팁 불필요한 곳"),
    ],
    "related": [
      ("../travel-exchange/", "해외 환전 가이드"),
      ("../travel-card/", "해외여행 카드 비교"),
      ("../travel-usa/", "미국 자유여행 가이드"),
      ("../travel-europe/", "유럽 자유여행 가이드"),
    ]
  },
  {
    "slug": "travel-sim",
    "title": "해외 유심 vs 포켓와이파이 vs 로밍 비교",
    "description": "해외여행 인터넷 3가지 방법 완전 비교. 유심(e-SIM 포함), 포켓와이파이, 통신사 로밍 — 비용·편의성·속도 총정리.",
    "og_image": "https://images.pexels.com/photos/607812/pexels-photo-607812.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "해외에서 인터넷은 필수입니다. 유심, 포켓와이파이, 로밍 — 세 가지 방법의 장단점을 비교해 자신에게 맞는 최적 선택을 해보세요.",
    "body": """    <h2 id="compare">📊 3가지 방법 핵심 비교</h2>
    <table class="compare-table">
      <tr><th>항목</th><th>현지 유심</th><th>e-SIM</th><th>포켓와이파이</th><th>로밍</th></tr>
      <tr><td>가격 (7일)</td><td>₩10,000~30,000</td><td>₩15,000~40,000</td><td>₩30,000~60,000</td><td>₩100,000~200,000</td></tr>
      <tr><td>속도</td><td>현지 수준</td><td>현지 수준</td><td>현지 수준</td><td>제한적</td></tr>
      <tr><td>기기 여러 대</td><td>X (1대)</td><td>X (1대)</td><td>O (최대 5~10대)</td><td>X (1대)</td></tr>
      <tr><td>기존 번호 유지</td><td>X</td><td>O (듀얼SIM)</td><td>O</td><td>O</td></tr>
      <tr><td>준비 편의성</td><td>사전 구매 필요</td><td>앱으로 간편</td><td>사전 구매 필요</td><td>신청만 하면 됨</td></tr>
    </table>
    <h2 id="esim">📱 e-SIM 완전 가이드</h2>
    <p>e-SIM은 물리적 유심 없이 QR코드로 개통하는 디지털 유심입니다. 아이폰 XS 이상, 갤럭시 S20 이상에서 지원합니다.</p>
    <ul>
      <li>✅ <strong>Airalo</strong> — 세계 최대 e-SIM 마켓, 170+국가, 가격 저렴</li>
      <li>✅ <strong>Holafly</strong> — 무제한 데이터 전문, 다소 비쌈</li>
      <li>✅ <strong>Nomad</strong> — 한국인 사용자 많음, 앱 한국어 지원</li>
      <li>✅ <strong>통신사 e-SIM</strong> — SKT·KT·LGU+ 공식 e-SIM (편리하지만 비쌈)</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ e-SIM 활성화는 출발 전 국내에서 하기 (현지에서 인터넷 없으면 개통 불가)</li>
        <li>✅ 듀얼 SIM 폰은 기존 번호(로밍) + e-SIM(데이터) 동시 사용 가능</li>
        <li>✅ 구형 폰은 e-SIM 미지원 — 기기 호환 먼저 확인</li>
      </ul>
    </div>
    <h2 id="recommendation">🎯 상황별 추천</h2>
    <table class="compare-table">
      <tr><th>상황</th><th>추천 방법</th><th>이유</th></tr>
      <tr><td>1인 여행, 장기체류</td><td>현지 유심 or e-SIM</td><td>가장 저렴하고 빠름</td></tr>
      <tr><td>가족·단체 여행</td><td>포켓와이파이</td><td>여러 기기 동시 사용</td></tr>
      <tr><td>짧은 출장 (2~3일)</td><td>로밍 데이터 (무제한)</td><td>편의성, 비용 무방</td></tr>
      <tr><td>듀얼SIM 폰 보유</td><td>e-SIM + 기존번호 로밍</td><td>번호 유지 + 저렴한 데이터</td></tr>
      <tr><td>오지·여러 나라</td><td>글로벌 e-SIM</td><td>나라별 갈아끼울 필요 없음</td></tr>
    </table>
    <h2 id="wifi-security">🔒 해외 Wi-Fi 보안</h2>
    <ul>
      <li>🚫 <strong>공공 Wi-Fi 금융 거래 금지</strong> — 카드 정보·인터넷 뱅킹 절대 금지</li>
      <li>🔐 <strong>VPN 사용</strong> — ExpressVPN, NordVPN 등으로 암호화</li>
      <li>📶 <strong>HTTPS 확인</strong> — 주소창 자물쇠 아이콘 확인 후 사용</li>
    </ul>""",
    "toc": [
      ("compare", "📊 3가지 방법 비교"),
      ("esim", "📱 e-SIM 완전 가이드"),
      ("recommendation", "🎯 상황별 추천"),
      ("wifi-security", "🔒 Wi-Fi 보안"),
    ],
    "related": [
      ("../travel-apps/", "해외여행 필수 앱"),
      ("../travel-wifi-security/", "해외 인터넷 보안"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
      ("../travel-card/", "해외여행 카드 비교"),
    ]
  },
  {
    "slug": "travel-apps",
    "title": "해외여행 필수 앱 모음",
    "description": "해외여행 전 꼭 설치해야 할 앱 총정리. 지도, 번역, 교통, 숙박, 환전, 비상연락 앱 카테고리별 추천.",
    "og_image": "https://images.pexels.com/photos/607812/pexels-photo-607812.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "스마트폰 하나로 해외여행의 90%는 해결할 수 있습니다. 카테고리별 필수 앱을 미리 설치하고 오프라인 모드까지 준비해두면 현지에서 인터넷 없이도 안전합니다.",
    "body": """    <h2 id="map">🗺️ 지도·내비게이션</h2>
    <ul>
      <li>📍 <strong>Google Maps</strong> — 필수 중의 필수. 오프라인 지도 다운로드 먼저 하기</li>
      <li>🗺️ <strong>Maps.me</strong> — 완전 오프라인 지도, 인터넷 없어도 OK</li>
      <li>🚇 <strong>Citymapper</strong> — 도시 대중교통 전문 (런던·파리·뉴욕 등)</li>
      <li>🚃 <strong>Moovit</strong> — 100개 이상 도시 대중교통 실시간 안내</li>
    </ul>
    <h2 id="translate">🌐 번역·언어</h2>
    <ul>
      <li>📖 <strong>Google 번역</strong> — 카메라 번역(메뉴판·간판), 음성 통역, 오프라인 지원</li>
      <li>🤖 <strong>Papago</strong> — 아시아 언어(일어·중어·태국어) 특히 정확</li>
      <li>🗣️ <strong>iTranslate</strong> — 실시간 대화 번역, 방언 지원</li>
    </ul>
    <h2 id="transport">✈️ 교통·숙박</h2>
    <ul>
      <li>✈️ <strong>Google Flights / 스카이스캐너</strong> — 항공권 검색·비교</li>
      <li>🏨 <strong>Booking.com / Agoda</strong> — 호텔·숙박 예약</li>
      <li>🏠 <strong>Airbnb</strong> — 현지 민박·아파트</li>
      <li>🚗 <strong>Uber / Grab</strong> — 차량 공유 (동남아는 Grab 필수)</li>
      <li>🚄 <strong>Omio / Rail Europe</strong> — 유럽 기차 예약</li>
    </ul>
    <h2 id="money">💰 환전·결제</h2>
    <ul>
      <li>💱 <strong>트래블월렛 / 트래블로그</strong> — 해외여행 전용 카드 앱</li>
      <li>📊 <strong>XE Currency</strong> — 실시간 환율 계산기</li>
      <li>💳 <strong>각 은행 앱</strong> — 모바일 환전 예약</li>
    </ul>
    <div class="tip-box">
      <ul>
        <li>✅ 출발 전 모든 앱 오프라인 데이터 다운로드 (지도, 번역 언어팩)</li>
        <li>✅ 앱 결제 정보 미리 입력 (호텔 체크인 시 인터넷 없을 수 있음)</li>
        <li>✅ 비상 연락처(한국 대사관, 여행보험사 번호)를 연락처에 저장</li>
      </ul>
    </div>
    <h2 id="safety">🆘 안전·비상</h2>
    <ul>
      <li>🆘 <strong>외교부 해외안전여행 앱</strong> — 국가별 위험 등급, 비상 연락처</li>
      <li>🏥 <strong>Zocdoc</strong> — 해외 영어권 의사 예약</li>
      <li>📋 <strong>TripIt</strong> — 여행 일정 통합 관리, 비행 알림</li>
      <li>🔒 <strong>1Password / LastPass</strong> — 해외에서 안전한 패스워드 관리</li>
    </ul>""",
    "toc": [
      ("map", "🗺️ 지도·내비게이션"),
      ("translate", "🌐 번역·언어"),
      ("transport", "✈️ 교통·숙박"),
      ("money", "💰 환전·결제"),
      ("safety", "🆘 안전·비상"),
    ],
    "related": [
      ("../travel-sim/", "유심 vs 로밍 비교"),
      ("../travel-wifi-security/", "해외 인터넷 보안"),
      ("../travel-theft/", "도난·분실 신고"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
    ]
  },
  {
    "slug": "travel-wifi-security",
    "title": "해외에서 안전하게 인터넷 사용하는 법",
    "description": "해외 공공 Wi-Fi 위험성과 안전한 인터넷 사용법. VPN, HTTPS, 개인정보 보호 실전 가이드.",
    "og_image": "https://images.pexels.com/photos/607812/pexels-photo-607812.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "카페·공항·호텔 무료 Wi-Fi는 편리하지만 해킹·개인정보 도용의 위험이 있습니다. 안전하게 인터넷을 사용하는 방법을 알아보세요.",
    "body": """    <h2 id="risks">⚠️ 공공 Wi-Fi의 위험</h2>
    <ul>
      <li>🕵️ <strong>중간자 공격(MITM)</strong> — 해커가 Wi-Fi 트래픽 가로채기</li>
      <li>📶 <strong>가짜 핫스팟</strong> — 정상 Wi-Fi처럼 위장한 해커 AP</li>
      <li>🔓 <strong>암호화 없는 연결</strong> — HTTP 사이트 데이터 평문 노출</li>
      <li>🦠 <strong>악성코드 배포</strong> — 공유기 감염으로 기기에 악성코드 설치</li>
    </ul>
    <h2 id="vpn">🔐 VPN 사용법</h2>
    <p>VPN(Virtual Private Network)은 모든 인터넷 트래픽을 암호화하여 공공 Wi-Fi에서도 안전하게 사용할 수 있게 해줍니다.</p>
    <table class="compare-table">
      <tr><th>VPN 서비스</th><th>가격/월</th><th>특징</th><th>추천도</th></tr>
      <tr><td>NordVPN</td><td>약 $5</td><td>속도 빠름, 서버 5,500+</td><td>★★★★★</td></tr>
      <tr><td>ExpressVPN</td><td>약 $8</td><td>안정성 최고, 직관적 UI</td><td>★★★★★</td></tr>
      <tr><td>Surfshark</td><td>약 $3</td><td>가성비, 무제한 기기</td><td>★★★★</td></tr>
      <tr><td>ProtonVPN</td><td>무료~$10</td><td>무료 플랜 있음, 보안 강점</td><td>★★★★</td></tr>
    </table>
    <div class="tip-box">
      <ul>
        <li>✅ VPN은 출발 전 한국에서 미리 설치·결제 (일부 국가는 VPN 차단)</li>
        <li>✅ 중국 여행 시 VPN 필수 (구글·유튜브·카카오 차단)</li>
        <li>✅ 금융 거래는 반드시 VPN + 개인 데이터(유심) 사용</li>
      </ul>
    </div>
    <h2 id="https">🔒 HTTPS & 브라우저 보안</h2>
    <ul>
      <li>🔒 <strong>자물쇠 아이콘 확인</strong> — HTTPS 사이트만 이용 (HTTP 절대 금지)</li>
      <li>🧩 <strong>HTTPS Everywhere 확장</strong> — 자동으로 HTTPS 버전으로 연결</li>
      <li>🕶️ <strong>프라이빗 모드 사용</strong> — 쿠키·히스토리 자동 삭제</li>
      <li>🔑 <strong>2단계 인증 설정</strong> — 구글·카카오·은행 앱 모두 2FA 활성화</li>
    </ul>
    <h2 id="checklist">✅ 출발 전 보안 체크리스트</h2>
    <ul>
      <li>📱 스마트폰 OS·앱 최신 업데이트</li>
      <li>🔐 VPN 앱 설치 및 테스트</li>
      <li>💳 카드사에 해외 사용 알림 설정</li>
      <li>🔑 중요 계정 2FA 활성화</li>
      <li>💾 여권·중요 서류 클라우드 백업</li>
      <li>📞 비상 연락처 저장 (해외 분실 시 카드 차단 번호)</li>
    </ul>""",
    "toc": [
      ("risks", "⚠️ 공공 Wi-Fi 위험"),
      ("vpn", "🔐 VPN 사용법"),
      ("https", "🔒 HTTPS 보안"),
      ("checklist", "✅ 보안 체크리스트"),
    ],
    "related": [
      ("../travel-sim/", "유심 vs 로밍 비교"),
      ("../travel-apps/", "해외여행 필수 앱"),
      ("../travel-theft/", "도난·분실 신고"),
      ("../travel-insurance/", "해외여행 보험 가이드"),
    ]
  },
  {
    "slug": "travel-visa",
    "title": "나라별 비자 완전 가이드 (한국 여권 기준)",
    "description": "한국 여권으로 무비자 방문 가능한 나라, 비자 필요 국가, 비자 신청 방법 총정리 2026년 기준.",
    "og_image": "https://images.pexels.com/photos/1591056/pexels-photo-1591056.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "intro": "한국 여권은 세계 최강 여권 중 하나로, 190개 이상의 국가를 무비자 또는 도착비자로 방문할 수 있습니다. 목적지별 비자 규정을 미리 확인해 두세요.",
    "body": """    <h2 id="power">💪 한국 여권 파워 (2026년 기준)</h2>
    <p>한국 여권(대한민국 여권)은 헨리 여권 지수 기준 세계 2~3위권으로, 무비자 접근 가능 국가가 190개 이상입니다.</p>
    <div class="info-box">
      <strong>ℹ️ 한국 여권 요약</strong><br>
      <ul style="margin:8px 0 0;padding-left:18px;font-size:.88rem;line-height:2">
        <li>무비자/도착비자 국가: 190개+ (2026년 기준)</li>
        <li>헨리 여권 지수: 세계 2~3위권</li>
        <li>여권 유효기간: 성인 10년, 미성년 5년</li>
        <li>잔여 유효기간: 입국일 기준 최소 6개월 이상 필수</li>
      </ul>
    </div>
    <h2 id="visa-free">✅ 주요 무비자 입국 국가</h2>
    <table class="compare-table">
      <tr><th>지역</th><th>국가</th><th>무비자 체류기간</th></tr>
      <tr><td>미주</td><td>미국 (ESTA 필요)</td><td>90일</td></tr>
      <tr><td>미주</td><td>캐나다 (eTA 필요)</td><td>180일</td></tr>
      <tr><td>유럽</td><td>솅겐 26개국</td><td>90일 (180일 중)</td></tr>
      <tr><td>아시아</td><td>일본</td><td>90일</td></tr>
      <tr><td>아시아</td><td>싱가포르</td><td>30일</td></tr>
      <tr><td>아시아</td><td>태국</td><td>30일</td></tr>
      <tr><td>중동</td><td>UAE</td><td>30일</td></tr>
      <tr><td>오세아니아</td><td>호주 (ETA 필요)</td><td>90일</td></tr>
    </table>
    <h2 id="required">📋 비자 필요 주요 국가</h2>
    <table class="compare-table">
      <tr><th>국가</th><th>비자 종류</th><th>신청 방법</th><th>처리 기간</th></tr>
      <tr><td>🇨🇳 중국</td><td>관광비자 (L)</td><td>대사관 방문</td><td>4~7일</td></tr>
      <tr><td>🇮🇳 인도</td><td>e-Visa</td><td>온라인 신청</td><td>3~5일</td></tr>
      <tr><td>🇷🇺 러시아</td><td>관광비자</td><td>대사관 방문</td><td>7~14일</td></tr>
      <tr><td>🇧🇷 브라질</td><td>e-Visa</td><td>온라인 신청</td><td>5~10일</td></tr>
      <tr><td>🇳🇬 나이지리아</td><td>관광비자</td><td>대사관 방문</td><td>14일+</td></tr>
    </table>
    <h2 id="tips">💡 비자 신청 주의사항</h2>
    <ul>
      <li>⏰ <strong>충분한 여유</strong> — 비자 발급에 최소 2~4주 여유를 두고 신청</li>
      <li>📸 <strong>사진 규격</strong> — 나라마다 사진 크기·배경색 다름 (미리 확인)</li>
      <li>💰 <strong>비자 수수료</strong> — 비자 종류·국적에 따라 다름 ($20~200)</li>
      <li>📋 <strong>서류 준비</strong> — 여권 사본·항공권·숙박 예약 확인서 필수</li>
      <li>🔍 <strong>공식 사이트 확인</strong> — 비자 대행 사이트 수수료 과다 청구 주의</li>
    </ul>""",
    "toc": [
      ("power", "💪 한국 여권 파워"),
      ("visa-free", "✅ 무비자 입국 국가"),
      ("required", "📋 비자 필요 국가"),
      ("tips", "💡 비자 신청 주의"),
    ],
    "related": [