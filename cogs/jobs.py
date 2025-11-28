"""
Jobs system for the economy.
Allows users to select jobs and collect salaries.
"""

from discord.ext import commands
import discord
from discord.ui import Button, View
from colorama import Fore
import random
import time
from utils.utilities import *
from utils.eco_support import *


class JobButton(Button):
    """Button for selecting a job."""

    def __init__(self, job_name, label):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.job_name = job_name

    async def callback(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        self.view.cog.user_jobs[user_id] = self.job_name
        await interaction.response.send_message(f"{interaction.user.mention}, you have selected the job: {self.job_name}!", ephemeral=True)


class JobView(View):
    """View containing job selection buttons."""

    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog
        for job_name, job_info in cog.jobs.items():
            self.add_item(JobButton(job_name, label=job_name.capitalize()))


class Jobs(commands.Cog):
    """Job system for earning steady income."""

    def __init__(self, bot):
        self.bot = bot
        self.jobs = {
            "freelancer": {"salary": (50, 100), "description": "Work on various tasks for clients."},
            "gamer": {"salary": (20, 80), "description": "Play games and earn money by streaming or winning tournaments."},
            "chef": {"salary": (30, 70), "description": "Cook and sell delicious meals."},
        }
        self.user_jobs = {}

    @commands.command(aliases=['job', 'jobs', 'list_jobs'])
    async def select_job(self, ctx):
        """Select a job to earn steady income."""
        embed = discord.Embed(title="Select a Job", description="Click a button to choose your job:", color=discord.Color.blue())

        job_list = "\n".join([f"**{job.capitalize()}**: {info['description']}\nSalary: {info['salary']}" for job, info in self.jobs.items()])

        embed.add_field(name="Available Jobs", value=job_list)

        await ctx.send(embed=embed, view=JobView(self))

    @commands.command()
    async def collect_salary(self, ctx):
        """Collect your job salary."""
        job_name = self.user_jobs.get(ctx.author.id)

        if not job_name:
            embed = discord.Embed(
                title="Job salary collected",
                description=f"{ctx.author.mention}, you don't have a job! Use `!job` to select one.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        job = self.jobs[job_name]
        salary = random.randint(*job['salary'])

        update_user_balance(ctx.author.id, salary)

        embed = discord.Embed(
            title="Job salary collected",
            description=f"{ctx.author.mention}, you collected **{salary} credits** from your job as a {job_name}.",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        print(f'{Fore.LIGHTGREEN_EX}{t}{Fore.LIGHTGREEN_EX} | Jobs Cog Loaded! {Fore.RESET}')


def setup(bot):
    bot.add_cog(Jobs(bot))
