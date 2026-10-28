const pptxgen = require('D:/DeepSeek/ppt_toolchain/node_modules/pptxgenjs');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = '安德投研';
pptx.company = '数字守楼人';
pptx.subject = '数字守楼人·活态客家魂｜12页路演';
pptx.title = '数字守楼人·活态客家魂｜12页路演 v1.0';
pptx.lang = 'zh-CN';
pptx.theme = { headFontFace: 'Noto Serif SC', bodyFontFace: 'Noto Sans SC', lang: 'zh-CN' };

const C = {
  cream: 'F7F3EC', green: '2F4F4F', dark: '1E2E2D', ochre: '8B5A3C',
  ink: '2E2A24', gold: 'B08D57', line: 'D9D2C5', white: 'FFFFFF',
  soft: 'EFE9DD', red: 'A34A3F', pale: 'E8DED0'
};
const W = 13.333, H = 7.5, M = 0.72;
const F = { serif: 'Noto Serif SC', sans: 'Noto Sans SC' };
const A = 'D:/DeepSeek/ppt_champion/03_assets/';
const IMG = A + 'images/';
const FIG = A + 'png/';

function txt(s, text, o = {}) {
  const opt = Object.assign({ fontFace: F.sans, fontSize: 14, color: C.ink, valign: 'mid' }, o);
  s.addText(text, opt);
}
function title(s, text, o = {}) {
  txt(s, text, Object.assign({ x: M, y: 0.72, w: W - 2 * M, h: 0.9, fontFace: F.serif, fontSize: 30, bold: true, color: C.ochre, fit: 'shrink' }, o));
}
function kicker(s, text, o = {}) {
  txt(s, text, Object.assign({ x: M, y: 0.34, w: 8, h: 0.3, fontSize: 9.5, color: C.gold, charSpacing: 1.6, bold: true }, o));
}
function footer(s, page, source = '') {
  s.addShape(pptx.ShapeType.line, { x: M, y: 6.82, w: W - 2 * M, h: 0, line: { color: C.line, width: 0.6 } });
  txt(s, '数字守楼人 · 活态客家魂', { x: M, y: 6.9, w: 4.2, h: 0.25, fontSize: 8.5, color: C.gold });
  if (source) txt(s, source, { x: 4.7, y: 6.9, w: 7.2, h: 0.25, fontSize: 7.5, color: C.gold, align: 'right' });
  txt(s, String(page), { x: W - 0.9, y: 6.9, w: 0.5, h: 0.25, fontSize: 8.5, color: C.ochre, align: 'right' });
}
function pageNo(s, page) {
  txt(s, String(page), { x: W - 0.9, y: H - 0.42, w: 0.5, h: 0.22, fontSize: 8, color: C.gold, align: 'right' });
}
function fullImage(s, file, page) {
  s.addImage({ path: file, x: 0, y: 0, w: W, h: H });
  pageNo(s, page);
}
function actBar(s, active) {
  const acts = ['退', '进', '算', '守'];
  const x0 = 8.25, y = 0.35;
  acts.forEach((a, i) => {
    const on = i === active;
    txt(s, a, { x: x0 + i * 1.0, y, w: 0.8, h: 0.3, fontSize: 10, color: on ? C.ochre : 'B9AD9B', bold: on, align: 'center' });
    if (i < 3) txt(s, '—', { x: x0 + i * 1.0 + 0.8, y, w: 0.2, h: 0.3, fontSize: 9, color: 'B9AD9B', align: 'center' });
  });
}

