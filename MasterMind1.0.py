import tkinter as t
import random as r
from tkinter import messagebox as m
global button_last,i,leve2s,leve3s
i=0

class master:
  
  def __init__(self,levels=0,root=1):
    
    self.color="#00ff00"
    self.color2="#ff9900"
    self.root=root
    relif="ridge"
    if levels==0:
      root.destroy()
      self.root=t.Tk()
      self.root.geometry("450x580+200+20")
      self.root.title("MASTER MIND")
      self.root.wm_resizable(0,0)
      self.root2=t.Frame(self.root,height=500,width=500,bg=self.color)
      self.root2.grid(row=0,column=2,padx=1,pady=1)
      self.intro=t.Label(self.root2,text=" Level "+str(levels+1),font=("arieal",30,"italic"),bg="#00ff00",fg="red").grid()
      self.li=[1,1,2,2,3,3,4,4,5,5,6,6]
      self.moves=20
      self.how_many=0
      self.last=0
    elif levels==1:
      self.root.geometry("550x580+200+20")
      self.root.title("MASTER MIND")
      self.root2=t.Frame(self.root,height=500,width=500,bg=self.color)
      self.root2.grid(row=0,column=2)
      self.intro=t.Label(self.root2,text=" Level "+str(levels+1),font=("arieal",30,"italic"),bg="#00ff00",fg="red").grid()
      self.li=[11,11,24,24,36,36,47,47,59,59,63,63,77,77,89,89]
      self.moves=20

      self.how_many=0
      self.last=0
    elif levels==2:
      self.root.geometry("550x680+200+20")
      self.root.title("MASTER MIND")
      self.root2=t.Frame(self.root,height=500,width=500,bg=self.color)
      self.root2.grid(row=0,column=2)
      self.intro=t.Label(self.root2,text=" Level "+str(levels+1),font=("arieal",30,"italic"),bg="#00ff00",fg="red").grid()
      self.li=[11,11,24,24,36,36,47,47,59,59,63,63,77,77,89,89,99,99,28,28]
      self.moves=30
      self.how_many=0
      self.last=0  

      
    r.shuffle(self.li)  
    
    self.root.configure(bg=self.color)
   
 

    self.root1=t.Frame(self.root,height=500,width=500)
    self.root1.grid(row=11,column=2)

    self.button1=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[0],self.button1,levels))
    self.button1.grid(row=5,column=0)

    self.button2=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[1],self.button2,levels))
    self.button2.grid(row=5,column=1)

    self.button3=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[2],self.button3,levels))
    self.button3.grid(row=5,column=2)

    self.button4=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[3],self.button4,levels))
    self.button4.grid(row=6,column=0)

    self.button5=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[4],self.button5,levels))
    self.button5.grid(row=6,column=1)

    self.button6=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[5],self.button6,levels))
    self.button6.grid(row=6,column=2)

    self.button7=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[6],self.button7,levels))
    self.button7.grid(row=7,column=0)
    

    self.button8=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[7],self.button8,levels))
    self.button8.grid(row=7,column=1)
    
    self.button9=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[8],self.button9,levels))
    self.button9.grid(row=7,column=2)


    self.button10=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[9],self.button10,levels))
    self.button10.grid(row=8,column=0)

    self.button11=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[10],self.button11,levels))
    self.button11.grid(row=8,column=1)

    self.button12=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[11],self.button12,levels))
    self.button12.grid(row=8,column=2)
    if levels==1 or levels==2:
      self.button5_1=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[12],self.button5_1,levels))
      self.button5_1.grid(row=5,column=3)

      self.button10_1=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[13],self.button10_1,levels))
      self.button10_1.grid(row=6,column=3)

      self.button15_1=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[14],self.button15_1,levels))
      self.button15_1.grid(row=7,column=3)

      self.button16_1=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[15],self.button16_1,levels))
      self.button16_1.grid(row=8,column=3)

      if levels==2:
        self.button17_2=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[16],self.button17_2,levels))
        self.button17_2.grid(row=9,column=0)

        self.button18_2=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[17],self.button18_2,levels))
        self.button18_2.grid(row=9,column=1)

        self.button19_2=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[18],self.button19_2,levels))
        self.button19_2.grid(row=9,column=2)

        self.button20_2=t.Button(self.root1,height=5,width=14,font=("arieal",10,"italic"),bg=self.color2,relief=relif,command=lambda:self.check( self.li[19],self.button20_2,levels))
        self.button20_2.grid(row=9,column=3)
        
    self.happen=t.Label(self.root2,text="You Click a Number :",font=("arieal",20,"italic"),bg=self.color)
    self.happen.grid(row=9,column=0)
    
    self.pair=t.Label(self.root2,text="Pair finds : 0",font=("arieal",20,"italic"),bg=self.color)
    self.pair.grid(row=10,column=0)

    self.move=t.Label(self.root2,text="Moves Left "+str(self.moves),font=("arieal",20,"italic"),bg=self.color)
    self.move.grid(row=11,column=0)

    self.fran=t.Frame(self.root,height=20,width=14,bg=self.color).grid()

    if levels==0:
       self.back=t.Button(self.root,text="Back",height=1,width=10,font=("arieal",10,"bold"),bg=self.color2,fg="purple",relief="groove",command=lambda:introduc(self.root))
       self.back.grid(row=15,column=2)

    root.mainloop()
  def won_check(self,levels):
      global leve2s,leve3s
      if levels==0:
       if self.how_many==6:
        m.showinfo("Result","You Won in level 1")
        self.moves=20
        self.how_many=0
        self.happen["text"]="You Click a Number :"
        master(1,self.root)
       elif self.moves==1:
        m.showinfo("Result","You loose level 1")
        self.moves=20
        self.how_many=0
        self.happen["text"]="You Click a Number :"
        master(0,self.root)
      elif levels==1:
        if self.how_many==8:
         m.showinfo("Result","You Won in level 2")
         
         self.moves=20
         self.how_many=0
         self.happen["text"]="You Click a Number :"
         master(2,self.root)
        elif self.moves==1:
          m.showinfo("Result","You loose level 2")
          self.moves=20
          self.how_many=0
          self.happen["text"]="You Click a Number :"
          master(1,self.root)
      elif levels==2:
        if self.how_many==10:
         m.showinfo("Result","You Completed The Game")
         self.moves=20
         self.how_many=0 
        elif self.moves==1:
          m.showinfo("Result","You loose level 3")
          self.moves=30
          self.how_many=0
          self.happen["text"]="You Click a Number :"
          master(2,self.root)
        
  def check(self,now,button_now,levels):
      global button_last,i
      self.happen["text"]="You Click a Number :"+str(now)
      self.colors=["red","blue","yellow","white","pink","black"]
      self.won_check(levels)
      if self.last==now:
       if button_now!= button_last:
        button_now["text"]=now
        button_last["text"]=self.last
        button_last["fg"]=self.colors[i]
        button_now['fg']=self.colors[i]
        i+=1 
        if i==5:
          i=0
        self.how_many+=1
      button_last=button_now
      self.last=now
      self.moves-=1
      self.move["text"]="Moves Left "+str(self.moves)
      self.pair["text"]="Pair finds: "+str(self.how_many)
      self.won_check(levels)

