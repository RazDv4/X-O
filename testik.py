maps = list(range(1,10))

def maps_board(maps):
    print(maps[0], maps[1], maps[2])
    print(maps[3], maps[4], maps[5])
    print(maps[6], maps[7], maps[8])

def take_input(player_token):
   game_over = False
   while not game_over:
      player_answer = input("Куда поставим " + player_token + "? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(maps[player_answer-1]) not in "XO"):
            maps[player_answer-1] = player_token
            game_over = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Введите число от 1 до 9.")

def check_win(maps):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if maps[each[0]] == maps[each[1]] == maps[each[2]]:
          return maps[each[0]]
   return False

def main(maps):
    counter = 0
    win = False
    while not win:
        maps_board(maps)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(maps)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    maps_board(maps)
main(maps)






