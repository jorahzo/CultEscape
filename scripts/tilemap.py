class Tilemap:
    def __init__(self, game, tile_size= 16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(30):
            self.tilemap[str(0 + i) + ';10'] = {'type': 'grass', 'variant': 8, 'pos': (0 + i, 1)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'wall', 'variant': 8, 'pos': (0, 0 + i)}

    def render(self, surf):
        # These would be our background assets
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
        # This would be our tiles in the front
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            # co-ordinate system is different between tilemap and tilegrid. tilegrid is pixels
            surf.blit(self.game.assets[tile['type']][tile['variant']],
                      (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))