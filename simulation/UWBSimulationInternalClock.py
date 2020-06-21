import numpy as np
import math
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

class UWBSimulationInternalClock(object):
    def __init__(self, Layout, root, anchors, trajectory, noise_var, cutoff, fGHz, BWGHz):
        self.L = Layout
        self.root = root
        self.anchors = anchors
        self.anchors_num = len(self.anchors[0])   
        self.trajectory = trajectory
        self.noise_var = noise_var
        self.dist_to_root = np.empty(shape=self.anchors_num )
        for i in range(0,self.anchors_num ):
            dist = math.sqrt((root[0] - anchors[0][i])**2 + (root[1] - anchors[1][i])**2)
            self.dist_to_root[i] = dist
        self.clock_diff = np.empty(shape=self.anchors_num +1)
        self.fGHz = fGHz
        self.lightspeed = 299792458 * (10**(-9)) 
        self.cutoff = cutoff
        self.BWGHz = BWGHz
        
        
    def synchronization_phase(self):
        print('Initialize anchor internal clocks...')
        # initial position of target
        tag_pos = [self.trajectory[0][0],self.trajectory[1][0]]
        self.clock_diff[0] = self.compute_toa(self.root, tag_pos)
        
        for i in range(1,self.anchors_num  + 1):
            anchor_pos = [self.anchors[0][i-1], self.anchors[1][i-1]]
            self.clock_diff[i] = self.compute_toa(self.root, anchor_pos)
    
    def trajectorySimulationInternalClocks(self):
        est_trajectory = np.empty(shape=(2,len(self.trajectory[0])))
        for i in range(0,len(self.trajectory[0])):
            tag_pos = [self.trajectory[0][i],self.trajectory[1][i]]
            est_pos = self.positionEstimationSimulation(tag_pos)
            print('Real position: ',tag_pos, 'Estimated position: ', est_pos)
            est_trajectory[0][i] = est_pos[0]
            est_trajectory[1][i] = est_pos[1]
        print('Estimated trajectory: ', est_trajectory)
        return est_trajectory
            
    
    def positionEstimationSimulation(self, tag_pos):
        # Phase 1: synchronisation. Root anchor sends to signal to all agents
        self.synchronization_phase()
        
        # Phase 2: upon root signal arrival, target send signal to all anchors
        # compute toa from tag to anchors
        t_tas =  self.compute_tag_toas (tag_pos)
        # estimate distance of all anchors to tag
        distances = self.compute_distance_to_tag(t_tas)
        # using distances to estimate position with least square
        est_pos = self.estimate_position_least_square(distances) 
        return est_pos
        
    def compute_tag_toas(self, tag_pos):
        # calculate the toas from target to all anchors
        t_tas = np.zeros(self.anchors_num + 1)  
        # first entry is for the root anchor
        t_tas[0] = self.compute_toa(tag_pos, self.root)
        
        for i in range(1, len(self.anchors[0] +1)):
            # get the toa with respect to target node
            anchor_pos = [self.anchors[0][i-1], self.anchors[1][i-1]]
            t_tas[i] = self.compute_toa(tag_pos, anchor_pos)
        return t_tas

    def compute_distance_to_tag(self, t_tas):
        distances = np.empty(shape=self.anchors_num +1)
        ###TODO: generate noise once at a time
        ####distance to root####
        # toa to root wrt root clock
        t_rt = t_tas[0]
        # add a stochastic error
        t_r = t_rt * 2 + np.random.normal(0,self.noise_var,1)
        distances[0] = self.lightspeed *  t_r/2
        
        #####distance to anchors####
        for i in range(1, len(self.anchors[0] +1)):
            t_ai = t_rt + t_tas[i] - self.clock_diff[i]
            # add a stochastic error
            t_ai = t_ai +  np.random.normal(0,self.noise_var,1)
            distances[i] = self.lightspeed * t_ai - distances[0] + self.dist_to_root[i-1]
        print(distances)
        return distances
            
    def estimate_position_least_square(self, distances):
        A = np.empty(shape=(self.anchors_num ,2))
        x_butlast = self.anchors[0]
        y_butlast = self.anchors[1]
        
        A[:,0] = 2 * self.root[0] - 2 * x_butlast
        A[:,1] = 2 * self.root[1] - 2 * y_butlast  
        
        b = distances[1:]**2 - distances[0]**2 - x_butlast**2 - y_butlast** 2 + self.root[0]**2 + self.root[1]**2
        
        print('A is: ', A)
        print('b is:', b)
        
        A_T = np.transpose(A)
        pe = np.linalg.inv(np.matmul(A_T,A))
        pe = np.matmul(pe,A_T)
        pe = np.matmul(pe,b)
        return pe
        
    def compute_toa (self, pa, pb):
        DL = DLink(L=self.L)
        DL.fGHz= self.fGHz
        DL.Aa = Antenna(typ='Omni')
        DL.Ab = Antenna(typ='Omni')
        ## 2D simulation
        DL.a = np.array([pa[0],pa[1], 2.0])        
        DL.b = np.array([pb[0],pb[1], 2.0]) 
        DL.eval(cutoff = self.cutoff)
        cir = DL.H.getcir(self.BWGHz,Nf=10000)
        return self.cal_toa(cir)
    def cal_toa(self, cir):
        signal_indx = np.argmax(20*np.log10(np.abs(cir.y[0,0,:])))
        toa1 = cir.x[signal_indx]
        return toa1
if __name__ == "__main__":
    import numpy as np
    import math
    from simulation import *
    L = Layout('testLayout.lay')
    sim = UWBSimulationInternalClock(L, [1,2], np.array([[0,6,7,3],[0,3,1,5]]),np.array([[1,3],[1,2]]),0.5,1,0.9, 0.5)
    sim.trajectorySimulationInternalClocks()
