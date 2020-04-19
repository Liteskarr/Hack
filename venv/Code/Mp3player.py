import pygame


class Mp3player:
    """"
    Музыкальный Плеер.
    """

    def __init__(self, fileWay):
        """
        :param fileWay - путь к файлу .mp3:
        """
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(fileWay)

    def play(self):
        """

        :воспроизвести музыку
        """
        pygame.mixer.music.play(loops=-1)
        while pygame.mixer.music.get_busy():
            self.clock.tick(1000)

    def stop(self):
        """
        Остановить музыку
        :return:
        """
        pygame.mixer.music.stop()
        pygame.music.music.quit()
