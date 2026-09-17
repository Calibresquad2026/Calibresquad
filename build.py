#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calibre Squad site generator.

Every page shares one shell - head, stylesheet, masthead, footer, scripts -
and differs only in its metadata and its body. Editing a page means editing
the matching *_BODY constant below, or the shared block if the change is
site-wide, then running this script.

    python3 build.py           rebuild every page
    python3 build.py --check   verify the files on disk match, change nothing

--check exits non-zero on any drift, so it is safe to run before committing.

Assets, the microsites (auramix/, hva-comply/), robots.txt and sitemap.xml
are NOT generated - they are committed files and this script never touches them.
"""

import io
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Shared shell
# --------------------------------------------------------------------------
HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%TITLE%</title>
<meta name="description" content="%DESC%">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="canonical" href="%CANON%">
<meta name="theme-color" content="#FBFBF9">
<meta property="og:type" content="%OG%">
<meta property="og:site_name" content="Calibre Squad">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="%TITLE%">
<meta property="og:description" content="%DESC%">
<meta property="og:url" content="%CANON%">
<meta property="og:image" content="https://calibresquad.com.au/assets/og-crest.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@calibresquad">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<script>/* apply the saved ground before paint so there is no flash */
(function(){try{var t=localStorage.getItem('cs-ground');
if(t==='dark'||t==='mixed')document.documentElement.setAttribute('data-t',t);}catch(e){}})();</script>
<style>"""

