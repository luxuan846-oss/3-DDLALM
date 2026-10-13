from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
plt.rcParams.update({'font.family':'serif','mathtext.fontset':'stix','font.size':11,'pdf.fonttype':42})
out=Path(__file__).resolve().parent
eps=.1; delta=1.; xs=delta/(2*eps)+eps
left=xs-2*eps; right=xs+2*eps
blue='#245A81'; orange='#C16A27'
def f(x):
    d=np.abs(x-xs)
    return np.where(d<=2*eps, .5*d*d, 2*eps*d-2*eps**2)
fig,ax=plt.subplots(figsize=(7.2,3.8))
ax.axvspan(0,left,color=blue,alpha=.07)
for a,b,c in [(-.4,left,blue),(left,right,orange),(right,7,blue)]:
    x=np.linspace(a,b,350); ax.plot(x,f(x),color=c,lw=2.3)
ax.plot([0,xs],[delta,0],'o',color=blue,ms=4)
ax.annotate(r'$(0,\Delta)$',xy=(0,delta),xytext=(.3,1.07))
ax.text(1.35,.78,r"$f'(x)=-2\epsilon$",color=blue,fontsize=13)
ax.text(5.85,.39,r"$f'(x)=2\epsilon$",color=blue,fontsize=12)
ax.annotate('',xy=(0,.1),xytext=(left,.1),arrowprops=dict(arrowstyle='<->',color=blue,lw=1))
ax.text(left/2,.145,r'$x_\star-2\epsilon=\Delta/(2\epsilon)-\epsilon$',ha='center',fontsize=11)
ax.set_xlim(-.4,7);ax.set_ylim(-.07,1.2)
ax.set_xticks([0,xs]);ax.set_xticklabels(['$0$',r'$x_\star$'])
ax.set_yticks([0,delta]);ax.set_yticklabels(['$0$',r'$\Delta$'])
ax.set_xlabel('$x$',loc='right');ax.set_ylabel('$f(x)$',rotation=0,labelpad=12)
ax.spines[['top','right']].set_visible(False)
ins=inset_axes(ax,width='37%',height='44%',loc='upper right',borderpad=1.2)
xx=np.linspace(xs-.5,xs+.5,500)
ins.plot(xx,f(xx),color=blue,lw=1.7)
mid=np.linspace(left,right,150);ins.plot(mid,f(mid),color=orange,lw=2.3)
ins.axvspan(left,right,color=orange,alpha=.09)
ins.plot([xs],[0],'o',color=orange,ms=3)
ins.set_xticks([left,xs,right]);ins.set_xticklabels([r'$x_\star-2\epsilon$',r'$x_\star$',r'$x_\star+2\epsilon$'],fontsize=8)
ins.set_yticks([0,2*eps**2]);ins.set_yticklabels(['$0$',r'$2\epsilon^2$'],fontsize=8)
ins.set_ylim(-.006,.09);ins.set_title('Quadratic region (enlarged)',fontsize=9)
ins.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.1,right=.98,bottom=.17,top=.96)
fig.savefig(out/'plateau_instance.pdf',bbox_inches='tight')
fig.savefig(out/'plateau_instance.png',dpi=220,bbox_inches='tight')
