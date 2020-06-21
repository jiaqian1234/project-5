from pylayers.gis.layout import *
from IPython.display import Image
from pylayers.antprop.slab import *
from pylayers.simul.link import *
import os
from pylayers.location.geometric.constraints.cla import *
from pylayers.location.geometric.constraints.toa import *
from math import sqrt
from pylayers.location.geometric.constraints.cla import *
import pylayers.util.pyutil as pyu
from pylayers.location.geometric.constraints.toa import *


class PyLayersUWBRayTracingSimulation(object):
    def __init__(self,Layout, anchors, traj, fGHz = 0.9, BWGHz = 5, cutoff  = 1):
        self.L = Layout
        self.anchors = anchors
        self.traj = traj
        #self.axes = widget_plot.axes
       # self.widget_plot = widget_plot
        self.fGHz = fGHz
        self.BWGHz = BWGHz
        self.cutoff = cutoff
        self.L._filename = os.path.basename(self.L._filename)
        #self.fig = widget_plot.fig
        
    def TrajectorySimulation(self, widget_plot, progressbar):  
        progress = 100/len(self.traj[0]);
        currentprogress = 0;
        progressbar.setProperty("value", currentprogress)
        est = np.zeros(shape=(2,len(self.traj[0])))
        toas = np.zeros(shape=(len(self.traj[0]),len(self.anchors[0])))
        for i in range(0, len(self.traj[0])):
            p = [self.traj[0][i], self.traj[1][i]]
            pe = self.DoRayTracing(widget_plot, p)
            est[0][i] = pe[0]
            est[1][i] = pe[1]
            toas[i] = self.toas
            print('-----------------Position ', i)
            currentprogress = currentprogress + progress
            print('-----------------Progress ', currentprogress)
            progressbar.setProperty("value", int(currentprogress))
        print('Real trajectory',self.traj)
        print('Estimated Trajectory', est)
        progressbar.setProperty("value", 100)
        #toas = self.toas####
        return est,toas

    def DoRayTracing(self, widget_plot, tx = [2,2]):
        widget_plot.axes.cla()
        self.toas = np.zeros(len(self.anchors[0]))  

        DL = DLink(L=self.L)
        DL.fGHz= np.array([self.fGHz])
        DL.Aa=Antenna(typ='Omni')
        DL.a = np.array(([tx[0], tx[1],2.]))
        for i in range(0, len(self.anchors[0])):
            DL.b = np.array(([self.anchors[0][i],self.anchors[1][i],2.]))
            DL.Ab=Antenna(typ='Omni')
            DL.eval(cutoff = self.cutoff)
            DL.R.show(L=DL.L, ax = widget_plot.axes, fig = widget_plot.fig)
            cir = DL.H.getcir(self.BWGHz,Nf=10000)
            self.toas[i] = self.cal_toa(cir)
            widget_plot.axes.plot(self.anchors[0][i],self.anchors[1][i],'or')
        pe = self.toas_eval(self.toas)
        widget_plot.axes.plot(tx[0],tx[1],'or',color='green')
        widget_plot.axes.plot(pe[0],pe[1],'or',color = 'blue')
        #plt.show()
        widget_plot.draw()
        return pe

    def toas_eval(self, toas):
        C = CLA()
        for i in range(0, len(self.anchors[0])):
            toa = TOA(id=i,value = toas[i], std = np.array([1.0]), p = np.array([self.anchors[0][i],self.anchors[1][i]]))
            C.append(toa)
        C.compute()
        return C.pe
    def cal_toa(self, cir):
        signal_indx = np.argmax(20*np.log10(np.abs(cir.y[0,0,:])))
        toa1 = cir.x[signal_indx]
        return toa1
    
