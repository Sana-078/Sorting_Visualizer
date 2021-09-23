import tkinter as tk
from tkinter import ttk
import random
import time
import tkinter.messagebox


        
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('sorting algorithm visualizer')
        self.maxsize(1500, 800)
        self.resizable('False','False')

        #detail canvas
        self.drawing_canvas=tk.Canvas(self, width=1000, height=600, bg="white")
        self.detail_canvas=tk.Frame(self, width=1000, height=100)
        self.algo_Frame=tk.Frame(self, width=400, height=700)
        
        #drawing canvas
        self.detail_canvas.grid(row=1, column=0 )
        self.drawing_canvas.grid(row=2, column=0)
        self.algo_Frame.grid(row=2, column=1)
        ##title
        self.title_label=ttk.Label(self, text="SORTING ALGORITHM VISUALIZER")
        self.title_label.grid(row=0, columnspan=3, pady=(0, 15))

        #variables for length, algorithm, speed
        self.le=tk.IntVar()
        self.algo=tk.StringVar()
        self.speed=tk.StringVar()


        self.algo_list=['bubble sort', 'merge sort',  'selection sort', 'insertion sort', 'quick sort']
        self.speed_list=['slow', 'medium', 'fast']
        self.len_list=[ 80, 100, 300, 600]
        
        self.array=[]

        self.th0=[]
        self.th1=[]
        
        self.thread_array=[]
        self.sp=0

        #labels for length, algorithm, speed
        self.len_label=ttk.Label(self.detail_canvas, text="* select the size of the array" )
        self.len_label.grid(row=0, column=0, padx=5)

        self.algo_label=ttk.Label(self.detail_canvas, text="* select one algorithm" )
        self.algo_label.grid(row=0, column=1 , padx=5)

        self.speed_label=ttk.Label(self.detail_canvas, text="* select a speed")
        self.speed_label.grid(row=0, column=2, padx=5)

        self.speed_label=ttk.Combobox(self.detail_canvas, textvariable=self.speed, values=self.speed_list)
        self.algo_list2=ttk.Combobox(self.detail_canvas, textvariable=self.algo, values=self.algo_list)
        self.len_list2=ttk.Combobox(self.detail_canvas, textvariable=self.le, values=self.len_list)
        
        self.len_list2.grid(row=1, column=0, padx=5, pady=5)
        
        self.algo_list2.grid(row =1, column=1, pady=5, padx=5)
        self.speed_label.grid(row=1, column=2, pady=5, padx=5)
        
        
        self.generate_button=ttk.Button(self.detail_canvas, text="generate", width=25, command=self.generate)
        self.generate_button.grid(row=1, column=3, padx=5)

        self.start_bu=ttk.Button(self.detail_canvas, text="Start", width=25)

        self.pivo=0
        ##concurrent function running
