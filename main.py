
import math

if __name__ == '__main__':

    (x, y, z) = (31, 22, -90)
    f = math.sqrt(81 * math.pow(y, 6) + 37 * z - 61) - math.sqrt((26 * math.pow(x, 4) + math.exp(y))/(math.pow(y, 7) + math.exp(x))) + ((math.tan(y) - math.exp(z) )/( 7 * math.pow(z, 7) - math.pow(z, 5)))
    print '%e' %f
