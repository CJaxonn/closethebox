import discord
import discord.utils
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as ' +
          str(client))  #Once bot is established in the server, let us know!

@client.event
async def on_message(message):
    if message.author == client.user:  #Dont respond to a message sent by the bot.
        return
    if (message.content.startswith('!box')):

        N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        gameNotOver = True

        while gameNotOver:

            await message.channel.send("Your numbers are `" + str(N[:]) +
                                       "` **!roll** the dice.")

            roll = await client.wait_for("message", timeout=60)
            if roll.content.startswith('!roll'):
                diceRoll1 = random.randint(1, 6)
                diceRoll2 = random.randint(1, 6)
                diceSum = diceRoll1 + diceRoll2
                await roll.channel.send(
                    "You rolled: `" + str(diceRoll1) + "` , `" +
                    str(diceRoll2) + "`")
                await roll.channel.send("What number(s) would you like to **!close**?")

                validClose = False
                while not validClose:
                    close = await client.wait_for("message", timeout=120)
                    c = close.content.split(' ')
                    
                    if c[0] == "!reset":
                        N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        await roll.channel.send('**Game Reset**')
                        break

                    elif c[0] == "!end":
                        await roll.channel.send("**Game Ended**")
                        gameNotOver = False
                        break

                    elif c[0] == "!numbers":
                      await roll.channel.send("Your numbers are " + str(N[:]))

                    elif c[0] != "!close":
                        await roll.channel.send(
                            "Command not recognized"
                        )
                    else:
                        try:

                            if len(c) == 1:
                                await roll.channel.send(
                                    "Invalid input, no numbers given"
                                )
                            elif len(c) == 3:
                              if int(c[1]) in N and int(c[2]) in N:
                                      if diceSum == int(c[1]) + int(
                                    c[2]):
                                
                                        N.remove(int(c[1]))
                                        N.remove(int(c[2]))
                                        if N == []:
                                            await roll.channel.send("YOU WIN! :trophy: ")
                                            gameNotOver = False
                                            break
                                        validClose = True
                                        break
                                
                                      else: await roll.channel.send(
                                        "Invalid input, addition error"
                                    )
                              elif int(c[1]) not in N and int(c[2]) not in N:
                                if int(c[1]) in range (1,10) and int(c[2]) in range (0, 10):
                                    await roll.channel.send(
                                        "Invalid input, both numbers already closed")
                                else:
                                  await roll.channel.send(
                                        "Invalid input, invalid number"
                                    )
                              else:
                                if int(c[1]) in range (0,10) and int(c[2]) in range (0,10):
                                    await roll.channel.send(
                                        "Invalid input, one number already closed")
                                else:
                                  await roll.channel.send(
                                        "Invalid input, invalid number"
                                    )
                          
                            elif len(c) == 2:
                              if diceSum == int(c[1]):
                                if int(c[1]) in N:
                                    N.remove(int(c[1]))
                                    if N == []:
                                        await roll.channel.send("YOU WIN!")
                                        gameNotOver = False
                                        break

                                    validClose = True
                                    break
                                elif int(c[1]) in range(0,10):
                                    await roll.channel.send(
                                        "Invalid input, number already closed"
                                    )
                                else:
                                  await roll.channel.send(
                                        "Invalid input, invalid number"
                                    )
                              else:  await roll.channel.send(
                                        "Invalid input, addition error"
                                    )
                        except:
                            await roll.channel.send(
                                "Invalid input"
                            )
                            pass
            if roll.content.startswith('!end'):
                await roll.channel.send("Game Ended")
                gameNotOver = False
                break

client.run('TOKEN')
