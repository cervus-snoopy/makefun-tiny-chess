import os,time,random,urllib.request,json
class TO(Exception):pass
D=lambda b:b-33-(b>39)-(b>92)
X=b'$F&0fp$e&3w&!n$R%Sd%p&2V&"kSSTSTUOSSSSSSSS$Vx"dv8$."P#"XagXvJ4#"YoLcUHX+OmPeXHW0RjSMaSr#"<v@P[{b"qjSSSSSSS!b$B$+D$c!k$F"Pvt$f/F{"v;5$`<pg#~"u6"xnUvCt"zW0e`PcJU6DbiQ]Q[*F;}]Ug3N"V$H.mdH]OMu"V#~`B$$DA~1X#|q*"ls$)YPNcF,Q]bsFS5JOgSa[=QMOcSSRaJKM_TCZb`31rHL[T8f$)^Ig`"wj`CXnWfF*f"|lZ^@pd#"+afgQ_(GC^b_^Ca6=h]RhPN7HpO_[`B"l$(YbdRJ##_QpqB$"DRU"hDvYB$=6n"jOlTioJ^"XS_Scf@VIBeR[QZMHdF]PZ`J+ogJYZAWQB]g:IM@D$LL4*jx_d5@aRW1]hu=AOnd##XP[DPX_=F$#9GLU_AySK;UbcGpYD"uiomR<$&;"k$2/$(IESSSSSSS%JND;aDuj"OYDAHPqU"yKHKLYaSOOGOSR_OXVFZRNWLiNSUVFUJZSSSSSSS"shmDPW//$>eBkLCT7pWrRIKI=lhgSSHP9S`j]JTF=NhUdNFBQ?j^XVAP>c=p[LW3E$%L^VTQKLdW_@]I]IdI[RR[MWL`VPXOLRK]^YGVFMP]_UVIIKTO_YXFMGWbEfOL_GrP[PPSOPYUSQEYXNWSSQRLQUZR^GTRQVTUVOJRQPZWNWMNWK^SYUHSQ[M_TOOKe;_sSXSKJ^.y`]e2X5?nV|QGCIMgUi`Be>"w$!JpCVXC,H~JV[LN8RLbSLFWRXY>z8`>2{eSZnH>XqPVSiDGRZYKXmR4>rUVRZL<>bmVVOE?Kdb^ULJCAdc]TIJG/ga^BbI@';MG=[0]*1664;EG=[0]*1664;W=[];v=0;i=0;j=0
while i<len(X):
 k=D(X[i]);i+=1
 if k<5:v+=k*92+D(X[i])-230;i+=1
 elif k==5:v+=D(X[i])*92+D(X[i+1])-1100;i+=2
 else:v+=k-49
 if j<19:W.append(v)
 else:
  k=j-19;t=k//64+1;a=k%64;q=(7-a//8)*16+a%8;w=a//8*16+a%8
  if k<384:MG[(t+6)*128+q]=W[t-1]+v;MG[(6-t)*128+w]=-W[t-1]-v
  else:t-=6;EG[(t+6)*128+q]=W[t+5]+v;EG[(6-t)*128+w]=-W[t+5]-v
 j+=1
PV=W[12:]
R=random.Random(20261119)
Z=[[R.getrandbits(64) for _ in range(128)] for _ in range(13)]
ZS=R.getrandbits(64);ZC=[R.getrandbits(64) for _ in range(16)];ZE=[R.getrandbits(64) for _ in range(8)]
V=[0,100,320,330,500,900,20000];RM={4:3,116:12,7:1,0:2,119:4,112:8}
B=[0]*128;S=1;C=0;E=-1;H=0;EM=EE=PH=0;U=[];HS=set();TT={};KL=[[0,0] for _ in range(256)]
N=0;L=150000;T0=0;TM=7;WK=4;BK=116
Q=b'$KfA5-]ZDM!uw;?61n"HPx37WyBW&<1b>&)SF~ogI@u<KKyqc{Fjioy,x>HZ#z"V:wg9`roDbD8OC4t+Ev*dF*V7PZ{jZaZ8xG.B(k>D:`I2/GX>2gZ6>UrvGa4mc(->q"Sk1!xj4Q#oOu?Yad|ks9`[!ifc3,ly7@[w>WRUM~c6V_6W(s(M.;&Yox(KuyvC"w8>0T00Q=UdR!bcZ/B&(nIq,pwTY@)dZS=dx[;X$dh](SlF.z~t;%Aq-L=r=/Ji><IEYEa^i^:B1.j@D*`Y';P={}
for i in range(0,len(Q),4):
 n=0
 for c in Q[i:i+4]:n=n*92+c-33-(c>39)-(c>92)
 P[n>>14]=n&16383
