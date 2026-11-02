from pathlib import Path
p=Path('dist/index.html');s=p.read_text(encoding='utf-8')
s=s.replace('in your tone and your language','in your tone')
s=s.replace('<a href="#languages">Languages</a>','')
s=s.replace('<span>◎ Pick your language</span>','<span>✧ Review your reply</span>')
s=s.replace('<p>◎ &nbsp; Your language</p>','')
start=s.index('<article class="feature language">');end=s.index('</article>',start)+len('</article>');s=s[:start]+s[end:]
start=s.index('<section class="section language-section"');end=s.index('</section>',start)+len('</section>');s=s[:start]+s[end:]
s=s.replace('<span>✓ Your language</span>','<span>✓ Your perspective</span>')
s=s.replace('Can I change the tone and language?','Can I change the tone?')
s=s.replace(', with support for English, Hindi, Gujarati, and Hinglish.','.')
p.write_text(s,encoding='utf-8')
p=Path('dist/app.js');s=p.read_text(encoding='utf-8').replace(',.language-grid article','');p.write_text(s,encoding='utf-8')
