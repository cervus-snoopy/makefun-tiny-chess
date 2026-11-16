import json,os,sys,urllib.request as u
E=os.environ.get('MAKEFUN_ENV_URL') or sys.exit('no env')
V=[0,100,320,330,500,900,0];M=1e5
x=0x9e3779b97f4a7c15
def R():
 global x;x=(x*6364136223846793005+1442695040888963407)&(1<<64)-1;return x
Z=[[R()for _ in range(128)]for _ in range(13)];ZS=R();ZC=[R()for _ in range(16)];ZE=[R()for _ in range(8)]
X=b'PPPPPPPP!6wu!4ls5!6N!4X!57U^dUsG1!57VlI`REU(LjMbUET-OgPJ^Po!579s=MXx_!5(gPPPPPPP!3^!6c!6KA!72!3g!6g!4Xsq!75,Cx!5-82!7/9md!6A!5,3!5/kRs@q!51T-b]M`GR3A_fNYNX!5;C8!6=YRd0K!4_!6i+jaEYLJr!4_!6A]?!6EA>!6>.U!6?n!5;!4tp!6IVMK`C)NY_pCP2GLdP^X:NJL`PPO^GHJ[Q@W_]0.oEIXQ5c!6IZFd]!5.g]@UkTcC!5;c!53iWZ=ma!57(^cdN[!59D@Z_[Z@^3:eYOeMK4EmL[X]?!4t!6HV_aOG!58[Nmn?!6CAOR!4pAsV?!6^3k!4rLiQflGZ!4aP[P`c=SF?bOXNWJEaCYMW]G(ldGVW>TN?Yd7FJ=A!6mI1!5;gu[a2=^OT.Yer:>Lka!58UMXAMU[:C!6D6DIR[>vPH8R_`DmVA!5,fljO9!6G8!4s!6R,!6HFBPPPPPPP!7wKA8^Arg!4WVA>EMnR!50HEHIV^PLLDLPO[LUSCWOKTIfKPRSCRGWPPPPPPP!5*ejAMT,,!6_b?hI@Q4mToOFHF:iedPPEM6P]gYGQC:KeRaKC?N<gZUS>M;`:mXIT0B!6FIZSQNHIaT[=YFYFaFXOOXJTI]SMULIOHYZVDSCJMY[RSFFHQL[VUCJDT_BcLI[DoMXMMPLMVRPNBVUKTPPNOINRWOZDQONSQRSLGONMWTKTJKTHZPVREPNXJ[QLLHb8[pPUPHGZ+v]Yb/U2<kS!6<ND@FJdRf]?b;!5.!6BGm@SU@)E!6>GSXIK5OI_PICTOUV;w5];/xbPWkE;UnMSPfADOWVHUjO1;oRSOWI9;_jSSLB<Ha_ZRIG@>a`YQFGD,d^Z?_F=!7A!8tm!74!<X!(t!6s!8/a!8K!;,!*,PPQPQRL';T=[];v=0;i=0
while i<len(X):
 c=X[i];i+=1
 if c==33:v+=((X[i]-40-(X[i]>91))*80+X[i+1]-40-(X[i+1]>91))-1100;i+=2
 else:v+=c-80-(c>91)
 T.append(v)
MG=[0]*1664;EG=[0]*1664
for q in range(128):
 if q&136:continue
 r=q>>4;f=q&7;i=(7-r)*8+f;j=r*8+f
 for t in range(1,7):
  MG[(t+6)*128+q]=T[768+t-1]+T[(t-1)*64+i];MG[(6-t)*128+q]=-(T[768+t-1]+T[(t-1)*64+j])
  EG[(t+6)*128+q]=T[774+t-1]+T[384+(t-1)*64+i];EG[(6-t)*128+q]=-(T[774+t-1]+T[384+(t-1)*64+j])
CK={0:13,7:14,4:12,112:7,119:11,116:3}
KN=(-33,-31,-18,-14,14,18,31,33);KI=(-17,-16,-15,-1,1,15,16,17);BI=(-17,-15,15,17);RI=(-16,-1,1,16)
B=[0]*128;S=1;C=0;Y=-1;W=0;WK=4;BK=116;H=0;U=[];HS=set();PC={};L=0;TT={};KL=[0]*256;EM=EE=PH=0
Q=b')4)L-+bg.Z+d)PK-f^.;0,<K=3[e.I5U./;5dCU]6G`1^7f(P+?B],/A_12_AaUJ9B]QU=C]3QXEX,*(IW0J*N;BSLP>V,ZUKQPJZ41S+]PQ*+^aKI]dNAUZ';P={}
for i in range(0,120,5):
 n=0
 for c in Q[i:i+5]:n=n*64+c-40-(c>91)
 P[n>>14]=n&16383
