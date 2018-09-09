from steamapi import core, user
import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='Steam Info Grabber by u/LunaFr0st')
                     
core.APIConnection(api_key='steam dev api key', validate_key=True)
subreddit = reddit.subreddit('Subreddits you want the bot to skim')

profileID = '[id]'
profileNum = '[64]'

for comment in subreddit.stream.comments():
    if not comment.saved():
        if profileID in comment.body:
            word = comment.body.replace(profileID, '')
            try:
                rUser = user.SteamUser(userurl=word)
                comment.reply('Name|Steam 64|URL|Has Vac?|Level|Current XP\n-|-|-|-|-|-\n'+rUser.name+'|'+str(rUser.steamid)+'|'+rUser.profile_url+'|'+str(rUser.is_vac_banned)+'|'+str(rUser.level)+'|'+str(rUser.xp))
                print('User: ' + str(rUser.steamid))
                comment.save()
            except Exception as e:
                print(e)
        if profileNum in comment.body:
            word = comment.body.replace(profileNum, '')
            try:
                rUser = user.SteamUser(userid=word)
                comment.reply('Name|Steam 64|URL|Has Vac?|Level|Current XP\n-|-|-|-|-|-\n'+rUser.name+'|'+str(rUser.steamid)+'|'+rUser.profile_url+'|'+str(rUser.is_vac_banned)+'|'+str(rUser.level)+'|'+str(rUser.xp))
                print('User: ' + str(rUser.steamid))
                comment.save()
            except Exception as e:
                print(e)
    else:
        print('Already replied to this comment')