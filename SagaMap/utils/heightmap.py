import numpy


class HeightMap:
    water_level = None
    HeightData = []
    info = None

    def __init__(self, info):
        self.info = info
        self.water_level = info.water_level
        self.LoadHMap()

    def LoadHMap(self):
        maxX = self.info.size;
        maxY = self.info.size;

        self.HeightData = numpy.zeros((maxX,maxY))

        try:
            with open('MapInfo/' + self.info.name + '.hmap', 'r') as hmap:
                binary = hmap.read()
                index = 0
                for y in xrange(maxY):
                    for x in xrange(maxX):
                        data = binary[index:index+2]
                        self.HeightData[x, y] = (((data[0] | data[1] << 8) - 32768) / 32768) * (self.info.size / 2);

        except Exception e:
            print e

