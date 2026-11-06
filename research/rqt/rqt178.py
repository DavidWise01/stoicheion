import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def model(b,g):
    assert 1<=b<=10 and 0<=g<=min(20-2*b,b-1)
    C=s.zeros(4)
    for j in range(4): C[(j+1)%4,j]=1
    Q=s.Matrix([[-1]]);R=s.Matrix([[0,-1],[1,0]])
    H=s.Matrix([[-1,0,0],[0,0,-1],[1,1,0]])
    return s.diag(C,*([Q]*(20-2*b-g)),*([R]*(b-1-g)),*([H]*g))

def rank2(A):
    basis={}
    for i in range(A.rows):
        x=sum((int(A[i,j])&1)<<j for j in range(A.cols))
        while x:
            j=x.bit_length()-1
            if j in basis: x^=basis[j]
            else: basis[j]=x;break
    return len(basis)

for b,g in [(1,0),(5,0),(5,2),(5,4),(10,0)]:
    X=model(b,g); I=s.eye(22); D=X-I
    N=I+X+X**2+X**3
    assert X**4==I and N.rank()==1
    assert N*I[:,0]==s.Matrix([1]*4+[0]*18)
    recovered_b=(22-s.trace(X**2))/4
    recovered_g=rank2(D)-recovered_b-2
    assert (recovered_b,recovered_g)==(b,g)
    SN=smith_normal_form(D,domain=ZZ)
    factors=[abs(int(SN[j,j])) for j in range(22)]
    assert tuple(factors.count(n) for n in (1,2,4,0))==(b+g+2,19-b-2*g,g,1)
    print('PASS',b,g,'rank2',rank2(D),'rank D²',rank2(D**2))
