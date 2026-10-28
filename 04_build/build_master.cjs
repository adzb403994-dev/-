const pptxgen = require('D:/DeepSeek/ppt_toolchain/node_modules/pptxgenjs');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = '安德投研';
pptx.company = '数字守楼人';
pptx.subject = '全国冠军PPT视觉母版';
pptx.title = '数字守楼人·活态客家魂｜PPT母版 v0.1';
pptx.lang = 'zh-CN';
pptx.theme = { headFontFace: 'Noto Serif SC', bodyFontFace: 'Noto Sans SC', lang: 'zh-CN' };
const C = { cream:'F7F3EC', green:'2F4F4F', ochre:'8B5A3C', ink:'2E2A24', gold:'B08D57', line:'D9D2C5', white:'FFFFFF', soft:'EFE9DD', red:'A34A3F' };
const W=13.333, H=7.5, M=0.75;

function foot(s, page, source='规划测算，不构成收益承诺'){
  s.addShape(pptx.ShapeType.line,{x:M,y:6.78,w:W-2*M,h:0,line:{color:C.line,width:0.6}});
  s.addText('数字守楼人 · 活态客家魂',{x:M,y:6.86,w:5,h:0.3,fontSize:9,color:C.gold,fontFace:'Noto Sans SC'});
  s.addText(source,{x:5.6,y:6.86,w:6.0,h:0.3,fontSize:8,color:C.gold,align:'right',fontFace:'Noto Sans SC'});
  s.addText(String(page),{x:W-1.1,y:6.86,w:0.35,h:0.3,fontSize:9,color:C.ochre,align:'right',fontFace:'Noto Sans SC'});
}
function kicker(s, text, color=C.gold){
  s.addText(text,{x:M,y:0.42,w:6,h:0.32,fontSize:10,color,charSpacing:2,fontFace:'Noto Sans SC'});
}
function title(s, text, size=32, color=C.ochre, y=0.8, w=W-2*M){
  s.addText(text,{x:M,y,w,h:1.0,fontSize:size,bold:true,color,fontFace:'Noto Serif SC',breakLine:false,fit:'shrink'});
}
function placeholder(s,x,y,w,h,label){
  s.addShape(pptx.ShapeType.rect,{x,y,w,h,fill:{color:C.soft},line:{color:C.gold,width:1,dashType:'dash'}});
  s.addText(label,{x:x+0.15,y:y+h/2-0.2,w:w-0.3,h:0.4,fontSize:10,color:C.gold,align:'center',fontFace:'Noto Sans SC'});
}

