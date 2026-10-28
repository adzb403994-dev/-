const path=require('path'); const fs=require('fs'); const echarts=require(path.join('D:/DeepSeek/ppt_toolchain/node_modules','echarts'));
const chart=echarts.init(null,null,{renderer:'svg',ssr:true,width:800,height:450});
chart.setOption({backgroundColor:'#F7F3EC',color:['#8B5A3C','#2F4F4F'],title:{text:'五年收入与净利',left:20,top:10,textStyle:{fontFamily:'Noto Serif SC',fontSize:20,color:'#2E2A24'}},xAxis:{type:'category',data:['Y1','Y2','Y3','Y4','Y5']},yAxis:{type:'value'},series:[{type:'bar',data:[839.9,1130.3,1307.7,1421.4,1421.4]},{type:'line',data:[-90,-9.2,31.6,76.4,63.8],smooth:true}]});
const svg=chart.renderToSVGString(); fs.writeFileSync('D:/DeepSeek/ppt_champion/05_output/_smoke_echarts.svg',svg); console.log('echarts ok',svg.length);