def PF(fen):
 global B,S,C,E,H,EM,EE,PH,WK,BK
 B=[0]*128;EM=EE=PH=0;H=0
 pp,sd,ca,ep,_,_=fen.split()
 r=7;f=0
 for ch in pp:
  if ch=='/':r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   p='PNBRQK'.index(ch.upper())+1
   if ch.islower():p=-p
   q=r*16+f;B[q]=p;EM+=MG[(p+6)*128+q];EE+=EG[(p+6)*128+q];PH+=PV[abs(p)];H^=Z[p+6][q]
   if p==6:WK=q
   if p==-6:BK=q
   f+=1
 S=1 if sd=='w' else -1
 if S<0:H^=ZS
 C=0
 if ca!='-':
  if 'K' in ca:C|=1
  if 'Q' in ca:C|=2
  if 'k' in ca:C|=4
  if 'q' in ca:C|=8
 H^=ZC[C]
 E=-1
 if ep!='-':
  E=(int(ep[1])-1)*16+ord(ep[0])-97;H^=ZE[E&7]
def J(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 if pr:s+='nbrq'[pr-2]
 return s
def AT(s,by):
 for x in (s-15*by,s-17*by):
  if not x&136 and B[x]==by:return 1
 for d,v in ((14,2),(18,2),(31,2),(33,2),(1,6),(15,6),(16,6),(17,6)):
  for x in (s+d,s-d):
   if not x&136 and B[x]==v*by:return 1
 for d,v in ((1,4),(16,4),(15,3),(17,3)):
  for g in (1,-1):
   x=s+g*d
   while not x&136:
    if B[x]:
     if B[x]==v*by or B[x]==5*by:return 1
     break
    x+=g*d
 return 0
def G(cp):
 ms=[]
 for q in range(128):
  if q&136:continue
  p=B[q]
  if p*S<=0:continue
  a=abs(p);d=16*S
  if a==1:
   t=q+d
   if not t&136 and B[t]==0:
    r=t>>4
    if r==7 or r==0:
     for pr in (5,4,3,2):ms.append(q|(t<<7)|(pr<<14))
    elif not cp:
     ms.append(q|(t<<7))
     t2=q+2*d
     if ((q>>4)==1 and S>0 or (q>>4)==6 and S<0) and not t2&136 and B[t2]==0:ms.append(q|(t2<<7))
   for t in (q+d-1,q+d+1):
    if t&136:continue
    if B[t]*S<0:
     r=t>>4
     if r==7 or r==0:
      for pr in (5,4,3,2):ms.append(q|(t<<7)|(pr<<14))
     else:ms.append(q|(t<<7))
    elif t==E and E>=0:ms.append(q|(t<<7))
  elif a==2 or a==6:
   for o in ((14,18,31,33),(1,15,16,17))[a==6]:
    for t in (q+o,q-o):
     if not t&136 and B[t]*S<=0 and (not cp or B[t]):ms.append(q|(t<<7))
  else:
   ds=(15,17) if a==3 else (1,16) if a==4 else (1,15,16,17)
   for o in ds:
    for g in (1,-1):
     t=q+g*o
     while not t&136:
      if B[t]:
       if B[t]*S<0:ms.append(q|(t<<7))
       break
      if not cp:ms.append(q|(t<<7))
      t+=g*o
 if not cp:
  for f,k,r,t,by,em,at in ((1,4,7,6,-1,(5,6),(4,5,6)),(2,4,0,2,-1,(3,2,1),(4,3,2)),(4,116,119,118,1,(117,118),(116,117,118)),(8,116,112,114,1,(115,114,113),(116,115,114))):
   if C&f and S==-by and B[k]==-6*by and B[r]==-4*by and all(B[e]==0 for e in em) and not any(AT(a,by) for a in at):ms.append(k|(t<<7))
 return ms
def K(m):
 global S,C,E,H,EM,EE,PH,WK,BK
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[f];cp=0;cq=t
 if B[t]:cp=B[t]
 elif abs(p)==1 and t==E and E>=0:cp=-S;cq=t-16*S
 U.append((f,t,p,cp,cq,C,E,H,EM,EE,PH,WK,BK))
 H^=Z[p+6][f]
 if cp:H^=Z[cp+6][cq];B[cq]=0;EM-=MG[(cp+6)*128+cq];EE-=EG[(cp+6)*128+cq];PH-=PV[abs(cp)]
 if E>=0:H^=ZE[E&7]
 E=-1;B[f]=0;EM-=MG[(p+6)*128+f];EE-=EG[(p+6)*128+f]
 if pr:
  n=pr*S;B[t]=n;H^=Z[n+6][t];EM+=MG[(n+6)*128+t];EE+=EG[(n+6)*128+t];PH+=PV[pr]
 else:
  B[t]=p;H^=Z[p+6][t];EM+=MG[(p+6)*128+t];EE+=EG[(p+6)*128+t]
 if abs(p)==6 and abs(t-f)==2:
  rf=f+3 if t>f else f-4;rt=f+1 if t>f else f-1;r=B[rf];B[rf]=0;B[rt]=r
  H^=Z[r+6][rf]^Z[r+6][rt];EM+=MG[(r+6)*128+rt]-MG[(r+6)*128+rf];EE+=EG[(r+6)*128+rt]-EG[(r+6)*128+rf]
  if p>0:WK=t
  else:BK=t
 elif abs(p)==6:
  if p>0:WK=t
  else:BK=t
 if abs(p)==1 and abs(t-f)==32:E=t-16*S;H^=ZE[E&7]
 o=C;C&=~RM.get(f,0);C&=~RM.get(t,0)
 if C!=o:H^=ZC[o]^ZC[C]
 S=-S;H^=ZS
 k=WK if S<0 else BK
 if AT(k,S):O();return 0
 return 1
def O():
 global S,C,E,H,EM,EE,PH,WK,BK
 f,t,p,cp,cq,C,E,H,EM,EE,PH,WK,BK=U.pop()
 S=-S
 if abs(p)==6 and abs(t-f)==2:
  rf=f+3 if t>f else f-4;rt=f+1 if t>f else f-1;r=B[rt];B[rt]=0;B[rf]=r
 B[t]=0;B[f]=p
 if cp:B[cq]=cp
def LG():
 ms=[]
 for m in G(0):
  if K(m):O();ms.append(m)
 return ms
def EV():
 s=(EM*PH+EE*(24-PH))//24
 return s if S>0 else -s
def OK(m,e=0,pl=0):
 t=(m>>7)&127;v=B[t]
 if m==e:return 1<<20
 if v:return V[abs(v)]*16-V[abs(B[m&127])]
 if m==KL[pl][0]:return 9000
 if m==KL[pl][1]:return 8000
 return 0
def QS(a,b,pl):
 global N
 N+=1
 if N>L or (N&1023==0 and time.time()-T0>TM):raise TO()
 s=EV()
 if s>=b:return b
 if s>a:a=s
 if pl>40:return a
 ms=G(1)
 ms.sort(key=OK,reverse=True)
 for m in ms:
  if K(m):
   s=-QS(-b,-a,pl+1);O()
   if s>=b:return b
   if s>a:a=s
 return a
def AB(d,a,b,pl):
 global N
 N+=1
 if N>L or (N&1023==0 and time.time()-T0>TM):raise TO()
 if pl and H in HS:return 0
 if d<=0:return QS(a,b,pl)
 e=TT.get(H);em=0
 if e:
  ed,es,ef,em=e
  if ed>=d:
   if ef==0:return es
   if ef==1 and es>=b:return b
   if ef==2 and es<=a:return a
 ms=G(0)
 ms.sort(key=lambda m:OK(m,em,pl),reverse=True)
 be=-30001;bm=0;lg=0;a0=a
 for i,m in enumerate(ms):
  if not K(m):continue
  lg+=1
  if i==0:s=-AB(d-1,-b,-a,pl+1)
  else:
   s=-AB(d-1,-a-1,-a,pl+1)
   if a<s<b:s=-AB(d-1,-b,-a,pl+1)
  O()
  if s>be:be=s;bm=m
  if s>a:a=s
  if a>=b:
   if not B[(m>>7)&127]:KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if lg==0:
  k=WK if S>0 else BK
  return -30000+pl if AT(k,-S) else 0
 TT[H]=(d,be,0 if be>a0 and be<b else 1 if be>=b else 2,bm)
 return be
def RT(ms):
 global N,T0
 k=H&4095
 if k in P:
  for m in ms:
   if m==P[k]:return m
 T0=time.time();N=0;be=ms[0]
 ms.sort(key=OK,reverse=True)
 for d in range(1,65):
  try:
   a=-30001;bm=be
   for m in ms:
    if not K(m):continue
    s=-AB(d-1,-30001,-a,1);O()
    if s>a:a=s;bm=m
   be=bm
   ms.remove(be);ms.insert(0,be)
   if abs(a)>29900:break
  except TO:break
 return be
def post(u,o):
 w=urllib.request
 r=w.Request(u,data=json.dumps(o).encode())
 with w.urlopen(r,timeout=30) as x:return json.load(x)
def main():
 u=os.environ.get('MAKEFUN_ENV_URL','')
 if not u:return
 while True:
  try:st=post(u+'/game',{})
  except Exception:time.sleep(.5);continue
  s=st.get('status')
  if s=='done':break
  if s!='your_move':time.sleep(.1);continue
  PF(st['fen']);HS.clear()
  PF('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1');HS.add(H)
  for mv in st.get('moves',[]):
   for c in LG():
    if J(c)==mv:K(c);HS.add(H);break
  PF(st['fen'])
  ms=LG()
  if not ms:break
  post(u+'/move',{'game':st['game'],'move':J(RT(ms))})
if __name__=='__main__':main()