// 1 Cover
let s = pptx.addSlide(); s.background={color:C.green};
s.addShape(pptx.ShapeType.rect,{x:0,y:0,w:6.2,h:H,fill:{color:'24403F'}});
placeholder(s,0.0,0.0,6.2,H,'封面主图：单座圆楼夜景 / 16:9 竖切');
s.addText('5 米，不能碰。',{x:6.9,y:0.95,w:5.7,h:0.55,fontSize:22,color:'D9C39A',fontFace:'Noto Serif SC'});
s.addText('15.2 米，不能直射。',{x:6.9,y:1.45,w:5.7,h:0.55,fontSize:22,color:'D9C39A',fontFace:'Noto Serif SC'});
s.addText('62 米，才是舞台。',{x:6.9,y:1.95,w:5.7,h:0.55,fontSize:22,color:'D9C39A',fontFace:'Noto Serif SC'});
s.addShape(pptx.ShapeType.line,{x:6.9,y:2.75,w:1.2,h:0,line:{color:C.gold,width:1.2}});
s.addText('数字守楼人 · 活态客家魂',{x:6.9,y:2.95,w:5.7,h:1.0,fontSize:34,bold:true,color:C.cream,fontFace:'Noto Serif SC',fit:'shrink'});
s.addText('把体验请出土楼，把收益留给村民。',{x:6.9,y:3.95,w:5.7,h:0.6,fontSize:19,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('2026 全国大学生文化旅游与会展竞赛｜旅游新业态策划组',{x:6.9,y:4.7,w:5.7,h:0.5,fontSize:10,color:'C9C0B2',fontFace:'Noto Sans SC'});
s.addText('安德投研｜2026.11',{x:6.9,y:5.1,w:5.7,h:0.4,fontSize:10,color:'C9C0B2',fontFace:'Noto Sans SC'});

// 2 Act divider 退
s = pptx.addSlide(); s.background={color:C.cream};
s.addText('01',{x:M,y:0.4,w:1.2,h:0.4,fontSize:12,color:C.gold,fontFace:'Noto Sans SC'});
s.addText('第一幕 · 退',{x:M+0.9,y:0.4,w:5,h:0.4,fontSize:12,color:C.gold,charSpacing:2,fontFace:'Noto Sans SC'});
s.addText('退',{x:1.1,y:0.7,w:4.5,h:5.4,fontSize:230,bold:true,color:'E8DED0',fontFace:'Noto Serif SC'});
s.addText('把体验退到楼外。',{x:5.7,y:2.0,w:6.8,h:0.9,fontSize:38,bold:true,color:C.ochre,fontFace:'Noto Serif SC'});
s.addText('本体零触碰，游客在楼外读懂楼。',{x:5.7,y:3.0,w:6.4,h:0.6,fontSize:18,color:C.ink,fontFace:'Noto Sans SC'});
s.addText('5m  ·  15.2m  ·  62m',{x:5.7,y:4.3,w:6,h:0.5,fontSize:16,color:C.gold,charSpacing:2,fontFace:'Noto Sans SC'});
foot(s,2,'');

// 3 Content split
s = pptx.addSlide(); s.background={color:C.cream};
kicker(s,'第一幕 · 退 / 问题');
title(s,'92% 的客流在东线，南溪只分到 8%',30);
s.addText('不是资源不足，是承载错位。',{x:M,y:1.75,w:6.0,h:0.45,fontSize:16,color:C.green,fontFace:'Noto Sans SC'});
s.addText('1120 万',{x:M,y:2.45,w:2.4,h:0.8,fontSize:32,bold:true,color:C.ochre,fontFace:'Noto Serif SC'});
s.addText('永定年客流',{x:M,y:3.2,w:2.4,h:0.3,fontSize:9,color:C.gold,fontFace:'Noto Sans SC'});
s.addText('92% / 8%',{x:M,y:3.65,w:2.6,h:0.8,fontSize:32,bold:true,color:C.ochre,fontFace:'Noto Serif SC'});
s.addText('东线 / 南溪',{x:M,y:4.4,w:2.4,h:0.3,fontSize:9,color:C.gold,fontFace:'Noto Sans SC'});
s.addText('1.5 小时',{x:M,y:4.85,w:2.5,h:0.6,fontSize:26,bold:true,color:C.ochre,fontFace:'Noto Serif SC'}); s.addText('98 元',{x:M+2.6,y:4.85,w:1.6,h:0.6,fontSize:26,bold:true,color:C.ochre,fontFace:'Noto Serif SC'});
s.addText('平均停留 / 客单',{x:M,y:5.55,w:3.0,h:0.3,fontSize:9,color:C.gold,fontFace:'Noto Sans SC'});
placeholder(s,5.6,1.65,7.0,4.8,'图：东线拥挤 vs 南溪空镜 / 双图对比');
foot(s,3,'来源：永定区 2026 年政府工作报告；8%/1.5h/98 元为团队调研估算');

// 4 Full-bleed data
s = pptx.addSlide(); s.background={color:C.cream};
kicker(s,'第一幕 · 退 / 空间纪律');
title(s,'5 米不能碰，15.2 米不能直射，62 米才是舞台',30);
placeholder(s,M,1.6,W-2*M,4.9,'图：三个距离剖面 / Kimi 02 · 16:9 满版');
s.addText('距离越远，保护越近。',{x:M,y:6.35,w:5,h:0.35,fontSize:14,color:C.ochre,fontFace:'Noto Serif SC'});
foot(s,4,'示意：非等比剖面；以批准的保护规划为准');

// 5 Close
s = pptx.addSlide(); s.background={color:C.green};
s.addText('不是再造一个景区，',{x:M,y:1.3,w:11.8,h:0.8,fontSize:30,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('是把南溪的一天做成产品。',{x:M,y:2.0,w:11.8,h:0.8,fontSize:30,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('不是把村民迁走，',{x:M,y:2.9,w:11.8,h:0.8,fontSize:30,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('是让 112 户留在楼里、也留在决策桌上。',{x:M,y:3.6,w:11.8,h:0.8,fontSize:30,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('不是把 5.7% 说成两位数增长，',{x:M,y:4.5,w:11.8,h:0.8,fontSize:30,color:'D9C39A',fontFace:'Noto Serif SC'});
s.addText('是把缺口和三条改进路径一起摊开。',{x:M,y:5.2,w:11.8,h:0.8,fontSize:30,color:'D9C39A',fontFace:'Noto Serif SC'});
s.addShape(pptx.ShapeType.line,{x:M,y:6.2,w:2.0,h:0,line:{color:C.gold,width:1.2}});
s.addText('把体验请出土楼，把收益留给村民。',{x:M,y:6.35,w:9,h:0.4,fontSize:18,color:C.cream,fontFace:'Noto Serif SC'});
s.addText('安德投研 · 2026.11',{x:9.5,y:6.35,w:3,h:0.4,fontSize:10,color:'C9C0B2',align:'right',fontFace:'Noto Sans SC'});

pptx.writeFile({fileName:'D:/DeepSeek/ppt_champion/05_output/PPT_master_v0.1.pptx'}).then(f=>console.log('master ok',f)).catch(e=>{console.error(e);process.exit(1)});
