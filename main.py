from map import Map

m = Map()
m.generateMap()
m.drawMap()
print('\n')
m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)

m = Map(mode=1)
m.generateMap()
m.drawMap()
print('\n')
m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)