CSS = """
*,*::before,*::after{box-sizing:border-box}
body{margin:0}
img{max-width:100%;display:block}
button{font:inherit;color:inherit}

:root{
  --ink:#0E0E0F;
  --body-ink:#26262A;
  --paper:#FBFBF9;
  --paper-2:#F2F2EF;
  --muted:#6C6C70;
  --line:#DCDCD7;
  --line-soft:#EAEAE5;
  --dw:400;
  --fd:'Newsreader',Georgia,serif;
  --ft:'Instrument Sans',-apple-system,'Segoe UI',sans-serif;
  --gut:clamp(1.5rem,5vw,5rem);
}
html[data-t="dark"]{
  --ink:#F4F4F1;
  --body-ink:#C9C9CE;
  --paper:#0C0C0D;
  --paper-2:#141416;
  --muted:#93939A;
  --line:#2C2C2F;
  --line-soft:#1F1F22;
  --dw:500;
}
html[data-t="mixed"] .tint{
  --ink:#F4F4F1;
  --body-ink:#C9C9CE;
  --paper:#0C0C0D;
  --paper-2:#141416;
  --muted:#93939A;
  --line:#2C2C2F;
  --line-soft:#1F1F22;
  --dw:500;
background:var(--paper);color:var(--ink)}

body{background:var(--paper);color:var(--ink);font-family:var(--ft);
  font-size:18px;line-height:1.75;font-weight:400;letter-spacing:-.004em;
  -webkit-font-smoothing:antialiased;
  transition:background .5s ease,color .5s ease}
.wrap{max-width:78rem;margin:0 auto;padding:0 var(--gut)}

.row{display:grid;grid-template-columns:11rem 1fr;gap:0 4rem;align-items:start}
.row > .label{font-size:.6875rem;font-weight:500;letter-spacing:.2em;text-transform:uppercase;
  color:var(--muted);padding-top:.55rem}
.col{max-width:38rem}
@media(max-width:860px){.row{grid-template-columns:1fr;gap:1.4rem}.row > .label{padding-top:0}}

.rule{border:0;border-top:1px solid var(--line);margin:0}
section[id]{scroll-margin-top:5.5rem}
html{scroll-behavior:smooth}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
section{padding-block:clamp(4.5rem,9vw,9.5rem);transition:background .5s ease,color .5s ease}
section.tight{padding-block:clamp(3.5rem,6vw,6rem)}
.tint{background:var(--paper-2)}

h1,h2,.display,.pull{font-family:var(--fd);font-weight:var(--dw);font-optical-sizing:auto;margin:0}
h1{font-size:clamp(3rem,8vw,6.6rem);line-height:1;letter-spacing:-.032em;max-width:15ch}
h2{font-size:clamp(1.85rem,3.6vw,3rem);line-height:1.1;letter-spacing:-.024em;max-width:20ch}
h3{font-family:var(--ft);font-size:1.0625rem;font-weight:500;letter-spacing:-.01em;margin:0 0 .5rem}
p{margin:0 0 1.35rem}
p:last-child{margin-bottom:0}
.lede{font-size:clamp(1.2rem,1.9vw,1.5rem);line-height:1.5;letter-spacing:-.015em;
  color:var(--ink);max-width:34ch;font-weight:400}
.body p{color:var(--body-ink);max-width:60ch}
.muted{color:var(--muted)}
a{color:inherit;text-decoration:underline;text-underline-offset:.28em;
  text-decoration-thickness:1px;text-decoration-color:var(--line);
  transition:text-decoration-color .35s ease}
a:hover{text-decoration-color:currentColor}

/* masthead */
.top{border-bottom:1px solid var(--line);position:sticky;top:0;z-index:60;
  background:var(--paper);transition:background .5s ease}
html[data-t="mixed"] .top{background:var(--paper)}
.top-in{display:flex;align-items:center;justify-content:space-between;gap:1.25rem;
  padding-block:1.15rem;min-height:4.6rem}
.brandmark{font-family:var(--fd);font-size:1.3rem;letter-spacing:-.015em;text-decoration:none;
  font-weight:var(--dw);white-space:nowrap}
.top-right{display:flex;align-items:center;gap:2rem}
.top nav{display:flex;gap:1.9rem}
.top nav a{font-size:.8125rem;letter-spacing:.01em;text-decoration:none;color:var(--muted)}
.top nav a:hover{color:var(--ink)}
@media(max-width:820px){.top nav{display:none}}
@media(max-width:520px){
  .brandmark{font-size:1.15rem;gap:.5rem}
  .brandmark .crest{width:26px;height:26px}
  .ground button{padding:.42rem .5rem}
}

/* ground switch */
.ground{display:flex;gap:0;border:1px solid var(--line)}
.ground button{background:transparent;border:0;border-right:1px solid var(--line);
  color:var(--muted);padding:.46rem .6rem;cursor:pointer;line-height:0;
  display:inline-flex;align-items:center;justify-content:center;
  transition:background .25s ease,color .25s ease}
.ground button svg{display:block}
.ground button:last-child{border-right:0}
.ground button:hover{color:var(--ink)}
.ground button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.ground button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}

.hero{padding-block:clamp(5rem,12vw,10.5rem) clamp(3.5rem,7vw,6.5rem)}
.kicker{font-size:.6875rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;
  color:var(--muted);margin:0 0 clamp(2rem,5vw,3.4rem)}
.hero .lede{margin-top:clamp(2rem,4vw,2.8rem)}

/* ruled rows */
.rr{display:grid;grid-template-columns:8rem 1fr auto;gap:0 2.5rem;align-items:start;
  padding:2.3rem 0;border-top:1px solid var(--line-soft)}
.rr:first-of-type{border-top:1px solid var(--line)}
.rr:last-of-type{border-bottom:1px solid var(--line)}
.rr .tagl{font-size:.6875rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted);padding-top:.3rem}
.rr p{font-size:.9688rem;line-height:1.72;color:var(--muted);max-width:52ch;margin:0}
.rr .st{font-size:.6875rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
  padding-top:.3rem;white-space:nowrap}
.rr a.more{display:inline-block;margin-top:.9rem;font-size:.875rem}
.rr .links{display:flex;flex-wrap:wrap;align-items:baseline;gap:.35rem .95rem;margin-top:.9rem}
/* client testimonial - a quote, not a card: one hairline and the display face */
.tmo{margin:0;display:flex;flex-direction:column;gap:1.15rem;
  border-left:2px solid var(--line);padding-left:clamp(1.15rem,3vw,2.1rem)}
.tmo p{font-family:var(--fd);font-weight:var(--dw);font-optical-sizing:auto;
  font-size:clamp(1.08rem,1.75vw,1.32rem);line-height:1.55;letter-spacing:-.005em;
  color:var(--ink);margin:0;max-width:58ch}
.tmo-by{display:flex;flex-direction:column;gap:.1rem;margin-top:.35rem}
.tmo-name{font-size:.9rem;font-weight:600;color:var(--ink)}
.tmo-org{font-size:.6875rem;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--muted)}
/* the client's own mark, desaturated so it sits inside the monochrome scheme */
.client-mark{display:block;width:9rem;max-width:100%;height:auto;margin-top:1.05rem;opacity:.9}
html[data-t="dark"] .client-mark{filter:invert(1);opacity:.85}
/* the pulled line on the work card */
.rr-quote{font-family:var(--fd);font-weight:var(--dw);font-size:1.02rem;line-height:1.5;
  color:var(--ink);margin:.85rem 0 0;max-width:46ch;
  display:flex;flex-direction:column;gap:.3rem}
.rr-quote span{font-family:var(--ft);font-size:.6875rem;font-weight:500;
  letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.rr .links a.more{margin-top:0}
.rr .links .sep{color:var(--line);font-size:.875rem;user-select:none}
.visit{display:inline-flex;align-items:center;gap:.45rem;text-decoration:none;
  border:1px solid var(--line);padding:.8rem 1.25rem;font-size:.8125rem;
  color:var(--ink);transition:background .25s ease,color .25s ease,border-color .25s ease}
.visit:hover,.visit:focus-visible{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.tagmini{display:inline-block;margin-left:.65rem;font-size:.5938rem;letter-spacing:.15em;
  text-transform:uppercase;color:var(--muted);border:1px solid var(--line);
  padding:.2rem .48rem;vertical-align:.22em;white-space:nowrap}
@media(max-width:820px){.rr{grid-template-columns:1fr;gap:.7rem}.rr .st{padding-top:0}}

.finding{display:grid;grid-template-columns:3.2rem 1fr;gap:0 1.6rem;
  padding:1.9rem 0;border-top:1px solid var(--line-soft);align-items:start}
.finding:first-of-type{border-top:1px solid var(--line)}
.finding:last-of-type{border-bottom:1px solid var(--line)}
.finding .num{font-family:var(--fd);font-size:1.4rem;line-height:1;color:var(--muted);padding-top:.15rem}
.finding p{font-size:.9688rem;line-height:1.7;color:var(--muted);margin:0;max-width:52ch}
@media(max-width:640px){.finding{grid-template-columns:2.2rem 1fr;gap:0 1rem}}

.phase{padding:2.4rem 0;border-top:1px solid var(--line-soft)}
.phase:first-of-type{border-top:1px solid var(--line)}
.phase:last-of-type{border-bottom:1px solid var(--line)}
.phase .when{font-size:.6875rem;font-weight:500;letter-spacing:.2em;text-transform:uppercase;
  color:var(--muted);display:block;margin-bottom:.9rem}
.phase p{font-size:.9688rem;line-height:1.75;color:var(--muted);max-width:56ch;margin:0}

.pull{font-size:clamp(1.7rem,3.4vw,2.7rem);line-height:1.18;letter-spacing:-.024em;max-width:23ch}

.figures{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line)}
.figure{padding:2.6rem 1.5rem 2.4rem 0;border-right:1px solid var(--line-soft)}
.figure:last-child{border-right:0}
.figure b{font-family:var(--fd);font-weight:var(--dw);font-size:clamp(2.6rem,5vw,4rem);
  line-height:1;display:block;letter-spacing:-.03em}
.figure span{display:block;margin-top:.85rem;font-size:.75rem;letter-spacing:.13em;
  text-transform:uppercase;color:var(--muted);line-height:1.5;max-width:12ch}
@media(max-width:760px){.figures{grid-template-columns:repeat(2,1fr)}
  .figure{padding-right:1rem;border-bottom:1px solid var(--line-soft)}
  .figure:nth-child(2n){border-right:0}}

/* contact form */
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
@media(max-width:700px){.form-row{grid-template-columns:1fr}}
.field{margin-bottom:1.5rem}
.field label{display:block;font-size:.6875rem;font-weight:500;letter-spacing:.18em;
  text-transform:uppercase;color:var(--muted);margin-bottom:.6rem}
.field input,.field textarea{width:100%;background:transparent;border:0;
  border-bottom:1px solid var(--line);color:var(--ink);font-family:var(--ft);
  font-size:1rem;padding:.6rem 0;transition:border-color .3s ease}
.field textarea{min-height:7rem;resize:vertical}
.field input:focus,.field textarea:focus{outline:none;border-bottom-color:var(--ink)}
.field input::placeholder,.field textarea::placeholder{color:var(--muted);opacity:.55}
.hp{position:absolute;left:-9999px}
.form-actions{display:flex;align-items:center;gap:1.6rem;flex-wrap:wrap;margin-top:.6rem}
.btn-primary{background:var(--ink);color:var(--paper);border:1px solid var(--ink);
  font-size:.875rem;letter-spacing:.02em;padding:.85rem 1.6rem;cursor:pointer;
  transition:opacity .3s ease}
.btn-primary:hover{opacity:.82}
.form-note{font-size:.8125rem;color:var(--muted)}
.form-status{font-size:.875rem;color:var(--muted);margin-top:1rem}

.rv{opacity:0;transform:translateY(12px);
  transition:opacity .55s cubic-bezier(.2,.7,.2,1),transform .55s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}
  *{transition:none!important}}

/* crest — recoloured to the scheme, adapts to the ground */
.crest{filter:brightness(0);opacity:.9;transition:filter .5s ease}
html[data-t="dark"] .crest{filter:brightness(0) invert(1)}
html[data-t="mixed"] .tint .crest{filter:brightness(0) invert(1)}
.brandmark{display:inline-flex;align-items:center;gap:.62rem}
.brandmark .crest{width:30px;height:30px;flex:none}

/* split hero - copy one side, crest the other, a rule between */
.hero-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.58fr);
  gap:clamp(2rem,5vw,4.6rem);align-items:center}
.hero-seal{align-self:stretch;display:flex;align-items:center;justify-content:center;
  border-left:1px solid var(--line);padding-left:clamp(2rem,5vw,4.6rem)}
.hero-seal .crest{width:min(100%,19rem);height:auto;opacity:.95}
@media(max-width:820px){
  .hero{padding-block:clamp(3.2rem,9vw,5rem) clamp(3.5rem,7vw,6.5rem)}
  .hero-split{grid-template-columns:1fr;gap:clamp(2rem,6vw,2.6rem)}
  .hero-seal{border-left:0;border-top:1px solid var(--line);
    padding-left:0;padding-top:clamp(2rem,6vw,2.6rem)}
  .hero-seal .crest{width:min(46vw,12rem)}
}

footer{border-top:1px solid var(--line);padding:3rem 0 4rem;font-size:.8125rem;color:var(--muted)}
.foot-in{display:flex;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;align-items:center}
.foot-mark{display:flex;align-items:center;gap:.7rem}
.foot-mark .crest{width:38px;height:38px;flex:none}
.foot-social{display:inline-flex;align-items:baseline;gap:.6rem}
.foot-social .sep{color:var(--line)}
"""

