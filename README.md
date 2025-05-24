# PythonPingPong

# README

## Описание

Это простая игра в пинг-понг, написанная на Python с использованием библиотеки Pygame. Игроки управляют ракетками и пытаются отбить мяч, чтобы не дать ему упасть за пределы экрана. Игра поддерживает двух игроков, которые могут управлять своими ракетками с помощью клавиатуры.

## Установка

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше).
2. Установите Pygame, выполнив команду: `
   pip install pygame
   `
3. Скачайте или клонируйте репозиторий с игрой.
4. Поместите необходимые изображения (например, ```
   player.png
   ```

   , ```
   enemy.png
   ```

   , ```
   ball.png
   ```

   , ```
   bg.png
   ```

   ) в папку ```
   pngs
   ```

   .
5. Создайте файл ```
   data/data.json
   ```

    с параметрами игры, например:```
   {
       "game_speed": 5,
       "ball_size": 20
   }
   
   ```

## Запуск игры

Запустите игру, выполнив команду:

```
python main.py
```

## Управление

- Игрок 1:
  - Двигаться влево: ```
    A
    ```
  - Двигаться вправо: ```
    D
    ```
- Игрок 2:
  - Двигаться влево: ```
    LEFT ARROW
    ```
  - Двигаться вправо: ```
    RIGHT ARROW
    ```
- Перезапустить игру: ```
  SPACE
  ```

   или ```
  R
  ```

## Примечания

- Игра имеет режим отладки, который можно включить, изменив переменную ```
  debug
  ```

   на ```
  True
  ```

   в коде.
- Вы можете изменить параметры игры, редактируя файл ```
  data/data.json
  ```

  .

---

## Description

This is a simple ping-pong game written in Python using the Pygame library. Players control paddles and try to hit the ball to prevent it from falling off the screen. The game supports two players who can control their paddles using the keyboard.

## Installation

1. Make sure you have Python installed (recommended version 3.6 and above).
2. Install Pygame by running the command:```
   pip install pygame
   
   ```
3. Download or clone the repository containing the game.
4. Place the necessary images (e.g., ```
   player.png
   ```

   , ```
   enemy.png
   ```

   , ```
   ball.png
   ```

   , ```
   bg.png
   ```

   ) in the ```
   pngs
   ```

    folder.
5. Create a ```
   data/data.json
   ```

    file with game parameters, for example:```
   {
       "game_speed": 5,
       "ball_size": 20
   }
   
   ```

## Running the Game

Run the game by executing the command:

```
python main.py
```

## Controls

- Player 1:
  - Move left: ```
    A
    ```
  - Move right: ```
    D
    ```
- Player 2:
  - Move left: ```
    LEFT ARROW
    ```
  - Move right: ```
    RIGHT ARROW
    ```
- Restart the game: ```
  SPACE
  ```

   or ```
  R
  ```

## Notes

- The game has a debug mode that can be enabled by changing the ```
  debug
  ```

   variable to ```
  True
  ```

   in the code.
- You can change game parameters by editing the ```
  data/data.json
  ```

   file.