/* ============ P1 COVER ============ */
let s = pptx.addSlide();
s.addImage({ path: IMG + 'IMG-13b2_夏_单座圆楼.jpg', x: 0, y: 0, w: W, h: H });
s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: H, fill: { color: C.dark, transparency: 35 }, line: { color: C.dark, transparency: 100 } });
txt(s, '2026 全国大学生文化旅游与会展竞赛 · 旅游新业态策划组', { x: M, y: 0.55, w: 8.8, h: 0.3, fontSize: 9.5, color: 'D9C39A', charSpacing: 1 });
txt(s, '数字守楼人 · 活态客家魂', { x: M, y: 3.05, w: 8.5, h: 0.65, fontFace: F.serif, fontSize: 38, bold: true, color: C.cream });
s.addShape(pptx.ShapeType.line, { x: M, y: 3.82, w: 1.25, h: 0, line: { color: C.gold, width: 1.5 } });
txt(s, '把体验请出土楼，把收益留给村民。', { x: M, y: 3.98, w: 7.8, h: 0.45, fontFace: F.serif, fontSize: 20, color: C.cream });
txt(s, '5 米，不能碰。   15.2 米，不能直射。   62 米，才是舞台。', { x: M, y: 4.75, w: 8.0, h: 0.35, fontSize: 12.5, color: 'D9C39A' });
txt(s, '安德投研｜2026.11', { x: M, y: 6.35, w: 4.0, h: 0.3, fontSize: 9.5, color: 'D9C39A' });
pageNo(s, 1);
s.addNotes('开场 25 秒：三句话各停 2 秒；最后一句“数字守楼人·活态客家魂”。不放团队履历、不放目录。');

/* ============ P2 PROBLEM ============ */
s = pptx.addSlide(); s.background = { color: C.cream };
kicker(s, '第一幕 · 退 / 问题');
actBar(s, 0);
title(s, '92% 的客流在东线，南溪只分到 8%', { y: 0.78, fontSize: 29 });
txt(s, '不是资源不足，是承载错位：体验压在本体上，收益留在外部。', { x: M, y: 1.72, w: 10.8, h: 0.42, fontSize: 15, color: C.green });
txt(s, '92%', { x: M, y: 2.38, w: 4.3, h: 1.1, fontFace: F.serif, fontSize: 78, bold: true, color: C.green });
txt(s, '客流在东线高北、洪坑', { x: M, y: 3.42, w: 4.3, h: 0.3, fontSize: 10.5, color: C.gold });
txt(s, '8%', { x: 5.35, y: 2.38, w: 3.2, h: 1.1, fontFace: F.serif, fontSize: 78, bold: true, color: C.ochre });
txt(s, '南溪只承接约 8%', { x: 5.35, y: 3.42, w: 3.2, h: 0.3, fontSize: 10.5, color: C.gold });
txt(s, '1.5 小时', { x: M, y: 4.55, w: 3.0, h: 0.55, fontFace: F.serif, fontSize: 30, bold: true, color: C.ochre });
txt(s, '平均停留', { x: M, y: 5.12, w: 2.4, h: 0.25, fontSize: 9.5, color: C.gold });
txt(s, '98 元', { x: 3.55, y: 4.55, w: 2.4, h: 0.55, fontFace: F.serif, fontSize: 30, bold: true, color: C.ochre });
txt(s, '现状客单', { x: 3.55, y: 5.12, w: 2.4, h: 0.25, fontSize: 9.5, color: C.gold });
txt(s, '1120 万人次 / 125 亿元', { x: 7.1, y: 4.55, w: 5.2, h: 0.35, fontSize: 13, color: C.ink });
txt(s, '永定 2025 年预计接待与总花费', { x: 7.1, y: 4.95, w: 5.2, h: 0.25, fontSize: 9, color: C.gold });
s.addShape(pptx.ShapeType.rect, { x: M, y: 5.65, w: W - 2 * M, h: 0.28, fill: { color: C.green }, line: { color: C.green, transparency: 100 } });
s.addShape(pptx.ShapeType.rect, { x: M + (W - 2 * M) * 0.92, y: 5.65, w: (W - 2 * M) * 0.08, h: 0.28, fill: { color: C.ochre }, line: { color: C.ochre, transparency: 100 } });
txt(s, '东线 92%', { x: M, y: 5.96, w: 3.0, h: 0.25, fontSize: 9, color: C.green, bold: true });
txt(s, '南溪 8%', { x: W - M - 1.6, y: 5.96, w: 1.6, h: 0.25, fontSize: 9, color: C.ochre, bold: true, align: 'right' });
footer(s, 2, '来源：永定区 2026 年政府工作报告；8%/1.5h/98 元为团队调研估算');
s.addNotes('安志逸 45 秒：永定一年 1120 万游客，92% 去东线；南溪只分到 8%，待 1.5 小时、花 98 块。不是资源不足，是承载错位。');

