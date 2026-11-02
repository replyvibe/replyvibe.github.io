document.querySelector('#year').textContent=new Date().getFullYear();
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
const motionButton=document.querySelector('#motion-toggle');
let paused=reducedMotion.matches;
function updateMotion(){document.body.classList.toggle('motion-paused',paused);motionButton.textContent=paused?'▷ Resume motion':'Ⅱ Pause motion';motionButton.setAttribute('aria-pressed',String(paused))}
motionButton.addEventListener('click',()=>{paused=!paused;updateMotion()});
reducedMotion.addEventListener('change',event=>{paused=event.matches;updateMotion()});
const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');revealObserver.unobserve(entry.target)}}),{threshold:.08});
document.querySelectorAll('.section-top,.feature,.steps article,.language-grid article,.history-features>div,.statement,.faq-section,.launch').forEach(element=>{element.classList.add('reveal');revealObserver.observe(element)});
updateMotion();
