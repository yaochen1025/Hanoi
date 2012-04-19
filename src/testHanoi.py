import Hanoi
import unittest
import random
import math

class Test_Hanoi(unittest.TestCase):


    def test_int2baseTwo(self):
        self.assertEqual(Hanoi.int2baseTwo(2),[0,1])
        self.assertEqual(Hanoi.int2baseTwo(74),[0,1,0,1,0,0,1])
        self.assertEqual(Hanoi.int2baseTwo(2363243),[1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])

    def test_randLocationR(self):
        r=Hanoi.randLocationR(100)
        self.assertEqual(0 in r, True)
        self.assertEqual(1 in r, True)
        self.assertEqual(2 in r, True)
        self.assertEqual(len(r),100)
        sm=0
        for i in range(100):
            self.assertTrue(r[i]==0 or r[i]==1 or r[i]==2)
            sm=sm+r[i]
        self.assertEqual(sm<125, True)
        self.assertEqual(sm>75, True)

    def test_rollcall2List(self):
        self.assertEqual(Hanoi.rollcall2List([0,1,0,1,2,0,2]) ,[[2,5,7],[4,6],[1,3]])
        self.assertEqual(Hanoi.rollcall2List([0,1,2,2,0]) ,[[1,5],[4],[2,3]])
        self.assertEqual(Hanoi.rollcall2List([0,0,0,1,1,1,2,2,2]) ,[[7,8,9],[4,5,6],[1,2,3]])
        
    def test_list2Rollcall(self):
        for i in range(5,100):
            r1=Hanoi.randLocationR(i)
            L=Hanoi.rollcall2List(r1)
            r2=Hanoi.list2Rollcall(L)
            self.assertEqual(r1,r2)

    def test_makeMoves(self): #probably calls isLegalMove
        L=[[4],[1,2,3],[]];
        Hanoi.makeMove(L,2,0);
        Hanoi.makeMove(L,2,2);
        Hanoi.makeMove(L,0,2);
        Hanoi.makeMove(L,1,2);
        Hanoi.makeMove(L,1,0);
        Hanoi.makeMove(L,2,0);
        Hanoi.makeMove(L,1,2);
        Hanoi.makeMove(L,0,1);
        Hanoi.makeMove(L,0,2);
        Hanoi.makeMove(L,1,2);
        k=[[],[],[1,2,3,4]];
        self.assertEqual(L,k);

    def test_rollcall2SA(self):
        R=[1,0,2,0,0,1,0]
        SA=[1,2,1,0,0,2,1]
        self.assertEqual(Hanoi.rollcall2SA(R),SA)

    def test_SA2rollcall(self):
        for i in range(7):
            for j in range(5,10):
                R1=Hanoi.randLocationR(j)
                SA=Hanoi.rollcall2SA(R1)
                R2=Hanoi.SA2rollcall(SA)
                self.assertEqual(R1,R2)

    def test_SA2TA(self):
        self.assertEqual(Hanoi.SA2TA([0,2,0,1]),[5,14,11])
        self.assertEqual(Hanoi.SA2TA([1,2,0,1]),[13,6,11])
        self.assertEqual(Hanoi.SA2TA([0,0,0]),[0,7,7])
        self.assertEqual(Hanoi.SA2TA([0,0,2]),[1,7,6])
        self.assertEqual(Hanoi.SA2TA([1,1,1]),[7,0,7])
        self.assertEqual(Hanoi.SA2TA([1,2,2]),[7,3,4])
        self.assertEqual(Hanoi.SA2TA([2,0,1]),[5,6,3])
        self.assertEqual(Hanoi.SA2TA([1,2,1,0,0,2,1]),[115,46,93])

    def test_TA2SA(self):
         for i in range(7):
            for j in range(5,10):
                SA1=Hanoi.randLocationR(j)#It's just 0,1,2's anyhow
                TA=Hanoi.SA2TA(SA1)
                SA2=Hanoi.TA2SA(TA)
                self.assertEqual(SA1,SA2)

    def test_reduceTA1(self):
        SA1=[1,2,0,1,2,1,0,1]
        SA2=[1,2,0,2,1,0,2,1]
        TA1=Hanoi.SA2TA(SA1)
        TA2=Hanoi.SA2TA(SA2)
        Hanoi.reduceTA(TA1,TA2)
        RSA1=Hanoi.TA2SA(TA1)
        RSA2=Hanoi.TA2SA(TA2)
        self.assertEqual(RSA1,[1,2,1,0,1])
        self.assertEqual(RSA2,[2,1,0,2,1])

    def test_reduceTA2(self):
        SA1=[2,1,0,0,2,0,1,2,0,0,0]
        SA2=[2,1,0,0,2,0,2,1,0,1,0]
        TA1=Hanoi.SA2TA(SA1)
        TA2=Hanoi.SA2TA(SA2)
        Hanoi.reduceTA(TA1,TA2)
        RSA1=Hanoi.TA2SA(TA1)
        RSA2=Hanoi.TA2SA(TA2)
        self.assertEqual(RSA1,[1,2,0,0,0])
        self.assertEqual(RSA2,[2,1,0,1,0])

    def test_reduceTA3(self):
        SA1=[2,1,0,0,2,0,1,2,0,0,0]
        SA2=[2,1,0,0,2,0,1,2,0,0,0]
        TA1=Hanoi.SA2TA(SA1)
        TA2=Hanoi.SA2TA(SA2)
        Hanoi.reduceTA(TA1,TA2)
        RSA1=Hanoi.TA2SA(TA1)
        RSA2=Hanoi.TA2SA(TA2)
        self.assertEqual(RSA1,[])
        self.assertEqual(RSA2,[])

    def test_distTA(self):
        self.assertEqual(Hanoi.distTA([5,14,11],[13,6,11]),12)
        self.assertEqual(Hanoi.distTA([1,7,6],[7,2,5]),7)
        self.assertEqual(Hanoi.distTA(Hanoi.SA2TA([0,0,0,2]),Hanoi.SA2TA([1,1,2,0])),14)
        self.assertEqual(Hanoi.distTA(Hanoi.SA2TA([1,2,1,0,0,0,2]),Hanoi.SA2TA([1,2,1,1,1,2,0])),14)
        self.assertEqual(Hanoi.distTA(Hanoi.SA2TA([0,0,0,2]),Hanoi.SA2TA([0,0,0,2])),0)
        

    def test_distCoherence(self):
        for iterations in range(10000):    
            R_A=Hanoi.randLocationR(8)
            T_A=Hanoi.SA2TA(Hanoi.rollcall2SA(R_A))
            L_A=Hanoi.rollcall2List(R_A)
            R_B=Hanoi.randLocationR(8)
            T_B=Hanoi.SA2TA(Hanoi.rollcall2SA(R_B))
            dist0=Hanoi.distTA(T_A,T_B)
            #look for neighbors of A, and their distances to B
            Legal=[[False,False,False],[False,False,False],[False,False,False]]
            for i in range(3):
                for j in range(3):
                    Legal[i][j]=Hanoi.isLegalMove(L_A,i,j)
                Legal[i][i]=False #not neighbor to self
            distVect=[]
            for i in range(3):
                for j in range(3):
                    if Legal[i][j]:
                        Hanoi.makeMove(L_A,i,j)
                        T_temp=Hanoi.SA2TA(Hanoi.rollcall2SA(Hanoi.list2Rollcall(L_A)))
                        distVect.append(Hanoi.distTA(T_temp,T_B))
                        Hanoi.makeMove(L_A,j,i)
            self.assertTrue((dist0-1 in distVect) or dist0==0)
            for e in distVect:
                stmt=(e==dist0 or e==dist0+1 or e==dist0-1)
                self.assertTrue(stmt)
            self.assertTrue(len(distVect)==3 or len(distVect)==2)    
        

        
unittest.main()
