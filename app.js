document.querySelector('#year').textContent=new Date().getFullYear();
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),motion=document.querySelector('#motion-toggle');
let paused=reduced.matches;
function motionState(){document.body.classList.toggle('motion-paused',paused);motion.setAttribute('aria-pressed',String(paused));motion.textContent=paused?'▷ Motion':'Ⅱ Motion';updateStack()}
motion.addEventListener('click',()=>{paused=!paused;motionState()});reduced.addEventListener('change',e=>{paused=e.matches;motionState()});
const cards=[...document.querySelectorAll('.stack-card')];let scheduled=false;
function updateStack(){cards.forEach((card,i)=>{const next=cards[i+1];if(!next||paused||reduced.matches){card.style.transform='';return}const rect=next.getBoundingClientRect(),start=innerHeight*.95,end=110+i*14;const progress=Math.max(0,Math.min(1,(start-rect.top)/(start-end)));card.style.transform=`scale(${1-progress*.035}) rotate(${-progress*1.2}deg)`});scheduled=false}
addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(updateStack)}},{passive:true});addEventListener('resize',updateStack);
const reveal=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');reveal.unobserve(e.target)}}),{threshold:.08});document.querySelectorAll('.work-intro,.section-heading,.plan,.faq,.launch').forEach(el=>{el.classList.add('reveal');reveal.observe(el)});
const navLinks=[...document.querySelectorAll('.rail a')];const navObserver=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){navLinks.forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}})},{rootMargin:'-15% 0px -55% 0px'});navLinks.forEach(a=>{const el=document.querySelector(a.hash);if(el)navObserver.observe(el)});
motionState();