BODY_OPEN = "</style>\n</head>\n<body>\n"

HEADER = """<header class="top">
  <div class="wrap top-in">
    <a class="brandmark" href="/"><img class="crest" src="/assets/crest.webp" alt="" width="30" height="30"><span>Calibre Squad</span></a>
    <div class="top-right">
      <nav>
        <a href="/#capabilities">What we do</a>
        <a href="/#work">Work</a>
        <a href="/#apps">Apps</a>
        <a href="/#about">About</a>
        <a href="/#contact">Contact</a>
      </nav>
      <div class="ground" role="group" aria-label="Page appearance">
        <button type="button" data-g="light" aria-pressed="true" aria-label="Light" title="Light">
          <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false">
            <circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.35"/>
          </svg>
        </button>
        <button type="button" data-g="dark" aria-pressed="false" aria-label="Dark" title="Dark">
          <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false">
            <circle cx="8" cy="8" r="6.2" fill="currentColor"/>
          </svg>
        </button>
        <button type="button" data-g="mixed" aria-pressed="false" aria-label="Mixed" title="Mixed">
          <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false">
            <circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.35"/>
            <path d="M8 1.8a6.2 6.2 0 0 1 0 12.4z" fill="currentColor"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</header>
"""

TAIL = """
<footer>
  <div class="wrap foot-in">
    <span class="foot-mark"><img class="crest" src="/assets/crest.webp" alt="" width="38" height="38">Calibre Squad</span>
    <span>Perth, Western Australia</span>
    <span class="foot-social"><a href="https://www.youtube.com/@calibresquad" target="_blank" rel="me noopener">YouTube &#8599;</a><span class="sep" aria-hidden="true">&middot;</span><a href="https://www.facebook.com/calibresquad26" target="_blank" rel="me noopener">Facebook &#8599;</a><span class="sep" aria-hidden="true">&middot;</span><a href="https://x.com/CalibreSquad" target="_blank" rel="me noopener">X &#8599;</a><span class="sep" aria-hidden="true">&middot;</span><a href="https://www.instagram.com/calibresquad" target="_blank" rel="me noopener">Instagram &#8599;</a><span class="sep" aria-hidden="true">&middot;</span><a href="https://www.reddit.com/user/Calibresquad" target="_blank" rel="me noopener">Reddit &#8599;</a></span>
    <span>&copy; 2026 &middot; <a href="mailto:info@calibresquad.com.au">info@calibresquad.com.au</a></span>
  </div>
</footer>
<script>
(function(){
  var root=document.documentElement;
  var btns=[].slice.call(document.querySelectorAll('.ground button'));
  function sync(){var c=root.getAttribute('data-t')||'light';
    btns.forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-g')===c));});}
  btns.forEach(function(b){b.addEventListener('click',function(){
    var g=b.getAttribute('data-g');
    if(g==='light'){root.removeAttribute('data-t');}else{root.setAttribute('data-t',g);}
    try{localStorage.setItem('cs-ground',g);}catch(e){}
    sync();
  });});
  sync();
  var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els=[].slice.call(document.querySelectorAll('.rv'));
  function revealAllInReach(){
    els.forEach(function(e){
      if(e.classList.contains('in')) return;
      if(e.getBoundingClientRect().top < innerHeight*1.25) e.classList.add('in');
    });
  }
  if(reduced||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in');});}
  else{
    var io=new IntersectionObserver(function(rows){rows.forEach(function(x){
      if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},
      {threshold:0,rootMargin:'0px 0px 14% 0px'});
    els.forEach(function(e,i){e.style.transitionDelay=(Math.min(i%3,2)*55)+'ms';io.observe(e);});
    /* safety net - nothing may sit invisible in or near the viewport */
    addEventListener('scroll',revealAllInReach,{passive:true});
    addEventListener('resize',revealAllInReach,{passive:true});
    addEventListener('load',revealAllInReach);
    setTimeout(revealAllInReach,1200);
  }
})();
</script>
<script data-goatcounter="https://calibresquad.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
"""

