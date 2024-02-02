

from installation import *
from utilities import *


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping Command
    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds
        embed = discord.Embed(title="Ping", description=f"Pong! Latency is {latency}ms", color=embed_colour)
        await ctx.send(embed=embed) 


    @commands.command()
    async def say(self, ctx, message: str=None):
        if message is None:
            embed = discord.Embed(
                title="Incorrect say usage",
                description=f"Please specify a message. Usage: `{prefix}say <message>`",
                color=embed_error
            )
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(title="Say", description=message, color=embed_colour) # 'description=message' set description to whatever their parsed in
        await ctx.send(embed=embed)


    # Invite Command
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite", description=bot_invite, color=embed_colour)
        await ctx.send(embed=embed) 


    @commands.command(aliases=['server'])
    async def server_info(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Server Information", color=embed_colour)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Server Name", value=guild.name, inline=True)
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Owner", value=guild.owner.display_name, inline=True)
        # Removed the line for region since it's no longer available
        embed.add_field(name="Creation Time", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        await ctx.send(embed=embed)


    @commands.command(aliases=['user'])
    async def user_info(self, ctx, user: commands.MemberConverter = None):
        user = user or ctx.author  # If user is None, use the author of the command
        embed = discord.Embed(title="User Information", color=embed_colour)
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="Username", value=user.display_name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    async def avatar(self, ctx, user: commands.MemberConverter = None):
        user = user or ctx.author # if no user is input then set it to the author (the one who ran the command)

        embed = discord.Embed(title=f"{user.display_name}'s Avatar", color=embed_colour)

        if user.avatar:
            # User has an avatar, include the URL in the embed
            embed.set_image(url=user.avatar.url)
        else:
            # User doesn't have an avatar, provide a default image or message
            embed.description = "This user does not have an avatar."

        await ctx.send(embed=embed)


    @commands.command(aliases=['ball', '8_ball', '8'])
    async def eight_ball(self, ctx, *, question: str=None):
        if question is None: # if no question is parsed
            embed = discord.Embed(
                title="Incorrect eight ball usage",
                description=f"Please specify a question. Usage: `{prefix}eight_ball <question>`",
                color=embed_error
            )
            await ctx.send(embed=embed)
            return
        
        responses = ["It is certain.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        answer = random.choice(responses)
        embed = discord.Embed(title="🎱 Magic 8-Ball", description=f"Question: {question}\nAnswer: {answer}", color=embed_error)
        await ctx.send(embed=embed)
    

    @commands.command(aliases=['qrcode'])
    async def qr(self, ctx, link: str=None):
        if link is None: # if no link is parsed
            embed = discord.Embed(
                title="Incorrect link usage",
                description=f"Please specify a link. Usage: `{prefix}qr <link>`",
                color=embed_error
            )
            await ctx.send(embed=embed)
            return

        # Generate QR code
        qr = qrcode.QRCode( 
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link) # add the link
        qr.make(fit=True) # fit to image (make it good size)

        img = qr.make_image(fill_color="black", back_color="white") # black and white

        # Save the image to a BytesIO object
        with BytesIO() as image_binary:
            img.save(image_binary, 'PNG') # save as png
            image_binary.seek(0)
            # Send the image in discord
            file = discord.File(fp=image_binary, filename='qr_code.png')
            await ctx.send(f"Here is your QR code linking to: {link}", file=file)
    

    @commands.command()
    async def membercount(self, ctx):
        guild = ctx.guild
        member_count = guild.member_count # get guild membercount

        # Create and send an embed
        embed = discord.Embed(title="Member Count", color=embed_colour)
        embed.add_field(name="Server Members", value=f"The server has {member_count} members.", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def dice(self, ctx):
        result = random.randint(1, 6) # random dice roll

        # Create and send an embed
        embed = discord.Embed(title="Dice Roll", color=embed_colour)
        embed.add_field(name="Result", value=f"You rolled a {result}!", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def quote(self, ctx):
        # Fetch a random quote from the Quotable API
        response = requests.get("https://api.quotable.io/random") # get random quote from this api

        # warning, speeds for this api can be slow during peak times (its a free api allow it)

        if response.status_code == 200:
            quote_data = response.json()
            content = quote_data.get("content", "Quote not available.")
            author = quote_data.get("author", "Unknown")

            # Create and send an embed
            embed = discord.Embed(title="Quote of the Day", color=embed_colour)
            embed.add_field(name="Content", value=content, inline=False)
            embed.add_field(name="Author", value=author, inline=False)

            await ctx.send(embed=embed)
        else: # if this happens open an error on github (this means the api is no longer valid or its offline)
            await ctx.send("Failed to fetch the daily quote. Try again later.")


    @commands.command(aliases=['calc'])
    async def calculator(self, ctx, expression: str = None):
        if expression is None:
            # Handle the case where no expression is provided
            embed = discord.Embed(title="Error", description="You need to provide a mathematical expression.", color=embed_error)
            await ctx.send(embed=embed)
            return

        try:
            result = eval(expression) # calculation

            # Create a success embed
            embed = discord.Embed(title="Calculation Result", color=embed_colour)
            embed.add_field(name="Expression", value=expression, inline=False)
            embed.add_field(name="Result", value=result, inline=False)

            await ctx.send(embed=embed)
        except Exception as e:
            # Create an error embed
            embed = discord.Embed(title="Error", description=str(e), color=embed_error)

            await ctx.send(embed=embed)


    @commands.command()
    async def joke(self, ctx):
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke") # random joke from api
            joke_data = response.json()
            setup = joke_data["setup"] # get the joke setup
            punchline = joke_data["punchline"] # get the punchline

            # Create an embed
            embed = discord.Embed(title="Joke Time!", color=embed_colour)
            embed.add_field(name="Setup", value=setup, inline=False)
            embed.add_field(name="Punchline", value=punchline, inline=False)

            # Send the embed
            await ctx.send(embed=embed)
        except Exception as e: # if this happens its probably because the api is no longer accessible (report this on github)
            await ctx.send(f"Error fetching joke: {e}")


    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx, choice: str = None):
        choices = ["heads", "tails"]
        result = random.choice(choices)

        if choice is None or choice.lower() not in choices:
            embed = discord.Embed(
                title="Coinflip",
                description=f"Please specify your choice: `{prefix}coinflip <heads/tails>`",
                color=embed_error
            )
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title="Coinflip",
            description=f"{ctx.author.mention} flipped a coin!",
            color=discord.Colour.blue()
        )
        embed.add_field(name="Your Choice", value=choice.capitalize(), inline=True)
        embed.add_field(name="Result", value=result.capitalize(), inline=True)

        if choice.lower() == result:
            embed.add_field(name="Outcome", value="Congratulations! You win!", inline=False)
        else:
            embed.add_field(name="Outcome", value="Better luck next time!", inline=False)

        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.LIGHTGREEN_EX}{t}{Fore.LIGHTGREEN_EX} | Fun Cog Loaded! {Fore.RESET}')

def fun_setup(bot):
    bot.add_cog(Fun(bot))
