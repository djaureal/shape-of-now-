(()=>{
  let ctx=null, master=null, active=false, currentMode='calm', nodes=[];
  const AC=window.AudioContext||window.webkitAudioContext;
  if(!AC) return;

  function ensure(){
    if(!ctx){
      ctx=new AC();
      master=ctx.createGain();
      master.gain.value=0;
      master.connect(ctx.destination);
    }
    if(ctx.state==='suspended') ctx.resume().catch(()=>{});
  }

  function clearNodes(){
    nodes.forEach(n=>{try{n.stop&&n.stop();}catch(e){} try{n.disconnect&&n.disconnect();}catch(e){}});
    nodes=[];
  }

  function osc(freq,type='sine',gain=.1,detune=0){
    const o=ctx.createOscillator();
    const g=ctx.createGain();
    o.type=type;o.frequency.value=freq;o.detune.value=detune;g.gain.value=gain;
    o.connect(g);g.connect(master);o.start();nodes.push(o,g);return {o,g};
  }

  function start(mode){
    ensure();
    currentMode=mode;
    clearNodes();
    const now=ctx.currentTime;
    master.gain.cancelScheduledValues(now);
    master.gain.setValueAtTime(.0001,now);

    if(mode==='strobe'){
      osc(36,'sine',.34);
      osc(72,'sine',.16);
      osc(108,'sine',.08);
      osc(216,'sine',.045);
      osc(432,'sine',.022);
      const sweep=osc(90,'sine',.07);
      const lfo=ctx.createOscillator(), depth=ctx.createGain();
      lfo.frequency.value=.11;depth.gain.value=34;lfo.connect(depth);depth.connect(sweep.o.frequency);lfo.start();nodes.push(lfo,depth);
      master.gain.exponentialRampToValueAtTime(.52,now+.35);
    }else{
      osc(36,'sine',.26);
      osc(72,'sine',.12);
      osc(144,'sine',.05);
      osc(288,'sine',.024);
      const tone=osc(631,'sine',.035);
      const lfo=ctx.createOscillator(), depth=ctx.createGain();
      lfo.frequency.value=.08;depth.gain.value=.014;lfo.connect(depth);depth.connect(tone.g.gain);lfo.start();nodes.push(lfo,depth);
      master.gain.exponentialRampToValueAtTime(.46,now+.65);
    }
    active=true;
  }

  function fade(to,time=.8){
    if(!ctx||!master) return;
    const now=ctx.currentTime;
    master.gain.cancelScheduledValues(now);
    master.gain.setValueAtTime(Math.max(.0001,master.gain.value),now);
    master.gain.exponentialRampToValueAtTime(Math.max(.0001,to),now+time);
  }

  function bind(){
    const calm=document.getElementById('btnCalm');
    const strobe=document.getElementById('btnStrobe');
    const room=document.getElementById('room');

    if(calm) calm.addEventListener('click',()=>{
      start('calm');
      if(ctx&&ctx.state==='suspended') ctx.resume();
    },{capture:true});

    if(strobe) strobe.addEventListener('click',()=>{
      start('strobe');
      if(ctx&&ctx.state==='suspended') ctx.resume();
    },{capture:true});

    if(room && 'IntersectionObserver' in window){
      new IntersectionObserver(entries=>{
        const visible=entries.some(e=>e.isIntersecting&&e.intersectionRatio>.08);
        if(!active) return;
        fade(visible?(currentMode==='strobe'?.52:.46):.0001,visible?.5:.35);
      },{threshold:[0,.08,.2]}).observe(room);
    }
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',bind,{once:true});
  else bind();
})();