/* ============ P3 DEFINITION ============ */
s = pptx.addSlide(); s.background = { color: C.cream };
kicker(s, '第一幕 · 退 / 模式');
actBar(s, 0);
title(s, '数字共益型遗产旅游', { x: M, y: 0.78, w: 8, fontSize: 32 });
txt(s, '不是做一个景区，是把保护、生活、分配装进同一个机制。', { x: M, y: 1.72, w: 11.4, h: 0.35, fontSize: 13, color: C.green });
const boxes = [
  ['01', '数字外移', '体验移到楼外\n本体零触碰'],
  ['02', '原住民共治', '112 户留在楼里\n也留在决策桌上'],
  ['03', '共益分配', '保底 → 分成 → 共益\n三层分账'],
  ['04', '沉浸体验', '看楼 · 懂楼\n建楼 · 守楼']
];
const bw = 2.55, gap = 0.38, y0 = 2.35;
boxes.forEach((b, i) => {
  const x = M + i * (bw + gap);
  s.addShape(pptx.ShapeType.roundRect, { x, y: y0, w: bw, h: 2.35, fill: { color: C.soft }, line: { color: C.line, width: 0.8 }, rectRadius: 0.04 });
  txt(s, b[0], { x: x + 0.18, y: y0 + 0.16, w: 1.0, h: 0.3, fontSize: 11, color: C.gold, bold: true });
  txt(s, b[1], { x: x + 0.18, y: y0 + 0.55, w: bw - 0.36, h: 0.4, fontFace: F.serif, fontSize: 17, bold: true, color: C.ochre });
  txt(s, b[2], { x: x + 0.18, y: y0 + 1.1, w: bw - 0.36, h: 0.95, fontSize: 9.5, color: C.ink, lineSpacingMultiple: 1.25 });
});
txt(s, '数字外移 ＋ 原住民共治 ＋ 共益分配 ＋ 沉浸体验  ＝  一个业态', { x: M, y: 5.15, w: W - 2 * M, h: 0.55, fontFace: F.serif, fontSize: 18, color: C.green, align: 'center' });
txt(s, '政策依据：《产业结构调整指导目录（2024 年本）》第三十四类“旅游业”鼓励类第 2 项', { x: M, y: 5.95, w: W - 2 * M, h: 0.3, fontSize: 8.5, color: C.gold, align: 'center' });
footer(s, 3, '');
s.addNotes('安志逸 30 秒：数字是保护手段，原住民是主体，共益是治理——三件事合成一个业态。');

/* ============ P4 DISTANCES ============ */
s = pptx.addSlide();
fullImage(s, FIG + '02_三个距离剖面.png', 4);
s.addNotes('安志逸 30 秒：5 米本体不安排经营，15.2 米光影不直射，62 米外做数字体验；62 米位于建控地带以外、环境协调区内，以批复规划为准。');

/* ============ P5 RESOURCE MAP ============ */
s = pptx.addSlide();
fullImage(s, FIG + '01_区位资源地图.png', 5);
s.addNotes('安志逸 20 秒：2 座世遗本体楼、1 处省保、3 个传统村落、112 户；这是永定南线少见的“世遗本体+活态原住民”组合。');

/* ============ P6 FLAGSHIP ============ */
s = pptx.addSlide(); s.background = { color: C.cream };
kicker(s, '第二幕 · 进 / 旗舰');
actBar(s, 1);
title(s, '20 分钟，看楼—懂楼—建楼—守楼', { x: M, y: 0.72, w: 11.8, fontSize: 27 });
s.addImage({ path: IMG + 'IMG-02_数字孪生体验舱_压缩版.jpg', x: M, y: 1.75, w: 5.15, h: 4.35 });
s.addShape(pptx.ShapeType.rect, { x: M, y: 1.75, w: 5.15, h: 4.35, fill: { color: C.dark, transparency: 100 }, line: { color: C.gold, width: 0.8 } });
const steps = [['3′', '入楼', '领身份卡，读保护规则'], ['5′', '看楼', 'AR 叠加真实与数字模型'], ['7′', '建楼', '虚拟工坊完成夯土工序'], ['5′', '守楼', '看监测数据，留下数字凭证']];
steps.forEach((st, i) => {
  const y = 1.8 + i * 1.05;
  txt(s, st[0], { x: 6.35, y, w: 0.8, h: 0.45, fontFace: F.serif, fontSize: 22, bold: true, color: C.ochre });
  txt(s, st[1], { x: 7.2, y, w: 1.6, h: 0.35, fontFace: F.serif, fontSize: 15, bold: true, color: C.green });
  txt(s, st[2], { x: 8.75, y: y + 0.02, w: 3.8, h: 0.45, fontSize: 9.5, color: C.ink });
  if (i < 3) s.addShape(pptx.ShapeType.line, { x: 6.72, y: y + 0.55, w: 0, h: 0.4, line: { color: C.line, width: 0.7 } });
});
txt(s, '68 元/人   ×   日容量约 200 人', { x: 6.35, y: 5.45, w: 5.8, h: 0.35, fontSize: 13, color: C.ochre, bold: true });
txt(s, '设备会旧，内容不会：每年更新 2—3 个场景或课程。', { x: 6.35, y: 5.9, w: 5.8, h: 0.3, fontSize: 9.5, color: C.gold });
footer(s, 6, '来源：v4.0 B 产品章；T2.1 关键数据');
s.addNotes('林雨嫣 50 秒：旗舰 20 分钟四段；票价 68 元、日容量约 200 人；设备会旧，内容不会。');

