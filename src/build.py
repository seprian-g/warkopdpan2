from PIL import Image, ImageOps
import base64, io, re
U='/root/.claude/uploads/2a2c632b-644f-586d-a0f1-a1ff5a64af1e/'
def uri(name, box=None, w=900, q=74):
    im=ImageOps.exif_transpose(Image.open(U+name)).convert('RGB')
    if box:
        W,H=im.size; im=im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
    im=im.resize((w, round(w*im.height/im.width)), Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=q); return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
old=open('/home/claude/site/warkop-dpan.html').read()
logo=re.search(r'src="(data:image/webp;base64,[^"]+)" alt="Logo', old).group(1)
s=open('src.html').read()
s=s.replace('__LOGO__',logo)
s=s.replace('__IMG_HERO__',uri('0a1cadc8-image.jpg',(0,.23,1,.83),1000,74))
s=s.replace('__IMG_ATAS__',uri('9c5aec58-image.jpg',None,720,70))
s=s.replace('__IMG_KASIR__',uri('d9dacee9-image.jpg',None,720,70))
s=s.replace('__IMG_DAPUR__',uri('07aea7ec-image.jpg',None,720,70))
s=s.replace('__IMG_KERUPUK__',uri('77be376d-image.jpg',None,720,70))
import base64 as B
s=s.replace('__POSTER__','data:image/jpeg;base64,'+B.b64encode(open('poster.jpg','rb').read()).decode()).replace('__VIDEO__','data:video/mp4;base64,'+B.b64encode(open('hero.mp4','rb').read()).decode())
open('warkop-dpan-landing.html','w').write(s); print(len(s)//1024,'KB')
