const path=require('path'); const pptxgen=require(path.join('D:/DeepSeek/ppt_toolchain/node_modules','pptxgenjs'));
const pptx=new pptxgen(); pptx.layout='LAYOUT_WIDE'; const s=pptx.addSlide(); s.background={color:'F7F3EC'}; s.addText('数字守楼人 · 测试',{x:0.6,y:0.6,w:8,h:1,fontSize:36,color:'8B5A3C',bold:true,fontFace:'SimSun'}); s.addText('把体验请出土楼，把收益留给村民。',{x:0.6,y:1.8,w:10,h:0.8,fontSize:20,color:'2F4F4F',fontFace:'Microsoft YaHei'});
pptx.writeFile({fileName:'D:/DeepSeek/ppt_champion/05_output/_smoke.pptx'}).then(f=>console.log('pptxgen ok',f)).catch(e=>{console.error(e);process.exit(1)});