# Only emitted on pages that actually carry the contact form.
FORM_SCRIPT = """
<script>
(function(){
  var form=document.getElementById('contact-form');
  if(!form) return;
  var status=document.getElementById('form-status');
  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(form.querySelector('[name="_honey"]').value) return;
    var name=form.name.value.trim(), email=form.email.value.trim(), message=form.message.value.trim();
    if(!name||!email||!message){status.textContent='Please fill in every field.';return;}
    status.textContent='Sending…';
    fetch('https://formsubmit.co/ajax/info@calibresquad.com.au',{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({name:name,email:email,message:message,_subject:'Enquiry from calibresquad.com.au'})
    }).then(function(r){return r.json();}).then(function(){
      form.reset();
      status.textContent='Message sent. We will be in touch shortly.';
    }).catch(function(){
      status.textContent='Something went wrong. Please email info@calibresquad.com.au instead.';
    });
  });
})();
</script>
"""

CLOSE = "</body>\n</html>\n"


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------
HOME_BODY = """
<section class="hero">
  <div class="wrap hero-split">
    <div class="hero-copy">
    <p class="kicker rv">Perth &nbsp;&middot;&nbsp; Western Australia</p>
    <h1 class="rv">Empowering excellence, from advice to application.</h1>
    <p class="lede rv">Calibre Squad is a Western Australian consultancy. We advise organisations, build the operational resources they run on, and develop purpose-built apps that put that expertise to work.</p>
  </div>
    <div class="hero-seal" aria-hidden="true"><img class="crest" src="/assets/crest.webp" alt="" width="360" height="360"></div>
  </div>
</section>

<hr class="rule">

<section class="tint" id="capabilities">
  <div class="wrap">
    <div class="row rv" style="margin-bottom:3rem">
      <div class="label">Capabilities</div>
      <div class="col">
        <h2>Three ways we work.</h2>
        <p class="muted" style="margin-top:1.4rem;max-width:46ch">Every engagement is grounded in the same standard: practical, precise, and built to hold up in the real world.</p>
      </div>
    </div>
    <div class="row rv">
      <div class="label"></div>
      <div style="max-width:58rem">
        <div class="rr">
          <span class="tagl">Advisory</span>
          <div><h3>Consultancy</h3><p>Hands-on advice for organisations that need clarity &mdash; from operational strategy and process design through to compliance and management systems that stand up to scrutiny.</p></div>
          <span class="st">Established</span>
        </div>
        <div class="rr">
          <span class="tagl">Resources</span>
          <div><h3>Resources &amp; documentation</h3><p>The working documents behind good operations: procedures, management systems, templates and reference material &mdash; written to be used, not filed away.</p></div>
          <span class="st">Established</span>
        </div>
        <div class="rr">
          <span class="tagl">Digital</span>
          <div><h3>Apps &amp; digital products</h3><p>Purpose-built software that turns our consulting and resource expertise into tools people use every day &mdash; designed around real operational workflows, not the other way round.</p></div>
          <span class="st">In beta</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="row rv" style="margin-bottom:3rem">
      <div class="label">Selected work</div>
      <div class="col">
        <h2>The brief describes the symptom.</h2>
        <p class="muted" style="margin-top:1.4rem;max-width:46ch">Most engagements arrive as one thing and turn out to be another. Finding that out early is usually where the value is.</p>
      </div>
    </div>
    <div class="row rv">
      <div class="label"></div>
      <div style="max-width:58rem">
        <div class="rr">
          <span class="tagl">Financial services</span>
          <div>
            <h3>Pura Finance Group <span class="tagmini">Case study</span></h3>
            <p>A Perth finance brokerage asked for changes to their website. It was still carrying a placeholder credit licence number, fabricated approval statistics and three testimonials that were never real. We cleared the exposure, then rebuilt.</p>
            <p class="rr-quote">&ldquo;The attention to detail and overall quality exceeded my expectations.&rdquo;<span>Lavi Midda, Pura Finance Group</span></p>
            <div class="links"><a class="more" href="/work/pura-finance-group/">Read the case study &#8594;</a><span class="sep" aria-hidden="true">&middot;</span><a class="more" href="https://purafinancegroup.com.au" target="_blank" rel="noopener">Visit the live site &#8599;</a></div>
          </div>
          <span class="st">2026</span>
        </div>
        <div class="rr">
          <span class="tagl">All projects</span>
          <div>
            <h3>More of the work</h3>
            <p>Compliance-led websites, operational systems and purpose-built software &mdash; the engagements behind the standard, and what each one actually turned out to be.</p>
            <a class="more" href="/work/">See all work &#8594;</a>
          </div>
          <span class="st"></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="tint" id="apps">
  <div class="wrap">
    <div class="row rv" style="margin-bottom:3rem">
      <div class="label">Apps</div>
      <div class="col">
        <h2>Built here. Used every day.</h2>
        <p class="muted" style="margin-top:1.4rem;max-width:46ch">Our own purpose-built apps &mdash; designed and engineered in Perth, shaped by the same standard as our consulting work.</p>
      </div>
    </div>
    <div class="row rv">
      <div class="label"></div>
      <div style="max-width:58rem">
        <div class="rr">
          <span class="tagl">iOS &middot; Audio</span>
          <div>
            <h3>AuraMix</h3>
            <p>A precision equaliser and audio toolkit for iPhone, iPad and Mac &mdash; a 31-band parametric EQ, signature presets, a live spectrum analyser and a player built around your own library.</p>
            <a class="more" href="https://auramix.com.au/">Explore AuraMix &#8594;</a>
          </div>
          <span class="st">TestFlight beta</span>
        </div>
        <div class="rr">
          <span class="tagl">Web &middot; Compliance</span>
          <div>
            <h3>HVA Comply</h3>
            <p>A WAHVA management system for Western Australian heavy-vehicle operators &mdash; pre-starts, fatigue, work diaries and audit-ready evidence in one place. Available to partners.</p>
            <a class="more" href="/hva-comply/">Explore HVA Comply &#8594;</a>
          </div>
          <span class="st">Early access</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="about">
  <div class="wrap row rv">
    <div class="label">About</div>
    <div class="col body">
      <h2 style="margin-bottom:2rem">Small team. High standard. No shortcuts.</h2>
      <p>Calibre Squad was built on a simple idea: the quality of the work should speak before we do. We keep our engagements focused, our advice honest, and our deliverables ready for the day they are needed &mdash; whether that is a boardroom, an audit, or an app store.</p>
    </div>
  </div>
  <div class="wrap rv" style="margin-top:4rem">
    <div class="figures">
      <div class="figure"><b>Perth</b><span>Western Australia</span></div>
      <div class="figure"><b>3</b><span>Consultancy &middot; Resources &middot; Apps</span></div>
      <div class="figure"><b>2</b><span>Products in the field</span></div>
      <div class="figure"><b>1</b><span>Standard, applied to all of it</span></div>
    </div>
  </div>
</section>

<section class="tint" id="contact">
  <div class="wrap row rv">
    <div class="label">Contact</div>
    <div class="col">
      <h2 style="margin-bottom:1.6rem">Let&rsquo;s talk about what you&rsquo;re building.</h2>
      <p class="muted" style="margin-bottom:3rem;max-width:44ch">Whether it is an engagement, a resource, or an idea for something digital &mdash; we would like to hear about it.</p>
      <form class="contact-form" id="contact-form" novalidate>
        <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="form-row">
          <div class="field">
            <label for="cf-name">Your name</label>
            <input id="cf-name" name="name" type="text" required autocomplete="name" placeholder="Jordan Blake">
          </div>
          <div class="field">
            <label for="cf-email">Your email</label>
            <input id="cf-email" name="email" type="email" required autocomplete="email" placeholder="you@company.com.au">
          </div>
        </div>
        <div class="field">
          <label for="cf-message">What can we help with?</label>
          <textarea id="cf-message" name="message" required placeholder="Tell us about the engagement, the resource, or the idea &mdash; whatever you&rsquo;re working on."></textarea>
        </div>
        <div class="form-actions">
          <button class="btn-primary" type="submit">Send message &#8599;</button>
          <span class="form-note">Or write to info@calibresquad.com.au</span>
        </div>
        <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""

WORK_BODY = """
<section class="hero">
  <div class="wrap hero-split">
    <div class="hero-copy">
    <p class="kicker rv">Selected work</p>
    <h1 class="rv">The work behind the standard.</h1>
    <p class="lede rv">Every engagement below started as one thing and turned out to be another. That is usually the useful part.</p>
  </div>
    <div class="hero-seal" aria-hidden="true"><img class="crest" src="/assets/crest.webp" alt="" width="360" height="360"></div>
  </div>
