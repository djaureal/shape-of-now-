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
    master.gain.setValueAtTime(Math.max(.0001,master.gain.value),now);

    if(mode==='strobe'){
      osc(36,'sine',.16);
      osc(72,'sine',.075);
      osc(108,'sine',.025);
      const sweep=osc(54,'sine',.035);
      const lfo=ctx.createOscillator(), depth=ctx.createGain();
      lfo.frequency.value=.11;depth.gain.value=22;lfo.connect(depth);depth.connect(sweep.o.frequency);lfo.start();nodes.push(lfo,depth);
      master.gain.exponentialRampToValueAtTime(.34,now+.7);
    }else{
      osc(36,'sine',.13);
      osc(72,'sine',.045);
      const tone=osc(631,'sine',.009);
      const pulse=ctx.createGain();
      pulse.gain.value=.5;tone.g.disconnect();tone.g.connect(pulse);pulse.connect(master);nodes.push(pulse);
      master.gain.exponentialRampToValueAtTime(.24,now+1.4);
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
    if(calm) calm.addEventListener('click',()=>start('calm'),{capture:true});
    if(strobe) strobe.addEventListener('click',()=>start('strobe'),{capture:true});

    if(room && 'IntersectionObserver' in window){
      new IntersectionObserver(entries=>{
        const visible=entries.some(e=>e.isIntersecting&&e.intersectionRatio>.08);
        if(!active) return;
        fade(visible?(currentMode==='strobe'?.34:.24):.0001,visible?.8:.45);
      },{threshold:[0,.08,.2]}).observe(room);
    }
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',bind,{once:true});
  else bind();
})();
