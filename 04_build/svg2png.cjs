const fs=require('fs'); const path=require('path'); const sharp=require('D:/DeepSeek/ppt_toolchain/node_modules/sharp');
const src='C:/Users/azy33/Desktop/三方共建工作台/05_Kimi产出/T9_视觉升级/03_核心图_16x9'; const out='D:/DeepSeek/ppt_champion/03_assets/png';
fs.readdirSync(src).filter(f=>f.endsWith('.svg')).forEach(f=>{
  const dst=path.join(out, f.replace('.svg','.png'));
  sharp(path.join(src,f),{density:192}).resize(1920,1080).png().toFile(dst).then(()=>console.log('ok',f)).catch(e=>console.error('fail',f,e.message));
});