</section>

<hr class="rule">

<section class="tint">
  <div class="wrap row rv">
    <div class="label">Projects</div>
    <div style="max-width:58rem">
      <div class="rr">
        <span class="tagl">Financial services</span>
        <div>
          <h3>Pura Finance Group <span class="tagmini">Case study</span></h3>
          <p>A Perth asset finance brokerage asked for changes to their website. What they had was a purchased template still carrying a placeholder credit licence number, fabricated approval statistics and three testimonials that were never real. We cleared the exposure, then rebuilt.</p>
          <div class="links"><a class="more" href="/work/pura-finance-group/">Read the case study &#8594;</a><span class="sep" aria-hidden="true">&middot;</span><a class="more" href="https://purafinancegroup.com.au" target="_blank" rel="noopener">Visit the live site &#8599;</a></div>
        </div>
        <span class="st">2026</span>
      </div>
      <div class="rr">
        <span class="tagl">Heavy vehicle</span>
        <div>
          <h3>HVA Comply</h3>
          <p>Our own WAHVA management system for Western Australian heavy-vehicle operators &mdash; pre-starts, fatigue, work diaries and audit-ready evidence in one place, with a driver app built for the cab rather than the office. Available to partners.</p>
          <a class="more" href="/hva-comply/">See the product &#8594;</a>
        </div>
        <span class="st">Early access</span>
      </div>
      <div class="rr">
        <span class="tagl">Consumer &middot; iOS</span>
        <div>
          <h3>AuraMix</h3>
          <p>A precision equaliser and audio toolkit for iPhone, iPad and Mac. A 31-band parametric EQ, signature presets, a live spectrum analyser and a player built around your own library. Designed and engineered in Perth.</p>
          <a class="more" href="https://auramix.com.au/">See the product &#8594;</a>
        </div>
        <span class="st">TestFlight beta</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap row rv">
    <div class="label">Working with us</div>
    <div class="col">
      <p class="pull">If the brief turns out to be wrong, we will say so.</p>
      <p class="muted" style="margin-top:2rem;max-width:48ch">Most of the value in an engagement sits in the first week, before anything is designed or built. That is when the real problem surfaces &mdash; and it is rarely the one written on the brief.</p>
      <p style="margin-top:2rem"><a href="/#contact">Start a conversation &#8599;</a></p>
    </div>
  </div>
