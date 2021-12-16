
import pandas as pd
import numpy as np
import math
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from Model.model import Strategy

def take_inputs():
   
    val = input('Hey! Welcome to Strategy Choosing Program. Please enter your preferences\n\nAre you bullish?:Enter b\nIf bearish:Enter be\nExpect Underlying to be range bound?:Enter r\nIf Expect Either Side Large Moves?:Enter mn\n\n')
    if val == 'b':
        rang = float(input('What % Of Upward Move is Expected?If 5%, Enter 5\n\n'))
    if val == 'be':
        rang = float(input('What % of Downward Move is Expected?If 5%, Enter 5\n\n'))
    if val == 'r':
        rang = float(input('What % Range From Spot is Expected?If 2%, Enter 2\n\n'))
    if val == 'mn':
        rang = float(input('Market Neutral:% Move Expected On Either Side?If 3%, Enter 3\n\n'))
    
    return val, rang  

def NameStrat():
    inp = input('Which Strategy you wanna call:\n\nFor put_ratio_back_spread:Enter prbs\nFor call_ratio_back_spread:Enter crbs\nFor bear_put_spread:Enter beps\nFor bear_call_spread:Enter becs\nFor bull_put_spread:Enter bps\nFor bull_call_spread:Enter bcs\nFor long_strangle:Enter lstrg\nFor short_strangle:Enter sstrg\nFor short_straddle:Enter sstrd\nFor long_straddle:Enter lstrd\n')
    
    return inp

def inp_parameters():
    LS = int(input('input lower strike?'))
    HS = int(input('input higher strike?'))
    hsp = int(input('input premium of higher strike?'))
    lsp = int(input('input premium of lower strike?'))
    return LS, HS, hsp, lsp



def Call_strategy():
    spot = int(input('Enter Current value of spot?\n'))
    inp = NameStrat()
    if inp == 'prbs':
        print("This Strategy requires you to: Buy 2 OTM PE, Sell an ITM PE\n")
        #take input strategy parameter LS, HS, hsp, lsp, 
        LS, HS, hsp, lsp = inp_parameters()
        prbs = Strategy(LS, spot, HS, hsp, lsp)
        print(prbs.put_ratio_back_spread())
    if inp == 'crbs':
        print("This Strategy requires you to: Buy 2 OTM CE, Sell ITM CE\n")
        #take input strategy parameter LS, HS, hsp, lsp,
        crbs = Strategy(LS, spot, HS, hsp, lsp)
        print(crbs.call_ratio_back_spread())
        
    if inp == 'beps':
        print("This Strategy requires you to: Buy ITM PE, Sell OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        beps = Strategy(LS, spot, HS, hsp, lsp)
        print(beps.bear_put_spread())
        
    if inp == 'becs':
        print("This Strategy requires you to: Buy OTM CE, Sell ITM CE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        becs = Strategy(LS, spot, HS, hsp, lsp)
        print(becs.bear_call_spread())
        
    if inp == 'bps':
        print("This Strategy requires you to: Buy OTM PE, Sell ITM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        bps = Strategy(LS, spot, HS, hsp, lsp)
        print(bps.bull_put_spread())
        
    if inp == 'bcs':
        print("This Strategy requires you to: Buy ITM CE, Sell OTM CE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        bcs = Strategy(LS, spot, HS, hsp, lsp)
        print(bcs.bull_call_spread())
        
    if inp == 'sstrd':
        print("This Strategy requires you to: Sell ATM CE, Sell ATM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        sstrd = Strategy(LS, spot, HS, hsp, lsp)
        sstrd.short_straddle()
        
    if inp == 'lstrd':
        print("This Strategy requires you to: Buy ATM CE, Buy ATM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        lstrd = Strategy(LS, spot, HS, hsp, lsp)
        print(lstrd.long_straddle())
        
    if inp == 'sstrg':
        print("This Strategy requires you to: Sell OTM CE, Sell OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        sstrg = Strategy(LS, spot, HS, hsp, lsp)
        print(sstrg.short_strangle())
        
    if inp == 'lstrg':
        print("This Strategy requires you to: Buy OTM CE, Buy OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        lstrg = Strategy(LS, spot, HS, hsp, lsp)
        print(lstrg.long_strangle())


Call_strategy()





