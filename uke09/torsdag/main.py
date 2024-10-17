from podcast import Podcast

def main():
    podcast = Podcast("Supernytt forklarer")
    podcast.legg_til_episode("Hva skjedde med Prime?", "Maria Pedko Lindbäck", ["KSI", "Logan Paul"])
    podcast.skriv_tabell()

main()