</section>
"""

CASE_BODY = """
<section class="hero">
  <div class="wrap hero-split">
    <div class="hero-copy">
    <p class="kicker rv"><a href="/work/" style="text-decoration:none;color:inherit">Work</a> &nbsp;&middot;&nbsp; Financial services &nbsp;&middot;&nbsp; Perth</p>
    <h1 class="rv">A compliance problem wearing a website&rsquo;s clothes.</h1>
    <p class="lede rv">Pura Finance Group asked us to make some changes to their website. Within an hour it was clear the changes were not the point.</p>
  </div>
    <div class="hero-seal" aria-hidden="true"><img class="crest" src="/assets/crest.webp" alt="" width="360" height="360"></div>
  </div>
</section>

<hr class="rule">

<section>
  <div class="wrap row rv">
    <div class="label">The brief</div>
    <div class="col body">
      <h2 style="margin-bottom:2rem">The site had been inherited, not chosen.</h2>
      <p>The business had commissioned a website from a previous developer and been handed the keys without the knowledge that comes with them. What they had was a purchased page-builder template that had never been fully de-templated &mdash; the demo content was still in place, underneath a coat of paint.</p>
      <p>That is a common enough story. What made this one urgent is that Pura Finance Group is a credit representative operating under an Australian Credit Licence. Several of the things sitting on that site were not cosmetic problems. They were representations a licensee has to be able to stand behind.</p>
      <p>So the first job was not design. It was working out what had to come off the site that day.</p>
    </div>
  </div>
