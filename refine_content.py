from pathlib import Path
p=Path('dist/index.html');s=p.read_text(encoding='utf-8')
s=s.replace('<a href="#demo">Try the demo</a>','<a href="#languages">Languages</a>')
s=s.replace('href="#demo"><span>✦</span> Find your reply vibe','href="#features"><span>✦</span> Explore ReplyVibe')
s=s.replace('href="#film"><span class="play">▷</span> Watch it work','href="#how-it-works"><span class="play">↗</span> How it works')
start=s.index('<div class="product-window"');end=s.index('</section><div class="benefit-strip">',start)
s=s[:start]+'''<div class="product-overview"><div class="overview-header"><span class="brand small"><span class="feather">✦</span>ReplyVibe<span class="ai">AI</span></span><span>MADE FOR CONVERSATIONS ON 𝕏</span></div><div class="overview-main"><div class="overview-intro"><span class="eyebrow">A REPLY THAT FEELS RIGHT</span><h2>Your voice.<br>A little more <span class="gradient">possibility.</span></h2><p>Choose how you want to sound.<br>Find the words. Make them your own.</p></div><div class="voice-options"><span>▣ <b>Professional</b><small>Keep it considered.</small></span><span>☺ <b>Friendly</b><small>Keep it conversational.</small></span><span>♡ <b>Supportive</b><small>Show a little encouragement.</small></span><span>ϟ <b>Witty</b><small>Add a little personality.</small></span></div></div><div class="overview-footer"><span>✧ Choose your tone</span><i></i><span>◎ Pick your language</span><i></i><span>↗ Make it yours</span></div></div>
''' + s[end:]
start=s.index('<section class="section film-section"');end=s.index('<section class="statement section">',start)
s=s[:start]+'''<section class="section language-section" id="languages"><div class="language-copy"><span class="eyebrow">SAY IT YOUR WAY</span><h2>A conversation feels better<br>in <span class="soft-purple">your language.</span></h2><p>From a quick hello to a thoughtful response, write in the language that feels natural to you.</p></div><div class="language-grid"><article><span lang="en">Hello.</span><p>English</p></article><article><span lang="hi">नमस्ते.</span><p>Hindi</p></article><article><span lang="gu">નમસ્તે.</span><p>Gujarati</p></article><article><span>Hey, kya haal?</span><p>Hinglish</p></article></div></section>
<section class="section history-section"><div><span class="eyebrow">KEEP THE CONVERSATION GOING</span><h2>Your activity.<br><span class="soft-purple">All in one place.</span></h2><p>See your reply usage, follow your weekly activity, and revisit recent replies from your ReplyVibe dashboard.</p></div><div class="history-features"><div><span>ϟ</span><h3>Reply usage</h3><p>Keep track of the replies you generate.</p></div><div><span>↗</span><h3>Weekly activity</h3><p>See how your replying habit takes shape.</p></div><div><span>↶</span><h3>Recent replies</h3><p>Find your previous replies in one place.</p></div></div></section>
''' +s[end:]
start=s.index('<details><summary>Is the demo using live AI?');end=s.index('</details>',start)+len('</details>');s=s[:start]+s[end:]
s=s.replace('AI DOES THE THINKING WITH YOU.','YOUR PERSPECTIVE COMES FIRST.')
s=s.replace('From idea to reply. Instantly.','From idea to reply.')
p.write_text(s,encoding='utf-8')
Path('dist/app.js').write_text('''document.querySelector('#year').textContent=new Date().getFullYear();
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
const motionButton=document.querySelector('#motion-toggle');
let paused=reducedMotion.matches;
function updateMotion(){document.body.classList.toggle('motion-paused',paused);motionButton.textContent=paused?'▷ Resume motion':'Ⅱ Pause motion';motionButton.setAttribute('aria-pressed',String(paused))}
motionButton.addEventListener('click',()=>{paused=!paused;updateMotion()});
reducedMotion.addEventListener('change',event=>{paused=event.matches;updateMotion()});
const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');revealObserver.unobserve(entry.target)}}),{threshold:.08});
document.querySelectorAll('.section-top,.feature,.steps article,.language-grid article,.history-features>div,.statement,.faq-section,.launch').forEach(element=>{element.classList.add('reveal');revealObserver.observe(element)});
updateMotion();
''',encoding='utf-8')
