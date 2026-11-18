from PIL import Image,ImageOps,ImageEnhance,ImageFilter,ImageDraw,ImageFont
import numpy as np
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET
import json,zipfile
ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'custom-assets'
OUT=ROOT.parent/'outputs';OUT.mkdir(exist_ok=True)
RNG=np.random.default_rng(4814); N=1600
# All keyframes belong to one 28.6-second clock; face returns after two symbols.
names=['face','coding','vercel','face','database','api','face']
holds=[3,2.5,2.5,3,2.5,2.5]; transition=1.6
clock=[0.]; indices=[0]
for k,h in enumerate(holds):
 clock.extend([clock[-1]+h,clock[-1]+h+transition]);indices.extend([k,k+1])
DURATION=clock[-1]; keys=np.array(clock)/DURATION

def sample(mask):
 ys,xs=np.where(mask); pts=np.stack([xs,ys],axis=1).astype(float)
 # Uniform candidates plus farthest-point sampling avoids random clumps.
 if len(pts)>18000:pts=pts[np.linspace(0,len(pts)-1,18000).astype(int)]
 dist=np.full(len(pts),np.inf); picked=[];j=int(len(pts)//2)
 for _ in range(N):
  picked.append(j);dist=np.minimum(dist,((pts-pts[j])**2).sum(axis=1));j=int(dist.argmax())
 return pts[picked]

def match(src,dst):
 # Greedy assignment refined with cost-decreasing swaps; no crossing reset at loop.
 ids=[];available=np.ones(N,bool)
 for p in src:
  d=((dst-p)**2).sum(axis=1);d[~available]=np.inf;j=int(d.argmin());ids.append(j);available[j]=False
 result=dst[ids].copy()
 for _ in range(250):
  a=RNG.permutation(N);b=np.roll(a,1)
  old=((src[a]-result[a])**2).sum(1)+((src[b]-result[b])**2).sum(1)
  new=((src[a]-result[b])**2).sum(1)+((src[b]-result[a])**2).sum(1)
  # Disjoint pairs so accepted swaps cannot overwrite each other.
  a=a[::2];b=b[::2];good=(new<old)[::2]
  aa=a[good];bb=b[good];result[aa],result[bb]=result[bb].copy(),result[aa].copy()
 return result

logo_masks={}
for name in ['coding','vercel','database','api']:
 im=Image.open(ASSETS/(name+'.png')).convert('RGBA')
 base=Image.new('RGBA',im.size,'white');base.alpha_composite(im);lum=ImageOps.grayscale(base.convert('RGB'))
 # Preserve complete uploaded artwork, including faint marks in the API image.
 ink=lum if name=='vercel' else ImageOps.invert(lum)
 box=ink.getbbox();ink=ink.crop(box)
 ink=ImageOps.contain(ink,(244,244),Image.Resampling.LANCZOS)
 canvas=Image.new('L',(300,340));canvas.paste(ink,((300-ink.width)//2,(340-ink.height)//2))
 logo_masks[name]=np.array(canvas.convert('1'))
logo_points={name:sample(mask) for name,mask in logo_masks.items()}
photo=ImageOps.fit(Image.open(ASSETS/'portrait.png').convert('RGB'),(300,340),centering=(.5,.4))
mask=np.min(np.asarray(photo),axis=2)<225
mask=np.asarray(Image.fromarray(mask).filter(ImageFilter.MaxFilter(5)))
gray=ImageEnhance.Contrast(ImageOps.autocontrast(ImageOps.grayscale(photo),cutoff=1).filter(ImageFilter.UnsharpMask(radius=3,percent=140))).enhance(1.3)
bits=np.asarray(gray.convert('1'))
rows=[('Subject','HARIHARAN B'),('Role','Full Stack Developer'),('Origin','Coimbatore, Tamil Nadu'),('Education','M.Sc Computer Science'),('Status','Building + Learning'),('ToolChain','VS Code / PyCharm / Figma'),('Frontend','HTML / CSS / JavaScript'),('Backend','Python / Node.js'),('Database','PostgreSQL / SQL'),('Mail','hariharan4814@gmail.com'),('Portfolio','hariharanb.me'),('LinkedIn','in/hariharan4814'),('GitHub','hariharan4814')]
kt=';'.join(f'{v:.8f}' for v in keys)
splines=';'.join(['.42 0 .58 1']*(len(keys)-1))
def anim(attr,values):
 return f'<animate attributeName="{attr}" values="'+ ';'.join(str(v) for v in values)+f'" keyTimes="{kt}" calcMode="spline" keySplines="{splines}" dur="{DURATION:g}s" repeatCount="indefinite"/>'
all_data={}
for theme in ['dark','light']:
 dark=theme=='dark';bg='#0A101F' if dark else '#F8FAFC';panel='#111B30' if dark else '#EEF2FF';ink='#F8FAFC' if dark else '#172033';muted='#94A3B8' if dark else '#526078';cyan='#22D3EE' if dark else '#0891B2';violet='#A78BFA' if dark else '#7C3AED'
 selected=(bits & mask) if dark else (~bits)
 face=sample(selected)
 states=[face]
 for name in names[1:]:states.append(face if name=='face' else match(states[-1],logo_points[name]))
 states=np.array(states);np.save(ROOT/(theme+'-custom-points.npy'),states)
 all_data[theme]=(states,selected)
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610" role="img" aria-labelledby="title desc"><title id="title">HARIHARAN B | Full Stack Developer</title><desc id="desc">Portrait, Coding, Vercel, portrait, Database, API, repeating. Artwork supplied by Hariharan.</desc>',f'<rect x="1" y="1" width="1178" height="608" rx="20" fill="{bg}" stroke="{cyan}" stroke-opacity=".35"/>',f'<path d="M1 62H1179" stroke="{cyan}" stroke-opacity=".25"/>']
 def text(x,y,s,size=14,color=None,extra=''):
  parts.append(f'<text x="{x}" y="{y}" font-family="Consolas,monospace" font-size="{size}" fill="{color or ink}" {extra}>{escape(s)}</text>')
 for x,c in [(28,'#FB7185'),(50,'#FBBF24'),(72,'#34D399')]:parts.append(f'<circle cx="{x}" cy="32" r="6" fill="{c}"/>')
 text(100,37,'profile.sh --live',16,muted);text(1000,37,'● LIVE',13,'#F87171')
 parts.append(f'<rect x="26" y="86" width="402" height="484" rx="12" fill="{panel}"/>');text(48,116,'VISUAL.MAP',13,cyan);text(454,116,'SYSTEM.INFO',13,cyan)
 parts.append(f'<g transform="translate(77 139)" fill="{violet}">')
 # Dense portrait supplies detail; it gently drifts and dissolves into travellers.
 ys,xs=np.where(selected);group_ids=RNG.integers(0,72,len(xs))
 for g in range(72):
  gx=xs[group_ids==g];gy=ys[group_ids==g]
  path=''.join(f'M{x} {y}h.85v.85h-.85z' for x,y in zip(gx,gy))
  dx=round(float(RNG.normal(0,13)),2);dy=round(float(RNG.normal(0,10)),2)
  op=[1 if names[i]=='face' else 0 for i in indices]
  moves=[('0 0' if names[i]=='face' else f'{dx} {dy}') for i in indices]
  parts.append(f'<path d="{path}">'+anim('opacity',op)+f'<animateTransform attributeName="transform" type="translate" values="'+ ';'.join(moves)+f'" keyTimes="{kt}" calcMode="spline" keySplines="{splines}" dur="{DURATION:g}s" repeatCount="indefinite"/></path>')
 parts.append('<g opacity="0">'+anim('opacity',[0 if names[i]=='face' else 1 for i in indices]))
 for j in range(N):
  coords=states[indices,j,:];moves=';'.join(f'{x:g} {y:g}' for x,y in coords)
  parts.append(f'<circle r="1.55"><animateTransform attributeName="transform" type="translate" values="{moves}" keyTimes="{kt}" calcMode="spline" keySplines="{splines}" dur="{DURATION:g}s" repeatCount="indefinite"/></circle>')
 parts.append('</g>')
 parts.append('</g>');text(48,518,'CODE / VERCEL / DATABASE / API',14,violet);text(48,547,'BUILD. LEARN. REPEAT.',12,muted)
 for i,(k,v) in enumerate(rows):
  y=154+i*28;text(454,y,k,14,muted);text(640,y,'····',14,muted);text(1140,y,v,14,ink,'text-anchor="end"')
 text(454,553,'> Building + Learning',16,'#10B981');text(454,581,'hariharan4814  /  full stack developer',12,muted)
 parts.append('</svg>');(OUT/(theme+'.svg')).write_text('\n'.join(parts),encoding='utf-8')
 root=ET.parse(OUT/(theme+'.svg')).getroot()
 for el in root.iter():
  if el.tag.split('}')[-1] in ['animate','animateTransform']:
   vals=el.attrib['values'].split(';');assert len(vals)==len(keys);assert vals[0]==vals[-1]
 assert np.array_equal(states[0],states[-1]);assert names[3]=='face'
 print(theme,(OUT/(theme+'.svg')).stat().st_size,'bytes; loop continuity and animation keyframes verified')
# Preview uses exactly the same positions, easing and opacity curves as the SVG.
def ease(q):
 lo,hi=0.,1.
 for _ in range(18):
  u=(lo+hi)/2;x=3*(1-u)**2*u*.42+3*(1-u)*u*u*.58+u**3
  if x<q:lo=u
  else:hi=u
 return 3*(1-u)*u*u+u**3

def frame(theme,t,scale=1):
 states,selected=all_data[theme];dark=theme=='dark';bg=np.array([17,27,48] if dark else [238,242,255]);fg=np.array([167,139,250] if dark else [124,58,237]);k=min(np.searchsorted(clock,t,side='right')-1,len(clock)-2);q=ease((t-clock[k])/(clock[k+1]-clock[k]));a,b=indices[k:k+2];pa=names[a]=='face';pb=names[b]=='face';face_op=(1-q)*pa+q*pb
 arr=np.tile(bg,(340,300,1)).astype(np.uint8);arr[selected]=(bg*(1-face_op)+fg*face_op).astype(np.uint8);im=Image.fromarray(arr).resize((600,680));d=ImageDraw.Draw(im);pos=states[a]*(1-q)+states[b]*q;op=1-face_op;r=1.55*2
 color=tuple((bg*(1-op)+fg*op).astype(int))
 if op>0:
  for x,y in pos*2:d.ellipse((x-r,y-r,x+r,y+r),fill=color)
 return im.resize((300,340),Image.Resampling.LANCZOS)
strip=Image.new('RGB',(1800,380),'#111B30');draw=ImageDraw.Draw(strip)
for i,t in enumerate([1,5.6,9.7,14,19,23]):strip.paste(frame('dark',t),(i*300,0));draw.text((i*300+100,355),names[i].upper(),fill='white')
strip.save(OUT/'custom-sequence.png')
frames=[frame('dark',float(t)) for t in np.arange(0,DURATION,.1)]
frames[0].save(OUT/'morph-preview.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=False)
(OUT/'preview.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>Hariharan custom morph</title></head><body style="background:#ddd;font-family:system-ui;margin:24px"><h2>Dark theme</h2><img src="dark.svg" width="1180" style="max-width:100%"><h2>Light theme</h2><img src="light.svg" width="1180" style="max-width:100%"><p>Face → Coding → Vercel → Face → Database → API → repeat. One cycle takes 28.6 seconds.</p></body></html>',encoding='utf-8')
p=OUT/'README.md';s=p.read_text(encoding='utf-8');start=s.index('Requested morph order:');end=s.index('\n',start);s=s[:start]+'Requested morph order: Face -> Coding -> Vercel -> Face -> Database -> API -> repeat.'+s[end:];s=s.replace('technology logos','your uploaded artwork');p.write_text(s,encoding='utf-8');(OUT/'HARIHARAN_B_README.txt').write_text(s,encoding='utf-8')
(OUT/'SETUP.txt').write_text('Upload dark.svg, light.svg and README.md to the main branch of hariharan4814/hariharan4814.\nOpen preview.html locally to see both SVG animations.\nSequence: Face -> Coding -> Vercel -> Face -> Database -> API -> repeat.\nPortrait holds: 3 seconds. Symbol holds: 2.5 seconds. Transitions: 1.6 seconds.\nThe supplied artwork is embedded as dots; no external images or solid-logo overlays are used.\nThe API source contains a faint watermark; use a licensed clean source if you want a clean replacement.\nSource generator requires Python, Pillow and NumPy; run source/build_custom.py after creating outputs/README.md from the supplied README.\n',encoding='utf-8')
with zipfile.ZipFile(OUT/'HARIHARAN_Custom_Profile.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['dark.svg','light.svg','README.md','HARIHARAN_B_README.txt','preview.html','custom-sequence.png','morph-preview.gif','SETUP.txt']:z.write(OUT/name,name)
 z.write(__file__,'source/build_custom.py')
 for f in ASSETS.iterdir():z.write(f,'source/custom-assets/'+f.name)
 for theme in ['dark','light']:z.write(ROOT/(theme+'-custom-points.npy'),'source/'+theme+'-custom-points.npy')
print('Custom package complete')
