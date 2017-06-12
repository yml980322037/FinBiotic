#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:53:58 2017

@author: jonfroiland
"""

class Support(object):
    
    def __init__(self, instrument, bid, ask, dfD, units, pivot, sl1, sl2, sl3,
                             rate1, rate2):
        self.instrument = instrument
        self.bid = bid
        self.ask = ask
        self.dfD = dfD
        self.units = units
        self.pivot = pivot
        self.sl1 = sl1
        self.sl2 = sl2
        self.sl3 = sl3
        self.rate1 = rate1
        self.rate2 = rate2
  
    def support(self):
        if (
                self.ask < self.pivot and self.bid > self.sl1 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long PP_SL1 ***', self.units
            profit = self.pivot
            loss = self.sl1
            return self.units, profit, loss
            
        elif (
                self.ask < self.pivot and self.bid > self.sl1 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short PP_SL1 ***', self.units
            profit = self.sl1
            loss = self.pivot
            return self.units, profit, loss
        
        elif (
                self.ask < self.sl1 and self.bid < self.sl2 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long SL1_SL2 ***', self.units
            profit = self.sl1
            loss = self.sl2
            return self.units, profit, loss
        
        elif (
                self.ask < self.sl1 and self.bid < self.sl2 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short SL1_SL2 ***', self.units
            profit = self.sl2
            loss = self.sl1
            return self.units, profit, loss 
        
        elif (
                self.ask < self.sl2 and self.bid < self.sl3 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long SL1_SL2 ***', self.units
            profit = self.sl2
            loss = self.sl3
            return self.units, profit, loss
        
        elif (
                self.ask < self.sl2 and self.bid < self.sl3 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short SL1_SL2 ***', self.units
            profit = self.sl3
            loss = self.sl2
            return self.units, profit, loss 
        
        elif (
                self.ask < self.sl3 and self.units is not None and \
                self.units > 0
            ):
            print '*** Long SL3 Breakout ***', self.units
            profit = self.bid - .002
            loss = self.sl3
            return self.units, profit, loss
        
        elif (
                self.bid < self.sl3 and self.units is not None and \
                self.units < 0
            ):
            print '*** Short RL3 Breakout ***', self.units
            profit = self.sl3
            loss = self.ask + .001
            return self.units, profit, loss
        
        else:
            return None