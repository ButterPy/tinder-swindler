from tinder_bot import bot


if __name__ == "__main__":
    like_hidden = True
    while not like_hidden:
        if search_like_button():
            like_hidden = False

    for i in range(1, 10):
        bot.like()