/* ============ P7 JOURNEY ============ */
s = pptx.addSlide();
fullImage(s, FIG + '03_空间与旅程.png', 7);
s.addNotes('林雨嫣 50 秒：一个旗舰带住、食、学、野、礼；一日精华、两日深度、三日研学，把 1.5 小时拉长到 2—3 天。');

/* ============ P8 FUNDING ============ */
s = pptx.addSlide();
fullImage(s, FIG + '04_资金瀑布.png', 8);
s.addNotes('刘璇 45 秒：政府 1018 万、村民及经营户 1010 万、公司 1159 万、合作方 983 万；公司只对 1159 万负责回本。');

/* ============ P9 TREND ============ */
s = pptx.addSlide();
fullImage(s, FIG + '05_五年趋势.png', 9);
s.addNotes('刘璇 75 秒：基准 5.7%，三路径争取 8%—10%；8% 是分红门槛；静态回收 3.32 年（项目现金流口径，不含建设期）；最低现金 -22.7 万，用增信和分期补。');

/* ============ P10 GOVERNANCE ============ */
s = pptx.addSlide();
fullImage(s, FIG + '06_治理共益.png', 10);
s.addNotes('刘璇 40 秒：保底是收入保障（租金/工资等合同对价），不是分红；再分成，最后共益；65/35、6%、9 人、一户一码。');