D=Exception()
A='abcdefgh'
def J(m):return A[m&7]+str(((m&127)>>4)+1)+A[(m>>7)&7]+str((((m>>7)&127)>>4)+1)+('nbrq'[(m>>14)-2] if m>>14 else '')
def at(q,by):
 b=B
 for d in (-15,-17) if by>0 else (15,17):
  z=q+d
  if 0<=z<128 and not z&136 and b[z]==by:return 1
 for ds,pp in ((KN,2),(KI,6)):
  for d in ds:
   z=q+d
   if 0<=z<128 and not z&136 and b[z]==by*pp:return 1
 for d in BI:
  z=q+d
  while 0<=z<128 and not z&136:
   p=b[z]
   if p:
    if p==by*3 or p==by*5:return 1
    break
   z+=d
 for d in RI:
  z=q+d
  while 0<=z<128 and not z&136:
   p=b[z]
   if p:
    if p==by*4 or p==by*5:return 1
    break
   z+=d
 return 0
def PP(ms,q,to):
 if to>>4 in(0,7):
  for pr in(5,4,3,2):ms.append(q|to<<7|pr<<14)
 else:ms.append(q|to<<7)
def G(o):
 b=B;ms=[]
 for q,p in enumerate(b):
  if p*S<=0:continue
  t=abs(p)
  if t==1:
   d=16*S;to=q+d
   if not b[to] and (not o or to>>4 in(0,7)):
    PP(ms,q,to)
    if not o and to>>4 not in(0,7) and (S>0 and q>>4==1 or S<0 and q>>4==6) and not b[q+2*d]:ms.append(q|(q+2*d)<<7)
   for z in(q+d-1,q+d+1):
    if z&136 or z<0 or z>=128:continue
    if b[z]*S<0 or z==Y:PP(ms,q,z)
  elif t==2:
   for d in KN:
    z=q+d
    if 0<=z<128 and not z&136 and b[z]*S<=0 and (not o or b[z]):ms.append(q|z<<7)
  elif t==6:
   for d in KI:
    z=q+d
    if 0<=z<128 and not z&136 and b[z]*S<=0 and (not o or b[z]):ms.append(q|z<<7)
   kf=4 if S>0 else 116
   for bt,md,to,rk,fr in ((1,5,6,7,-1),(2,3,2,0,1)) if S>0 else ((4,117,118,119,-1),(8,115,114,112,113)):
    if not o and C&bt and not b[md] and not b[to] and b[rk]==4*S and (fr<0 or not b[fr]) and not at(kf,-S) and not at(md,-S) and not at(to,-S):ms.append(kf|to<<7)
  else:
   ds=BI if t==3 else RI if t==4 else BI+RI
   for d in ds:
    z=q+d
    while 0<=z<128 and not z&136:
     if b[z]*S<=0 and (not o or b[z]):ms.append(q|z<<7)
     if b[z]:break
     z+=d
 return ms
def K(m):
 global S,C,Y,W,WK,BK,H,EM,EE,PH
 b=B;f=m&127;t=m>>7&127;pr=m>>14;p=b[f];cp=b[t];ec=-1
 if abs(p)==1 and t==Y and not cp:ec=t-16*S;cp=b[ec]
 e=ec if ec>=0 else t
 U.append((cp,C,Y,W,H,WK,BK,ec,f,t,p,pr,EM,EE,PH))
 u=MG;g=EG;o=(p+6)*128
 dm=u[(pr*S+6)*128+t]-u[o+f] if pr else u[o+t]-u[o+f]
 de=g[(pr*S+6)*128+t]-g[o+f] if pr else g[o+t]-g[o+f]
 dp=T[780+pr]
 if cp:
  c=(cp+6)*128+e;dm-=u[c];de-=g[c];dp-=T[780+abs(cp)]
 if abs(p)==6 and abs(t-f)==2:
  r=f+3 if t>f else f-4;v=f+1 if t>f else f-1;dm+=u[(4*S+6)*128+v]-u[(4*S+6)*128+r];de+=g[(4*S+6)*128+v]-g[(4*S+6)*128+r]
 EM+=dm;EE+=de;PH+=dp
 H^=Z[p+6][f]
 if cp:H^=Z[cp+6][e]
 b[f]=0;b[t]=pr*S if pr else p
 H^=Z[b[t]+6][t]
 if ec>=0:b[ec]=0
 if abs(p)==6 and abs(t-f)==2:
  r=f+3 if t>f else f-4;v=f+1 if t>f else f-1;b[v]=b[r];b[r]=0;H^=Z[10 if S>0 else 2][r];H^=Z[10 if S>0 else 2][v]
 H^=ZC[C];C&=CK.get(f,15)&CK.get(t,15);H^=ZC[C]
 if Y>=0:H^=ZE[Y&7]
 Y=f+16*S if abs(p)==1 and abs(t-f)==32 else -1
 if Y>=0:H^=ZE[Y&7]
 W=0 if abs(p)==1 or cp else W+1
 if abs(p)==6:
  if p>0:WK=t
  else:BK=t
 H^=ZS;S=-S
 if at(WK if p>0 else BK,S):O();return 0
 return 1
