class Sphere:

    def __init__(self, radius=None, x=None, y=None, z=None):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        if radius is None and x is None and y is None and z is None:
            self.radius = 1
            self.x = 0
            self.y = 0
            self.z = 0
        elif radius and x is None and y is None and z is None:
            self.radius = radius
            self.x = 0
            self.y = 0
            self.z = 0

    def get_volume(self):
        return 4 / 3 * 3.14 * (self.radius ** 3)

    def get_square(self):
        return 4 * 3.14 * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        xyz = []
        xyz.append(self.x)
        xyz.append(self.y)
        xyz.append(self.z)
        return tuple(xyz)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        if (self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2 + self.z1 - self.z ** 2 < self.radius ** 2:
            return True
        else:
            return False

sphere = Sphere(radius=4)
print(sphere.get_volume())
print(sphere.get_square())
print(sphere.get_radius())
print(sphere.get_center())
sphere.set_radius(radius=3)
sphere.set_center(x=2, y=2, z=2)
print(sphere.is_point_inside(x1=5, y1=6, z1=5))