from episode import Episode

class Podcast:
    def __init__(self, navn: str):
        self._navn = navn
        self._episode = []
        self._ant_episoder = 0

    def legg_til_episode(self, episodenavn: str, hostnavn: str, gjestenavn: list[str]):
        self._ant_episoder += 1
        episode = Episode(episodenavn, self._ant_episoder)
        episode.legg_til_host(hostnavn)
        for navn in gjestenavn:
            episode.legg_til_gjest(navn)
        self._episode.append(episode)

    def skriv_tabell(self):
        for episode in self._episode:
            print(episode)
            print()
