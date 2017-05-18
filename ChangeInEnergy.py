"""Trends in Dirty Energy (Coal and FossFuel) by State in the period 2010-2014
largest percentule change in energy BTU consumption 2010-2014 by US State"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
dfMain=pd.read_csv('Energy Census and Economic Data US 2010-2014.csv')
df=dfMain[['State','TotalC2010','TotalC2011','TotalC2012','TotalC2013','TotalC2014',
'CoalC2010','CoalC2011','CoalC2012','CoalC2013','CoalC2014',
'FossFuelC2010','FossFuelC2011','FossFuelC2012','FossFuelC2013','FossFuelC2014']][:50]
dfTotal=df[['State','TotalC2010','TotalC2011','TotalC2012','TotalC2013','TotalC2014']]
dfCoal=df[['State','CoalC2010','CoalC2011','CoalC2012','CoalC2013','CoalC2014']]
dfFossFuel=df[['State','FossFuelC2010','FossFuelC2011','FossFuelC2012','FossFuelC2013','FossFuelC2014']]
TotalAvgChange=[sum([dfTotal.loc[i][j]/dfTotal.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
CoalAvgChange=[sum([dfCoal.loc[i][j]/dfCoal.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
FossFuelAvgChange=[sum([dfFossFuel.loc[i][j]/dfFossFuel.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
StateEnergyTrends=[[TotalAvgChange[i],CoalAvgChange[i],FossFuelAvgChange[i]] for i in range(50)]
dfFinal=df[['State']]
dfFinal['Trends']=pd.Series(StateEnergyTrends).values           

def assembleState(state):                 
    d=dfFinal[dfFinal['State']==state]
    p=[list(d['Trends'])[0][k]*100 for k in range(3)]
    q=["%.2f"%(float(i)-100) for i in p]
    r=[round(float(i),2) for i in q]
    return r  
outputData=[[s,assembleState(s)] for s in list(dfFinal['State'])] #this list of lists is the data to chart

def showState(state):
    thisState=outputData[[o[0] for o in outputData].index(state)]
    plt.figure(figsize=(4,4))
    plt.title('\n'+state+'\nEnergy Trends \n'+'2010-2014',fontsize=18,y=1.05,color='purple')
    y_positions = np.arange(3)+.1
    plt.yticks(y_positions,('FossFuel','Coal','Total'),fontsize=14,color='purple',x=-.05)
    plt.xlabel('Avgerage Annual % Change',fontsize=14,color='purple',y=2)
    shade=plt.get_cmap('RdYlGn')
    stateExtreme=math.ceil(max(abs(min(thisState[1])),abs(max(thisState[1]))))
    plt.axis([-stateExtreme-1,stateExtreme+1,-.5,2.75])
    plt.plot(x=0)
    barcolors=[shade(.5-(thisState[1][2]/(2*stateExtreme))),shade(.5-(thisState[1][1]/(2*stateExtreme))),
                shade(.5-(thisState[1][0]/(2*stateExtreme)))] #dynamic coloring based on .5 centerpoint of shade
    plt.barh(y_positions,[thisState[1][2],thisState[1][1],thisState[1][0]],align="center",color=barcolors)

def main():
    for b in [a[0] for a in outputData]:
        showState(b)

main()


"""
TotalC{year}: Total energy consumption in billion BTU in given year.
TotalP{year}: Total energy production in billion BTU in given year.
TotalE{year}: Total Energy expenditures in million USD in given year.
TotalPrice{year}: Total energy average price in USD/million BTU in given year.
TotalC{first year}–{second year}: The first year’s total energy consumption divided by the second year’s total energy consumption, times 100. (The percent change between years in total energy consumption.)
TotalP{first year}–{second year}: The first year’s total energy production divided by the second year’s total energy production, times 100. (The percent change between years in total energy production.)
TotalE{first year}–{second year}: The first year’s total energy expenditure divided by the second year’s total energy expenditure, times 100. (The percent change between years in total energy expenditure.)
TotalPrice{first year}–{second year}: The first year’s total energy average price divided by the second year’s total energy average price, times 100. (The percent change between years in total energy average price.)
BiomassC{year}: Biomass total consumption in billion BTU in given year.
CoalC{year}: Coal total consumption in billion BTU in given year.
CoalP{year}: Coal total production in billion BTU in given year.
CoalE{year}: Coal total expenditures in million USD in given year.
CoalPrice{year}: Coal average price in USD per million BTU in given year.
ElecC{year}: Electricity total consumption in billion BTU in given year.
ElecE{year}: Electricity total expenditures in million USD in given year.
ElecPrice{year}: Electricity average price in USD per million BTU in given year.
FossFuelC{year}: Fossil fuels total consumption in billion BTU in given year.
GeoC{year}: Geothermal energy total consumption in billion BTU in given year.
GeoP{year}: Geothermal energy net generation in the electric power sector in million kilowatt hours in given year.
HydroC{year}: Hydropower total consumption in billion BTU in given year.
HydroP{year}: Hydropower total net generation in million kilowatt hours in given year.
NatGasC{year}: Natural gas total consumption (including supplemental gaseous fuels) in billion BTU in given year.
NatGasE{year}: Natural gas total expenditures in million USD in given year.
NatGasPrice{year}: Natural gas average price in USD per million BTU in given year.
LPGC{year}: LPG total consumption in billion BTU in given year.
LPGE{year}: LPG total expenditures in million USD in given year.
LPGPrice{year}: LPG average price in USD per million BTU in given year.
"""
      