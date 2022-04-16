import pytest
import calcLib

class Test_Basic:

    #ADDITION
    @pytest.mark.parametrize("x,y,z",[(1,2,3),
                                      (1,0,1),
                                      (0,0,0),
                                      (2,-1,1),
                                      (1,-2,-1),
                                      (1.365,-2,-0.635)])
    def test_add(self,x,y,z):
        assert calcLib.add(x,y) == z
        assert calcLib.add(y,x) == z
    
    #SUBTRACTION
    @pytest.mark.parametrize("x,y,z",[(2,1,1),
                                      (1,0,1),
                                      (0,0,0),
                                      (2,-1,3),
                                      (1,-2,3),
                                      (1.365,2,-0.635)])
    def test_sub(self,x,y,z):
        assert calcLib.sub(x,y) == z
        assert calcLib.sub(y,x) == -z
    
    #MULTIPLICATION
    @pytest.mark.parametrize("x,y,z",[(2,2,4),
                                      (5,0,0),
                                      (2,-2,-4),
                                      (-3,-3,9),
                                      (3.698,3,11.094),
                                      (2.789,-5.852,-16.321228)])
    def test_multiply(self,x,y,z):
        assert calcLib.mul(x,y) == z
        assert calcLib.mul(y,x) == z

    #DIVISION
    @pytest.mark.parametrize("x,y,z",[(6,3,2),
                                      (0,3,0),
                                      (-6,2,-3),
                                      (-8,-4,2),
                                      (3.456,9.852,0.3507917174177832),
                                      (8.456,-4.852,-1.7427864798021433)])
    def test_division(self,x,y,z):
        assert "{0:.16f}".format(calcLib.div(x,y)) == "{0:.16f}".format(z)
        if x!=0:
            assert "{0:.14f}".format(calcLib.div(y,x)) == "{0:.14f}".format(1/z)
    
    def test_division_zero(self):
        with pytest.raises(ZeroDivisionError):
            calcLib.div(1,0)


class Test_advanced:
    
    #FACTORIAL
    def test_factorial(self):
        assert calcLib.fac(10) == 3628800
        assert calcLib.fac(15) == 1307674368000
        assert calcLib.fac(1) == 1
        assert calcLib.fac(0) == 1
        with pytest.raises(TypeError):
            calcLib.fac(-1)
        with pytest.raises(TypeError):
            calcLib.fac(3.35)
        with pytest.raises(TypeError):
            calcLib.fac(-2.963)
    
    #POWER
    @pytest.mark.parametrize("x,n,y",[(2,2,4),
                                      (5,1,5),
                                      (32,0,1),
                                      (-6,2,36),
                                      (-3,3,-27),
                                      (3.3,3,35.937),
                                      (5,-5,1/3125),
                                      (-3.3,-3,-1/35.937),
                                      (5,1/2,2.2360679774997896964091736687313),
                                      (4,-2/3,0.396850262992050),
                                      (0,0,1)])     #Using definition 0^0=1
    def test_power(self,x,n,y):
        assert "{0:.15f}".format(calcLib.pwr(x,n)) == "{0:.15f}".format(y)
    
    #ROOT
    @pytest.mark.parametrize("x,n,y",[(4,2,2),
                                      (27,3,3),
                                      (0,35,0),
                                      (1,32,1),
                                      (-27,3,-3),
                                      (985,1,985)])
    def test_root(self,x,n,y):
        assert "{0:.15f}".format(calcLib.root(x,n)) == "{0:.15f}".format(y)
    
    @pytest.mark.parametrize("x,n",[(1,-2),
                                    (5,0),
                                    (2,1/2),
                                    (3,-5/3),
                                    (-4,2),
                                    (-8,-3)])
    def test_root_exception(self,x,n):
        with pytest.raises(TypeError):
            calcLib.root(x,n)

    @pytest.mark.parametrize("x,y",[(1,0),
                                    (2,0.6931471805599453),
                                    (3,1.0986122886681096),
                                    (5,1.6094379124341003),
                                    (50,3.912023005428146),
                                    (0.05,-2.995732273553991),
                                    (0.5,-0.6931471805599453),
                                    (0.3,-1.2039728043259361),
                                    (0.2,-1.6094379124341003)])
    def test_ln(self,x,y):
        assert "{0:.15}".format(calcLib.ln(x)) == "{0:.15}".format(y)
    
    @pytest.mark.parametrize("x",[0,-1,-2,-500,-0.1,-0.5,-0.0000003])
    def test_ln_exception(self,x):
        with pytest.raises(TypeError):
            calcLib.ln(x)