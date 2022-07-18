import os

class Word:
    def __init__(self, word, tip):
        self.word = word
        self.tip = tip
        self._tela = list('_' * len(self.word))

    def tela(self):
        print('―' * 60)
        print('Qual a palavra?'.center(25), ' '.join(self._tela).center(10))
        print('Dica: '.center(25), self.tip.center(len(self.word) * 2))
        print('―' * 60)

    def completed(self):
        if '_' not in self._tela:
            return True
        else:
            return False

    def tem_letra(self, _letra):
        if _letra in self.word:
            for index, letra in enumerate(self.word):
                if letra == _letra:
                    self._tela[index] = _letra
            return True
        else:
            return False

    def valid_word(self):
        return self.word.isalpha()


class Hangman():
    def __init__(self, class_word):
        self.word_class = class_word
        self._life = 5
        self._typed = []

    def show_status(self):
        letters = '\033[31m' + ','.join(self._typed).rjust(20) + '\033[0;0m'
        self.word_class.tela()
        print(letters, '\033[33m' + 'Vidas: '.rjust(30) + '\033[0;0m', self._life)

    def is_valid_letter(self, letter):
        if letter not in self._typed:
            return letter.isalpha()

    def play(self):
        os.system('cls')
        while True:
            self.show_status()
            letter_player = input('[J-2] Adivinhe a letra: ')
            os.system('cls')
            if self.is_valid_letter(letter_player):
                self._typed.append(letter_player)
                if not self.word_class.tem_letra(letter_player):
                    self._life -= 1
                    if self._life == 0:
                        bad = '\033[31m' + f'Vc tem {self._life} vidas Fim de Jogo !' + '\033[0;0m'
                        print(bad.center(55), '\n' * 10)
                        break
            if self.word_class.completed():
                sucess = '\033[32m' + 'Parabéns voçê advinhou a palavra' + '\033[0;0m'
                self.show_status()
                print('\n\n', sucess.center(63), '\n' * 7)
                break


if __name__ == '__main__':
    os.system('cls')
    while True:
        player_word = input('[J-1] Digite uma Palavra ou Enter p/ encerrar: ').replace(' ', '')
        if player_word == '':
            break
        if player_word.isalpha():
            player_tip = input('[ ? ] Dica da palavra: ')
            word = Word(player_word, player_tip)
            game = Hangman(word)
            game.play()
        else:
            os.system('cls')

