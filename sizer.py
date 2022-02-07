def sizer(clss):
    def size(self):
        if hasattr(self,'__len__') or hasattr(self,'__abs__'):
            try:
                sz=len(self)
            except:
                try:
                    sz=abs(self)
                except:
                    sz=0 
        else:
            sz=0               
        return sz

    clss.size=property(size)
    return clss    
