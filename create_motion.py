from pathlib import Path
import subprocess
filters=[]
def box(x,y,w,h,color,enable=None):
    f=f'drawbox=x={x}:y={y}:w={w}:h={h}:color={color}:t=fill'
    if enable:f+=f":enable='{enable}'"
    filters.append(f)
def text(value,x,y,size=24,color='0xeee7fa',enable=None,alpha=None):
    f=f"drawtext=fontfile='C\\:/Windows/Fonts/segoeui.ttf':text='{value}':x={x}:y={y}:fontsize={size}:fontcolor={color}"
    if enable:f+=f":enable='{enable}'"
    if alpha:f+=f":alpha='{alpha}'"
    filters.append(f)
box(0,0,1280,720,'0x09070e');box(0,0,7,720,'0x9a66d0')
text('ReplyVibe',65,40,29);text('PRODUCT CONCEPT / 12 SEC',940,50,14,'0x9f8caf')
text('A better reply starts with you.',65,110,42)
box(65,195,1150,435,'0x17111f');box(66,196,1148,48,'0x21182b')
text('X / HOME',90,208,15,'0xbda2d2');text('YOUR REPLY CO-PILOT',940,208,14,'0xbda2d2')
text('Jamie Parker',100,275,24);text('@jamiebuilds',265,281,16,'0x998ca5')
text('Just shipped my first side project.',100,322,29)
text('Not perfect. But finally out in the world.',100,365,23,'0xb2a5be')
box(92,425,1094,155,'0x100b18')
text('01  FIND A CONVERSATION',100,660,18,'0xc9a1f3',"lt(t,4)")
text('02  CHOOSE YOUR TONE',100,660,18,'0xc9a1f3',"between(t,4,7)")
text('03  REVIEW. MAKE IT YOURS.',100,660,18,'0xc9a1f3',"gte(t,7)")
text('What would you say?',120,465,31,'0x80728e',"lt(t,3)")
text('ReplyVibe helps you find the words.',120,515,18,'0x9e8caf',"lt(t,3)")
box(116,447,195,47,'0x7541a5',"between(t,3,6)");box(327,447,195,47,'0x2d203c',"between(t,3,6)");box(538,447,195,47,'0x2d203c',"between(t,3,6)")
text('Friendly',160,455,22,enable="between(t,3,6)");text('Professional',355,455,22,enable="between(t,3,6)");text('Supportive',568,455,22,enable="between(t,3,6)")
text('Your tone. Your conversation.',120,522,20,'0xbca3d2',"between(t,3,6)")
text('Shipping something you care about is a win in itself.',120,449,26,enable="gte(t,6)",alpha='min(1,(t-6)*2)')
text('Congrats on taking that first step!',120,493,26,enable="gte(t,7)",alpha='min(1,(t-7)*2)')
box(1000,532,158,34,'0x7846ab',"gte(t,8)")
text('Copy reply',1030,535,18,enable="between(t,8,9.5)")
text('Copied!',1042,535,18,enable="gte(t,9.5)")
text('Sample content / You always choose what to post',690,661,14,'0x96849f')
box(0,714,1280,6,'0x211629');filters.append("drawbox=x=0:y=714:w=1280:h=6:color=0xb583e9:t=fill")
filters.append('fade=t=in:st=0:d=0.4');filters.append('fade=t=out:st=11.5:d=0.5')
Path('video-filter.txt').write_text(',\n'.join(filters),encoding='utf-8')
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','color=c=0x09070e:s=1280x720:r=30:d=12','-filter_script:v','video-filter.txt','-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart','-an','dist/assets/replyvibe-motion.mp4'],check=True)
print('Created 12-second 1280x720 H.264 motion video')
