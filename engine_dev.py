import json,os,sys,urllib.request as u
E=os.environ.get('MAKEFUN_ENV_URL') or sys.exit('no env')
V=[0,100,320,330,500,900,0];M=1e5
x=0x9e3779b97f4a7c15
def R():
 global x;x=(x*6364136223846793005+1442695040888963407)&(1<<64)-1;return x
Z=[[R() for _ in range(128)] for _ in range(13)];ZS=R();ZC=[R() for _ in range(16)];ZE=[R() for _ in range(8)]
MGV=[82,337,365,477,1025,0];EGV=[94,281,297,512,936,0];PV=[0,0,1,1,2,4,0]
MGP=[[0, 0, 0, 0, 0, 0, 0, 0, 98, 134, 61, 95, 68, 126, 34, -11, -6, 7, 26, 31, 65, 56, 25, -20, -14, 13, 6, 21, 23, 12, 17, -23, -27, -2, -5, 12, 17, 6, 10, -25, -26, -4, -4, -10, 3, 3, 33, -12, -35, -1, -20, -23, -15, 24, 38, -22, 0, 0, 0, 0, 0, 0, 0, 0],
 [-167, -89, -34, -49, 61, -97, -15, -107, -73, -41, 72, 36, 23, 62, 7, -17, -47, 60, 37, 65, 84, 129, 73, 44, -9, 17, 19, 53, 37, 69, 18, 22, -13, 4, 16, 13, 28, 19, 21, -8, -23, -9, 12, 10, 19, 17, 25, -16, -29, -53, -12, -3, -1, 18, -14, -19, -105, -21, -58, -33, -17, -28, -19, -23],
 [-29, 4, -82, -37, -25, -42, 7, -8, -26, 16, -18, -13, 30, 59, 18, -47, -16, 37, 43, 40, 35, 50, 37, -2, -4, 5, 19, 50, 37, 37, 7, -2, -6, 13, 13, 26, 34, 12, 10, 4, 0, 15, 15, 15, 14, 27, 18, 10, 4, 15, 16, 0, 7, 21, 33, 1, -33, -3, -14, -21, -13, -12, -39, -21],
 [32, 42, 32, 51, 63, 9, 31, 43, 27, 32, 58, 62, 80, 67, 26, 44, -5, 19, 26, 36, 17, 45, 61, 16, -24, -11, 7, 26, 24, 35, -8, -20, -36, -26, -12, -1, 9, -7, 6, -23, -45, -25, -16, -17, 3, 0, -5, -33, -44, -16, -20, -9, -1, 11, -6, -71, -19, -13, 1, 17, 16, 7, -37, -26],
 [-28, 0, 29, 12, 59, 44, 43, 45, -24, -39, -5, 1, -16, 57, 28, 54, -13, -17, 7, 8, 29, 56, 47, 57, -27, -27, -16, -16, -1, 17, -2, 1, -9, -26, -9, -10, -2, -4, 3, -3, -14, 2, -11, -2, -5, 2, 14, 5, -35, -8, 11, 2, 8, 15, -3, 1, -1, -18, -9, 10, -15, -25, -31, -50],
 [-65, 23, 16, -15, -56, -34, 2, 13, 29, -1, -20, -7, -8, -4, -38, -29, -9, 24, 2, -16, -20, 6, 22, -22, -17, -20, -12, -27, -30, -25, -14, -36, -49, -1, -27, -39, -46, -44, -33, -51, -14, -14, -22, -46, -44, -30, -15, -27, 1, 7, -8, -64, -43, -16, 9, 8, -15, 36, 12, -54, 8, -28, 24, 14]]
EGP=[[0, 0, 0, 0, 0, 0, 0, 0, 178, 173, 158, 134, 147, 132, 165, 187, 94, 100, 85, 67, 56, 53, 82, 84, 32, 24, 13, 5, -2, 4, 17, 17, 13, 9, -3, -7, -7, -8, 3, -1, 4, 7, -6, 1, 0, -5, -1, -8, 13, 8, 8, 10, 13, 0, 2, -7, 0, 0, 0, 0, 0, 0, 0, 0],
 [-58, -38, -13, -28, -31, -27, -63, -99, -25, -8, -25, -2, -9, -25, -24, -52, -24, -20, 10, 9, -1, -9, -19, -41, -17, 3, 22, 22, 22, 11, 8, -18, -18, -6, 16, 25, 16, 17, 4, -18, -23, -3, -1, 15, 10, -3, -20, -22, -42, -20, -10, -5, -2, -20, -23, -44, -29, -51, -23, -15, -22, -18, -50, -64],
 [-14, -21, -11, -8, -7, -9, -17, -24, -8, -4, 7, -12, -3, -13, -4, -14, 2, -8, 0, -1, -2, 6, 0, 4, -3, 9, 12, 9, 14, 10, 3, 2, -6, 3, 13, 19, 7, 10, -3, -9, -12, -3, 8, 10, 13, 3, -7, -15, -14, -18, -7, -1, 4, -9, -15, -27, -23, -9, -23, -5, -9, -16, -5, -17],
 [13, 10, 18, 15, 12, 12, 8, 5, 11, 13, 13, 11, -3, 3, 8, 3, 7, 7, 7, 5, 4, -3, -5, -3, 4, 3, 13, 1, 2, 1, -1, 2, 3, 5, 8, 4, -5, -6, -8, -11, -4, 0, -5, -1, -7, -12, -8, -16, -6, -6, 0, 2, -9, -9, -11, -3, -9, 2, 3, -1, -5, -13, 4, -20],
 [-9, 22, 22, 27, 27, 19, 10, 20, -17, 20, 32, 41, 58, 25, 30, 0, -20, 6, 9, 49, 47, 35, 19, 9, 3, 22, 24, 45, 57, 40, 57, 36, -18, 28, 19, 47, 31, 34, 39, 23, -16, -27, 15, 6, 9, 17, 10, 5, -22, -23, -30, -16, -16, -23, -36, -32, -33, -28, -22, -43, -5, -32, -20, -41],
 [-74, -35, -18, -18, -11, 15, 4, -17, -12, 17, 14, 17, 17, 38, 23, 11, 10, 17, 23, 15, 20, 45, 44, 13, -8, 22, 24, 27, 26, 33, 26, 3, -18, -4, 21, 24, 27, 23, 9, -11, -19, -3, 11, 21, 23, 16, 7, -9, -27, -11, 4, 13, 14, 4, -5, -17, -53, -34, -21, -11, -28, -14, -24, -43]]
