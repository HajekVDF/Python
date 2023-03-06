"""
Funkce pro nalezení trojúhelníku s největším obsahem na základě čtyř bodů (souřadnic) na vstupu.

"""


def get_area(a, b, c):
    area = 0.5*((a[0]*(b[1]-c[1])) + (b[0]*(c[1]-a[1])) + (c[0]*(a[1]-b[1])))
    return abs(area) 

def get_triangle(point_a, point_b, point_c, point_d = False):
    try:
        area_abc = get_area(point_a, point_b, point_c)
        area_abd = get_area(point_a, point_b, point_d)
        area_bcd = get_area(point_b, point_c, point_d)
        area_acd = get_area(point_a, point_c, point_d)
    except:
        if area_abc == 0:
            return False
        else:
            return point_a, point_b, point_c
    
    triangle_points = {
        "abc": (point_a, point_b, point_c),
        "abd": (point_a, point_b, point_d),
        "acd": (point_a, point_c, point_d),
        "bcd": (point_b, point_c, point_d)
    }

    triangle_areas = {
        "abc": area_abc,
        "abd": area_abd,
        "acd": area_acd,
        "bcd": area_bcd
    }

    if max(triangle_areas.values()) == 0:
        return False

    biggest = max(triangle_areas, key=triangle_areas.get)

    return triangle_points[biggest]


print(get_triangle((1,1),(3,1),(2,2),(2,3)))
