const replies={Friendly:"Shipping something you care about is a win in itself. Congrats on taking that first step — excited to see where it goes! 🚀",Professional:"Congratulations on the launch. Taking an idea from concept to a shipped product is a meaningful achievement. Looking forward to seeing how it develops.",Witty:"The hardest feature to ship is the courage to hit publish. Looks like you just nailed that one. 🚀",Supportive:"That first step takes so much courage. It doesn't have to be perfect to be worth sharing — you should be proud of yourself. 💜"};
document.querySelectorAll('[data-tone]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-tone]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button))});document.querySelector('#reply').textContent=replies[button.dataset.tone];document.querySelector('#copy').textContent='▢  Copy reply'}));
document.querySelector('#copy').addEventListener('click',async function(){try{await navigator.clipboard.writeText(document.querySelector('#reply').textContent);this.textContent='✓  Copied!';setTimeout(()=>this.textContent='▢  Copy reply',2000)}catch{this.textContent='Select reply to copy';const selection=window.getSelection();const range=document.createRange();range.selectNodeContents(document.querySelector('#reply'));selection.removeAllRanges();selection.addRange(range)}});
document.querySelector('#year').textContent=new Date().getFullYear();
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
const motionButton=document.querySelector('#motion-toggle');
const demoButton=document.querySelector('#auto-demo');
const film=document.querySelector('#walkthrough-video');
let paused=reducedMotion.matches, autoDemo=!paused, demoTimer, typingTimer;
function stopTyping(){clearInterval(typingTimer);document.querySelector('.reply-panel').classList.remove('is-typing')}
function animateReply(button){
  stopTyping();
  document.querySelectorAll('[data-tone]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button))});
  const panel=document.querySelector('.reply-panel'),reply=document.querySelector('#reply'),value=replies[button.dataset.tone];
  reply.setAttribute('aria-live','off');reply.textContent='';panel.classList.add('is-typing');let cursor=0;
  typingTimer=setInterval(()=>{cursor+=3;reply.textContent=value.slice(0,cursor);if(cursor>=value.length)stopTyping()},24);
}
function updateDemo(){clearInterval(demoTimer);demoButton.setAttribute('aria-pressed',String(autoDemo));demoButton.textContent=autoDemo?'Ⅱ Pause demo':'▷ Play demo';if(autoDemo&&!paused){demoTimer=setInterval(()=>{if(document.hidden)return;const buttons=[...document.querySelectorAll('[data-tone]')];const current=buttons.findIndex(b=>b.classList.contains('active'));animateReply(buttons[(current+1)%buttons.length])},5500)}}
document.querySelectorAll('[data-tone]').forEach(button=>button.addEventListener('click',()=>{stopTyping();autoDemo=false;updateDemo();document.querySelector('#reply').textContent=replies[button.dataset.tone];document.querySelector('#reply').setAttribute('aria-live','polite')}));
demoButton.addEventListener('click',()=>{autoDemo=!autoDemo;if(autoDemo&&paused){paused=false;updateMotion()}stopTyping();document.querySelector('#reply').textContent=replies[document.querySelector('[data-tone].active').dataset.tone];updateDemo()});
function updateMotion(){document.body.classList.toggle('motion-paused',paused);motionButton.textContent=paused?'▷ Resume motion':'Ⅱ Pause motion';motionButton.setAttribute('aria-pressed',String(paused));if(paused){stopTyping();film.pause();document.querySelector('#reply').textContent=replies[document.querySelector('[data-tone].active').dataset.tone]}updateDemo()}
motionButton.addEventListener('click',()=>{paused=!paused;updateMotion()});
motionButton.addEventListener('click',()=>{const bounds=film.getBoundingClientRect();if(!paused&&bounds.top<innerHeight&&bounds.bottom>0)film.play().catch(()=>{})});
document.querySelector('#copy').addEventListener('click',()=>{stopTyping();autoDemo=false;updateDemo();document.querySelector('#reply').textContent=replies[document.querySelector('[data-tone].active').dataset.tone]},true);
reducedMotion.addEventListener('change',event=>{paused=event.matches;updateMotion()});
const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');revealObserver.unobserve(entry.target)}}),{threshold:.08});
document.querySelectorAll('.section-top,.feature,.steps article,.film-frame,.momentum-copy,.activity-ui,.statement,.faq-section,.launch').forEach(element=>{element.classList.add('reveal');revealObserver.observe(element)});
const videoObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting&&!paused){film.play().catch(()=>{})}else{film.pause()}}),{threshold:.35});videoObserver.observe(film);
document.addEventListener('visibilitychange',()=>{if(document.hidden){film.pause();stopTyping()}});
updateMotion();