</section>

<section class="tint">
  <div class="wrap">
    <div class="row rv" style="margin-bottom:3.5rem">
      <div class="label">The audit</div>
      <div class="col"><h2>What was actually on the site.</h2></div>
    </div>
    <div class="row rv">
      <div class="label"></div>
      <div style="max-width:56rem">
        <div class="finding"><span class="num">01</span><div><h3>Australian Credit Licence XXXXX</h3><p>A placeholder sat where the licence number belongs, in the footer of every page. For a credit representative that is a disclosure failure, not a typo.</p></div></div>
        <div class="finding"><span class="num">02</span><div><h3>Performance claims that could not be substantiated</h3><p>99% approval. 8,900 happy customers. $90K in daily payments. A 99.9% success rate guarantee. All template filler, all live on a regulated business.</p></div></div>
        <div class="finding"><span class="num">03</span><div><h3>Three testimonials that were never real</h3><p>Different names, the same job title, stock avatars. Demo content shipped with the template and never replaced.</p></div></div>
        <div class="finding"><span class="num">04</span><div><h3>Another company&rsquo;s name in the service copy</h3><p>The template vendor&rsquo;s brand appeared twice on the homepage, describing the services as though it were them.</p></div></div>
        <div class="finding"><span class="num">05</span><div><h3>Lorem ipsum on three homepage cards</h3><p>Placeholder Latin sitting where each service description should have been.</p></div></div>
        <div class="finding"><span class="num">06</span><div><h3>A contact form that delivered nothing</h3><p>It reported success on every submission. The messages were accepted and silently discarded. Enquiries had been going missing since launch.</p></div></div>
        <div class="finding"><span class="num">07</span><div><h3>No Credit Guide, complaints process or privacy policy</h3><p>Three documents a credit representative is expected to make available. None were published.</p></div></div>
        <div class="finding"><span class="num">08</span><div><h3>No H1 headings and no meta descriptions, anywhere</h3><p>Across every page checked. Search engines had almost nothing to work with.</p></div></div>
        <div class="finding"><span class="num">09</span><div><h3>Not one clickable phone number or email address</h3><p>On a business where most traffic arrives on a phone, the number could not be tapped to dial.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap row rv">
    <div class="label">Why it mattered</div>
    <div class="col">
      <p class="pull">Fabricated numbers on a credit licensee&rsquo;s website are not a copywriting problem.</p>
      <p class="muted" style="margin-top:2.2rem;max-width:52ch">Approval rates and customer counts are representations. Invented testimonials are misleading conduct. A placeholder where a licence number belongs is a disclosure failure. None of it had been put there deliberately &mdash; it arrived with the template &mdash; but it was published, and it was live.</p>
    </div>
  </div>
</section>

<section class="tint">
  <div class="wrap">
    <div class="row rv" style="margin-bottom:3rem">
      <div class="label">The work</div>
      <div class="col"><h2>Exposure first. Everything else after.</h2></div>
    </div>
    <div class="row rv">
      <div class="label"></div>
      <div style="max-width:56rem">
        <div class="phase"><span class="when">Day one</span><h3>Take the exposure down</h3><p>Deletions only, no design work. The fabricated statistics, the three invented testimonials, the other company&rsquo;s name, the lorem ipsum, a line offering student lending they do not provide. Nothing here needed a decision &mdash; it needed removing, and it was gone the same afternoon.</p></div>
        <div class="phase"><span class="when">Week one</span><h3>Correct the disclosure, fix what was broken</h3><p>We traced the licensing chain properly &mdash; the licensee, the Australian Credit Licence, both credit representative numbers, AFCA and FBAA memberships &mdash; and verified every figure against the AFCA register and the client&rsquo;s own documents before publishing any of it. Then the contact form, which turned out to be a longer story.</p></div>
        <div class="phase"><span class="when">Weeks two to four</span><h3>Rebuild, rather than patch</h3><p>The template was fighting every change. We rebuilt the site by hand &mdash; eleven pages, no page builder, no plugin stack &mdash; with the copy written around what the business actually does: asset and equipment finance for sole traders, companies, trusts and partnerships.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap row rv">
    <div class="label">The interesting bit</div>
    <div class="col body">
      <h2 style="margin-bottom:2rem">The form said it worked. It did not.</h2>
      <p>Every submission returned a success message. Nothing ever arrived. The obvious suspects &mdash; spam folder, wrong address, a misconfigured plugin &mdash; all came back clean.</p>
      <p>The delivery log told the real story: zero records. The messages were not failing to deliver, they were never entering a queue that delivers. The domain&rsquo;s mail runs on Microsoft 365, but the web host was accepting mail for it locally and dropping it into a mailbox that did not exist.</p>
      <p>At that point the right call is to stop debugging someone else&rsquo;s mail server. We moved the enquiry pipeline onto an email API we could observe, on a dedicated sending subdomain so the client&rsquo;s Microsoft 365 configuration was never touched. Every enquiry is now written to disk before the send is attempted, so a delivery failure can never again cost them a lead silently.</p>
    </div>
  </div>