def introduc(roo):
  global leve2s,leve3s
  roo.destroy()
  root=t.Tk()
  root.title("MASTER MIND")
  root.wm_resizable(0,0)
  root.geometry("560x500+200+20")
  color="#00ffcc"
  color2="#ff9900"
  root.configure(bg=color)
  intro=t.Label(root,text="   Welcome To Master Mind ",font=("arieal",30,"italic"),bg="#00ffcc").grid()
  framess=t.Frame(root,height=90,width=50,bg=color)
  framess.grid()
  frame=t.Frame(root,height=90,width=50,bg=color)
  frame.grid()
  leve1s=t.Button(frame,text="Strat The Game",font=("arieal",30,"italic"),bg=color2,command=lambda:master(0,root))
  leve1s.grid(row=5,column=1)
  about=t.Label(text="\n\n\nAbout Game:",bg=color,font=("arieal",19,"italic"),fg="#cc0066").grid()
  label=t.Label(text="This game is test your memory power\n you need find the pair of number\n if you compelete a level 1 you move to level 2 \nand level 3 is the final",bg=color,fg="#cc0066",font=("arieal",15,"italic")).grid()
  created=t.Label(text="By\n@Programmer Raja",font=("arieal",15,"italic"),bg=color,fg="#0000ff").grid()
  root.mainloop()
root=t.Tk()
introduc(root)    
