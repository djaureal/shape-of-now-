(()=>{
  let ctx=null, master=null, active=false, currentMode='calm', nodes=[], syncTimer=null, startedAt=0;
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
    if(syncTimer){clearInterval(syncTimer);syncTimer=null;}
    nodes.forEach(n=>{try{n.stop&&n.stop();}catch(e){} try{n.disconnect&&n.disconnect();}catch(e){}});
    nodes=[];
  }

  function osc(freq,type='sine',gain=.1){
    const o=ctx.createOscillator();
    const g=ctx.createGain();
    o.type=type;o.frequency.value=freq;g.gain.value=gain;
    o.connect(g);g.connect(master);o.start();nodes.push(o,g);return {o,g};
  }

  function startCalm(){
    clearNodes();
    const now=ctx.currentTime;
    master.gain.cancelScheduledValues(now);
    master.gain.setValueAtTime(.0001,now);
    osc(36,'sine',.24);
    osc(72,'sine',.11);
    osc(144,'sine',.05);
    osc(288,'sine',.022);
    osc(631,'sine',.03);
    master.gain.exponentialRampToValueAtTime(.42,now+.65);
  }

  function strobeBand(seconds){
    const lt=(seconds%24)/24;
    if(lt<0.15) return 6;
    if(lt<0.33) return 10;
    if(lt<0.52) return 18;
    if(lt<0.86) return 40;
    return 0;
  }

  function startStrobe(){
    clearNodes();
    const now=ctx.currentTime;
    master.gain.cancelScheduledValues(now);
    master.gain.setValueAtTime(.0001,now);

    // Audible carrier stack. The displayed 6/10/18/40 Hz value is the
    // actual amplitude-modulation (entrainment) rate applied to this stack.
    const carrier=ctx.createOscillator();carrier.type='sine';carrier.frequency.value=144;
    const harmonic=ctx.createOscillator();harmonic.type='sine';harmonic.frequency.value=288;
    const carrierGain=ctx.createGain();carrierGain.gain.value=.12;
    const harmonicGain=ctx.createGain();harmonicGain.gain.value=.035;
    carrier.connect(carrierGain);harmonic.connect(harmonicGain);
    carrierGain.connect(master);harmonicGain.connect(master);

    const lfo=ctx.createOscillator();lfo.type='sine';lfo.frequency.value=6;
    const lfoDepth=ctx.createGain();lfoDepth.gain.value=.085;
    lfo.connect(lfoDepth);lfoDepth.connect(carrierGain.gain);

    const sub=osc(36,'sine',.16);
    carrier.start();harmonic.start();lfo.start();
    nodes.push(carrier,harmonic,carrierGain,harmonicGain,lfo,lfoDepth);

    startedAt=performance.now();
    const sync=()=>{
      const sec=(performance.now()-startedAt)/1000;
      const hz=strobeBand(sec);
      const t=ctx.currentTime;
      if(hz>0){
        lfo.frequency.setTargetAtTime(hz,t,.025);
        carrierGain.gain.setTargetAtTime(.12,t,.05);
        harmonicGain.gain.setTargetAtTime(hz>=18?.05:.035,t,.05);
      }else{
        carrierGain.gain.setTargetAtTime(.025,t,.10);
        harmonicGain.gain.setTargetAtTime(.006,t,.10);
      }
    };
    sync();syncTimer=setInterval(sync,50);
    master.gain.exponentialRampToValueAtTime(.48,now+.35);
  }

  function start(mode){
    ensure();
    currentMode=mode;
    mode==='strobe'?startStrobe():startCalm();
    active=true;
  }

  function stop(){
    if(!ctx||!master){active=false;return;}
    const now=ctx.currentTime;
    master.gain.cancelScheduledValues(now);
    master.gain.setTargetAtTime(.0001,now,.06);
    setTimeout(()=>{clearNodes();},260);
    active=false;
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
    const strobeGo=document.getElementById('strobeGo');
    const room=document.getElementById('room');

    if(calm) calm.addEventListener('click',()=>setTimeout(()=>{
      calm.classList.contains('on')?start('calm'):stop();
    },0));

    if(strobe) strobe.addEventListener('click',()=>setTimeout(()=>{
      strobe.classList.contains('on')?start('strobe'):stop();
    },0));

    if(strobeGo) strobeGo.addEventListener('click',()=>setTimeout(()=>{
      const b=document.getElementById('btnStrobe');
      if(b&&b.classList.contains('on')) start('strobe');
    },0));

    if(room && 'IntersectionObserver' in window){
      new IntersectionObserver(entries=>{
        const visible=entries.some(e=>e.isIntersecting&&e.intersectionRatio>.08);
        if(!active) return;
        fade(visible?(currentMode==='strobe'?.48:.42):.0001,visible?.5:.35);
      },{threshold:[0,.08,.2]}).observe(room);
    }
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',bind,{once:true});
  else bind();
})();
