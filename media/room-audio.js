(()=>{
  let ctx=null, master=null, active=false, currentMode='calm', nodes=[], syncTimer=null, startedAt=0;
  let volume=.65;
  const AC=window.AudioContext||window.webkitAudioContext;
  if(!AC) return;

  const modeLevel=()=>currentMode==='strobe'?.48:.42;
  const audibleLevel=()=>Math.max(.0001,modeLevel()*volume);

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

  function silenceNow(){
    if(master){
      const now=ctx.currentTime;
      master.gain.cancelScheduledValues(now);
      master.gain.setValueAtTime(0,now);
    }
    clearNodes();
    active=false;
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
    master.gain.exponentialRampToValueAtTime(audibleLevel(),now+.45);
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

    const carrier=ctx.createOscillator();carrier.type='sine';carrier.frequency.value=144;
    const harmonic=ctx.createOscillator();harmonic.type='sine';harmonic.frequency.value=288;
    const carrierGain=ctx.createGain();carrierGain.gain.value=.12;
    const harmonicGain=ctx.createGain();harmonicGain.gain.value=.035;
    carrier.connect(carrierGain);harmonic.connect(harmonicGain);
    carrierGain.connect(master);harmonicGain.connect(master);

    const lfo=ctx.createOscillator();lfo.type='sine';lfo.frequency.value=6;
    const lfoDepth=ctx.createGain();lfoDepth.gain.value=.085;
    lfo.connect(lfoDepth);lfoDepth.connect(carrierGain.gain);

    osc(36,'sine',.16);
    carrier.start();harmonic.start();lfo.start();
    nodes.push(carrier,harmonic,carrierGain,harmonicGain,lfo,lfoDepth);

    startedAt=performance.now();
    const sync=()=>{
      if(!active||currentMode!=='strobe') return;
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
    active=true;
    sync();syncTimer=setInterval(sync,50);
    master.gain.exponentialRampToValueAtTime(audibleLevel(),now+.3);
  }

  function start(mode){
    ensure();
    silenceNow();
    currentMode=mode;
    active=true;
    mode==='strobe'?startStrobe():startCalm();
    active=true;
  }

  function reconcile(){
    const calm=document.getElementById('btnCalm');
    const strobe=document.getElementById('btnStrobe');
    const calmOn=!!(calm&&calm.classList.contains('on'));
    const strobeOn=!!(strobe&&strobe.classList.contains('on'));
    if(strobeOn){if(!active||currentMode!=='strobe')start('strobe');return;}
    if(calmOn){if(!active||currentMode!=='calm')start('calm');return;}
    silenceNow();
  }

  function setVolume(v){
    volume=Math.max(0,Math.min(1,Number(v)||0));
    if(ctx&&master&&active){
      const now=ctx.currentTime;
      master.gain.cancelScheduledValues(now);
      master.gain.setTargetAtTime(volume===0?0:audibleLevel(),now,.04);
    }
  }

  function addVolumeControl(){
    const controls=document.querySelector('#room .room-ctrl');
    if(!controls||document.getElementById('roomVolume')) return;
    const wrap=document.createElement('label');
    wrap.className='room-volume';
    wrap.setAttribute('aria-label','3D visualiser volume');
    wrap.innerHTML='<span>room vol</span><input id="roomVolume" type="range" min="0" max="100" value="65" step="1"><output id="roomVolumeValue">65%</output>';
    controls.appendChild(wrap);
    const input=wrap.querySelector('input');
    const out=wrap.querySelector('output');
    input.addEventListener('input',()=>{out.textContent=input.value+'%';setVolume(input.value/100);});

    const style=document.createElement('style');
    style.textContent='.room-volume{display:flex;align-items:center;gap:8px;padding:8px 12px;border:1px solid var(--line);background:rgba(8,11,15,.5);backdrop-filter:blur(6px);font:8px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--dim);white-space:nowrap}.room-volume input{width:92px;accent-color:var(--filament);cursor:pointer}.room-volume output{min-width:30px;text-align:right;color:var(--filament);font:8px var(--mono);letter-spacing:.04em}@media(max-width:780px){.room-ctrl{flex-wrap:wrap}.room-volume{width:100%;justify-content:flex-end}.room-volume input{width:min(180px,42vw)}}';
    document.head.appendChild(style);
  }

  function bind(){
    const calm=document.getElementById('btnCalm');
    const strobe=document.getElementById('btnStrobe');
    const strobeGo=document.getElementById('strobeGo');
    const room=document.getElementById('room');
    addVolumeControl();

    [calm,strobe,strobeGo].forEach(el=>{
      if(el) el.addEventListener('click',()=>setTimeout(reconcile,0));
    });

    if(calm&&strobe){
      const mo=new MutationObserver(()=>reconcile());
      mo.observe(calm,{attributes:true,attributeFilter:['class']});
      mo.observe(strobe,{attributes:true,attributeFilter:['class']});
    }

    if(room && 'IntersectionObserver' in window){
      new IntersectionObserver(entries=>{
        const visible=entries.some(e=>e.isIntersecting&&e.intersectionRatio>.08);
        if(!active||!master) return;
        const now=ctx.currentTime;
        master.gain.cancelScheduledValues(now);
        master.gain.setTargetAtTime(visible?audibleLevel():0,now,visible?.08:.04);
      },{threshold:[0,.08,.2]}).observe(room);
    }
  }

  window.COTRoomAudio={stop:silenceNow,setVolume,reconcile};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',bind,{once:true});
  else bind();
})();
