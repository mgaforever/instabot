def unlike(bot, media_id):
    if not bot.check_media(media_id):
        return False
    if super(bot.__class__, bot).unlike(media_id):
        bot.total_unliked += 1
        return True
    return False

def unlike_medias(bot, media_ids):
    # TODO: unlike each media from list
    pass
