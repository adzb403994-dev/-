# -*- coding: utf-8 -*-
"""Build a rich 16:9 HTML deck for the 7-section roadshow, then render to PDF/PNG/PPTX.
Design reference: user's 31-slide defense deck (full-bleed section dividers, dense two-column content).
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = r'D:\DeepSeek\ppt_champion\05_output\deck_html'
os.makedirs(OUT, exist_ok=True)
A = 'file:///D:/DeepSeek/ppt_champion/deck_assets/'

CSS = r"""
:root{
  --cream:#F5EFE6; --paper:#FBF8F1; --green:#203B38; --green2:#2F4F4F;
  --ochre:#A45E3A; --rust:#A34A3F; --gold:#B08D57; --ink:#211F1B;
  --muted:#6D6559; --line:#D8CCBA; --teal:#3E6B66; --pale:#E9DFD0;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff;color:var(--ink);font-family:'Noto Sans SC','Microsoft YaHei',sans-serif;-webkit-font-smoothing:antialiased}
@page{size:1920px 1080px;margin:0}
.slide{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--cream);page-break-after:always;break-after:page}
.slide:last-child{page-break-after:auto;break-after:auto}
img{display:block}
.serif{font-family:'Noto Serif SC','Songti SC',serif}
.kicker{font-size:20px;letter-spacing:4px;color:var(--gold);font-weight:600}
.source{position:absolute;left:100px;bottom:40px;font-size:14px;color:var(--muted);letter-spacing:.5px}
.pageno{position:absolute;right:100px;bottom:38px;font-size:15px;color:var(--gold);letter-spacing:2px}
.rule{width:96px;height:4px;background:var(--ochre);margin:28px 0 32px}
/* cover */
.cover{position:absolute;inset:0;background:#13211F}
.cover .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cover .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(12,22,21,.93) 0%,rgba(12,22,21,.72) 44%,rgba(12,22,21,.18) 100%)}
.cover .top{position:absolute;left:100px;top:64px;color:#D9C39A;font-size:19px;letter-spacing:3px}
.cover .main{position:absolute;left:100px;top:238px;width:1080px}
.cover h1{font-family:'Noto Serif SC',serif;color:#FAF7F0;font-size:100px;line-height:1.16;font-weight:700;letter-spacing:2px}
.cover .sub{font-family:'Noto Serif SC',serif;color:#E9DFD0;font-size:36px;margin-top:30px;letter-spacing:2px}
.cover .three{display:flex;gap:24px;margin-top:52px}
.cover .three div{border-left:3px solid var(--gold);padding-left:18px}
.cover .three b{display:block;font-family:'Noto Serif SC',serif;font-size:42px;color:#FAF7F0;font-weight:700}
.cover .three span{display:block;font-size:17px;color:#CFC4B2;margin-top:8px;letter-spacing:1px}
.cover .team{position:absolute;left:100px;bottom:58px;color:#CFC4B2;font-size:18px;letter-spacing:1px}
/* contents */
.contents{padding:82px 100px 0}
.contents h2{font-family:'Noto Serif SC',serif;font-size:76px;color:var(--green);font-weight:700}
.contents .en{font-size:18px;letter-spacing:6px;color:var(--gold);margin-top:12px}
.contents .grid{display:grid;grid-template-columns:1fr 1fr;gap:0 74px;margin-top:54px}
.contents .item{display:flex;gap:26px;align-items:flex-start;padding:25px 0;border-top:1px solid var(--line)}
.contents .num{font-family:'Noto Serif SC',serif;font-size:50px;color:var(--pale);font-weight:700;line-height:1;min-width:74px}
.contents .t{font-family:'Noto Serif SC',serif;font-size:34px;color:var(--green);font-weight:700}
.contents .d{font-size:17px;color:var(--muted);margin-top:8px;line-height:1.45}
.contents .side{position:absolute;right:0;top:0;width:430px;height:1080px}
.contents .side img{width:100%;height:100%;object-fit:cover;opacity:.92}
.contents .side:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--cream),transparent 38%)}
.contents .toc-quote{position:absolute;left:100px;bottom:58px;font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ochre);letter-spacing:1px}
.contents .toc-quote span{display:block;font-family:'Noto Sans SC',sans-serif;font-size:14px;color:var(--muted);letter-spacing:1px;margin-top:6px}
/* divider */
.divider{position:absolute;inset:0;background:var(--green)}
.divider .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.86}
.divider .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,32,30,.96) 0%,rgba(18,32,30,.82) 46%,rgba(18,32,30,.18) 100%)}
.divider .num{position:absolute;left:82px;top:128px;font-family:'Noto Serif SC',serif;font-size:420px;line-height:.8;color:rgba(233,223,208,.16);font-weight:700}
.divider .txt{position:absolute;left:100px;top:372px;width:930px}
.divider .k{color:#D9C39A;font-size:18px;letter-spacing:5px}
.divider h2{font-family:'Noto Serif SC',serif;font-size:78px;color:#FAF7F0;line-height:1.22;margin-top:22px;font-weight:700}
.divider .sub{font-family:'Noto Serif SC',serif;font-size:30px;color:#E9DFD0;margin-top:22px;line-height:1.5}
.divider .bottom{position:absolute;left:100px;bottom:54px;color:#CFC4B2;font-size:17px;letter-spacing:2px}
.divider .chapter{position:absolute;right:100px;bottom:54px;color:#D9C39A;font-size:17px;letter-spacing:2px}
/* content */
.content{position:absolute;inset:0;padding:64px 100px 0}
.content .top{display:flex;justify-content:space-between;align-items:center}
.content .tag{font-size:17px;letter-spacing:3px;color:var(--gold);font-weight:600}
.content .sec{font-size:16px;letter-spacing:2px;color:var(--muted)}
.content h2{font-family:'Noto Serif SC',serif;font-size:58px;line-height:1.24;color:var(--green);font-weight:700;margin-top:22px;max-width:1650px}
.content .lead{font-size:22px;line-height:1.55;color:var(--muted);margin-top:16px;max-width:1560px}
.content .body{position:absolute;left:100px;right:100px;top:300px;bottom:92px}
.note{font-size:15px;color:var(--muted);line-height:1.6}
.small{font-size:16px;line-height:1.65;color:var(--muted)}
.phase-list{margin:18px 0 0 18px;color:inherit;font-size:14px;line-height:1.8;opacity:.9}
.phase-list li{margin-bottom:4px}
.statrow{display:flex;gap:28px;margin-top:30px}
.statrow div{border-left:2px solid var(--gold);padding-left:14px}
.statrow b{display:block;font-family:'Noto Serif SC',serif;font-size:38px;line-height:1}
.statrow span{display:block;font-size:13px;color:inherit;opacity:.8;margin-top:4px}
.panel.green .statrow span{color:#D8D0C2;opacity:1}
.panel.rust .statrow span{color:#6D3B33;opacity:1}
.strip3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px}
.strip3 .ph{position:relative;height:150px;overflow:hidden}
.strip3 .ph img{width:100%;height:100%;object-fit:cover}
.strip3 .ph span{position:absolute;left:14px;bottom:10px;color:#FAF7F0;font-size:14px;letter-spacing:1px;text-shadow:0 1px 5px rgba(0,0,0,.55)}
/* generic panels */
.panel{background:var(--paper);border:1px solid var(--line);padding:30px 30px}
.panel h3{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--green);font-weight:700}
.panel p{font-size:17px;line-height:1.7;color:var(--muted);margin-top:12px}
.panel .num{font-family:'Noto Serif SC',serif;font-size:54px;color:var(--ochre);font-weight:700;line-height:1}
.panel.green{background:var(--green);border-color:var(--green)}
.panel.green h3,.panel.green .num{color:#FAF7F0}
.panel.green p,.panel.green li{color:#D8D0C2}
.panel.ochre{background:#F1E2D4;border-color:#E3C9B4}
.panel.rust{background:#F3E2DE;border-color:#E4C5BE}
.panel.teal{background:#E3ECE8;border-color:#C7DAD3}
.card{background:var(--paper);border:1px solid var(--line);padding:26px 24px}
.card .n{font-family:'Noto Serif SC',serif;font-size:24px;color:var(--gold);letter-spacing:2px}
.card h3{font-family:'Noto Serif SC',serif;font-size:27px;color:var(--green);margin-top:10px;font-weight:700}
.card p{font-size:16px;line-height:1.65;color:var(--muted);margin-top:10px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.metrics{display:flex;gap:0}
.metrics .m{flex:1;border-left:1px solid var(--line);padding:2px 28px}
.metrics .m:first-child{border-left:0;padding-left:0}
.metrics b{display:block;font-family:'Noto Serif SC',serif;font-size:64px;color:var(--ochre);line-height:1;font-weight:700}
.metrics span{display:block;font-size:16px;color:var(--muted);margin-top:10px}
.bar{height:26px;background:var(--green);position:relative;margin-top:12px}
.bar i{position:absolute;right:0;top:0;bottom:0;width:8%;background:var(--ochre)}
.barbox{font-size:16px;color:var(--muted);display:flex;justify-content:space-between;margin-top:8px}
/* image layouts */
.imgframe{position:relative;overflow:hidden;background:#E7DDCE}
.imgframe img{width:100%;height:100%;object-fit:cover}
.imgframe .cap{position:absolute;left:22px;bottom:18px;color:#FAF7F0;font-size:15px;letter-spacing:1px;text-shadow:0 1px 6px rgba(0,0,0,.4)}
.figure{width:100%;background:#FBF8F1;border:1px solid var(--line)}
.figure img{width:100%;height:auto;display:block}
/* special */
.problem-left{width:690px}
.problem-left .lead2{font-size:22px;line-height:1.6;color:var(--muted);margin-top:20px;max-width:650px}
.problem-right{position:absolute;right:0;top:0;width:960px}
.pain{display:flex;gap:18px;padding:16px 0;border-top:1px solid var(--line)}
.pain b{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--ochre);min-width:48px}
.pain h4{font-size:21px;color:var(--green);font-weight:700}
.pain p{font-size:15px;color:var(--muted);line-height:1.6;margin-top:5px}
.modelformula{display:flex;gap:12px;align-items:stretch;margin-top:20px}
.modelformula .b{flex:1;background:var(--green);padding:22px 18px;color:#FAF7F0}
.modelformula .b.alt{background:var(--ochre)}
.modelformula .b.alt2{background:var(--teal)}
.modelformula .b .n{font-size:14px;letter-spacing:2px;color:#D9C39A}
.modelformula .b h4{font-family:'Noto Serif SC',serif;font-size:24px;margin-top:8px}
.modelformula .b p{font-size:14px;line-height:1.5;color:#EDE5D8;margin-top:8px}
.modelformula .eq{align-self:center;font-size:36px;color:var(--gold);padding:0 2px}
.fitrow{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:24px}
.fitrow .f{border-top:4px solid var(--ochre);background:var(--paper);padding:20px 22px}
.fitrow .f:nth-child(2){border-color:var(--green)}
.fitrow .f:nth-child(3){border-color:var(--teal)}
.fitrow h4{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--green)}
.fitrow p{font-size:15px;line-height:1.65;color:var(--muted);margin-top:8px}
/* resource */
.res-left{width:520px}
.res-left .stats{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}
.res-left .stat{background:var(--paper);border:1px solid var(--line);padding:18px}
.res-left .stat b{display:block;font-family:'Noto Serif SC',serif;font-size:46px;color:var(--ochre);line-height:1}
.res-left .stat span{display:block;font-size:14px;color:var(--muted);margin-top:6px}
.res-right{position:absolute;right:0;top:0;width:1190px}
.res-right img{width:100%;border:1px solid var(--line)}
/* swot */
.swot{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:18px;height:540px}
.swot .q{padding:24px 28px;position:relative}
.swot .q h3{font-family:'Noto Serif SC',serif;font-size:30px;margin-bottom:10px}
.swot .q p{font-size:16px;line-height:1.7}
.swot .s{background:#E3ECE8;border-left:6px solid var(--teal)}
.swot .w{background:#F3E2DE;border-left:6px solid var(--rust)}
.swot .o{background:#F1E2D4;border-left:6px solid var(--ochre)}
.swot .t{background:#E8E4DA;border-left:6px solid #7B7467}
.swot .s h3,.swot .w h3,.swot .o h3,.swot .t h3{color:var(--green)}
/* concept cards */
.concept{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.concept .c{padding:28px 24px;min-height:510px;display:flex;flex-direction:column}
.concept .c:nth-child(1){background:var(--green);color:#FAF7F0}
.concept .c:nth-child(2){background:#EEE4D5}
.concept .c:nth-child(3){background:#E3ECE8}
.concept .c:nth-child(4){background:#F1E2D4}
.concept .c .n{font-family:'Noto Serif SC',serif;font-size:52px;color:var(--gold);line-height:1}
.concept .c h3{font-family:'Noto Serif SC',serif;font-size:30px;margin-top:26px;color:inherit}
.concept .c p{font-size:16px;line-height:1.7;margin-top:14px;color:inherit;opacity:.86}
.concept .c .quote{margin-top:auto;font-size:14px;line-height:1.6;opacity:.78}
/* space */
.space-wrap{display:flex;gap:34px}
.space-left{width:520px}
.space-right{flex:1}
.space-left .redline{display:flex;gap:16px;padding:16px 0;border-top:1px solid var(--line)}
.space-left .redline b{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--ochre);min-width:70px}
.space-left .redline h4{font-size:20px;color:var(--green)}
.space-left .redline p{font-size:14px;line-height:1.55;color:var(--muted);margin-top:4px}
.space-right img{width:100%;border:1px solid var(--line)}
/* product matrix */
.products{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.prod{background:var(--paper);border:1px solid var(--line);padding:20px 16px;min-height:280px}
.prod .tag{font-size:12px;letter-spacing:1px;color:var(--gold)}
.prod h4{font-family:'Noto Serif SC',serif;font-size:20px;color:var(--green);margin-top:8px}
.prod p{font-size:13px;line-height:1.55;color:var(--muted);margin-top:8px}
.prod b{display:block;font-family:'Noto Serif SC',serif;font-size:23px;color:var(--ochre);margin-top:12px}
/* tables */
.table{width:100%;border-collapse:collapse;font-size:16px}
.table th{background:var(--green);color:#FAF7F0;text-align:left;padding:12px 14px;font-weight:600;font-size:15px}
.table td{border-bottom:1px solid var(--line);padding:12px 14px;color:var(--muted);vertical-align:top}
.table td b{color:var(--ink)}
/* market bars */
.mbar{display:flex;flex-direction:column;gap:16px}
.mbar .row{display:grid;grid-template-columns:180px 1fr 110px;gap:16px;align-items:center}
.mbar .lab{font-size:16px;color:var(--green);font-weight:600}
.mbar .track{height:18px;background:#E6DCCD;position:relative}
.mbar .fill{height:100%;background:var(--ochre)}
.mbar .val{font-size:15px;color:var(--muted);text-align:right}
/* gantt */
.gantt{width:100%;border-collapse:collapse;font-size:15px}
.gantt th{color:var(--muted);font-weight:500;padding:8px 6px;border-bottom:1px solid var(--line);font-size:13px}
.gantt td{padding:10px 6px;border-bottom:1px solid #E9E1D4;color:var(--muted)}
.gantt .bar-cell{position:relative;height:22px}
.gantt .bar{height:18px;background:var(--green)}
.gantt .bar.o{background:var(--ochre)}.gantt .bar.t{background:var(--teal)}
/* timeline */
.timeline{position:relative;margin-top:8px}
.timeline .axis{display:grid;grid-template-columns:180px 1fr;gap:18px;font-size:12px;color:var(--muted);letter-spacing:1px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.timeline .axis .ticks{display:flex;justify-content:space-between;padding:0 8px}
.timeline .row{display:grid;grid-template-columns:180px 1fr;gap:18px;padding:16px 0;border-bottom:1px solid #E9E1D4;align-items:start}
.timeline .head{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--green);line-height:1.4;padding-top:2px}
.timeline .head small{display:block;font-family:'Noto Sans SC',sans-serif;font-size:13px;color:var(--gold);font-weight:400;margin-top:4px}
.timeline .track{position:relative;height:30px;background:#E9DFD0;margin-top:2px}
.timeline .track .fill{position:absolute;top:0;bottom:0;background:var(--green);display:flex;align-items:center;padding-left:14px;color:#FAF7F0;font-size:12px;letter-spacing:1px}
.timeline .track .fill.o{background:var(--ochre)} .timeline .track .fill.t{background:var(--teal)}
.timeline .deliv{font-size:13px;color:var(--muted);line-height:1.5;margin-top:8px}
.quote-line{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--ochre);letter-spacing:1px;margin-top:24px}
/* risk */
.risk-grid{display:grid;grid-template-columns:540px 1fr;gap:38px}
.matrix{position:relative;height:490px;background:#F1E9DC;border:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr}
.matrix .q{position:relative;padding:18px;border-right:1px solid rgba(33,31,27,.13);border-bottom:1px solid rgba(33,31,27,.13)}
.matrix .q:nth-child(2n){border-right:0}
.matrix .q:nth-child(n+3){border-bottom:0}
.matrix .q1{background:#F3E2DE}.matrix .q2{background:#F1E2D4}.matrix .q3{background:#E3ECE8}.matrix .q4{background:#E8E4DA}
.matrix .q span{font-size:12px;letter-spacing:1px;color:var(--muted)}
.matrix .q b{display:block;font-family:'Noto Serif SC',serif;font-size:15px;color:var(--green);margin-top:2px}
.axis-note{font-size:13px;color:var(--muted);letter-spacing:1px;margin-top:10px}
.matrix .axis-x,.matrix .axis-y{position:absolute;font-size:13px;color:var(--muted);background:rgba(245,239,230,.85);padding:2px 6px}
.matrix .axis-x{right:18px;bottom:10px}.matrix .axis-y{left:10px;top:8px}
.matrix .dot{position:absolute;width:18px;height:18px;border-radius:50%;background:var(--rust);border:4px solid #F7F1E7;box-shadow:0 0 0 1px var(--rust)}
.matrix .dot.g{background:var(--green);box-shadow:0 0 0 1px var(--green)}
.matrix .dot.o{background:var(--ochre);box-shadow:0 0 0 1px var(--ochre)}
.matrix .lab{position:absolute;font-size:14px;color:var(--ink);font-weight:600}
.risk-list{display:flex;flex-direction:column;gap:0}
.risk-list .r{border-top:1px solid var(--line);padding:16px 0;display:grid;grid-template-columns:160px 1fr;gap:16px}
.risk-list .r h4{font-family:'Noto Serif SC',serif;font-size:20px;color:var(--green)}
.risk-list .r p{font-size:14px;line-height:1.6;color:var(--muted)}
.risk-list .r .tag{font-size:12px;color:var(--ochre);letter-spacing:1px}
/* conclusion */
.closing{position:absolute;inset:0;background:var(--green)}
.closing .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.62}
.closing .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(16,29,27,.95),rgba(16,29,27,.6))}
.closing .inner{position:absolute;left:100px;top:120px;width:1280px}
.closing .k{font-size:18px;letter-spacing:4px;color:#D9C39A}
.closing h2{font-family:'Noto Serif SC',serif;font-size:64px;line-height:1.35;color:#FAF7F0;margin-top:22px}
.closing h2 em{font-style:normal;color:#E0BE93}
.closing .three{display:flex;gap:18px;margin-top:40px}
.closing .three div{background:rgba(250,247,240,.08);border:1px solid rgba(217,195,154,.35);padding:20px 22px;flex:1}
.closing .three b{display:block;font-family:'Noto Serif SC',serif;font-size:20px;color:#E9DFD0}
.closing .three span{display:block;font-size:14px;color:#CFC4B2;line-height:1.5;margin-top:6px}
.closing .claim{position:absolute;left:100px;bottom:56px;color:#FAF7F0;font-family:'Noto Serif SC',serif;font-size:27px;letter-spacing:1px}
.thanks{position:absolute;inset:0;background:var(--green)}
.thanks .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.3}
.thanks .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,32,30,.9),rgba(18,32,30,.72))}
.thanks .inner{position:absolute;left:100px;top:240px}
.thanks .en{color:#D9C39A;font-size:20px;letter-spacing:6px}
.thanks h2{font-family:'Noto Serif SC',serif;font-size:94px;color:#FAF7F0;margin-top:18px}
.thanks p{font-size:23px;color:#E9DFD0;line-height:1.8;margin-top:26px}
.thanks .meta{position:absolute;left:100px;bottom:70px;color:#CFC4B2;font-size:16px;letter-spacing:1px}
"""


def slide(content, cls='', page=0):
    pn = f'<div class="pageno">{page:02d}</div>' if page else ''
    return f'<section class="slide {cls}">{content}{pn}</section>'


def header(tag, title, lead=''):
    lead_html = f'<div class="lead">{lead}</div>' if lead else ''
    return f'''<div class="content"><div class="top"><div class="tag">{tag}</div><div class="sec">七部分 · 逐一作答</div></div>
    <h2 class="serif">{title}</h2>{lead_html}<div class="body">'''


def end_content(source=''):
    src = f'<div class="source">{source}</div>' if source else ''
    return f'</div>{src}</div>'


def divider(num, title, sub, img, page, extra=''):
    return f'''<div class="divider"><img class="bg" src="{A}{img}" alt=""><div class="shade"></div>
    <div class="num serif">{num}</div><div class="txt"><div class="k">PART {num} / 07</div>
    <h2 class="serif">{title}</h2><div class="sub serif">{sub}</div></div>
    <div class="bottom">数字守楼人 · 活态客家魂</div><div class="chapter">{num} / 07 · {extra}</div></div>'''


slides = []

# 01 cover
slides.append(slide(f'''<div class="cover"><img class="bg" src="{A}summer.jpg" alt=""><div class="shade"></div>
<div class="top">2026 全国大学生文化旅游与会展竞赛 · 旅游新业态策划组</div>
<div class="main"><h1>数字守楼人<br>活态客家魂</h1><div class="sub">把体验请出土楼，把收益留给村民。</div>
<div class="three"><div><b>4170 万</b><span>四主体总投资</span></div><div><b>30 万人次</b><span>成熟期年客流</span></div><div><b>1421 万</b><span>T2.1 成熟期营收</span></div></div></div>
<div class="team">福建龙岩湖坑镇十里南溪文旅新业态策划方案　｜　安志逸 · 林雨嫣 · 刘璇 · 刘彧安</div></div>''', 'cover-page', 0))

# 02 contents
slides.append(slide(f'''<div class="contents"><div class="kicker">CONTENTS</div><h2 class="serif">七个部分，一条逻辑</h2><div class="en">FROM PROTECTION TO PRODUCT, FROM PRODUCT TO BENEFIT</div>
<div class="grid">
<div class="item"><div class="num">01</div><div><div class="t">旅游新业态模式解读</div><div class="d">传统观光为什么走不通，数字共益型遗产旅游是什么</div></div></div>
<div class="item"><div class="num">02</div><div><div class="t">旅游目的地概述</div><div class="d">2 座世遗本体、112 户原住民、南溪的存量与短板</div></div></div>
<div class="item"><div class="num">03</div><div><div class="t">策划理念与定位</div><div class="d">活态传承、自主选择、沉浸共生、数字示范</div></div></div>
<div class="item"><div class="num">04</div><div><div class="t">产品与服务设计</div><div class="d">一条溪、一个旗舰、五类产品、三条线路</div></div></div>
<div class="item"><div class="num">05</div><div><div class="t">市场分析与营销策略</div><div class="d">1120 万客流的 8%，三阶段营销与私域</div></div></div>
<div class="item"><div class="num">06</div><div><div class="t">实施计划与预期效益</div><div class="d">三期、4170 万、T2.1 账本、8% 门槛</div></div></div>
<div class="item"><div class="num">07</div><div><div class="t">风险评估与应对策略</div><div class="d">政策、市场、运营、财务四类风险与止损线</div></div></div>
</div><div class="toc-quote">“楼外看楼，楼里受益。”<span>七个部分，回答一个问题：怎样让保护与收益同时发生。</span></div><div class="side"><img src="{A}night.jpg" alt=""></div></div>''', 'contents-page', 2))

# 03 divider 01
slides.append(slide(divider('01', '旅游新业态模式解读', '数字世遗保护 ＋ 原住民活态传承<br>从“门票经济”转向“体验经济”', 'wall.jpg', 3, '模式'), '', 3))

# 04 problem
slides.append(slide(header('01 / 模式解读', '92% 的客流在东线，南溪只分到 8%', '不是资源不足，是承载错位：体验压在本体上，收益留在外部。') + f'''
<div class="problem-left"><div class="metrics" style="margin-top:8px"><div class="m"><b style="font-size:130px">92%</b><span>客流集中在东线高北、洪坑</span></div><div class="m"><b style="font-size:130px;color:var(--ochre)">8%</b><span>南溪只承接约 8%</span></div></div>
<div class="bar"><i></i></div><div class="barbox"><span>东线 92%</span><span>南溪 8%</span></div>
<div class="metrics" style="margin-top:42px"><div class="m"><b>1.5 小时</b><span>现状平均停留</span></div><div class="m"><b>98 元</b><span>现状客单</span></div></div>
<div class="lead2">永定一年 1120 万人次、125 亿元总花费；南溪不是没有资源，是没有把“停留”和“消费”留在村里。</div></div>
<div class="problem-right">
<div class="pain"><b>01</b><div><h4>走马观花</h4><p>看楼 20 分钟、拍照 10 分钟，游客留不下、也花不出。</p></div></div>
<div class="pain"><b>02</b><div><h4>原住民外迁</h4><p>楼在人走，生活场景消失，土楼变成“空壳展品”。</p></div></div>
<div class="pain"><b>03</b><div><h4>本体承载过重</h4><p>体验、餐饮、停车都往楼边挤，保护压力越来越大。</p></div></div>
<div class="pain"><b>04</b><div><h4>产品同质化</h4><p>看楼＋拍照＋特产，客单 98 元，复购和过夜都起不来。</p></div></div>
<div class="panel green" style="margin-top:18px"><h3>所以，第一件事不是“再建一个景区”</h3><p>而是把体验移出本体、把收益留在村里。</p></div></div>''' + end_content('来源：永定区 2026 年政府工作报告；8%/1.5h/98 元为团队调研估算'), '', 4))

# 05 model
slides.append(slide(header('01 / 模式解读', '数字共益型遗产旅游：四件事装进一个机制', '数字是保护手段，原住民是主体，共益是治理，沉浸是产品。') + f'''
<div class="modelformula"><div class="b"><div class="n">01 / 数字外移</div><h4>体验出楼</h4><p>62 米外做数字体验；本体不安排经营。</p></div><div class="eq">＋</div>
<div class="b alt"><div class="n">02 / 原住民共治</div><h4>112 户留下</h4><p>村民是经营主体，也是决策主体。</p></div><div class="eq">＋</div>
<div class="b alt2"><div class="n">03 / 共益分配</div><h4>三层分账</h4><p>保底 → 分成 → 共益，8% 是分红门槛。</p></div><div class="eq">＋</div>
<div class="b"><div class="n">04 / 沉浸体验</div><h4>20 分钟</h4><p>看楼、懂楼、建楼、守楼。</p></div></div>
<div class="fitrow">
<div class="f"><h4>资源匹配</h4><p>2 座世遗本体楼、1 处省保、3 个中国传统村落、112 户原住民；世遗本体＋活态生活同时成立。</p></div>
<div class="f"><h4>市场匹配</h4><p>1120 万区域客流、92% 在东线；南溪不需要从零造客流，先承接 5%—8% 的溢出。</p></div>
<div class="f"><h4>政策匹配</h4><p>数字文旅、乡村振兴、世遗保护三条政策线交汇；以保护规划批复为前置条件。</p></div></div>
<div class="panel ochre" style="margin-top:24px"><h3>一句话定义</h3><p>用数字技术把体验移出本体，用原住民共治把生活留在楼里，用共益分配把收益留在村里。</p></div>''' + end_content('来源：v4.0 A/B/C 内容稿；T2.1 财务口径'), '', 5))

# 06 divider 02
slides.append(slide(divider('02', '旅游目的地概述', '2 座世遗本体楼 ＋ 112 户原住民<br>一条溪串起四片区，存量就在那里', 'summer.jpg', 6, '目的地'), '', 6))

# 07 resources
slides.append(slide(header('02 / 目的地', '南溪的资源，不是“又一片土楼”', '世遗本体、活态原住民、溪田竹系统，三者同时成立的地方不多。') + f'''
<div class="res-left"><div class="stats">
<div class="stat"><b>2</b><span>座世遗本体楼<br>衍香楼 · 振福楼</span></div>
<div class="stat"><b>1</b><span>处省级文保<br>环极楼</span></div>
<div class="stat"><b>3</b><span>个中国传统村落<br>南江 · 南中 · 新南</span></div>
<div class="stat"><b>112</b><span>户原住民<br>活态客家生活</span></div></div>
<div class="panel" style="margin-top:22px"><h3>四个片区，一条溪</h3><p>西片做服务与集散，南江做集散与夜游，南中做研学与梯田，新南做数字与建筑研学。</p></div></div>
<div class="res-right"><img src="{A}map.png" alt="区位资源地图"></div>''' + end_content('来源：v4.0 A《目的地概述》；图为关系示意，非导航/权属/行政边界图'), '', 7))

# 08 current + positioning
slides.append(slide(header('02 / 目的地', '基础已有，短板在“把资源变成产品”', '东线过载、南线闲置；南溪的定位不是替代东线，是承接与升级。') + f'''
<div class="grid2" style="height:430px">
<div class="panel green"><h3>已经有的</h3><p>环世遗土楼公路、南溪十里长廊、部分民宿与展馆、主要节点通信覆盖；世遗本体与村落格局完整。</p><p style="margin-top:22px;color:#E9DFD0">这些是“底子”，不是“产品”。</p><div class="statrow"><div><b>2</b><span>座世遗本体楼</span></div><div><b>112</b><span>户原住民</span></div></div></div>
<div class="panel rust"><h3>还不够的</h3><p>标识系统不统一、无障碍设施不足、夜间产品空白、数字体验缺失、专业运营人才缺乏；游客停留 1.5 小时、客单 98 元。</p><p style="margin-top:22px;color:#7A3B32">这些是“机会”，也是“门槛”。</p><div class="statrow"><div><b>1.5h</b><span>现状平均停留</span></div><div><b>98 元</b><span>现状客单</span></div></div></div></div>
<div class="panel ochre" style="margin-top:18px"><h3>定位：东线之外的“补充与升级”</h3><p>不争东线的第一站，做东线之后的第二晚；不拼客流规模，拼停留时长与客单结构。</p></div>''' + end_content('来源：v4.0 A 目的地概述；现状数据为团队调研估算'), '', 8))

# 09 SWOT
slides.append(slide(header('02 / 目的地', 'SWOT：把“保护约束”变成“差异化壁垒”', '优势在世遗本体与活态原住民；劣势在配套与运营；机会在分流与深度体验；威胁在审批与同质化。') + f'''
<div class="swot">
<div class="q s"><h3>S 优势</h3><p>2 座世遗本体楼＋1 处省保；112 户原住民常住；溪田竹生态完整；环世遗公路改善可达性。</p></div>
<div class="q w"><h3>W 劣势</h3><p>数字化程度低；标识、无障碍、夜间产品缺位；运营人才不足；现状停留 1.5 小时。</p></div>
<div class="q o"><h3>O 机会</h3><p>东线旺季过载，南溪可承接 5%—8% 溢出；短途、高频、过夜与深度体验增长；政策支持数字文旅与乡村振兴。</p></div>
<div class="q t"><h3>T 威胁</h3><p>世遗保护政策收紧、审批周期长；区域同质化竞争；旅游消费波动；村民预期管理难度。</p></div></div>
<div class="panel" style="margin-top:18px"><h3>策略：SO 打差异，WO 补配套，ST 守红线，WT 控节奏</h3><p>用“数字外移＋原住民共治”建立别人复制不了的壁垒；用分期与闸门控制投资节奏。</p></div>''' + end_content('来源：v4.0 A 目的地概述；SWOT 为团队分析'), '', 9))

# 10 divider 03
slides.append(slide(divider('03', '策划理念与定位', '不做土楼的过客，只做客家的归人<br>四大理念，四个标杆', 'people.jpg', 10, '理念'), '', 10))

# 11 concepts
slides.append(slide(header('03 / 理念', '四大理念：保护、生活、体验、分配，缺一不可', '不是四句口号，是四条会进入合同和考核的机制。') + f'''
<div class="concept">
<div class="c"><div class="n">01</div><h3>活态传承</h3><p>112 户原住民常住；非遗传承人常驻带徒；村民是经营主体，不是被展示的对象。</p><div class="quote">“楼里有人，文化才活着。”</div></div>
<div class="c"><div class="n">02</div><h3>自主选择</h3><p>数字产品模块化，线下业态可组合；游客自选一日、两日、三日，不把所有人塞进同一条线。</p><div class="quote">“把选择权还给游客。”</div></div>
<div class="c"><div class="n">03</div><h3>沉浸共生</h3><p>保护、体验、发展三方共生；用监测数据与共益账本，把“共生”变成可考核的指标。</p><div class="quote">“保护越好，体验越深。”</div></div>
<div class="c"><div class="n">04</div><h3>数字示范</h3><p>数字外移、本体零触碰；62 米外做体验；形成可复制的世遗数字管护标准。</p><div class="quote">“先守住，再谈创新。”</div></div></div>
<div class="panel green" style="margin-top:22px"><h3>理念落地：三张纸</h3><p>共益公约（村民）＋ 保护协议（文物部门）＋ 运营合同（公司/合作方）——每一条理念都有对应条款。</p></div>''' + end_content('来源：v4.0 B 第 3 章；共益机制见第 6 部分'), '', 11))

# 12 positioning/benchmarks
slides.append(slide(header('03 / 定位', '从“一个文旅项目”升级为“世遗活态传承示范”', '整体定位：世界遗产活态传承与乡村振兴共生示范项目。') + f'''
<div class="grid2" style="height:460px">
<div class="panel green"><div class="kicker" style="color:#D9C39A">POSITIONING</div><h3 style="font-size:40px;line-height:1.45;margin-top:18px">世界遗产活态传承<br>与乡村振兴共生示范</h3><p style="margin-top:20px">以数字守护世遗本体，以活态传承激活客家文化，以三方共建实现乡村振兴。</p></div>
<div class="grid2" style="gap:16px">
<div class="card"><div class="n">标杆 01</div><h3>数字世遗保护</h3><p>数字外移、本体零触碰；监测、档案、预警形成闭环。</p></div>
<div class="card"><div class="n">标杆 02</div><h3>活态传承</h3><p>112 户常住；非遗传承人常驻；生活场景就是产品。</p></div>
<div class="card"><div class="n">标杆 03</div><h3>乡村振兴</h3><p>保底＋分成＋共益；村民户均收益可核验。</p></div>
<div class="card"><div class="n">标杆 04</div><h3>全龄服务</h3><p>无障碍、亲子、银发、研学四类服务标准。</p></div></div></div>
<div class="panel ochre" style="margin-top:18px"><h3>一句话</h3><p>不是把南溪做成“第二个东线”，是把南溪做成“东线之后的那一晚”。</p></div>''' + end_content('来源：v4.0 B 第 3 章；定位与标杆为团队提炼'), '', 12))

# 13 divider 04
slides.append(slide(divider('04', '产品与服务设计', '一个旗舰、五类产品、三条线路<br>把 1.5 小时拉成 2—3 天', 'guesthouse.jpg', 13, '产品'), '', 13))

# 14 space
slides.append(slide(header('04 / 产品', '一溪两岸、三区多点；三条红线、三种动作', '先划清“不能做什么”，再谈“能做什么”。') + f'''
<div class="space-wrap"><div class="space-left">
<div class="redline"><b>5m</b><div><h4>本体保护范围</h4><p>本体＋5 米，不安排经营、不触摸、不改动；公益参观。</p></div></div>
<div class="redline"><b>15.2m</b><div><h4>光影最近距离</h4><p>低照度、不直射墙体；只做“照亮轮廓”，不做“照亮墙面”。</p></div></div>
<div class="redline"><b>62m</b><div><h4>数字体验外移</h4><p>建控地带以外、环境协调区内；游客服务中心与数字体验区。</p></div></div>
<div class="panel" style="margin-top:16px"><h3>一溪两岸 · 三区多点</h3><p>入口服务区、南江夜游区、南中研学区、新南数字区；用溪流串起来，不搞均匀铺开。</p></div></div>
<div class="space-right"><img src="{A}dist.png" alt="三个距离剖面"></div></div>''' + end_content('来源：v4.0 B 第 4 章；非等比剖面，以批准的保护规划为准'), '', 14))

# 15 products
slides.append(slide(header('04 / 产品', '一个旗舰、五类产品、三条线路', '旗舰负责“来”，五类产品负责“留”，三条线路负责“再来”。') + f'''
<div class="products">
<div class="prod"><div class="tag">FLAGSHIP</div><h4>数字孪生体验</h4><p>20 分钟四段：入楼、看楼、建楼、守楼。</p><b>68 元/人</b></div>
<div class="prod"><div class="tag">住</div><h4>主题民宿</h4><p>15 家存量民居改造；村民 65% / 公司 35%。</p><b>15 家</b></div>
<div class="prod"><div class="tag">食</div><h4>客家美食街</h4><p>本地食材、明档厨房；村民自营为主。</p><b>一条街</b></div>
<div class="prod"><div class="tag">学</div><h4>分龄研学</h4><p>小学 / 初中 / 高中三档课程；对接课标。</p><b>3 档</b></div>
<div class="prod"><div class="tag">野</div><h4>徒步与露营</h4><p>3km / 6km / 10km 三条线；星河露营地。</p><b>3 条线</b></div></div>
<div class="grid2" style="margin-top:22px"><div class="panel"><h3>三条线路</h3><p>一日精华：数字孪生 → 衍香楼 → 美食街 → 溪畔徒步。<br>两日深度：＋主题民宿、非遗工坊、守夜人。<br>三日研学：＋土楼测绘、夯土实验、共益调研。</p></div>
<div class="panel green"><h3>产品逻辑</h3><p>旗舰不靠“设备”赚钱，靠“内容”复购；民宿不靠“床位”赚钱，靠“村民经营”分成；线路不靠“门票”赚钱，靠“过夜与二消”。</p></div></div>
<div class="strip3"><div class="ph"><img src="{A}digital.jpg" alt=""><span>数字孪生体验</span></div><div class="ph"><img src="{A}guesthouse.jpg" alt=""><span>主题民宿</span></div><div class="ph"><img src="{A}camp.jpg" alt=""><span>星空露营</span></div></div>''' + end_content('来源：v4.0 B 第 4 章；价格与容量为测算值，以正式运营为准'), '', 15))

# 16 flagship detail
slides.append(slide(header('04 / 产品', '旗舰：20 分钟，把“看楼”变成“懂楼”', '68 元/人，日容量约 200 人；设备会旧，内容不会。') + f'''
<div style="display:flex;gap:26px;height:560px"><div class="imgframe" style="width:760px;height:560px"><img src="{A}digital.jpg" alt="数字孪生体验舱"><div class="cap">数字孪生体验舱 · 效果示意</div></div>
<div style="flex:1"><div class="grid2" style="gap:14px">
<div class="panel"><div class="num">3′</div><h3>入楼</h3><p>领身份卡，读保护规则；先建立“不能碰”的边界。</p></div>
<div class="panel"><div class="num">5′</div><h3>看楼</h3><p>AR 叠加真实与数字模型；看见墙体、梁架、排水。</p></div>
<div class="panel"><div class="num">7′</div><h3>建楼</h3><p>虚拟工坊完成夯土、架梁、铺瓦；理解“为什么这样建”。</p></div>
<div class="panel"><div class="num">5′</div><h3>守楼</h3><p>看监测数据，留下数字凭证；把游客变成“守楼人”。</p></div></div>
<div class="panel ochre" style="margin-top:14px"><h3>运营口径</h3><p>68 元/人 × 日容量约 200 人；每年更新 2—3 个场景或课程；设备折旧 5 年，内容更新单列。</p></div></div></div>''' + end_content('来源：v4.0 B 第 4 章；票价为测算值'), '', 16))

# 17 divider 05
slides.append(slide(divider('05', '市场分析与营销策略', '1120 万客流的 8%，就是南溪的存量<br>不造客流，先接溢出', 'food.jpg', 17, '市场'), '', 17))

# 18 market
slides.append(slide(header('05 / 市场', '南溪不需要“从零造客流”', '永定 1120 万人次、125 亿元；92% 在东线，南溪只占 8%。') + f'''
<div style="display:flex;gap:34px;height:540px"><div style="width:780px">
<div class="mbar"><div class="row"><div class="lab">东线高北、洪坑</div><div class="track"><div class="fill" style="width:92%"></div></div><div class="val">92%</div></div>
<div class="row"><div class="lab">南溪</div><div class="track"><div class="fill" style="width:8%;background:var(--ochre)"></div></div><div class="val">8%</div></div></div>
<div class="metrics" style="margin-top:44px"><div class="m"><b>1120 万</b><span>永定年客流</span></div><div class="m"><b>125 亿</b><span>旅游总花费</span></div><div class="m"><b>1.5h</b><span>南溪现状停留</span></div></div>
<div class="panel green" style="margin-top:26px"><h3>目标客群：60 / 30 / 10</h3><p>25—45 岁都市白领与亲子家庭约 60%；20—35 岁轻度户外与文化爱好者约 30%；55 岁以上银发与摄影客群约 10%。</p></div></div>
<div style="flex:1"><div class="grid2" style="gap:14px">
<div class="card"><div class="n">抢</div><h3>东线溢出</h3><p>承接东线 5%—8% 的溢出客流，约 4—7 万人次/年；先做“第二晚”。</p></div>
<div class="card"><div class="n">留</div><h3>过夜与二消</h3><p>从 1.5 小时拉到 2—3 天；民宿、夜游、研学、美食是增量。</p></div>
<div class="card"><div class="n">差</div><h3>差异化</h3><p>对比高北、田螺坑：不拼规模，拼“数字体验＋原住民共治”。</p></div>
<div class="card"><div class="n">复</div><h3>复购</h3><p>数字凭证、认养计划、研学课程，把一次性游客变成年度用户。</p></div></div></div></div>''' + end_content('来源：永定区 2026 年政府工作报告；客群比例为团队调研估算'), '', 18))

# 19 marketing
slides.append(slide(header('05 / 营销', '三阶段营销：先被看见，再被选择，最后被记住', '不铺全渠道，先把“数字守楼人”做成一个可传播的内容 IP。') + f'''
<div class="grid3" style="height:420px">
<div class="panel ochre"><div class="kicker" style="color:var(--ochre)">PHASE 01 · 预热</div><h3>先被看见</h3><p>品牌发布、媒体通稿、KOL 探访、官方小程序上线；用“数字守楼人”公益计划建立好感。</p><ul class="phase-list"><li>品牌片 + 媒体通稿</li><li>20 位在地 KOL 探访</li><li>小程序预约与公益认领</li></ul></div>
<div class="panel teal"><div class="kicker" style="color:var(--teal)">PHASE 02 · 爆发</div><h3>再被选择</h3><p>节假日主题活动、达人直播、短视频矩阵、OTA 促销、研学机构与企业团建；把“种草”变“订单”。</p><ul class="phase-list"><li>五一/暑期/国庆三波主题</li><li>直播 + 短视频矩阵</li><li>OTA 与研学 B 端同开</li></ul></div>
<div class="panel green"><div class="kicker" style="color:#D9C39A">PHASE 03 · 长尾</div><h3>最后被记住</h3><p>会员体系、私域社群、数字藏品/凭证、老客推荐；用复购和口碑替代一次性投放。</p><ul class="phase-list"><li>会员与数字凭证</li><li>社群 + 老客推荐</li><li>四季内容持续更新</li></ul></div></div>
<div class="grid2" style="margin-top:20px"><div class="panel"><h3>内容 IP：四个固定栏目</h3><p>「守楼人的一天」「数字守楼人」「客家十二时辰」「南溪四季」——每周更新，形成可持续内容资产。</p></div>
<div class="panel"><h3>渠道：一个中心、三个圈层</h3><p>官方小程序为中心；OTA/短视频为公域；公众号/社群为私域；研学机构/企业工会为 B 端。</p></div></div>''' + end_content('来源：v4.0 C 第 5 章；不设未经核实的营销预算承诺'), '', 19))

# 20 divider 06
slides.append(slide(divider('06', '实施计划与预期效益', '三期推进、四主体分担 4170 万<br>基准 5.7%，8% 是分红门槛', 'wall.jpg', 20, '实施'), '', 20))

# 21 implementation
slides.append(slide(header('06 / 实施', '三期、六道关、一道闸门', '先审批、再建设；先一期、再二期；没达到闸门条件，不进下一期。') + f'''
<div style="display:grid;grid-template-columns:1.15fr .85fr;gap:30px;height:560px"><div>
<div class="timeline"><div class="axis"><div></div><div class="ticks"><span>M1</span><span>M6</span><span>M18</span><span>M36</span></div></div>
<div class="row"><div class="head">一期 · 基础<small>M1—M6 · 约 6 个月</small></div><div><div class="track"><div class="fill" style="left:0;width:17%">审批 · 基建</div></div><div class="deliv">服务中心、停车场、数字系统、团队；完成文评与审批路径。</div></div></div>
<div class="row"><div class="head">二期 · 产品<small>M7—M18 · 约 12 个月</small></div><div><div class="track"><div class="fill o" style="left:17%;width:33%">产品落地</div></div><div class="deliv">民宿、美食街、夜游、研学、露营；开业首年完成市场验证。</div></div></div>
<div class="row"><div class="head">三期 · 品牌<small>M19—M36 · 约 18 个月</small></div><div><div class="track"><div class="fill t" style="left:50%;width:50%">品牌与复制</div></div><div class="deliv">品牌、4A 创建、标准输出；形成可复制模块。</div></div></div></div>
<div class="panel" style="margin-top:14px;padding:18px 22px"><h3 style="font-size:22px">关键交付</h3><p style="font-size:14px">一期先通审批与基建；二期先把产品跑通；三期再谈品牌与复制，不颠倒顺序。</p></div><div class="quote-line">“没有闸门条件，就没有下一期。”</div></div>
<div><div class="panel green"><h3>4170 万，四方分担</h3><p>政府 1018 万；村民及经营户 1010 万；项目公司 1159 万；合作方 983 万。</p><p style="margin-top:14px">公司只对 1159 万负责回本；不搞重资产自持。</p></div>
<div class="panel ochre" style="margin-top:18px"><h3>六道关</h3><p>文评 → 范围核查 → 方案审批 → 施工许可 → 运营筹备 → 联合验收；未达闸门条件，不进入下一期。</p></div>
<div class="panel" style="margin-top:18px"><h3>三方待办</h3><p>政府：支持函、文评与审批路径；村集体：决议、112 户台账、共益公约；合作方：运营意向、渠道与订单。</p></div></div></div>''' + end_content('来源：v4.0 C 第 6 章；T2.1 资金与审批口径'), '', 21))

# 22 finance
slides.append(slide(header('06 / 效益', 'T2.1 基准：5.7% 是真实的，8% 是门槛', '不把 5.7% 包装成两位数增长；把缺口和三条改进路径一起摊开。') + f'''
<div style="display:flex;gap:28px;height:560px"><div class="figure" style="width:960px"><img src="{A}trend.png" alt="五年趋势与现金"></div>
<div style="flex:1"><div class="metrics" style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="m" style="border:0;padding:0"><b>1421 万</b><span>Y4 含税收入</span></div><div class="m" style="border:0;padding:0"><b>76 万</b><span>Y4 净利润</span></div><div class="m" style="border:0;padding:0"><b style="color:var(--ochre)">5.7%</b><span>净利率（不含税收入口径）</span></div><div class="m" style="border:0;padding:0"><b>3.32 年</b><span>静态回收（不含建设期）</span></div></div>
<div class="panel ochre" style="margin-top:20px"><h3>三个必须说的数</h3><p>峰值资金需求 992 万；融资覆盖 1.0078；最低现金 -22.7 万——覆盖不等于时点安全，需增信与分期。</p></div>
<div class="panel" style="margin-top:16px"><h3>三条改进路径</h3><p>客单 +3%、销量 +5%、营销 -10% 分别只能把净利率推到 7.77%、8.56%、7.42%，不可叠加；目标 8%—10% 需组合验证。</p></div></div></div>''' + end_content('来源：T2.1 基准方案 xlsx；净利率按不含税收入口径；回收期按项目现金流口径，不含建设期'), '', 22))

# 23 benefits
slides.append(slide(header('06 / 效益', '四重效益，最后落到“村民账本”', '经济、社会、文化、生态；每一本账都要能查。') + f'''
<div class="grid4" style="height:300px">
<div class="panel ochre"><div class="num">经济</div><h3>可持续经营</h3><p>T2.1 成熟期营收 1421 万、净利 76 万；目标 8%—10%。</p></div>
<div class="panel teal"><div class="num">社会</div><h3>112 户受益</h3><p>保底＋分成＋共益；9 人共益理事会；一户一码。</p></div>
<div class="panel"><div class="num">文化</div><h3>活态传承</h3><p>非遗传承人常驻带徒；客家生活场景不被展演化。</p></div>
<div class="panel green"><div class="num">生态</div><h3>低干扰</h3><p>本体零触碰；数字外移；溪田竹系统低强度利用。</p></div></div>
<div class="grid2" style="margin-top:22px"><div class="panel"><h3>三层共益分配</h3><p>保底：租金、工资、农产品收购、非遗课时费；分成：民宿 65/35、增量 60/40、非遗 70/20/10、优先股 6%；共益：营收 1%＋超额 20%。</p></div>
<div class="panel green"><h3>一条硬约束</h3><p>公司净利率低于 8%，暂停股东分红与扩张；村民保底不因亏损取消。共益基金为税后分配，不计成本、不抵税。</p></div></div>''' + end_content('来源：v4.0 C 第 6 章；T2.1 基准；共益机制为合同约定'), '', 23))

# 24 divider 07
slides.append(slide(divider('07', '风险评估与应对策略', '政策、市场、运营、财务四类风险<br>先设止损线，再谈增长', 'night.jpg', 24, '风险'), '', 24))

# 25 risks
slides.append(slide(header('07 / 风险', '四类风险，四条应对，三条止损线', '风险不是“零风险”，是“提前看见、有人负责、触发就执行”。') + f'''
<div class="risk-grid"><div><div class="matrix">
<div class="q q1"><span>高影响 · 低概率</span><b>黑天鹅</b></div>
<div class="q q2"><span>高影响 · 高概率</span><b>政策 / 世遗</b></div>
<div class="q q3"><span>低影响 · 低概率</span><b>常规运营</b></div>
<div class="q q4"><span>低影响 · 高概率</span><b>市场 / 财务</b></div>
<div class="dot" style="left:70%;top:22%"></div>
<div class="dot" style="left:57%;top:36%"></div>
<div class="dot o" style="left:39%;top:46%"></div>
<div class="dot g" style="left:28%;top:66%"></div></div><div class="axis-note">横轴：发生概率　｜　纵轴：影响程度</div></div>
<div class="risk-list">
<div class="r"><div><h4>政策/世遗</h4><div class="tag">高影响 · 中概率</div></div><p>保护政策收紧、审批周期延长。应对：三级红线、本体零触碰、文评前置、监测数据与文物部门互通。</p></div>
<div class="r"><div><h4>市场</h4><div class="tag">中高影响 · 中概率</div></div><p>同质化、消费波动。应对：数字差异化、内容年更、客群分层、渠道多元。</p></div>
<div class="r"><div><h4>运营</h4><div class="tag">高影响 · 中概率</div></div><p>服务不稳、文化走样。应对：SOP、村民培训、文化顾问委员会、主理人机制。</p></div>
<div class="r"><div><h4>财务</h4><div class="tag">中影响 · 中低概率</div></div><p>现金流缺口、融资不到位。应对：分月资金计划、增信/股东借款、投资延后、成本共担。</p></div>
<div class="panel" style="margin-top:18px;padding:18px 22px"><h3 style="font-size:21px">风险治理机制</h3><p style="font-size:13px">三方联席会议每月一次；共益理事会每季一次；监测报告与财务月报同步；触发止损线，24 小时内启动预案。</p></div></div></div>
<div class="panel ochre" style="margin-top:18px"><h3>三条止损线</h3><p>净利率低于 8%：暂停分红与扩张；现金低于 3 个月运营成本：启动应急融资；发生重大文物安全事件：立即停业整改。</p></div>''' + end_content('来源：v4.0 C 第 7 章；风险矩阵为团队评估'), '', 25))

# 26 conclusion
slides.append(slide(f'''<div class="closing"><img class="bg" src="{A}guesthouse.jpg" alt=""><div class="shade"></div><div class="inner">
<div class="k">CONCLUSION / 不是……而是……</div><h2>不是再造一个景区，<br>是把南溪的一天做成产品。<br><em>不是把村民迁走，是让 112 户留在楼里、也留在决策桌上。</em></h2>
<div class="three"><div><b>数字守楼人</b><span>数字外移，本体零触碰；62 米外做体验。</span></div><div><b>活态客家魂</b><span>112 户原住民常住；生活就是产品。</span></div><div><b>共益分配</b><span>保底 → 分成 → 共益；8% 是门槛。</span></div></div></div>
<div class="claim">把体验请出土楼，把收益留给村民。</div></div>''', '', 26))

# 27 thanks
slides.append(slide(f'''<div class="thanks"><img class="bg" src="{A}night.jpg" alt=""><div class="shade"></div><div class="inner">
<div class="en">THANK YOU</div><h2 class="serif">数字守楼人<br>活态客家魂</h2><p>福建龙岩湖坑镇十里南溪文旅新业态策划方案<br>安志逸 · 林雨嫣 · 刘璇 · 刘彧安</p></div>
<div class="meta">2026 全国大学生文化旅游与会展竞赛 · 旅游新业态策划组　｜　请评委指正</div></div>''', '', 27))

html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<title>数字守楼人·活态客家魂｜七部分路演</title><style>{CSS}</style></head><body>
{''.join(slides)}
<script>
document.fonts && document.fonts.ready.then(()=>{{ window.__pagedDone = true; }});
setTimeout(()=>{{ window.__pagedDone = true; }}, 1200);
</script></body></html>'''

path = os.path.join(OUT, 'deck.html')
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('html', path, len(html))