/* ============ P11 LANDING ============ */
s = pptx.addSlide(); s.background = { color: C.cream };
kicker(s, '第四幕 · 守 / 落地');
actBar(s, 3);
title(s, '三期、六道关、一道闸门', { y: 0.72, fontSize: 30 });
const phases = [['一期', 'M1—M6', '基础建设', '服务中心、停车场、数字系统、团队'], ['二期', 'M7—M18', '产品落地', '民宿、美食街、夜游、研学、露营'], ['三期', 'M19—M36', '品牌提升', '品牌、4A 创建、复制标准']];
phases.forEach((ph, i) => {
  const x = M + i * 4.05;
  s.addShape(pptx.ShapeType.roundRect, { x, y: 1.65, w: 3.85, h: 1.45, fill: { color: C.soft }, line: { color: C.line, width: 0.7 }, rectRadius: 0.03 });
  txt(s, ph[0], { x: x + 0.2, y: 1.78, w: 1.0, h: 0.3, fontFace: F.serif, fontSize: 14, bold: true, color: C.ochre });
  txt(s, ph[1], { x: x + 1.05, y: 1.8, w: 2.6, h: 0.28, fontSize: 9, color: C.gold });
  txt(s, ph[2], { x: x + 0.2, y: 2.15, w: 3.4, h: 0.3, fontFace: F.serif, fontSize: 14, bold: true, color: C.green });
  txt(s, ph[3], { x: x + 0.2, y: 2.52, w: 3.45, h: 0.5, fontSize: 8.5, color: C.ink, lineSpacingMultiple: 1.15 });
});
const gates = ['文评', '范围核查', '方案审批', '施工许可', '运营筹备', '联合验收'];
gates.forEach((g, i) => {
  const x = M + i * 1.97;
  s.addShape(pptx.ShapeType.rect, { x, y: 3.55, w: 1.75, h: 0.62, fill: { color: i === 5 ? C.ochre : C.white }, line: { color: i === 5 ? C.ochre : C.line, width: 0.7 } });
  txt(s, String(i + 1).padStart(2, '0'), { x: x + 0.08, y: 3.6, w: 0.35, h: 0.2, fontSize: 7.5, color: i === 5 ? C.cream : C.gold });
  txt(s, g, { x: x + 0.08, y: 3.78, w: 1.6, h: 0.28, fontSize: 8.5, color: i === 5 ? C.cream : C.green, bold: true });
  if (i < 5) txt(s, '›', { x: x + 1.77, y: 3.64, w: 0.18, h: 0.3, fontSize: 15, color: C.gold, align: 'center' });
});
txt(s, '一道闸门：未达闸门条件，不进入下一期。', { x: M, y: 4.45, w: 6.6, h: 0.3, fontSize: 10, color: C.ochre, bold: true });
const asks = [['政府', '支持函、文评与审批路径、基础设施'], ['村集体', '决议、112 户台账、共益公约'], ['合作方', '运营意向、渠道与订单、融资/授信意向']];
asks.forEach((a, i) => {
  const x = M + i * 3.95;
  s.addShape(pptx.ShapeType.line, { x, y: 5.15, w: 0, h: 0.55, line: { color: C.gold, width: 1.2 } });
  txt(s, a[0], { x: x + 0.16, y: 5.08, w: 1.0, h: 0.3, fontFace: F.serif, fontSize: 12, bold: true, color: C.ochre });
  txt(s, a[1], { x: x + 0.16, y: 5.4, w: 3.45, h: 0.5, fontSize: 8.2, color: C.ink, lineSpacingMultiple: 1.15 });
});
txt(s, '四类风险：审批、客流、资金、村民关系；对应六道关、闸门、增信、共议。', { x: M, y: 5.98, w: 11.8, h: 0.28, fontSize: 8.8, color: C.green });
footer(s, 11, '来源：v4.0 C 实施计划与审批路径');
s.addNotes('刘彧安 50 秒：三期推进，每期一道闸门；文评—核查—审批—施工—筹备—验收；四类风险对应六道关、闸门、增信、共议；没达到闸门条件，不进下一期。');

/* ============ P12 CLOSE ============ */
s = pptx.addSlide();
s.addImage({ path: IMG + 'IMG-04c_民宿窗外土楼夜景.jpg', x: 0, y: 0, w: W, h: H });
s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: H, fill: { color: C.dark, transparency: 42 }, line: { color: C.dark, transparency: 100 } });
txt(s, '不是……而是……', { x: M, y: 0.72, w: 5, h: 0.3, fontSize: 11, color: 'D9C39A', charSpacing: 2 });
const lines = [
  ['不是再造一个景区，', '是把南溪的一天做成产品。'],
  ['不是把村民迁走，', '是让 112 户留在楼里、也留在决策桌上。'],
  ['不是把 5.7% 说成两位数增长，', '是把缺口和三条改进路径一起摊开。']
];
lines.forEach((l, i) => {
  const y = 1.35 + i * 1.45;
  txt(s, l[0], { x: M, y, w: 10.8, h: 0.45, fontFace: F.serif, fontSize: 22, color: 'D9C39A' });
  txt(s, l[1], { x: M, y: y + 0.45, w: 11.0, h: 0.45, fontFace: F.serif, fontSize: 22, color: C.cream });
});
s.addShape(pptx.ShapeType.line, { x: M, y: 6.18, w: 1.5, h: 0, line: { color: C.gold, width: 1.2 } });
txt(s, '把体验请出土楼，把收益留给村民。', { x: M, y: 6.32, w: 8.2, h: 0.4, fontFace: F.serif, fontSize: 18, color: C.cream });
txt(s, '安德投研 · 2026.11', { x: 9.3, y: 6.38, w: 3.2, h: 0.3, fontSize: 9, color: 'D9C39A', align: 'right' });
pageNo(s, 12);
s.addNotes('刘彧安 30 秒：三个“不是”，落回主张。四人只在最后齐说“楼外看楼，楼里受益”8 个字；长句由刘彧安一个人收。');

pptx.writeFile({ fileName: 'D:/DeepSeek/ppt_champion/05_output/数字守楼人_路演PPT_v1.0.pptx' })
  .then(f => console.log('deck ok', f)).catch(e => { console.error(e); process.exit(1); });