def O():
 global S,C,Y,W,H,WK,BK,EM,EE,PH
 b=B;cp,C,Y,W,H,WK,BK,ec,f,t,p,pr,EM,EE,PH=U.pop()
 S=-S;b[f]=p;b[t]=0 if ec>=0 else cp
 if ec>=0:b[ec]=-S
 if abs(p)==6 and abs(t-f)==2:
  if t>f:b[f+3]=b[f+1];b[f+1]=0
  else:b[f-4]=b[f-1];b[f-1]=0
def EV():
 ph=min(PH,24)
 s=(EM*ph+EE*(24-ph))//24
 return s*S
def OD(ms,tm,pl):
 b=B;r=[]
 for m in ms:
  s=0;t=m>>7&127;c=b[t]
  if m==tm:s=1000000
  else:
   if c:s=100000+10*V[abs(c)]-abs(b[m&127])
   if m>>14:s+=200000+V[m>>14]
   elif m==KL[pl*2]:s=50000
   elif m==KL[pl*2+1]:s=40000
  r.append((-s,m))
 r.sort();return [m for _,m in r]
def QS(a,b,pl):
 global N
 N+=1
 if N>L:raise D
 if pl>64:return EV()
 k=WK if S>0 else BK;ch=at(k,-S)
 if ch:bt=-M-1
 else:
  st=EV()
  if st>=b:return st
  bt=st
  if st>a:a=st
 lg=0
 for m in (OD(G(1),0,pl) if not ch else OD(G(0),0,pl)):
  if not K(m):continue
  lg+=1;s=-QS(-b,-a,pl+1);O()
  if s>bt:bt=s
  if s>=b:return s
  if s>a:a=s
 if ch and not lg:return -M+pl
 return bt
def SR(d,a,b,pl):
 global N
 N+=1
 if N>L:raise D
 if pl>0 and (W>=100 or H in HS or PC.get(H,0)>1):return 0
 if d<=0:return QS(a,b,pl)
 e=TT.get(H);tm=0
 if e and e[0]>=d:
  s=e[1]
  if s>M-1000:s-=pl
  elif s<-M+1000:s+=pl
  tm=e[3]
  if e[2]==1:return s
  if e[2]==2 and s>=b:return s
  if e[2]==3 and s<=a:return s
 a0=a;bt=-M-1;bm=0;lg=0
 for m in OD(G(0),tm,pl):
  if not K(m):continue
  lg+=1;PC[H]=PC.get(H,0)+1;s=-SR(d-1,-b,-a,pl+1);PC[H]-=1;O()
  if s>bt:bt=s;bm=m
  if s>a:a=s
  if a>=b:
   if not B[m>>7&127] and not m>>14:
    if KL[pl*2]!=m:KL[pl*2+1]=KL[pl*2];KL[pl*2]=m
   break
 if not lg:return -M+pl if at(WK if S>0 else BK,-S) else 0
 ss=bt+pl if bt>M-1000 else bt-pl if bt<-M+1000 else bt
 TT[H]=(d,ss,3 if bt<=a0 else 2 if bt>=b else 1,bm)
 if len(TT)>1e6:TT.clear()
 return bt
def RT(ms):
 global L,N
 N=0;bt=ms[0];od=ms
 k=H&65535
 if k in P:
  for m in ms:
   if m==P[k]:return m
 for d in range(1,65):
  L=1e9 if d==1 else 1.5e5
  try:
   sc={};a=-M-1
   for m in od:
    K(m);PC[H]=PC.get(H,0)+1;s=-SR(d-1,-M-1,-a,1);PC[H]-=1;O();sc[m]=s
    if s>a:a=s
   od=sorted(od,key=lambda m:-sc[m]);bt=od[0]
   if sc[bt]>=M-200:break
  except:break
 return bt
def PO(p,bo):
 q=u.Request(E+p,data=json.dumps(bo).encode())
 try:
  with u.urlopen(q) as r:return json.load(r)
 except:sys.exit()
def PF(fn):
 global S,C,Y,W,H,WK,BK,EM,EE,PH
 f=fn.split();B[:]=[0]*128;H=0;EM=EE=PH=0
 for i,row in enumerate(f[0].split('/')):
  r=7-i;c=0
  for ch in row:
   if ch.isdigit():c+=int(ch)
   else:
    q=(r<<4)+c;p=('pnbrqk'.index(ch.lower())+1)*(1 if ch.isupper() else -1);B[q]=p;t=abs(p);H^=Z[p+6][q];EM+=MG[(p+6)*128+q];EE+=EG[(p+6)*128+q];PH+=T[780+t]
    if t==6:
     if p>0:WK=q
     else:BK=q
    c+=1
 S=1 if f[1]=='w' else -1;C=0
 if f[2]!='-':
  for ch in f[2]:C|=1<<'KQkq'.index(ch)
 Y=-1 if f[3]=='-' else (int(f[3][1])-1)*16+A.index(f[3][0]);W=int(f[4])
 if S<0:H^=ZS
 H^=ZC[C]
 if Y>=0:H^=ZE[Y&7]
def LG():
 ms=[]
 for m in G(0):
  if K(m):ms.append(m);O()
 return ms
