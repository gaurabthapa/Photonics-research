import numpy as np 
import matplotlib.pyplot as plt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 
    
def get_MMIoutorigions(Ymat,Zmat,Emat,height,width):
    Erow, Ecolumn =Emat.shape

    try: 
        Efirst, Esecond=np.hsplit(Emat, 2)
        halfcolumn=int(Ecolumn/2)
    except:
        halfcolumn=int((Ecolumn+1)/2)
        Efirst =Emat[:,:halfcolumn]
        Esecond =Emat[:,halfcolumn:Ecolumn]
    

    E1MaxPos=np.argmax(Efirst)
    E1MaxRow, E1MaxColumn = divmod(E1MaxPos, halfcolumn)
    M1Maxpos=[Ymat[E1MaxRow,E1MaxColumn],Zmat[E1MaxRow,E1MaxColumn]]

    E2MaxPos=np.argmax(Esecond)
    E2MaxRow, E2MaxColumn = divmod(E2MaxPos, (Ecolumn-halfcolumn))
    M2Maxpos=[Ymat[E2MaxRow,E2MaxColumn+halfcolumn],Zmat[E2MaxRow,E2MaxColumn+halfcolumn]]

    rectdim=[width/2,height/2]
    rectE1origin=np.array(M1Maxpos)-np.array(rectdim)
    rectE2origin=np.array(M2Maxpos)-np.array(rectdim)
    return rectE1origin,rectE2origin

#name of text file and the headings for data in the text file from lumerical
fname = '2inputsMMI6.5.txt'
lookup1 = 'x(microns)'
lookup2 = 'y(microns)'
lookup3 = 'field_profile:E:'


with open(fname) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup1 in line:
            print ('begin x-data at row', num)
            n1 = num
        elif lookup2 in line:
            print ('begin z-data at row', num)
            n2 = num
        elif num > 10 and lookup3 in line:
            n3 = num
            print ('begin fields data at row', n3)
            
Y= np.genfromtxt(fname=fname, dtype=float, skip_header=(n1),max_rows=(n2-(n1+2)))[np.newaxis]
Z= np.genfromtxt(fname=fname, dtype=float, skip_header=(n2),max_rows=(n3-(n2+2)))[np.newaxis]
Emat= np.genfromtxt(fname=fname, dtype=float, skip_header=(n3))
Emat=Emat.T
Ymat, Zmat = np.meshgrid(Y,Z)
print(Ymat.shape)
#plt.style.use('grayscale')
cs=plt.pcolormesh(Ymat,Zmat,Emat) #vmin=0, vmax=0.25
#plt.contour(Ymat, Zmat,Emat, 4, colors='k')#the z and y values need to be a matrix
plt.colorbar(cs)
plt.xlabel('Distance in X axis(um)')
plt.ylabel('Distance in Y axis(um)')

#===============================================================================
#MMI to plot points for the waveguides
# height=0.22
# width=0.8
# rectE1origin,rectE2origin =get_MMIoutorigions(Ymat=Ymat,Zmat=Zmat,Emat=Emat,height=height,width=width)
# plt.gca().add_patch(plt.Rectangle(xy=rectE1origin,height=height,width=width,fill=False))
# plt.gca().add_patch(plt.Rectangle(xy=rectE2origin,height=height,width=width,fill=False)) 
#===============================================================================

plt.show()
