class Collection:
for game in self.gameList:
            print(game)
    def DisplayMovie(self):
        for movie in self.movieList:
            print(movie)
    def DisplayFavGame(self):
        print(f'Fav Game: {self.favGame}')
    def DisplayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')
    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovie()
        self.DisplayFavMovie()
    def setfavmovie(self, movie):
        if movie not in self.movieList:
            self.AddMovie(movie)
        self.favMovie = movie
    def setfavgame(self, game):
        if game not in self.gameList:
            self.AddGame(game)
        self.favGame = game

















































