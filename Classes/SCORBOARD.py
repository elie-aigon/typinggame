from Settings import *

class SCOREBOARD():
    def __init__(self, surface, pos):
        self.pos = pos
        self.surface = surface
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 180, 300)
        self.background = pygame.image.load("Data/Images/scorebaord_box.png")
        self.background = pygame.transform.scale(self.background, (450, 700))
        self.scoreboard_title = font_mid.render("Leaderboard", True, grey)

        self.sorted_scores_dic_str = []

        self.sort_scores()

    def draw_scoreboard(self):
        self.surface.blit(self.background, self.rect)
        self.surface.blit(self.scoreboard_title, ( self.pos[0] + (self.background.get_width()//2 - self.scoreboard_title.get_width()//2), self.pos[1] + 30))

        self.scoreboard_value_x = self.pos[0] + 55
        self.scoreboard_value_y = self.pos[1] + 100
        for element in self.sorted_scores_dic_str:
            scoreboard_score_rect = pygame.Rect(self.scoreboard_value_x, self.scoreboard_value_y, 303, 400)
            self.socreboard_names = font_small.render(element, True, white)
            self.surface.blit(self.socreboard_names, scoreboard_score_rect)
            self.scoreboard_value_y += 30

    def convert_time(self, seconds):
        seconds = seconds % (24 * 3600)
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%02d:%02d" % (minutes, seconds)

    def sort_scores(self):
        self.sorted_scores_dic = dict(sorted(scores_dic.items(), key=itemgetter(1), reverse=True))
        rank = 1    
        for key, value in self.sorted_scores_dic.items():
            element = " ".join((str(rank), ':', str(key), ':', str(value)))
            self.sorted_scores_dic_str.append(element)
            rank += 1

    def update_score(self, name, score):
        if name in scores_dic:
            if score < scores_dic[name]:
                scores_dic[name] = score
        else:
            scores_dic[name] = score
        with open('Data/JSON/scores.json', 'w') as f:
            json.dump(scores_dic, f)
        self.sorted_scores_dic_str = []
        self.sort_scores()