#!/usr/bin/env python2

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from Tkinter import *

master = Tk()
L = Label(master, text="File Name (including Path)")
L.pack()
e = Entry(master)
e.pack()
e.focus_set()

L1 = Label(master, text="Column 1 name")
L1.pack()
e1 = Entry(master)
e1.pack()
e1.focus_set()

L2 = Label(master, text="Column 2 name")
L2.pack()
e2 = Entry(master)
e2.pack()
e2.focus_set()

L3 = Label(master, text=".prn filename (format:/filepath/1902-DOW-005_00)")
L3.pack()
e3 = Entry(master)
e3.pack()
e3.focus_set()

L4 = Label(master, text=".jpg graph filename (format:/filepath/1902-DOW-005_00)")
L4.pack()
e4 = Entry(master)
e4.pack()
e4.focus_set()

L5 = Label(master, text="Graph Title (format:I-V Curve 1902-DOW-005-)")
L5.pack()
e5 = Entry(master)
e5.pack()
e5.focus_set()

def callback():
    
        #read input parameters
        text_filename = e.get()
        column_1 = e1.get()
        column_2 = e2.get()
        prn_filepath = e3.get()
        jpg_filepath = e4.get()
        graph_title = e5.get()
        
        #open new file
        open_text_file = open(text_filename,'r')

        #read new file
        df3 = pd.read_csv(open_text_file)

        #convert text file to csv
        df3.to_csv('FFS_numbers.csv', sep=r',')
        df4 = pd.read_csv('FFS_numbers.csv')

        #extract the columns
        flash_numbers_list = df3[column_2].tolist()
        panel_numbers_list = df3[column_1].tolist()
        
        #generate all required plots
        for j in range(len(flash_numbers_list)):

                if flash_numbers_list[j] < 1000:
                        str_flash = "0" + str(flash_numbers_list[j])
                elif flash_numbers_list[j] >= 1000:
                        str_flash = str(flash_numbers_list[j])
                
                if panel_numbers_list[j] < 10:
                        str_panel = "00" + str(panel_numbers_list[j])
                elif panel_numbers_list[j] > 9 and panel_numbers_list[j] <100:
                        str_panel = "0" + str(panel_numbers_list[j])
                elif panel_numbers_list[j] > 99:
                        str_panel = str(panel_numbers_list[j])
                        
                str_panel = str_panel[0:3]
                
                filename = prn_filepath + str_flash + ".prn"
        
                plot_name = jpg_filepath + str_panel + '.jpg'
                
                title_name = graph_title + str_panel
        
                #open new file
                new_file = open(filename,'r')
        
                #read new file
                df1 = pd.read_fwf(new_file)
        
                #convert to CSV
                df1.to_csv('new.csv')
        
                #read CSV file
                df2 = pd.read_csv('new.csv', sep=r',', header=10, skipfooter=398, engine='python')
        
                #convert CSV to required format
                df2.to_csv('out.csv', sep='\t')
        
                #read modified CSV file
                df = pd.read_csv('out.csv')
        
                #extract required columns
                list_1 = df['[V]Ucor'].tolist()
                list_2 = df['[A]Icor'].tolist()
                    
                #remove negative values
                def removeNegative (list_1, list_2):
                        for i in range(len(list_1)):
        	                if list_1[i] < 0 or list_2[i] < 0:
        	                        list_1[i] = None
                                        list_2[i] = None
        
                #calling function
                removeNegative (list_1, list_2)
        
                #plotting
                plt.figure(j)
                plt.plot(list_1, list_2)
                plt.grid(color='g', linestyle='--', linewidth=0.5)
                plt.ylim(0, 12)
                plt.xlim(0, 50)
                plt.xlabel('Voltage (V)')
                plt.ylabel('Current (A)')
                plt.title(title_name)
                plt.savefig(plot_name)

b = Button(master, text="Enter", width=10, command=callback)
b.pack()

mainloop()
