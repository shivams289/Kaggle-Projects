
import pandas as pd
import numpy as np
import math
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

#Maximize (delta+gamma -theta) while chossing strike
#LS -> Lower strike 
#spot -> Spot price 
#HS -> Higher strike
#hsp -> Higher strike Premium
#lsp -> Lower strike Premium

class Strategy():
    def __init__(self, LS, spot, HS, hsp, lsp): 
        def round_spot(spot):
            if spot%100>50:
                spot -= (spot%100)
                spot += 100
            else:
                spot -= spot%100
            return spot
        
        self.spot = round_spot(spot)
        self.LS = LS
        self.HS = HS
        self.premium1 = hsp
        self.premium2 = lsp
        self.market_expiry = [expiry for expiry in range(self.spot-1500, self.spot+1500, 100)]
        deviation = [(expiry-spot)/spot*100 for expiry in self.market_expiry]
        self.lsdf = pd.DataFrame({'market_expiry':self.market_expiry, 'mx_%deviation':deviation})
        
    def long_strangle(self):#lstrg
        print(f"Buy OTM {self.HS} CE, Buy OTM {self.LS} PE")
        ce_payoff = [(max(expiry - self.HS, 0 ) - self.premium1) for expiry in self.market_expiry]
        pe_payoff = [(max(self.LS - expiry, 0 ) - self.premium2) for expiry in self.market_expiry]
        self.lsdf['ce_payoff'] = ce_payoff
        self.lsdf['pe_payoff'] = pe_payoff      
        self.lsdf['strategy_payoff'] = self.lsdf.ce_payoff + self.lsdf.pe_payoff
        net_credit = -(self.premium1 + self.premium2)
        maxloss = net_credit
        lower_breakeven = self.LS + maxloss
        upper_breakeven = self.HS - maxloss
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxloss:{maxloss}\nNet_Credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
        
    def short_strangle(self):#sstrg
        print(f"Sell OTM {self.HS} CE, Sell OTM {self.LS} PE")
        ce_payoff = [(self.premium1 - max(expiry - self.HS, 0 )) for expiry in self.market_expiry]
        pe_payoff = [(self.premium2 - max(self.LS - expiry, 0 ) ) for expiry in self.market_expiry]
        self.lsdf['ce_payoff'] = ce_payoff
        self.lsdf['pe_payoff'] = pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.ce_payoff + self.lsdf.pe_payoff
        net_credit = self.premium1 + self.premium2
        maxprofit = net_credit
        lower_breakeven = self.LS - net_credit
        upper_breakeven = self.HS + net_credit
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxProfit:{maxprofit}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'], self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
    
    def long_straddle(self):#lstrd
        print(f"Buy ATM {self.HS} CE, Buy ATM {self.LS} PE")
        ce_payoff = [(max(expiry - self.HS, 0 ) - self.premium1) for expiry in self.market_expiry]
        pe_payoff = [(max(self.LS - expiry, 0 ) - self.premium2) for expiry in self.market_expiry]
        self.lsdf['ce_payoff'] = ce_payoff
        self.lsdf['pe_payoff'] = pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.ce_payoff + self.lsdf.pe_payoff
        net_credit = -(self.premium1 + self.premium2)
        maxloss = net_credit
        lower_breakeven = self.LS + net_credit
        upper_breakeven = self.HS - net_credit
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxloss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
        
    def short_straddle(self):#sstrd
        print(f"Sell ATM {self.HS} CE, Sell ATM {self.LS} PE")
        ce_payoff = [(self.premium1 - max(expiry - self.HS, 0 )) for expiry in self.market_expiry]
        pe_payoff = [(self.premium2 - max(self.LS - expiry, 0 ) ) for expiry in self.market_expiry]
        self.lsdf['ce_payoff'] = ce_payoff
        self.lsdf['pe_payoff'] = pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.ce_payoff + self.lsdf.pe_payoff
        net_credit = self.premium1 + self.premium2
        maxprofit = net_credit
        lower_breakeven = self.LS - net_credit
        upper_breakeven = self.HS + net_credit
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxProfit:{maxprofit}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
    
    def bull_put_spread(self):#bps
        print(f"Buy OTM {self.LS} PE, Sell ITM {self.HS} PE")
        hs_pe_payoff = [(self.premium1 - max(self.HS - expiry, 0 ) ) for expiry in self.market_expiry]
        ls_pe_payoff = [(max(self.LS - expiry, 0 ) - self.premium2) for expiry in self.market_expiry]
        self.lsdf['otm_pe_payoff'] = ls_pe_payoff
        self.lsdf['itm_pe_payoff'] = hs_pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.otm_pe_payoff + self.lsdf.itm_pe_payoff  
        net_credit = self.premium1 - self.premium2
        maxprofit = net_credit
        spread = self.HS - self.LS
        maxloss =   spread - net_credit
        breakeven = self.HS - net_credit       
        print(f'Breakeven_point:{breakeven}\nMaxProfit:{maxprofit}\nMaxLoss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
        
    def bull_call_spread(self):#bcs
        print(f"Buy ITM {self.LS} CE, Sell OTM {self.HS} CE")
        hs_pe_payoff = [(self.premium1 - max(expiry - self.HS, 0 ) ) for expiry in self.market_expiry]
        ls_pe_payoff = [(max(expiry - self.LS, 0 ) - self.premium2) for expiry in self.market_expiry]
        self.lsdf['otm_pe_payoff'] = ls_pe_payoff
        self.lsdf['itm_pe_payoff'] = hs_pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.otm_pe_payoff + self.lsdf.itm_pe_payoff   
        spread = self.HS - self.LS
        net_credit = self.premium1 - self.premium2 #Net debit
        maxprofit = spread + net_credit
        maxloss =   net_credit
        breakeven = self.HS - maxprofit       
        print(f'Breakeven_point:{breakeven}\nMaxProfit:{maxprofit}\nMaxLoss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
    
    def bear_put_spread(self):#beps
        print(f"Buy ITM {self.HS} PE, Sell OTM {self.LS} PE")
        hs_pe_payoff = [(max(self.HS - expiry, 0 ) - self.premium1) for expiry in self.market_expiry]
        ls_pe_payoff = [(self.premium2 - max(self.LS - expiry, 0 ) ) for expiry in self.market_expiry]
        self.lsdf['otm_pe_payoff'] = ls_pe_payoff
        self.lsdf['itm_pe_payoff'] = hs_pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.otm_pe_payoff + self.lsdf.itm_pe_payoff
        spread = self.HS - self.LS
        net_credit = -(self.premium1 - self.premium2)
        maxloss =   net_credit
        maxprofit = spread - net_credit        
        breakeven = self.HS - net_credit       
        print(f'Breakeven_point:{breakeven}\nMaxProfit:{maxprofit}\nMaxLoss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'], self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
        
    def bear_call_spread(self):#becs
        print(f"Buy OTM {self.HS} CE, Sell ITM {self.LS} CE")
        hs_ce_payoff = [(max(expiry - self.HS, 0 ) - self.premium1) for expiry in self.market_expiry]
        ls_ce_payoff = [(self.premium2 - max(expiry - self.LS, 0 ) ) for expiry in self.market_expiry]
        self.lsdf['otm_ce_payoff'] = hs_ce_payoff
        self.lsdf['itm_ce_payoff'] = ls_ce_payoff        
        lsdf['strategy_payoff'] = self.lsdf.otm_ce_payoff + self.lsdf.itm_ce_payoff        
        spread = self.HS - self.LS
        net_credit = (self.premium1 - self.premium2)
        maxprofit =   net_credit
        maxloss = spread - net_credit        
        breakeven = self.LS + net_credit       
        print(f'Breakeven_point:{breakeven}\nMaxProfit:{maxprofit}\nMaxLoss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
    
    def call_ratio_back_spread(self):#crbs
        print(f"Buy 2 OTM {self.HS} CE, Sell ITM {self.LS} CE")
        hs_ce_payoff = [(2*max(expiry - self.HS, 0 ) - self.premium1) for expiry in self.market_expiry]
        ls_ce_payoff = [(self.premium2 - max(expiry - self.LS, 0 ) ) for expiry in self.market_expiry]
        self.lsdf['otm_ce_payoff'] = hs_ce_payoff
        self.lsdf['itm_ce_payoff'] = ls_ce_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.otm_ce_payoff + self.lsdf.itm_ce_payoff       
        net_credit = (self.premium2 - self.premium1)
        spread = self.HS - self.LS
        maxloss = -(spread - net_credit)
        lower_breakeven = self.LS + net_credit
        upper_breakeven = self.HS - maxloss
        
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxloss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'],self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
        
    def put_ratio_back_spread(self):#prbs
        print(f"Buy 2 OTM {self.LS} PE, Sell ITM {self.HS} PE")
        hs_pe_payoff = [(self.premium1 - max(self.HS - expiry, 0 ) ) for expiry in self.market_expiry]
        ls_pe_payoff = [(2*max(self.LS - expiry, 0 ) - self.premium2 ) for expiry in self.market_expiry]
        self.lsdf['otm_pe_payoff'] = ls_pe_payoff
        self.lsdf['itm_pe_payoff'] = hs_pe_payoff
        self.lsdf['strategy_payoff'] = self.lsdf.otm_pe_payoff + self.lsdf.itm_pe_payoff
        
        net_credit = self.premium1 - self.premium2
        spread = self.HS - self.LS
        maxloss = -(spread - net_credit)
        lower_breakeven = self.LS + maxloss
        upper_breakeven = self.LS - maxloss
        
        print(f'Breakeven_points:{(lower_breakeven, upper_breakeven)}\nMaxloss:{maxloss}\nNet_credit:{net_credit}')
        print(self.lsdf)
        plt.plot(self.lsdf['market_expiry'], self.lsdf['strategy_payoff'])
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
   