MG=[0]*1664;EG=[0]*1664
for q in range(128):
 if q&136:continue
 r=q>>4;f=q&7;i=(7-r)*8+f;j=r*8+f
 for t in range(1,7):
  MG[(t+6)*128+q]=MGV[t-1]+MGP[t-1][i];MG[(6-t)*128+q]=-(MGV[t-1]+MGP[t-1][j])
  EG[(t+6)*128+q]=EGV[t-1]+EGP[t-1][i];EG[(6-t)*128+q]=-(EGV[t-1]+EGP[t-1][j])
CK={0:13,7:14,4:12,112:7,119:11,116:3}
KN=(-33,-31,-18,-14,14,18,31,33);KI=(-17,-16,-15,-1,1,15,16,17);BI=(-17,-15,15,17);RI=(-16,-1,1,16)
B=[0]*128;S=1;C=0;Y=-1;W=0;NP=0;WB=0;BB=0;WK=4;BK=116;H=0;U=[];HS=set();PC={};N=0;L=40000;TT={};KL=[0]*256;EM=EE=PH=0
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
 global S,C,Y,W,NP,WB,BB,WK,BK,H,EM,EE,PH
 b=B;f=m&127;t=m>>7&127;pr=m>>14;p=b[f];cp=b[t];ec=-1
 if abs(p)==1 and t==Y and not cp:ec=t-16*S;cp=b[ec]
 U.append((cp,C,Y,W,H,NP,WB,BB,WK,BK,ec,f,t,p,pr,EM,EE,PH))
 u=MG;g=EG;o=(p+6)*128
 dm=u[(pr*S+6)*128+t]-u[o+f] if pr else u[o+t]-u[o+f]
 de=g[(pr*S+6)*128+t]-g[o+f] if pr else g[o+t]-g[o+f]
 dp=PV[pr]
 if cp:
  c=(cp+6)*128+(ec if ec>=0 else t);dm-=u[c];de-=g[c];dp-=PV[abs(cp)]
 if abs(p)==6 and abs(t-f)==2:
  r=f+3 if t>f else f-4;v=f+1 if t>f else f-1;dm+=u[(4*S+6)*128+v]-u[(4*S+6)*128+r];de+=g[(4*S+6)*128+v]-g[(4*S+6)*128+r]
 EM+=dm;EE+=de;PH+=dp
 H^=Z[p+6][f]
 if cp:H^=Z[cp+6][ec if ec>=0 else t]
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
 if cp:
  if abs(cp)!=1:NP-=V[abs(cp)]
  if abs(cp)==3:
   if cp>0:WB-=1
   else:BB-=1
 if pr:NP+=V[pr]
 if abs(p)==6:
  if p>0:WK=t
  else:BK=t
 H^=ZS;S=-S
 if at(WK if p>0 else BK,S):O();return 0
 return 1
def O():
 global S,C,Y,W,H,NP,WB,BB,WK,BK,EM,EE,PH
 b=B;cp,C,Y,W,H,NP,WB,BB,WK,BK,ec,f,t,p,pr,EM,EE,PH=U.pop()
 S=-S;b[f]=p;b[t]=0 if ec>=0 else cp
 if ec>=0:b[ec]=-S
 if abs(p)==6 and abs(t-f)==2:
  if t>f:b[f+3]=b[f+1];b[f+1]=0
  else:b[f-4]=b[f-1];b[f-1]=0
def EV():
 ph=min(PH,24)
 s=(EM*ph+EE*(24-ph))//24
 return s if S>0 else -s
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
 TT[H]=(d,ss,1 if bt<=a0 else 2 if bt>=b else 3,bm)
 if len(TT)>1e6:TT.clear()
 return bt
def RT(ms):
 global L,N
 N=0;bt=ms[0];od=ms
 for d in range(1,65):
  L=9**9 if d==1 else 1.5e5
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
 global S,C,Y,W,H,NP,WB,BB,WK,BK,EM,EE,PH
 f=fn.split();B[:]=[0]*128;H=0;NP=0;WB=0;BB=0;EM=EE=PH=0
 for i,row in enumerate(f[0].split('/')):
  r=7-i;c=0
  for ch in row:
   if ch.isdigit():c+=int(ch)
   else:
    q=(r<<4)+c;p=('pnbrqk'.index(ch.lower())+1)*(1 if ch.isupper() else -1);B[q]=p;t=abs(p);H^=Z[p+6][q];EM+=MG[(p+6)*128+q];EE+=EG[(p+6)*128+q];PH+=PV[t]
    if t!=1:NP+=V[t]
    if t==3:
     if p>0:WB+=1
     else:BB+=1
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