#        self.con_label=ttk.Label(self.detail_canvas, text="running concurrent function")
#        self.con_label.grid(row=7, column=0, pady=10)

       
        #Algo Details Section
        self.Algo_details=ttk.Button(self.algo_Frame, text="Show Algo Detail", width=40,command=self.algo_detail)
        self.Algo_details.grid(row=0, columnspan=3, padx=5, pady=10)

        self.separator=ttk.Separator(self.algo_Frame, orient='horizontal')
        self.separator3=ttk.Separator(self.algo_Frame, orient='horizontal')
        self.separator2=ttk.Separator(self.algo_Frame, orient='vertical')
        
        self.tc_text=ttk.Label(self.algo_Frame, text="Time Complexity", font=('Helvatical bold',15))
        self.tc_text.grid(row=1, columnspan=3, pady=10, padx=10)

        self.separator.grid(row=2, columnspan=3,  sticky="ew", pady=5)
        self.separator2.grid(rowspan=6, column=1,  sticky="ns", pady=10)
        self.separator3.grid(row=6, columnspan=3,  sticky="ew", pady=5)
        
        self.tc_best_case=ttk.Label(self.algo_Frame, text="Best Case:" ,font=('Helvatical bold',10))
        self.tc_best_case.grid(row=3, column=0, pady=10, padx=10)

        self.tc_best_case2=ttk.Label(self.algo_Frame, text="__________ " ,font=('Helvatical bold',10))
        self.tc_best_case2.grid(row=3, column=2, pady=10, padx=10)
        
        self.tc_average_case=ttk.Label(self.algo_Frame, text="Average Case:" ,font=('Helvatical bold',10))
        self.tc_average_case.grid(row=4, column=0, pady=10, padx=10)

        self.tc_average_case2=ttk.Label(self.algo_Frame, text="__________" ,font=('Helvatical bold',10))
        self.tc_average_case2.grid(row=4, column=2, pady=10, padx=10)

        self.tc_worst_case=ttk.Label(self.algo_Frame, text="Worst Case:" ,font=('Helvatical bold',10))
        self.tc_worst_case.grid(row=5, column=0, pady=10, padx=10)

        self.tc_worst_case2=ttk.Label(self.algo_Frame, text="__________" ,font=('Helvatical bold',10))
        self.tc_worst_case2.grid(row=5, column=2, pady=10, padx=10)
        
        self.sc_text=ttk.Label(self.algo_Frame, text="space complexity:", font=('Helvatical bold',15))
        self.sc_text.grid(row=7, columnspan=3, pady=10, padx=10)

        self.sc_text2=ttk.Label(self.algo_Frame, text="Worst Case:", font=('Helvatical bold',10))
        self.sc_text2.grid(row=8, column=0, pady=10, padx=10)
        
        self.sc_worstcase=ttk.Label(self.algo_Frame, text="__________", font=('Helvatical bold',10))
        self.sc_worstcase.grid(row=8, column=2, pady=10, padx=10)

        
    def algo_detail(self):
        n=self.algo.get()
        if n!='':
            if n=="bubble sort" or n =="insertion sort" or n=="selection sort":
                tc_average="Θ(N2)"
                tc_worst="O(N2)"
                sc="O(1)"
                if n=="selection sort":
                    tc_best="Ω(N2)"
                else:
                    tc_best="Ω(N)"
                
            elif n=="merge sort" or n=="quick sort":
                tc_best="Ω(N log N)"
                tc_average="Θ(N log N)"
                if n=="quick sort":
                    tc_worst="O(N2)"
                    sc="O(log N)"
                else:
                    tc_worst="O(N log N)"
                    sc="O(N)"
                
        else:
            tkinter.messagebox.showinfo("error", "please select an algorithm to show details")

        self.tc_best_case2.config(text=tc_best)
        self.tc_average_case2.config(text=tc_average)
        self.tc_worst_case2.config(text=tc_worst)
        self.sc_worstcase.config(text=sc)

        
    def generate(self):
        
        self.array=[]
        print(self.le.get())
        for i in range(self.le.get()):
            num=random.randint(0, 100)
            self.array.append(num)
       
        if self.le.get()==80:
            self.sp=12
        elif self.le.get()==100:
            self.sp=9.8
        elif self.le.get()==300:
            self.sp=3.2
        elif self.le.get()==600:
            self.sp=1.6
        else:
           tkinter.messagebox.showinfo("error", "please select the size of the\n array to generate") 
        if self.sp !=0:
            self.draw(self.array, ["blue" for x in range(len(self.array))])
            self.start_bu['command']=self.sort
            self.start_bu.grid(row=1, column=4, padx=5)
        
    def sort(self):
        n=len(self.array)-1
        if self.algo.get()=="bubble sort":
            self.bubblesort(self.array, self.draw)
        elif self.algo.get()=="insertion sort":
            self.insertionsort(self.array, self.draw)
        elif self.algo.get()=="selection sort":
            self.selectionsort(self.array, self.draw)
            
        elif self.algo.get()=="merge sort":
            self.merge_sort(self.array,0,n, self.draw)
        elif self.algo.get()=="quick sort":
            self.quick_sort(0, n, self.array, self.draw)
        else:
            tkinter.messagebox.showinfo("error", "please select an algorithm to run")

    '''draw function algorithm works as follows:
     1: take each element from the array which is a random number generated between 1 and 100
     2: deduct the element from 100 to make the coordinates for rectangles, the resultant num will work
       as y2 for the new coordinate if the height of the canvas is 100, but in this case it is 600
     3: so we will multiply it by 490 to get a value around  500.
     4: we will specify y1 as 0, to get the bars upside down.you can specify 600 as y1 and get the bars straight up,
        but replace (div * 490)/100 with (div * 590)/100 and in the place of y0 use percent+10.
        This is because ,imagine you get 1 as the value,from the calculation the final value will be 584.1 which looks
        pretty high from the y1 which is 600 for a value 1. Also imagine if the value is 100, then by the calculation
        the final value will be 0. 0 for y0 will pretty much look like it is stuck up on the top. So by adding 10 ,
        for the value 1 we will get 594.1 and for 100 it will be 0+10=10 which sums it up.
    '''    
    def draw(self, data, colorarr):
        self.drawing_canvas.delete("all")
        x0=6
        y1=0
        x1=self.sp
        for i, num in enumerate(data):
            div=100-num
            percent=(div* 490)/ 100
            down=500-percent
            self.drawing_canvas.create_rectangle(x0+self.sp, down , x1+self.sp, y1, fill=colorarr[i])
            x0=x0+self.sp
            x1=x1+self.sp
        

        self.update_idletasks()

    def set_speed(self):
        if self.speed.get()=="fast":
            return 0.001
        elif self.speed.get()=="medium":
            return 0.1
        elif self.speed.get()=="slow":
            return 0.3
        else:
            tkinter.messagebox.showinfo("error", "please select a speed")

    #bubblesort 
    def bubblesort(self,data, draw):
        sorted_arr=[]
        self.end=0
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1] :
                    
                    data[j], data[j+1] = data[j+1], data[j]
                   
                    draw(data, ["yellow" if x == j else "red" if x == j+1 else "green" if x in sorted_arr else "blue" for x in range(len(data))])
                    time.sleep(self.set_speed())
            sorted_arr.append(n-i-1)
        draw(data,[ "green" if x in sorted_arr else "blue" for x in range(len(data))])
        
    #insertionsort
    def insertionsort(self, data, draw):
        n=len(data)
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >=0 and key < data[j] :
                data[j+1] = data[j]
                draw(data, ["yellow" if x == j else "red" if x == j+1 else "green" if x<i else "blue" for x in range(len(data))] )
                self.end=j
                j -= 1
            data[j+1] = key
            time.sleep(self.set_speed())
        draw(data,["green" for x in range(len(data))])

    #selectionsort
    def selectionsort(self, data, draw):
        for i in range(len(data)):
            self.end=0
            min_idx=i
            for j in range(i+1, len(data)):
                if data[min_idx]>data[j]:
                    min_idx=j
                    time.sleep(0.003)
            data[i], data[min_idx]=data[min_idx], data[i]
            self.end=i
            
            draw(data, ["yellow" if x == i else "red" if x == min_idx else "green" if x<=self.end else "blue" for x in range(len(data))] )
            time.sleep(self.set_speed())
            
        draw(data,[ "green" if x <=self.end else "blue" for x in range(len(data))])
        
    #mergesort
    def merge(self,data, start, mid, end, draw):
        p = start
        q = mid + 1
        tempArray = []

        for i in range(start, end+1):
            if p > mid:
                tempArray.append(data[q])
                q+=1
            elif q > end:
                tempArray.append(data[p])
                p+=1
            elif data[p] < data[q]:
                tempArray.append(data[p])
                p+=1
            else:
                tempArray.append(data[q])
                q+=1

        for p in range(len(tempArray)):
            data[start] = tempArray[p]
            start += 1

    def merge_sort(self, data, start, end, draw):
        
        if start < end:
            mid = int((start + end) / 2)
            self.merge_sort(data, start, mid, draw)
            self.merge_sort(data, mid+1, end, draw)
            self.merge(data, start, mid, end, draw)

            
            draw(data, ["orange" if x >= start and x < mid else "yellow" if x == mid 
                        else "red" if x > mid and x <=end else "green" if x<=end else "blue" for x in range(len(data))])
            
            time.sleep(self.set_speed())

        
        draw(data, ["green" if x<=end else "blue" for x in range(len(data))])

    #quick sort
    def partition(self, start, end, array, draw):
        
        pivot_index=start
        pivot=array[pivot_index]

        while start < end:
            while start<len(array) and array[start]<= pivot:
                start+=1
            while array[end]>pivot:
                end-=1
                
            if (start<end):
                array[start], array[end]=array[end], array[start]
                draw(array, ["pink" if x==start else "black" if x==end else"red" if x<end and x>start else "green" if x<pivot_index else "blue" for x in range(len(array))])
                
        array[end], array[pivot_index]=array[pivot_index], array[end]
        
        self.pivo=pivot_index
     
        draw(array, ["orange" if x == end  else "yellow" if x == pivot_index else "green" if x<pivot_index  else "blue" for x in range(len(array))])
 
        time.sleep(self.set_speed())
        return end


    def quick_sort(self, start, end, array, draw):
        self.run=True   
            
        if(start < end):
            p = self.partition(start, end, array, draw)
            self.quick_sort(start, p-1, array, draw)
            self.quick_sort(p+1, end, array, draw)

        if end==len(array)-1:
            draw(array, [ "green"  for x in range(len(array))])
            self.run=False

        if self.run==True:
            end_color="blue"
        else:
            end_color="green"
            
        draw(array, [ "green" if x<self.pivo  else end_color for x in range(len(array))])
    
            
if __name__=="__main__":
    app=App()
    app.mainloop()