</section>

<section class="tight tint">
  <div class="wrap rv">
    <div class="figures">
      <div class="figure"><b>11</b><span>Pages rebuilt by hand</span></div>
      <div class="figure"><b>8</b><span>Legacy URLs redirected</span></div>
      <div class="figure"><b>3</b><span>Compliance documents published</span></div>
      <div class="figure"><b>0</b><span>Placeholders remaining</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap row rv">
    <div class="label">Where it landed</div>
    <div class="col body">
      <h2 style="margin-bottom:2rem">What the business has now.</h2>
      <p>Eleven hand-built pages with a single H1 and a unique description each &mdash; previously there were none of either. Licensing disclosure that is correct and verified. A Credit Guide page, and complaints and privacy pages that now carry the licensee&rsquo;s own mandated policies, in place of the generic text the old site had borrowed.</p>
      <p>Every address from the old site &mdash; eight of them &mdash; redirects permanently to its replacement, so no bookmark and no search result was lost on the day of the switch. The changeover took under an hour, with the previous site left intact and reversible for a fortnight afterwards.</p>
      <p>And the enquiry form delivers, which it had not been doing for as long as anyone could establish.</p>
      <p style="margin-top:2.6rem"><a class="visit" href="https://purafinancegroup.com.au" target="_blank" rel="noopener">See the site we built &#8599;</a></p>
    </div>
  </div>
</section>

<hr class="rule">

<section>
  <div class="wrap row rv">
    <div class="label">In the client&rsquo;s words<img class="client-mark" src="/assets/pura-logo-mono.png" alt="Pura Finance Group" width="404" height="135" loading="lazy"></div>
    <div class="col">
      <blockquote class="tmo">
        <p>Absolutely fantastic work! I&rsquo;m extremely happy with the website that was created for my company &ldquo;Pura Finance&rdquo;. It looks modern, professional, and very impressive, while also being easy to use and highly functional. The website handles customer enquiries smoothly and keeps me updated, which makes managing everything much easier. The attention to detail and overall quality exceeded my expectations.</p>
        <p>Wonderful job, well done. I&rsquo;m a very happy client and would highly recommend their services.</p>
        <div class="tmo-by">
          <span class="tmo-name">Lavi Midda</span>
          <span class="tmo-org">Pura Finance Group</span>
        </div>
      </blockquote>
    </div>
  </div>
</section>

<section class="tint">
  <div class="wrap row rv">
    <div class="label">The through-line</div>
    <div class="col">
      <p class="pull">The brief said &ldquo;make some changes to the website&rdquo;. The job was a compliance audit that happened to end in a rebuild.</p>
      <p class="muted" style="margin-top:2rem;max-width:46ch">Most engagements are like this. The brief describes the symptom.</p>
      <p style="margin-top:2.4rem"><a href="/#contact">Start a conversation &#8599;</a></p>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

PAGES = [
    dict(
        out='index.html',
        title='Calibre Squad &mdash; Consultancy, Resources &amp; Digital Products',
        desc='Calibre Squad is a Western Australian consultancy providing advisory services, operational resources and purpose-built digital products. Empowering excellence.',
        canon='https://calibresquad.com.au/',
        og='website',
        body=HOME_BODY,
    ),
    dict(
        out='work/index.html',
        title='Work &mdash; Calibre Squad',
        desc='Selected client work and products from Calibre Squad: compliance-led websites, operational systems and purpose-built software, built in Perth, Western Australia.',
        canon='https://calibresquad.com.au/work/',
        og='website',
        body=WORK_BODY,
    ),
    dict(
        out='work/pura-finance-group/index.html',
        title='Pura Finance Group &mdash; case study &mdash; Calibre Squad',
        desc='A Perth finance brokerage asked for website changes. We found a placeholder credit licence number, fabricated statistics and a contact form quietly discarding enquiries. How we cleared the exposure and rebuilt.',
        canon='https://calibresquad.com.au/work/pura-finance-group/',
        og='article',
        body=CASE_BODY,
    ),
]


def render(page):
    head = (HEAD.replace("%TITLE%", page["title"])
                .replace("%DESC%",  page["desc"])
                .replace("%CANON%", page["canon"])
                .replace("%OG%",    page["og"]))
    body = page["body"]
    form = FORM_SCRIPT if 'id="contact-form"' in body else ""
    return head + CSS + BODY_OPEN + HEADER + body + TAIL + form + CLOSE


def main():
    check = "--check" in sys.argv
    drift = 0
    for page in PAGES:
        path = os.path.join(REPO, page["out"])
        want = render(page)
        if check:
            have = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
            if have == want:
                print("  ok      {}".format(page["out"]))
            else:
                drift += 1
                print("  DRIFT   {}  (on disk {}, generated {})".format(
                    page["out"], len(have) if have else "missing", len(want)))
        else:
            d = os.path.dirname(path)
            if d and not os.path.isdir(d):
                os.makedirs(d)
            io.open(path, "w", encoding="utf-8").write(want)
            print("  wrote   {} ({:.0f} KB)".format(page["out"], len(want) / 1024.0))
    if check and drift:
        print("\n  {} file(s) differ from what this script generates.".format(drift))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
